
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic.edit import FormView
from .forms import QuestionForm


from .models import Poll, Choice, Question
from django.views.generic import DetailView


# Get questions and display them


def home(request):
    poll = Poll.objects.all()
    context = {'poll': poll}
    return render(request, 'poll/index.html', context)


# Show specific question and choices


# Get question and display results


def results(request, poll_id):
    question = get_object_or_404(Question, pk=poll_id)
    return render(request, 'polls/results.html', {'question': question})

# Vote for a question choice


# def vote(request, poll_id):
#     # print(request.POST['choice'])
#     question = get_object_or_404(Poll, pk=poll_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'poll/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('poll:results', args=(poll.id,)))

class VoteView(DetailView):
    model = Poll
    template_name = 'poll/test.html'


class DetailView(DetailView):
    model = Poll
    slug_field = 'slug'
    template_name = 'poll/test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["question"] = Question.objects.all()
        context["choice"] = Choice.objects.all()
        return context


class PollTake(FormView):
    form_class = QuestionForm
    template_name = 'poll.html'

    def get_form_kwargs(self):
        kwargs = super(PollTake, self).get_form_kwargs()
        return dict(kwargs, question=self.question)

    def form_valid(self, form):
        if self.logged_in_user:
            self.form_valid_user(form)
        self.request.POST = {}

        return super(PollTake, self).get(self, self.request)

    def get_context_data(self, **kwargs):
        context = super(PollTake, self).get_context_data(**kwargs)
        context['question'] = self.question
        context['quiz'] = self.poll
        if hasattr(self, 'previous'):
            context['previous'] = self.previous
        if hasattr(self, 'progress'):
            context['progress'] = self.progress
        return context
