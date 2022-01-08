from rest_framework.response import Response
from rest_framework.views import APIView

from game.serializer import GameSerializer
from game.service import get_user_games_history


class GamesHistory(APIView):
    def get(self, request):
        return Response(get_user_games_history(request.user))
