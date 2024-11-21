from django.urls import path
from .views import *

urlpatterns = [
    ## PAGES ##
    path("",view_main, name="view-main"),
    path("dashboard/", view_dashboard, name="view-dashboard"),

    ## USER HANDLING
    path("create-account/", create_account, name="create-account"),
    path("login-account/", login_user, name="login-account"),
    path("logout-account/", logout_user, name="logout-account" )

]