
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Poll, Choice, Question


# Get questions and display them


def home(request):
    poll = Poll.objects.all()
    context = {'poll': poll}
    return render(request, 'poll/index.html', context)


def index(request):
    latest_question_list = Poll.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request, 'poll/index.html', context)


# Show specific question and choices


def detail(request, poll_id):
    try:
        question = Question.objects.get(pk=poll_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'poll/detail.html', {'poll': poll})

# Get question and display results


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# Vote for a question choice


def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'poll/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))
