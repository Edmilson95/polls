from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

"""
Cada generic view precisa saber em qual modelo ela atuará.
Isso é fornecido usando o atributo model (neste exemplo,
model = Question para DetailView e ResultsView) ou definindo o método get_queryset()
(conforme mostrado em IndexView).
"""
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Retorna as ultimas cinco questões publicadas. Não incluir aquelas definidas
        para serem publicadas no futuro.
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
        ]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        # Exclui qualquer questions que nao foi publicado ainda
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Reexibir o formulário de votação de perguntas
        return render(
            request,
            "/polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        select_choice.votes = F("votes") + 1
        select_choice.save()
        # Sempre retorne um HttpResponseRedirect após lidar com sucesso
        # com dados POST. Isso evita que os dados sejam postados duas vezes se um
        # usuário clicar no botão Voltar
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

