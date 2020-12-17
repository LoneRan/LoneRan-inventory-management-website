from django.urls import path
from . import views

app_name = 'freshness'

urlpatterns = [
    # here name is name of the url
    path('',views.freshness, name = 'fresh'),
    path('importdata',views.import_data, name = 'freshdata'),
    path('predict',views.predict, name = 'predict_result'),

]