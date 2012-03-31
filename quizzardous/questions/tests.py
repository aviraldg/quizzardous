from django.test import TestCase
from django.contrib.auth.models import User
from .models import Question, Answer

class QuestionTest(TestCase):
    def setUp(self):
        self.user = User(username='testuser')
        self.user.save()
        self.question = Question()
        self.question.content = 'Lorem ipsum dolor sit amet?'
        self.question.author = self.user
        self.question.correct_answers = ('lorem, ipsum, dolor, sit, amet')
        self.question.save()

    def test_default_hearter_count(self):
        """
        Tests that the hearts count is 0 by default.
        """
        self.assertEqual(self.question.hearts, 0)
