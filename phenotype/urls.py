from django.urls import path
from . import views
from .views import PostDetailView
from .views import GenotyprDetailView

urlpatterns = [
    path('', views.index),
    path( 'post_list/', views.post_list, name='post_list'),
    path( '<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path( 'genotype/', views.genotype, name='genotype'),
    path( 'genotype/<int:pk>/', GenotyprDetailView.as_view(), name='genotypeDetail'),
    path ( 'info/', views.info, name='info'),
    # path( 'genotype/<int:pk>/', views.accessions_list, name='genotypeDetail'),
]

 