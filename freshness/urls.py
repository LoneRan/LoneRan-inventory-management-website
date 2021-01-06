from django.urls import path
from . import views

app_name = 'freshness'

urlpatterns = [
    # here name is name of the url
    path('',views.freshness, name = 'fresh'),
    path('importdata',views.import_data, name = 'freshdata'),
    path('predict',views.predict, name = 'predict_result'),
    path('reports',views.reports, name = 'reports'),
    path('analysis/overview-chart',views.overview_chart, name = 'overview-chart'),
    path('analysis/price-chart/',views.price_chart, name = 'price-chart'),
    path('analysis/price/',views.price, name = 'price'),
]