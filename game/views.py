from rest_framework.response import Response
from rest_framework.views import APIView

from game.serializer import GameSerializer
from game.service import get_user_game_history, get_user_info


class GameHistory(APIView):
    def get(self, request):
        return Response(get_user_game_history(request.user))


class UserInfo(APIView):
    def get(self, request):
        return Response(get_user_info(request.user))

