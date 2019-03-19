from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
   


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ListQuestionView(generic.ListView):
    template_name = 'polls/listQuestion.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        return Question.objects.all

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def delete(request):
    try:
        selected_question = Question.objects.get(pk=request.POST['Question'])
    except (KeyError, Question.DoesNotExist):
        return render(request, 'polls/listQuestion.html', {
            'question_list': Question.objects.all,
            'error_message': "You didn't select a Question.",
        })
    else:
        selected_question.delete()
        return HttpResponseRedirect(reverse('polls:index'))
   

