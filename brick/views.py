from django.http import HttpResponse
from django.shortcuts import render
import random


def index(request):
    return render(request, 'brick/index.html', {'context': create_context()})


def create_context():
    context = [random.randint(1, 20), random.randint(1, 20)]
    for i in range(len(context)):
        if context[i] == 2:
            context[i] = 'qaz'

    for i in range(len(context)):
        if context[i] == 1:
            context[i] = 'qwe'

    return context

