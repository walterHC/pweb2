from django.urls import path
from . import views 


urlpatterns = [
        
        path('administrar', views.administration, name="zonaAdminstracion"),
        path('addDestination', views.addDestination, name="añadirDestinos2"),
        path('añadir', views.addDestination, name="añadirDestino"),
        path('listar', views.listDestinations, name="listarDestinos"),
        path('<int:myID>/', views.showDestination, name="mostrarDestino"),
        path('<int:myID>/editar', views.editDestination, name="editarDestino"),
        path('<int:myID>/borrar', views.deleteDestination, name="eliminarDestino")
    ]
