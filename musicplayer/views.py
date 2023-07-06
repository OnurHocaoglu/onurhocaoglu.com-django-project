from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from . models import Song
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required()
def music_view(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"index.html",context)
