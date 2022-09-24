from django.shortcuts import get_object_or_404, redirect
from rest_framework.permissions import IsAuthenticated
from .serializers import LinkSerializer
from .permitions import OnlyOwnObjects
from .serializers import LinkSerializer
from rest_framework import generics
from django.views import View
from .models import Link


class LinkListCreateAPIView(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Link.objects.filter(user_id=self.request.user.id)
    
class LinkRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [OnlyOwnObjects]

class RedirectView(View):
    def get(self, request, user_id, path):
        link = get_object_or_404(Link, truncated_url=path, user_id=user_id)
        link.is_transition()
        link.save()
        return redirect(link.raw_url)
    



