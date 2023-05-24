from .models import Categories, SubCategories


def category_list(request):
    return {
        "categories": Categories.objects.all()
    }


def sub_category_list(request):
    return {
        "sub_categories": SubCategories.objects.all()
    }
