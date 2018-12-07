from django.shortcuts import render, get_object_or_404
# render is a shortcut that combines a call to loader and HttpResponse
# from django.template import loader
# from django.http import HttpResponse, Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    ## loader/HttpResponse syntax
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))

    # render shortcut syntax
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # # Verbose method
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})

    # Shortcut method
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST gives access to submitted data as a dictionary. return value is always string
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form
        context = {
            'question': question,
            'error_message': "You didn't select a choice.",
        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully handling
        # POST data. This prevents data from being posted twice if a 
        # user hits the Back button
        # reverse() is a dynamic url constructor that returns a url-encoded string by referencing the urls.py file
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
