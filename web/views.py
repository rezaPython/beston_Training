from django.conf.urls import url
from django.shortcuts import render
from json import JSONEncoder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Token, Expense, Income
import datetime
from django.http import HttpResponse



@csrf_exempt
def income(request):
    token = request.POST['token']
    user = User.objects.filter(token__token=token).get()
    amount= request.POST['amount']
    date = datetime.datetime.now()
    text = request.POST['text']
    Income.objects.create(user=user, amount=amount, date=date, text=text)

    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)





@csrf_exempt
def submit_expense(request):
    token = request.POST['token']
    user = User.objects.filter(token__token=token).get()
    amount = request.POST['amount']
    date = datetime.datetime.now()
    text = request.POST['text']
    Expense.objects.create(user=user, amount=amount, date=date, text=text)
    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)










