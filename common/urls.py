from django.urls import path
from .views import signup
from django.contrib.auth.views import LogoutView,LoginView

app_name='common'

urlpatterns=[
    path('login/',LoginView.as_view(template_name='common/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('signup/',signup,name='signup'),
]