"""
Definition of urls for LiveRank.
"""

from datetime import datetime
from django.conf.urls import url,include
import django.contrib.auth.views
from django.contrib import admin

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.dashboard, name='dashboard'),
    url(r'^register$', app.views.PlayerRegisterFormView.as_view(), name='player_register_form'),
    url(r'^login$', app.views.PlayerLoginFormView.as_view(), name='player_login_form'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rankings', app.views.RankingView.as_view(), name='player_login_form'),
]
