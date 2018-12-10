from django.test import TestCase
import datetime
from django.utils import timezone

from .models import Question

# Create your tests here.

class QuestionModelTests(TestCase):

    # Just like python testing, methods should begin with 'test_'
    def test_was_published_recently_with_future_question(self):
        """ was_published_recently() returns False for questions whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
