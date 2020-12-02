"""grocery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from buy import views
from homepage.views import HomeView
from django.conf import settings
from django.conf.urls.static import static
from stock.views import StockChartView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.index,name = 'index'),
    path('stock/',StockChartView.as_view(), name = 'stock'),
    path('',HomeView.as_view(), name = 'home'),
    path('buy/',include('buy.urls')),
    path('search/',include('search_app.urls')),
    path('cart/',include('cart.urls')),
    path('order/',include('order.urls')),
    path('accounts/create/',views.signupView,name = 'signup'),
    path('accounts/login/',views.signinView,name = 'signin'),
    path('accounts/logout/',views.signoutView,name = 'signout'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
