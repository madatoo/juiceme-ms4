""" model for FAQ """
from django.db import models
from profiles.models import UserProfile


class FaqPosts(models.Model):
    """class for handeling FAQs"""
    class Meta:
        """ class dispay the new fAQs first"""
        ordering = ['-date_added']

    question = models.CharField(max_length=200,
                                unique=True, blank=False, null=False)
    author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                               null=True, blank=True)
    answer = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.question)


class CommentsFaqPost(models.Model):
    """this class for handeling comments for faq"""
    class Meta:
        """ class dispay the new coments first"""
        ordering = ['-date_added']

    comment = models.ForeignKey(FaqPosts,
                                on_delete=models.CASCADE,
                                null=True, blank=True)
    comments_author = models.ForeignKey(UserProfile,
                                        on_delete=models.SET_NULL,
                                        null=True, blank=True)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)
