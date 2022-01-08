from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from game.models import Game, GameQuestion, Answer, Question


class AnswerSerializer(ModelSerializer):

    class Meta:
        model = Answer
        exclude = ['question']


class QuestionSerializer(ModelSerializer):
    answers = AnswerSerializer()

    class Meta:
        model = Question
        fields = '__all__'


class GameSerializer(ModelSerializer):
    questions = SerializerMethodField()

    class Meta:
        model = Game

    def get_questions(self, obj):
        return


class GameQuestionSerializer(ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = GameQuestion
        exclude = ['game']
