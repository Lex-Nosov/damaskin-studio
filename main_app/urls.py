from django.urls import path, include
from .views import MainView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('appointment/', include('service_appointment_app.urls'))
]
