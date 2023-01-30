from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Distribute/', views.Distribute, name='distribute'),
    path('index/', views.index)
]
