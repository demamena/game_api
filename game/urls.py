from django.urls import path
import views

urlpatterns = [
    path('user-info/', views.UserInfo.as_view()),
    path('get-top', views.GetTopUsers.as_view()),
    path('reset-score/', views.ResetScore.as_view()),
    path('game-history/', views.GameHistory.as_view()),
    path('set-username/', views.SetUsername.as_view()),
    path('change-game/<int:game_id>', views.ChangeGame.as_view()),
    path('create-game/', views.CreateGame.as_view()),
    path('game-info/<int:game_id>', views.GameInfo.as_view()),
]
