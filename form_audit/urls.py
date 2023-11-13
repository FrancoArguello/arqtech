from django.urls import path
from . import views
from .views import download_excel

urlpatterns=[
    path('form/', views.form_template, name = 'form_audit'),
    path('save_form/', views.form_audit, name = 'save_audit'),
    path('audit/', views.search_template, name = 'search_audits'),
    path('result_search/', views.search_audit, name = 'result_search'),
    path('logout/', views.logout_view, name='logout'),
    path('download_excel/', download_excel, name='download_excel')
    
]