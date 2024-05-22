from django.contrib import admin
from django.urls import path, include
import debug_toolbar

from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', include('post.urls')),
    path('accounts/', include('allauth.urls')),
    path('search/', views.PostSearch.as_view(), name='post_search'),
    path('cabinet/', views.subscriptions, name='cabinet'),

    # debug toolbar URLS
    path('__debug__/', include(debug_toolbar.urls)),

]
