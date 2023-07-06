from todo.models import Category

def global_todo_category_context(request):
    return dict(
        todo_categories = Category.objects.filter(
        is_active = True
        )
    )

