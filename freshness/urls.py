from django.urls import path
from . import views

app_name = 'freshness'

urlpatterns = [
    # here name is name of the url
    path('',views.import_data, name = 'freshdata'),

]