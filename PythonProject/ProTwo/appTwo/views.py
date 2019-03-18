from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from appTwo.models import Branch,AdmissionStats, Question, Choice

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions':latest_questions}
    return render(request, 'appTwo/index.html',context)

def detail(request, question_id):
    question = Question.objects.get(pk = question_id)
    return render(request, 'appTwo/detail.html', {'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'appTwo/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request, 'appTwo/detail.html', {'question':question, 'error_message':"Please select a choice"})
    else:
        selected_choice.votes+=1
        selected_choice.save()

        return HttpResponseRedirect(reverse('appTwo:results', args=(question.id,)))


def login(request):
    return render(request, 'appTwo/login.html')

def about(request):
    return render(request, 'appTwo/about.html')

def admissions(request):
    data_list = AdmissionStats.objects.order_by('branch_name')
    data_dict = {'records': data_list}
    return render(request, 'appTwo/admissions.html', context=data_dict)

def placements(request):
    return render(request, 'appTwo/placements.html')