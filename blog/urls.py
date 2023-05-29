from django.urls import path
from . import views
from user import views as user_view
from .views import PostListView, PostDetailView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', PostListView.as_view(), name='home'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('register/', user_view.register, name='register'),
]
