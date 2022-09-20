from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/links/', views.LinkListCreateAPIView.as_view()),
    path('api/v1/links/<int:pk>/', views.LinkRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('<int:user_id>/<path:path>', views.RedirectView.as_view(), name='redirectView'),
]

