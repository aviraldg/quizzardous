from django import test
from django.contrib.auth.models import User
from django.core import urlresolvers
from .models import Question, Answer

class QuestionAnswerTest(test.TestCase):
    def setUp(self):
        self.user = User(username='testuser')
        self.user.set_password('test')
        self.user.save()
        self.question = Question()
        self.question.question = 'Lorem ipsum dolor sit amet?'
        self.question.author = self.user
        self.question.correct_answer = ('lorem ipsum dolor sit amet')
        self.question.save()

    def test_default_hearter_count(self):
        self.assertEqual(self.question.hearters.count(), 0)

    def test_default_report_count(self):
        self.assertEqual(self.question.reporters.count(), 0)

    def test_answer_own_question(self):
        '''
        Verifies that a User can't answer his or her own question.
        '''
        c = test.client.Client()
        c.login(username='testuser', password='test')
        response = c.post(urlresolvers.reverse('question',
            kwargs={'pk': self.question.pk, 'slug': self.question.slug}),
            {'answer': 'spam'})
        self.assertEqual(response.status_code, 401)
