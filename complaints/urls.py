from django.urls import path
from .views import *

urlpatterns = [
    path("",view=view_complaint_dashboard, name="complaint-dashboard"),
    path("create_complaint/",view=create_complaint, name="create_complaint"),
    path("single_complaint/<str:pk>", view=view_single_complaint, name="view_single_complaint"),

    ## OFFICIAL
    path("official/", view=view_official_complaint_dashboard, name="view_official_dashboard"),
    path("official/update/<str:pk>", view=update_official_complaint, name="update_official_dashboard"),
    path("official/<str:pk>", view=view_single_official_complaint, name="view_single_official_complaint")

]