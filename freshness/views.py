from .models import food
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import csv

from freshness_classification import predict_freshness, cross_val
# Create your views here.
path = './staticfiles/data/Freshness_classification.csv'
def import_data(request):
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = food.objects.get_or_create(
                item_no=row[0],
                item=row[1],
                description=row[2],
                price = row[3],
                temp = row[4],
                humidity = row[5],
                co2 = row[6],
                o2 = row[7],
                freshlevel = row[8],
                )
    text_var = 'Data has been successfully imported into database!'
    return HttpResponse(text_var)

def freshness(request):
	
	return render(request, 'index.html')

def predict(request):
    text_var = 'Predict successful!'
    predict_freshness()
    scores = cross_val()
    return render(request,'prediction.html')


