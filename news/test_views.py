from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment, Vote


class TestNewsViews(TestCase):
    """
    Test for the voting functionality on Post objects.

    This includes verifying:
    - Users can upvote a post.
    - Users can downvote a post.
    - Users can toggle votes.
    - The vote counts are updated correctly.
    """

    def setUp(self):
        """
        Create test data
        """
        self.user = User.objects.create_user(
            username='testuser', password='password')

        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='This is a test post content.',
            status=1
        )

        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            body='This is a test comment.',
            approved=True
        )


    def test_post_list_view(self):
        """
        Test the home page.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/index.html')
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        """
        Test the post detail view for a certain post.
        """
        response = self.client.get(reverse(
            'post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/post_detail.html')
        self.assertContains(response, 'This is a test post content.')
        self.assertContains(response, 'This is a test comment.')

    def test_add_comment(self):
        """
        Test adding new comment to post.
        """
        self.client.login(username='testuser', password='password')
        response = self.client.post(
            reverse('post_detail', args=[self.post.slug]),
            {'body': 'Another test comment'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(self.post.comments.filter(
            body='Another test comment').exists())

    def test_upvote_post(self):
        """
        Test that a logged-in user can upvote a post.
        """
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse(
                'vote_post', args=[self.post.id, 'up']))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.post.votes.count(), 1)
        vote = self.post.votes.first()
        self.assertEqual(vote.value, 1)

    def test_downvote_post(self):
        """
        Test that a logged-in user can downvote a post.
        """
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse(
            'vote_post', args=[self.post.id, 'down']))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.post.votes.count(), 1)
        vote = self.post.votes.first()
        self.assertEqual(vote.value, -1)

    def test_toggle_vote(self):
        """
        Test that clicking the same vote again removes it.
        """
        self.client.login(username='testuser', password='password')
        self.client.get(reverse('vote_post', args=[self.post.id, 'up']))
        self.client.get(reverse('vote_post', args=[self.post.id, 'up']))
        self.assertEqual(self.post.votes.count(), 0)

    def test_vote_requires_login(self):
        """
        Test that voting on a post requires the user to be logged in.
        """
        response = self.client.get(reverse(
            'vote_post', args=[self.post.id, 'up']))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(self.post.votes.exists())
