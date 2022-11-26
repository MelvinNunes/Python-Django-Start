from django.urls import path
from .views import Bairro_View, Distrito_View, Provincia_View, Provincia_Admin_View, Bairro_Admin_View, Distrito_Admin_View


urlpatterns = [
    path('bairros', Bairro_View.as_view()),
    path('bairros/<int:id>', Bairro_View.as_view()),
    path('distritos', Distrito_View.as_view()),
    path('distritos/<int:id>', Distrito_View.as_view()),
    path('provincias', Provincia_View.as_view()),
    path('provincias/<int: id>', Provincia_View.as_view()),
    path('admin/bairros', Bairro_Admin_View.as_view()),
    path('admin/provincias', Provincia_Admin_View.as_view()),
    path('admin/distritos', Distrito_Admin_View.as_view()),
]
