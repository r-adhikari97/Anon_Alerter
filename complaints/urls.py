from django.urls import path
from .views import *

urlpatterns = [
    path("",view=view_complaint_dashboard, name="complaint-dashboard"),
    path("create_complaint/",view=create_complaint, name="create_complaint"),
    path("single_complaint/<str:pk>", view=view_single_complaint, name="view_single_complaint"),

    ## OFFICIAL
    path("official/", view=view_admin_complaint_dashboard, name="view_admin_dashboard"),
    path("official/update/<str:pk>", view=update_admin_complaint_status, name="update_admin_complaint_status"),
    path("official/<str:pk>", view=view_single_admin_complaint, name="view_single_admin_complaint")

]