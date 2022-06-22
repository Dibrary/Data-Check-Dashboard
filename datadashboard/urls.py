
from django.contrib import admin
from django.urls import path

from read_db_data.views import data_LV, data_DV

urlpatterns = [
    path('admin/', admin.site.urls),
    path('checkData/', data_LV.as_view(), name='index'),
    path('checkData/<int:pk>', data_DV.as_view(), name='detail'),
]
