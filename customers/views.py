from customers.models import Customer
from django.http import JsonResponse, Http404
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
            'customers' : serializer.dataJsonResponse
        }
    )

def customer( request, id ) :
    try :
        data = Customer.objects.get( pk = id )
    except Customer.DoesNotExist :
        raise Http404( 'Customer does not exisit' )
        serializer = CustomerSerializer( data ) 
        return JsonResponse( 
            {
                'customer' : serializer.data
            }
        )