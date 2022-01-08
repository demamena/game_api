from django.urls import path
import views

urlpatterns = [
    path('get-user/<user_id>', ''),
    path('get-top', ''),
    path('reset-score/<user_id>', ''),
    path('game-history/<user_id>', ''),
    path('set-score/<user_id>', ''),
    path('set-username/<user_id>', ''),

]
