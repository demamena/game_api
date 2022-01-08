from django.urls import path
import views

urlpatterns = [
    path('user-info/', views.UserInfo.as_view()),
    path('get-top', views.GetTopUsers.as_view()),
    path('reset-score/', ''),
    path('game-history/', views.GameHistory.as_view()),
    path('set-score/', ''),
    path('set-username/', ''),
    path('create-game/', ''),
    path('change-game', ''),
]
