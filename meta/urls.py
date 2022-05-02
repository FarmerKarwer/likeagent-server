"""likeagent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from website.views import *

urlpatterns = [
    path('', QuizListView.as_view()),
    path('admin/', admin.site.urls),
    path('tests/', tests),
    path('tests/swl/', tests_swl),
    path('tests/big5/', tests_big5),
    path('tests/temper/', tests_temper),
    path('tests/typeofthinking/', tests_typeofthinking),
    path('tests/<pk>/', quiz_view, name='quiz-view'),
    path('tests/<pk>/save/', save_quiz_view, name='save-view'),
    path('tests/<pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('accounts/', include('website.urls')),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
