from django.urls import path
from .views import imc_view, success_view

urlpatterns = [
    path('', imc_view, name='home'),
    path('success/', success_view, name='success'),  # ✅ must exist
]