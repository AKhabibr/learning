from django.shortcuts import render

from orders.models import SalesOrder
from orders.serializers import OrderSerializer  # Импорт сериализатора
from rest_framework.viewsets import ModelViewSet  
# Create your views here.
# claasic approach, without API
def orders_page(request):
	return render(request, 'index.html', {'orders': SalesOrder.objects.all()})


class OrderView(ModelViewSet):
	# Это указывает, что все заказы из модели SalesOrder будут доступны для API.
	queryset = SalesOrder.objects.all()
	# Указывает, что данные будут сериализоваться с использованием OrderSerializer, то есть через API будут передаваться только поля amount и description.
	serializer_class = OrderSerializer
