from rest_framework import serializers # serializers used to return json from the database
from customers.models import Customer


# Read all fields from defined Model
class CustomerSerializer( serializers.ModelSerializer ) :
    class Meta :
        model = Customer
        fields = "__all__"

