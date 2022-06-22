from django.contrib import admin
from read_db_data.models import read_data_from_DB

@admin.register(read_data_from_DB)
class read_data_admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')


