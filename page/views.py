from django.shortcuts import render

#My Models
from page.models import PageLatesProjects,ContactMe



def home_view(request):
    projects = PageLatesProjects.objects.all()
    context = dict(
        projects=projects
    )
    return render(request,"page/index.html",context)


def contact_me(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"] 
        message = request.POST["message"]

        contact = ContactMe(name = name, email = email, subject = subject, message = message)
        contact.save()

    context = dict(
        contact = contact,
    )
    return render(request,"page/index.html",context)
