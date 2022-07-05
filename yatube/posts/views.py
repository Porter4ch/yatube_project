from email.policy import HTTP
import http
from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HTTPResponse('Главная страница')

def grup_posts(request):
        return HTTPResponse('Группы по интересам')