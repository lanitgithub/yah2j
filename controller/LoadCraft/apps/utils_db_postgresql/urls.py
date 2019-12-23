from django.urls import path, include
from rest_framework import routers
from . import views

api_router = routers.DefaultRouter()
api_router.register('postgresql_settings', views.PostgresqlSettingsView)


urlpatterns = [
    path('', include(api_router.urls)),
    path('check_connection/<str:postgresql_settings_label_id>/',
         views.PostgresqlSettingsView.check_connection),
    # path('cancel_payments/', views.cancel_payments)
]
