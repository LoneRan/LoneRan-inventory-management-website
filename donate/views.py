from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.models import Group, User

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import TemplateView

import pandas as pd
# from donate.emailNotificationDonation import sendEmail
# from html import HTML
# Create your views here.

file = 'donation.xls'

def index(request):
    text_var = 'This is customer donation app'
    return HttpResponse(text_var)

def donate(request):
	return render(request, 'donation/donapage.html')

def viewExcel(request):
    dishesList = pd.read_excel(file, sheet_name=0, index_col=0)
    excel = dishesList.to_html()

    return render(request, 'donation/donapage.html', {'excel': excel})

def sendNoti(request):
    #sendEmail()
    text_var = 'Email has been sent'
    return HttpResponse(text_var)
    # return render(request, 'donation/donapage.html')