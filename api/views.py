from datetime import datetime

from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.db.models import Q


def PostListView(request):
    quest = Question.objects.all().order_by('-date')
    answer = Answer.objects.all().order_by('-date')
    return render(request, 'api/home.html', {'posts': quest, 'answer': answer})


def adding_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'api/add.html', {'form': form})


class QuestionDetail(DetailView):
    model = Question
    template_name = 'api/detail.html'
    context_object_name = 'detail'


