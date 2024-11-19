from django.urls import path
from .views import *

urlpatterns = [
    path("create_complaint/",view=create_complaint, name="create_complaint"),
    path("",view=view_complaint_dashboard, name="complaint-dashboard")
]