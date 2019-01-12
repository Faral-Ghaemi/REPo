from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.template import loader
import os, errno
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from filebrowser.sites import site
from filebrowser.base import FileListing

def index(request):
    """
    View function for home page of site.
    """
    rep = models.repository.objects.all()
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'rep' : rep},
    )
    #
    # try:
    #     os.makedirs(name)
    # except OSError as e:
    #     if e.errno != errno.EEXIST:
    #         raise
def userrepView(request):
    repha=models.repository.objects.filter(usern=request.user)
    filelisting = FileListing(site.storage.location, sorting_by='date', sorting_order='desc')

    context = {
        'rep': repha,
        'folder' : filelisting.listing(),
    }
    template = loader.get_template('myrep.html')
    return HttpResponse(template.render(context,request))


def repview(request, username, name):
    return

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('git:index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
