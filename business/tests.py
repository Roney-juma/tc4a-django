
from django.test import TestCase
from .models import Customer, Order

class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(name="Roney Juma", code="")

    def test_customer_creation(self):
        john = Customer.objects.get(name="John Doe")
        self.assertEqual(john.code, "JD123")

class OrderTestCase(TestCase):
    def setUp(self):
        customer = Customer.objects.create(name="John Doe", code="JD123")
        Order.objects.create(customer=customer, item="Book", amount=29.99)

    def test_order_creation(self):
        order = Order.objects.get(item="Book")
        self.assertEqual(order.amount, 29.99)

