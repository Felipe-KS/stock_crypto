from django.urls import path

from .views import IndexPage

urlpatterns = [
    path('dashboard/', IndexPage.as_view(), name='dashboard')
]