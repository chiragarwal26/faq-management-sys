from rest_framework import viewsets
from django.core.cache import cache
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        cached_data = cache.get(cache_key)
        if cached_data is not None:
            return Response(cached_data)
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        cache.set(cache_key, data, timeout=60*15)
        return Response(data)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context