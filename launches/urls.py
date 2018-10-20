from django.urls import path

from . import views

urlpatterns = [
    path('', views.Launches.as_view()),
    # r/ Request
    path('l/<int:id>', views.LaunchView.as_view()),
]
