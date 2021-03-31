from django.urls import path
from shortner import views


urlpatterns = [
    path('',views.index,name="index"),
    path('create',views.create,name="create"),
    path('<str:pk>',views.go,name="go"),
]
