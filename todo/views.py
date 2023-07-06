from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required # Todoları görmek için login ol sayfasına yönlendirme / but .. login olmayan user sayfayı görüntülerken hata alır! 

#My Models
from todo.models import Todo,Category,Tag

# @login_required(login_url="/admin/login/")# Anasayfada Todo görmek için admin logine yönlendirme 
def todo_home(request):
   # todos = Todo.objects.all() # Tüm todo tablosunu çağırırsak ve sonradan active olanları çağırırsak fazladan yük bindiririz 
    todos = Todo.objects.filter(
        # user = request.user,
        is_active = True, # sadece active olanlar çağırıldı. 
       # title__icontains = 'todo' # çağırılan active todoların içinde titlesi todo olanlar çağırıldı. 
    )
   # todos = Todo.objects.exclude(title__icontains='todo')  titlesi todo olmayanları çağırır. (exclude)
    context= dict(
        todos = todos
    )
    return render(request,'todo/todo_list.html',context)

@login_required(login_url="/admin/login/")
def category_detail_view(request,category_slug):
    category = get_object_or_404(Category,slug=category_slug)
    todos = Todo.objects.filter(
        user = request.user,
        is_active = True,
        category = category,
    )
    context = dict(
        todos= todos,
        category = category,
    )
    return render(request,'todo/todo_list.html',context)

@login_required(login_url="/admin/login/")
def todo_detail_view(request,id,category_slug):
    # try:
    #     todo_id = Todo.objects.get(pk=id)
    #     context = dict(
    #         todo_id = todo_id,              # bu yol uzun yol , shortcuts sayesinde get object or 404 ile daha kısa :) 
    #     )
    #     return render(request,'todo/todo_detail.html',context)
    # except Todo.DoesNotExist:
    #     raise Http404
    
    todoid = get_object_or_404(Todo, category__slug=category_slug, pk=id, user=request.user)#request.user ile online olan user todo görür. 
    context = dict(
        todoid = todoid,
    )
    return render(request,'todo/todo_detail.html',context)

@login_required(login_url="/admin/login/")
def tag_view(request, tag_slug):
    tag = get_object_or_404(Tag, slug = tag_slug)
    context= dict(
        tag=tag,
        todos = tag.todo_set.filter(user=request.user) # todo.set.filter ile var olan taglerin, eklenen todolarına ulaşabiliyoruz.
    )
    return render(request,'todo/todo_list.html',context)