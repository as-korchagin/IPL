"""lab_5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import testApp.views as views
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^function_view/', views.function_view),
    url(r'^$', views.Homepage.as_view()),
    url(r'^cycles', views.Cycles.as_view()),
    url(r'^nested_fields', views.NestedFields.as_view()),
    url(r'^variables', views.Variables.as_view()),
    url(r'^conditions', views.Conditions.as_view()),
    url(r'^cycle/(?P<id>\d+)', views.CycleElement.as_view(), name='element_url')
]
