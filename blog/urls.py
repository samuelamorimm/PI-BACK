from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='landing-page'),
    path('blog/', views.post_list, name='post_list'),
    path('blog/post/<int:pk>/', views.post_detail, name='post_detail'),
    path('blog/post/new/', views.post_create, name='post_create'),
    path('blog/post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('blog/post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]