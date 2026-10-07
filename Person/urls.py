from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(
        template_name="Person/login.html",
        redirect_authenticated_user=True,),
         name="log"),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),
    path('SignUp/',views.SignUp,name="register")
]
