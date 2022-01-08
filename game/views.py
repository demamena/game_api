from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from game.models import Game
from game.service import get_user_game_history, get_user_info, get_top_users, reset_score, change_name, rand_question, \
    set_game_questions_answers


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
        rand_question(game, request.POST.get('guestion_count'))
        return Response({'success': True})


class ChangeGame(APIView):
    def put(self, request, game_id):
        game = Game.objects.get(game__id=game_id, user=request.user)
        game.game_end = timezone.now()
        game.total_score = request.POST.get('total_score')
        game.save()
        set_game_questions_answers(game, request.POST.get('questions').split(','))
        return Response({'success': True})


class SetUsername(APIView):
    def put(self, request):
        change_name(request.user, request.POST.get('username'))
        return Response({'success': True})
