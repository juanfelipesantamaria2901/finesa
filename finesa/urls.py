from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('finesa', views.formulario, name='formulario'),
    path('PolizaVida', views.polizavida, name='polizavida'),
    path('PolizaHogar', views.polizahogar, name='polizahogar'),
    path('PolizaAuto', views.polizaauto, name='polizaauto'),
    path('FomularioEmision1', views.formulario_emision1, name='formulario_emision1'),
    path('FomularioEmision3', views.formulario_emision3, name='formulario_emision3'),
    path('FomularioEmision4', views.formulario_emision4, name='formulario_emision4'),
    path('FormularioInspeción', views.formulario_inspecion, name='formulario_inspecion'),
]