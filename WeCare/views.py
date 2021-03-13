from django.shortcuts import render
from registration.models import Questions,Answers
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.db.models import Q
from datetime import date,datetime
from django.utils import timezone

# Create your views here.
def getquestioninfo(request):
    c={}
    c.update(csrf(request))
    que = Questions.objects.all()
    return render(request,'addquestion.html',{'que':que ,'c':c})

def postquestion(request):
    question_text = request.POST.get('question', '')
    cnt = 0
    questions = Questions.objects.all()
    if questions is not None:
        for que in questions:
            if que.que_text == question_text:
                cnt = 1
                break
    if(cnt != 1):
        question = Questions(que_text=question_text)
        question.save()
        return HttpResponseRedirect('/home')
    else:
        print(question_text)
        ans=Answers.objects.filter(question_text=question_text)
        return render(request,'addquestion.html',{'msg1':'Question already exists.','ans':ans})

def viewquestion(request):
    que=Questions.objects.all()
    return render(request,'viewquestion.html',{'que':que})

def allquestions(request):
    que=Questions.objects.all()
    return render(request,'allquestions.html',{'que':que})

def postanswer(request):
    que = request.GET.get('question','')
    print(que)
    question = Questions.objects.filter(que_text=que)
    c={}
    c.update(csrf(request))
    ans=Answers.objects.filter(question_text=que)
    return render(request,'getanswer.html',{'question':question,'c':c,'ans':ans})

def addanswer(request):
    que = request.GET.get('que_text','')
    ans = request.GET.get('answer_text','')
    print(que)
    #questions = Questions.objects.get(que_text=que)
    #questions = Questions(que_text=que)
    #print(type(questions))
    c={}
    c.update(csrf(request))
    answer = Answers(ans_text=ans,question_text=que, date_answer_posted=datetime.now())
    print("Answer")
    answer.save()
    return HttpResponseRedirect('viewquestion')

def deletequestion(request):
    que = request.GET.get('question','')
    q = Questions.objects.get(que_text=que)
    q.delete()
    return HttpResponseRedirect('viewquestion')

def viewanswer(request):
    que = request.GET.get('question','')
    print(que)
    ans=Answers.objects.filter(question_text=que)
    return render(request,'viewanswer.html',{'ans':ans})    

