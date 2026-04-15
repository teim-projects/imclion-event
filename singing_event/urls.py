from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ HOME PAGE → imc.html
    path('', include('registration.urls')),
]