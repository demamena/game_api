from rest_framework.response import Response
from rest_framework.views import APIView

from game.models import Game
from game.serializer import GameSerializer
from game.service import get_user_game_history, get_user_info, get_top_users, reset_score, change_name


class GameHistory(APIView):
    def get(self, request):
        return Response(get_user_game_history(request.user))


class UserInfo(APIView):
    def get(self, request):
        return Response(get_user_info(request.user))


class GetTopUsers(APIView):
    def get(self, request):
        return Response(get_top_users())


class ResetScore(APIView):
    def post(self, request):
        reset_score(request.user)
        return Response({'success': True})


class CreateGame(APIView):
    def post(self, request):
        game = Game.objects.create(user=request.user)
        for i in range(0, request.POST.get('questions_count')):
            pass
            # TODO: создать вопрос GameQuestion рандомный без повторений
        return Response({'success': True})


class SetUsername(APIView):
    def put(self, request):
        change_name(request.user)
        return Response({'success': True})
