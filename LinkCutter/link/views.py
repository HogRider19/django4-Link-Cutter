from django.shortcuts import get_object_or_404, redirect
from django.views import View
from rest_framework.viewsets import ModelViewSet
from .models import Link
from .serializers import LinkSerializer


class LinkAPIViewSet(ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class RedirectView(View):
    def get(self, request, path):
        link = get_object_or_404(Link, truncated_url=path)
        link.is_transition()
        link.save()
        return redirect(link.raw_url)
    



