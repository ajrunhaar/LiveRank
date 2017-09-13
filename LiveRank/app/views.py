"""
Definition of views.
"""

from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth import authenticate,login
from django.db.models import Q
from django.views.generic import View
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.forms import *
import logging

logger = logging.getLogger('liverank.logging.views')

def dashboard(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated():
        return render(
            request,
            'app/dashboard.html',
            {
                'RankedPlayers':Player.objects.filter(Q(rank__isnull=False)),
                'UnrankedPlayers':Player.objects.filter(Q(rank__isnull=True)),
                
            }
        )
    else:
        return redirect('/login')

class PlayerRegisterFormView(View):
    form_class = RegistrationForm
    template_name = 'app/registration.html'

    #Display blank for for new user
    def get(self,request):
        logger.debug("PlayerFormView Get")
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    #Process form data
    def post(self,request):
        logger.debug("PlayerFormView Post")
        form = self.form_class(request.POST)
        if form.is_valid():
            logger.debug("PlayerFormView Form Valid")
            user = form.save(commit = False)
            # cleaned (normalised) data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            contact = form.cleaned_data['contact']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
        
            user = authenticate(username = username,password=password)

            if user is not None:
                logger.debug("User not none")
                if user.is_authenticated:
                    logger.debug("User authenticated")
                else:
                    logger.debug("User not authenticate")
            else:
                logger.debug("User is none")
        else:
            logger.debug(form.errors)
            return render(request,self.template_name,{'form':form,'errors':form.errors})
        return render(request,self.template_name,{'form':form})


class PlayerLoginFormView(View):
    form_class = LoginForm
    template_name = 'app/login.html'

    #Display blank for for new user
    def get(self,request):
        logger.debug("PlayerFormView Get")
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})

    #Process form data
    def post(self,request):
        logger.debug("PlayerFormView Post")
        form = self.form_class(request.POST)

        logger.debug("PlayerFormView Form Valid")
        # cleaned (normalised) data
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username = username,password=password)

        if user is not None:
            logger.debug("User not none")
            if user.is_active:
                logger.debug("User authenticated")
                login(request,user)
                return redirect('/')
            else:
                logger.debug("User not authenticate")
                return render(request,self.template_name,{'form':form,'errors':'User inactive: Please contact the site admin'})
        else:
            logger.debug("User is none")
            return render(request,self.template_name,{'form':form,'errors':'Username or password incorrect'})


class RankingView(View):

    template_name = 'app/rankings.html'
    #Display blank for for new user
    def get(self,request):
        logger.debug("RankingView Get")
        return render(
            request,
            self.template_name,
            {
                'Players':Player.objects.all(),
                'PlayersRange':range(1,Player.objects.all().count()+1),
            },
        )

    #Process form data
    def post(self,request):
        logger.debug("RankingView Post")
        logger.debug(request.POST)
        for player in Player.objects.all():
            
            if request.POST[player.username] and request.POST[player.username]!="None":
                player.rank = request.POST[player.username]
                player.save()
            else:
                player.rank = None
                player.save()

        return render(
            request,
            self.template_name,
            {
                'Players':Player.objects.all(),
                'PlayersRange':range(1,Player.objects.all().count()+1),
            },
        )
