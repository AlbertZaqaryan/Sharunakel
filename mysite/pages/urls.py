from django.urls import path
from . import views

urlpatterns=[
    path('', views.IndexListView.as_view(), name='index'),
    path('nout/', views.NoutListView.as_view(), name='nout'),
    path('nout_info/', views.NoutInfoListView.as_view(), name='nout_info'),
]