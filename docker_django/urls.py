# docker_django/urls.py
from django.contrib import admin
from django.urls import path, include
from django.db import connections
from django.db.utils import OperationalError
import sys

# Check database connection
try:
    connection = connections['default']
    connection.cursor()
    print("✅ Database connection successful!")
except OperationalError as e:
    print("❌ Database connection failed!")
    print(f"Error: {e}")
    sys.exit(1)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('product.urls')),  # This means all product URLs start with /product/
]
