from django.contrib.auth.models import AbstractUser
from django.db.models import Model, TextField, ImageField, DecimalField, DateTimeField, BooleanField, CharField, \
    FileField, IntegerField, TimeField, ForeignKey, CASCADE
from django.utils import timezone


class Question(Model):
    name = CharField(max_length=255)
    question = TextField(max_length=5000)
    preview = ImageField()
    rating = DecimalField(default=0, decimal_places=2, max_length=3)
    add_date = DateTimeField(default=timezone.now)
    is_hidden = BooleanField(default=True)
    video = FileField()
    time_code = TimeField(default=0)


class Answer(Model):
    answer = TextField(max_length=5000)
    is_correct = BooleanField(default=False)


class User(AbstractUser):
    score = IntegerField(default=0)
    games_count = IntegerField(default=0)


class Game(Model):
    game_start = DateTimeField(default=timezone.now)
    game_end = DateTimeField(default=timezone.now)


class GameQuestion(Model):
    game = ForeignKey(Model, on_delete=CASCADE)
    question = ForeignKey(Question, on_delete=CASCADE)
    is_answer_correct = BooleanField(default=False)
