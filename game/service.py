from game.models import User, Game
from game.serializer import GameSerializer


def get_user_games_history(user: User) -> dict:
    return GameSerializer(Game.objects.filter(user=user)).data
