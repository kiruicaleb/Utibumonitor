from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Medication, Order, Statement
from .serializers import MedicationSerializer, OrderSerializer, StatementSerializer

class MedicationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

class StatementListAPIView(generics.ListAPIView):
    serializer_class = StatementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Statement.objects.filter(customer=self.request.user)
