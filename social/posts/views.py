from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts
from .forms import PersonForm

from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):

  posts = Posts.objects.all()[:10]

  context = {
    'title': 'Latest Posts',
    'posts': posts
  }

  return render(request, 'posts/index.html', context)

def details(request, id):
  post = Posts.objects.get(id=id)

  context = {
    'post': post
  }

  return render(request, 'posts/details.html', context)
  
@login_required(login_url="/accounts/signup")
def create_form(request):
  form = PersonForm(request.POST or None)
  if form.is_valid():
    form.save()

  context = {
    'form': form
  }
  return render(request, 'posts/create.html', context)
