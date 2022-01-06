from django.urls import path
from .views import *

urlpatterns = [
    #bookamrk/까지 온 후 2차 url
    path("",BookmarkListView.as_view(),name='list'),
    path("add/",BookmarkCreateView.as_view(),name='add'),
    path("detail/<int:pk>/",BookmarkDetailView.as_view(),name='detail'),
    path("update/<int:pk>/",BookmarkUpdateView.as_view(),name='update'),
    path("delete/<int:pk>/",BookmarkDeleteView.as_view(),name='delete'),
]

#path(2차 url,불러올 view,테이블에서 url을 불러올 형식)

