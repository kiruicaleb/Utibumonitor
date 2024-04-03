# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Medication(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    stock_quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} by {self.customer.username}"

class Statement(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Statement for {self.customer.username}"