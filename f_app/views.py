from django.shortcuts import render,redirect,get_object_or_404
from f_app.forms import *
from .models import BlogModel

# Create your views here.

def welcome_view(request):

    return render(request, 'welcome.html')

def blog_list(request):
    blog_data = BlogModel.objects.all()

    context = {
        'blog_data': blog_data
    }
    return render(request, 'blog_list.html', context)




def add_blog(request):
    form_data = BlogForm()
    if request.method == 'POST':
        form_data = BlogForm(request.POST, request.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect('blog_list')
    context = {
        'form_data': form_data
    }

    return render(request, 'add_blog.html', context)

def update_blog(request, id):
    blog_data = get_object_or_404(BlogModel, id = id)
    form_data = BlogForm(instance=blog_data)
    if request.method == 'POST':
        form_data = BlogForm(request.POST, request.FILES, instance=blog_data)
        if form_data.is_valid():
            form_data.save()
            return redirect('blog_list')
    context={
        'form_data': form_data
    }
    return render(request, 'update_blog.html',context)