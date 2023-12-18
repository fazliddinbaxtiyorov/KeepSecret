from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.db.models import Q


@login_required
def PostListView(request):
    quest = Question.objects.all().order_by('-date')
    answer = Answer.objects.all().order_by('-date')
    return render(request, 'api/home.html', {'posts': quest, 'answer': answer})


@login_required
def adding_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'api/add.html', {'form': form})


@login_required
class QuestionDetail(DetailView):
    model = Question
    template_name = 'api/detail.html'
    context_object_name = 'detail'


@login_required
def add_comment(request, pk):
    question = Question.objects.get(id=pk)
    comments = Answer.objects.filter(quests_text=question)
    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=question)
        if form.is_valid():
            name = request.user
            body = form.cleaned_data['answer_text']
            data = Answer(quests_text=question, user=name, answer_text=body, date=datetime.now())
            data.save()
            question.comment = comments.count()
            question.save()
            return redirect('home')
        else:
            print('form is invalid')
    else:
        form = AnswerForm()

    return render(request, 'api/new.html', {'form': form})


@login_required
def search(request):
    query = request.GET.get('q')
    page_search = Question.objects.filter(Q(hashtag__icontains=query))

    return render(request, 'api/search.html', {'search': page_search})
