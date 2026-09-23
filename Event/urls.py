from django.urls import path
from . import views
urlpatterns = [
    path("show/",views.Hello,name="aff")
]
