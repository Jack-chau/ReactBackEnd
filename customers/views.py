from customers.models import Customer
from django.http import JsonResponse
from customers.serializers import CustomerSerializer

'''
    We take the data variable,
    we pass through the serializer and 
    we use serializer.data to get the serializer version 
'''
def customers( request ) :
    # invoke serializer and return to client ( serializer use to turn database object to JSON data )
    data = Customer.objects.all( )
    serializer = CustomerSerializer( data, many = True )
    return JsonResponse( 
        {
            'customers' : serializer.data
        }
    )

