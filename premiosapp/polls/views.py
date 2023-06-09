from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Question

def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html", {
        "latest_question_list": latest_question_list
    })
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()
    return render(request, "polls/detail.html",{
        "question" : question,
        "choices": choices
    })

def results(request, question_id):
    return HttpResponse(f'Estas viendo los resultados de la pregunta numero {question_id}')


def vote(request, question_id):
    return HttpResponse(f'Estas votando la pregunta numero {question_id}')