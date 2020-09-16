from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question

# Create your views here.

def index(request):
	'''
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#output = '<br>'.join([q.question_text + ' ' + str(q.pub_date) for q in latest_question_list])
	context = { 'latest_question_list': latest_question_list}
	#return(render(request, 'index/index.html', context))
	return(HttpResponse(loader.get_template('index/index.html').render(context, request)))
	'''
	latest_question_list = get_list_or_404(Question)
	context = { 'latest_question_list': latest_question_list}
			
	return(HttpResponse(loader.get_template('index/index.html').render(context, request)))

def detail(request, question_id):
	'''
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404('Question with id %s does not exist.' % question_id)
	return(HttpResponse(loader.get_template('index/detail.html').render({'question': question}, request)))
	'''
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'index/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


