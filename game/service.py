from game.models import User, Game, GameQuestion
import random

from game.models import User, Game, Question
from game.serializer import GameSerializer, UserSerializer, QuestionSerializer


def get_user_game_history(user: User) -> dict:
    return GameSerializer(Game.objects.filter(user=user), many=True).data


def get_user_info(user: User) -> dict:
    return UserSerializer(user).data


def get_top_users() -> dict:
    return UserSerializer(User.objects.all().order_by('score')[:50]).data


def reset_score(user: User) -> None:
    user.score = 0
    Game.objects.filter(user=user).delete()
    user.save()


def change_name(user: User, username: str) -> None:
    user.username = username
    user.save()


def set_game_questions_answers(game: Game, questions_list: list) -> None:
    for question in questions_list:
        question_id, is_correct = question.split(':')
        is_correct = True if is_correct == 'true' else False
        set_question_answer(game, question_id, is_correct)


def set_question_answer(game: Game, question_id: int, is_correct: bool) -> None:
    game_question = GameQuestion.objects.get(game=game, question__id=question_id)
    game_question.is_answer_correct = is_correct
    game_question.save()


def rand_question(game: Game, questions_count: int) -> list:
    question_shuffle = list(range(Question.objects.filter(is_hidden=False)))
    random.shuffle(question_shuffle)
    questions = []
    for question in question_shuffle:
        if len(questions) >= questions_count:
            break
        questions.append(QuestionSerializer(question).data)
    return questions
