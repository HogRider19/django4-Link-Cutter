from django.urls import path
from . import views


urlpatterns = [
    path('api/v1/links', views.LinkAPIViewSet.as_view({'get': 'list'})),
    path('<int:user_id>/<path:path>', views.RedirectView.as_view(), name='redirectView'),
]

