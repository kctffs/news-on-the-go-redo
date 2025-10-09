from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
    """
    Test the CommentForm for correctly monitoring valid and invalid input.
    """

    def test_form_is_valid(self):
        """
        Test that the CommentForm is valid when a body is provided.
        """
        comment_form = CommentForm({'body': 'This post exceeds expectations'})
        self.assertTrue(comment_form.is_valid(), msg="""Form invalid when it
        should be valid""")

    def test_form_is_invalid(self):
        """
        Test that the CommentForm is invalid when no body is provided.
        """
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="""Form is valid when it
        should be invalid""")


class TestCommentFormValidation(TestCase):
    """
    Test the CommentForm for different types of input to be sure
    it validates correctly.
    """

    def test_form_valid_with_regular_text(self):
        """
        Form should be valid with normal text input.
        """
        form = CommentForm({'body': 'This post exceeds expectations'})
        self.assertTrue(form.is_valid(), msg="Form invalid with normal text")

    def test_form_invalid_when_empty(self):
        """
        Form should be invalid if body is empty.
        """
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid(), msg="Form is valid but empty")

    def test_form_valid_with_special_characters(self):
        """
        Form should accept special characters and emojis.
        """
        special_text = "Wow! 🔥 <b>Bold Text</b> & special chars ©®™"
        form = CommentForm({'body': special_text})
        self.assertTrue(form.is_valid(), msg="""Form invalid with special
        characters""")
