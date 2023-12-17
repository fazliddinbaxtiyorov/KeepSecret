from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm


class PostListView(ListView):
    model = Question
    template_name = 'api/home.html'
    context_object_name = 'posts'


def adding_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'api/add.html', {'form': form})


def show(request, task_id):
    task = get_object_or_404(Question, id=task_id)
    if request.method == 'POST':
        return redirect('index')
    return render(request, 'api/show.html', {'task': task})
