from .models import Post, Comment, Categories, SubCategories


def category_list(request):
    return {
        "categories": Categories.objects.all()
    }


def sub_category_list(request):
    return {
        "sub_categories": SubCategories.objects.all()
    }

# def popular_posts(request):
#     return{
#         "popular_posts": Post.objects.all().filter()
#     }
