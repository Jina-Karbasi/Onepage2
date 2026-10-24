
from django.urls import path, include
from oneapp.views import *

urlpatterns = [
    path("home", index_view)
]
