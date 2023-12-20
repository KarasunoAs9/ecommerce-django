from .models import Category


def menu_list(request):
    link = Category.objects.all()
    return dict(link=link)
