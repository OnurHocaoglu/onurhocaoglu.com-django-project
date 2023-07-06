from django.urls import path
from page.views import home_view,contact_me

urlpatterns = [
    path("", home_view, name="index"),
    path("contact",contact_me,name="contact_me")
]

