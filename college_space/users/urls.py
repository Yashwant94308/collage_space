from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # url(r'^register/$', views.RegistrationView.as_view(), name='register'),

    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    path('register', views.RegistrationView.as_view(), name='register'),
    path('request-reset-email', views.RequestResetEmailView.as_view(), name='request-reset-email'),
    path('activate/<uidb64>/<token>',
         views.ActivateAccountView.as_view(), name='activate'),
    path('set-new-password/<uidb64>/<token>',
         views.SetNewPasswordView.as_view(), name='set-new-password'),

]
