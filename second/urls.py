from django.urls import path,include
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', views.home, name='home'),
    path('success-mail', TemplateView.as_view(template_name='success_mail.html'), name='success_mail'),

]