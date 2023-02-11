from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['title', 'description']  # изменил название с filterset_fields для работы поиска.


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filterset_fields = ['address', 'products']  # добавил поле products, чтобы работал поиск склада с продуктом
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['address', 'product']

