from django.urls import path
from .views import home,view_course,become_pro,charge
urlpatterns = [
    path('',home,name='home'),
    path('course/<slug>/',view_course,name='course'),
    path('become_pro/',become_pro,name='become_pro'),
    path('charge/',charge,name='charge'),
]
