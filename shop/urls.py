from.import views
from django.urls import path

urlpatterns = [
     path("",views.index,name="shophome"),
     path("about/",views.about,name="About Us"),
     path("contact/", views.contact, name="ContactUs"),
     path("tracking/",views.tracker,name="TrackingStatus"),
     path("search/",views.search,name="Search"),
     path("products/<int:myid>",views.prodview,name="ProductView"),
     path("checkout/",views.checkout,name="checkout"),
     path("login/",views.login,name="login"),
     path("signup/",views.signup,name="signup"),


]