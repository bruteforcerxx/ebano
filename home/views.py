from django.http import HttpResponse
from rest_framework import status
from django.template import loader
from rest_framework.decorators import api_view

from django.shortcuts import redirect
import random
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail

from django.utils import timezone
# Create your views here.


@api_view(['GET'])
def home_page(request):
    page = 'index.html'
    template = loader.get_template(page)
    context = {}
    return HttpResponse(template.render(context, request), status=status.HTTP_200_OK)
