from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from game.models import Question, User, Game, GameQuestion, Answer


@admin.register(Question)
class AdminAdmin(UserAdmin):
    list_display = ('id', 'name', 'question', 'preview', 'rating', 'add_date', 'is_hidden', 'video', 'time_code')
    list_display_links = ('id', 'name', 'question', 'rating', 'add_date', 'is_hidden')
    fieldsets = (
        ('Main', {"fields": ("username", 'full_name', "phone", "picture",
                             'registration_date')}),
    )
    readonly_fields = ['id', 'add_date', 'preview']
    search_fields = ('id', 'name', 'question', 'add_date')