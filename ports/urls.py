from django.urls import path

from . import views

urlpatterns = [
    path('', views.Ports.as_view()),
    # r/ Request
    path('p/<int:id>', views.PortView.as_view()),
]
