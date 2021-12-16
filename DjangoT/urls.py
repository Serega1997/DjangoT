
from django.urls import path, include

urlpatterns = [
    path('', include('homepage.urls')),
    path('Caesar', include('Caesar.urls'))
]
