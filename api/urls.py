from django.urls import path
from .views import PostListView, adding_question, adding_answer

urlpatterns = [
    path('quests/', PostListView.as_view(), name='home'),
    path('new_question/', adding_question, name='post_new'),
    path('new_answer/', adding_answer, name='new')
]
