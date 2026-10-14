from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import Affiche_Event,Details,Supp,Update,Ajout
urlpatterns = [
    path("show/",views.Hello,name="aff"),
    path("event_list/",views.Event_List,name="list"),
    path('generic_list/',Affiche_Event.as_view(),name="Gen_list"),
    path('Details/<int:pk>',Details.as_view(),name="Det"),
    path('Delete/<int:pk>',Supp.as_view(),name="Supp"),
    path('Update/<int:pk>',Update.as_view(),name="Up"),
    path('Ajout/',Ajout.as_view(),name="Add"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
