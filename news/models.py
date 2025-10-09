from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Represents a blog post with fields for title, slug,
    author, featured image, content, timestamps, status,
    and an optional excerpt.
    """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="news_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    def upvotes(self):
        """Return the number of upvotes."""
        return self.votes.filter(value=1).count()

    def downvotes(self):
        """Return the number of downvotes."""
        return self.votes.filter(value=-1).count()

    def score(self):
        """Return the score (upvotes - downvotes)."""
        return self.upvotes() - self.downvotes()


class Comment(models.Model):
    """
    Represents a comment made by a user on a specific post.
    Author, content of the comment, approval status, and timestamp.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


class Vote(models.Model):
    """
    A vote can either be an upvote or a downvote.
    Tracks the user, the post being voted on, the vote value
    and the timestamp.
    """
    UPVOTE = 1
    DOWNVOTE = -1
    VOTE_CHOICES = (
        (UPVOTE, "Upvote"),
        (DOWNVOTE, "Downvote"),
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="votes")
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="votes")
    value = models.SmallIntegerField(choices=VOTE_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "post")

    def __str__(self):
        return f"""{self.user} voted {self.get_value_display()} on
        {self.post.title}"""
