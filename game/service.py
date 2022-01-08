from game.models import User, Game
from game.serializer import GameSerializer, UserSerializer


def get_user_game_history(user: User) -> dict:
    return GameSerializer(Game.objects.filter(user=user), many=True).data


def get_user_info(user: User) -> dict:
    return UserSerializer(user).data


def get_top_users() -> dict:
    return UserSerializer(User.objects.all().order_by('score')[:50]).data
