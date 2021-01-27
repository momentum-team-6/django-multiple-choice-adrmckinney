from django.shortcuts import render
from api.serializers import SnippetSerializer
from core.models import Snippet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class SnippetListCreateView(ListCreateAPIView):
    serializer_class = SnippetSerializer

    def get_queryset(self):
        return Snippet.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SnippetDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = SnippetSerializer

    def get_queryset(self):
        if self.request.method == "GET":
            return Snippet.objects.all()
        
        return self.request.user.snippets

