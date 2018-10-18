from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import BlogModel


def index(request):
    blog_list = BlogModel.objects.all()
    context = {'blog_list': blog_list}
    return render(request, 'auth_app/index.html', context)

@login_required()
def userIndex(request):
    blog_list =BlogModel.objects.filter(username= request.user)
    context = {' blog_list': blog_list}
    return render(request, 'auth_app/index.html', context)

