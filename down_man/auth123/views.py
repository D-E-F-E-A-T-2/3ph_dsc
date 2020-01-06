from django.shortcuts import render
from django.http import HttpResponse


def testing(self):
    return HttpResponse('OK')
