from django.urls import path
from .views import PostListView, adding_question

urlpatterns = [
    path('quests/', PostListView.as_view(), name='home'),
    path('new/', adding_question, name='post_new')
]