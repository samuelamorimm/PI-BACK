from django.urls import path
from . import views

urlpatterns = [
    path('', views.publish_feedback, name='publish_feedback'),
    path('enviar-feedback/', views.send_feedback, name='send_feedback'),
    path('feedback-enviado/', views.feedback_sent, name='feedback_sent'),
]