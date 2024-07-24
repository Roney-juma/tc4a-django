from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from .utils import send_sms_alert

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            order = Order.objects.get(id=response.data['id'])
            customer = order.customer
            message = f"Hello {customer.name}, your order for {order.item} has been placed."
            send_sms_alert(customer.phone_number, message)
        return response


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

