from django.db.models import Model, TextField, ImageField, DecimalField, DateTimeField, BooleanField, CharField, \
    FileField, IntegerField
from django.utils import timezone


class Question(Model):
    name = CharField(max_length=255)
    question = TextField(max_length=5000)
    preview = ImageField()
    rating = DecimalField(default=0, decimal_places=2, max_length=3)
    add_date = DateTimeField(default=timezone.now)
    is_hidden = BooleanField(default=True)
    video = FileField()
    time_code = CharField(max_length=15, default="0:00")


class Answer(Model):
    answer = TextField(max_length=5000)
    is_correct = BooleanField(default=False)


class Statistics(Model):
    game_count = IntegerField()
    score = IntegerField()

