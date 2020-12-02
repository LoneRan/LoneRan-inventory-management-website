from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Stock

# Create your views here.

class StockChartView(TemplateView):
    template_name = 'stock/chart2.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Stock.objects.all()
        return context
