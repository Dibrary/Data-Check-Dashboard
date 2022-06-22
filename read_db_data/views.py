from django.shortcuts import render
from django.views.generic import ListView, DetailView

from read_db_data.models import read_data_from_DB

class data_LV(ListView):
    model = read_data_from_DB

class data_DV(DetailView):
    model = read_data_from_DB


