
from django.contrib import admin
from django.urls import path
from alumno import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ListAlumno.as_view(), name='list'),
    path('crear/', views.AddAlumno.as_view(), name='add')
]
