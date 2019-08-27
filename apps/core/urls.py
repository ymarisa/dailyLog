from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from apps.core import views

urlpatterns = [
    path('', views.api_root),
    path('habits/',
         views.HabitList.as_view(),
         name='user-habits'),
    path('logs/',
         views.LogList.as_view(),
         name='log-entries'),
    path('log/<int:pk>/',
         views.LogDetail.as_view(),
         name='log-detail'),
    path('habit/<int:pk>',
         views.HabitDetail.as_view(),
         name='habit-detail'),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)