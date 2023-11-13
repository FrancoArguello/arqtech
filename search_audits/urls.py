from django.urls import path
from . import views

urlpatterns=[
    path('audit/', views.search_audits, name = 'search_audits'),
]