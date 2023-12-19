from django.urls import path
from .views import PostListView, adding_question, search, QuestionDetail, add_comment, LikeView, migration

urlpatterns = [
    path('quests/', PostListView, name='home'),
    path('detail/<int:pk>/', QuestionDetail.as_view(), name='detail'),
    path('new_question/', adding_question, name='post_new'),
    path('new_answer/<int:pk>', add_comment, name='new'),
    path('search/', search, name='search'),
    path('like/<int:pk>/', LikeView, name='like'),
    path('migration', migration, name='migration'),

]
