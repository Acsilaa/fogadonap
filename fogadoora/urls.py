from django.urls import path, include
from .controllers import views
urlpatterns = [
    path('', views.index)
    
]
