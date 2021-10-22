from . import views
from django.urls import path

app_name = 'token_app'

urlpatterns = [

    path('add/',views.add,name='add'),

]