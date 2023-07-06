from django.urls import path
from todo.views import todo_home,todo_detail_view,category_detail_view,tag_view
from onurhocaoglu.views import logout_view

app_name = 'todo' # Config-Urls'te oluşturduğumuz namespace  

urlpatterns = [
    path("", todo_home, name='todo_home'),
    path("logout/", logout_view, name='logout_view'),# Anaprojedeki logout view. 
    path("<slug:category_slug>/", category_detail_view, name='category_detail_view'),
    path("tag/<slug:tag_slug>/", tag_view, name='tag_view'),
    path("<slug:category_slug>/<int:id>/", todo_detail_view, name='todo_detail'),
    

]
