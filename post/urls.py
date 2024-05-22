from django.urls import path
from django.views.decorators.cache import cache_page

from .views import (
    PostCreate, PostDelete, PostDetail, PostEdit,
    PostHome, PostList, subscriptions,
    )


urlpatterns = [
    # path('', cache_page(60)(PostHome.as_view()), name='portal_home'),
    path('', PostHome.as_view(), name='portal_home'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('news/', PostList.as_view(), name='list_news'),
    path('article/', PostList.as_view(), name='list_article'),
    path('notification/', PostList.as_view(), name='list_notification'),
    path('subscriptions/', cache_page(300)(subscriptions), name='subscriptions'),
]
