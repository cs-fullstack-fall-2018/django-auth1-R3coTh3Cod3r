from django.shortcuts import render


from .models import BlogModel


def index(request):
    blog_list = BlogModel.objects.all()
    context = {'blog_list': blog_list}
    return render(request, 'auth_app/index.html', context)


def userIndex(request):
    blog_list =BlogModel.objects.filter(username= request.user)
    context = {' blog_list': blog_list}
    return render(request, 'auth_app/index.html', context)