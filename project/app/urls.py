from django.urls import path
from . import views
from views import CustomLoginView

urlpatterns = [
    path("", views.index, name='index'),
    path('register/', views.registerPage, name='register'),
    path('order/', views.order, name='order'),
    path('login/', views.loginPage, name='login'),
    # API URLs
    path('api/medications/', api.MedicationListCreateAPIView.as_view(), name='medication-list-create'),
    path('api/orders/', api.OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('api/statements/', api.StatementListAPIView.as_view(), name='statement-list'),
]