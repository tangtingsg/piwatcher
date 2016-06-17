import logging

from django.shortcuts import render_to_response

logger = logging.getLogger('default')


def home(request):
    return render_to_response('index.html')
