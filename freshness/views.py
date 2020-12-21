from .models import food
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import csv


from freshness.freshness_classification import predict_freshness, cross_val, yPred, xTest

from django.db import connection
import pandas as pd
# Create your views here.
path = './staticfiles/data/Freshness_classification.csv'
cursor = connection.cursor()

def import_data(request):
    # cursor.execute('TRUNCATE TABLE freshness_food')
    food.objects.all().delete()
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
    importdata = True
    return render(request, 'index.html',{'importdata':importdata})

def freshness(request):
	
	return render(request, 'index.html')

def predict(request):
    text_var = 'Predict successful!'
    predict_freshness()
    query = 'SELECT * FROM freshness_food'
    # cursor.execute('SELECT * FROM freshness_food ORDER BY item')
    # print(cursor.fetchall())
    table = pd.read_sql(query,connection)
    table = table.to_html()

    y_pred = pd.DataFrame(yPred())
    x_test = xTest()
    x_test = pd.DataFrame(x_test)
    y_pred.rename(columns={"0":"Prediction"})
    x_test.rename(columns={"0":"item","1":"Description"})
    table_pred = pd.concat([x_test,y_pred],axis=1,join='inner')
    table_pred = table_pred.to_html()
  
    scores = cross_val()
    return render(request,'subpage/prediction.html',{'table_pred':table_pred, 'table':table, 'scores':scores})

def reports(request):
    return render(request,'subpage/reports.html')


