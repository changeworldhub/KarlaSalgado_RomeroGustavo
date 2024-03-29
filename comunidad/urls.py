from django.urls import path 
from . import views

 
urlpatterns = [
   path('',views.index,name='index'),
   path('registrar/', views.register, name="registrar"),
   path('Login/', views.Login, name='Login'),
   path('nosotros/', views.nosotros,name='nosotros'),
   path('Crear/Voluntario', views.voluntario_create,name='voluntario_create'),
   path('suscripcion', views.suscripcion_view,name='suscribir'),
   path('Listar/',views.VoluntarioListView.as_view(),name='voluntarios'),
   path('voluntario/<int:pk>',views.VoluntarioDetailView.as_view(),name='voluntario-detail'),
   path('Editar/<int:pk>', views.VoluntarioUpdate.as_view(),name='voluntario_update'),
   path('Eliminar/<int:pk>', views.VoluntarioDelete.as_view(),name='voluntario_eliminar'),
   path('logout/', views.logout_view, name='logout'),
]


