from django.urls import path
from . import views

app_name = 'donate'

urlpatterns = [
    # here name is name of the url
    path('',views.donate, name = 'donate'),
    path('donation/',views.viewExcel, name = 'excel'),
    path('sentemail',views.sendNoti, name = 'sendNoti'),

]
