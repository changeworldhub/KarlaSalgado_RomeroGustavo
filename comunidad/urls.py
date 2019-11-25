from django.urls import path 
from . import views

 
urlpatterns = [
   path('',views.index,name='index'),
   path('registrar/', views.RegistroUsuario.as_view(), name="registrar"),
   path('nosotros/', views.nosotros,name='nosotros'),
   path('Crear/Voluntario', views.voluntario_create,name='voluntario_create'),
   path('suscripcion', views.suscripcion_view,name='suscribir'),
   path('Listar/',views.VoluntarioListView.as_view(),name='voluntarios'),
   path('voluntario/<int:pk>',views.VoluntarioDetailView.as_view(),name='voluntario-detail'),
   path('Editar/<int:pk>', views.VoluntarioUpdate.as_view(),name='voluntario_update'),
   path('Eliminar/<int:pk>', views.VoluntarioDelete.as_view(),name='voluntario_eliminar'),
]


