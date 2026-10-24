from django.urls import path
from . import views
app_name='webs'
urlpatterns = [
    path('',views.index,name='index'),
    path('quiz/', views.quiz_view, name='quiz'),
]
