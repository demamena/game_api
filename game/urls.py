from django.urls import path
import views

urlpatterns = [
    path('user-info/', views.UserInfo.as_view()),
    path('get-top', views.GetTopUsers.as_view()),
    path('reset-score/', views.ResetScore.as_view()),
    path('game-history/', views.GameHistory.as_view()),
    path('set-score/', ''),
    path('set-username/', views.SetUsername.as_view()),
    path('create-game/', ''),
    path('create-game/', ''),
]
