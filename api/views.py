from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.models import Product,EcommUser,UserAddress
from .serializers import ProductSerializer,EcommUserSerializer,UserAddressSerializer

@api_view(['GET'])
def viewProducts(request):
    productview=Product.objects.all().order_by('price')

    serializer1=ProductSerializer(productview,many=True)
    return Response(serializer1.data)

@api_view(['POST'])
def addProduct(request):
    serializer1=ProductSerializer(data=request.data)
    if serializer1.is_valid():
        serializer1.save()
    return Response(serializer1.data)

@api_view(['POST'])
def addUser(request):
    serializer2=EcommUserSerializer(data=request.data)
    if serializer2.is_valid():
        serializer2.save()
    return Response(serializer2.data)


@api_view(["DELETE", ])
def deleteItem(request, slug):
    try:
        product_to_delete=Product.objects.get(slug=slug)
    except:
            user_to_delete = EcommUser.objects.get(slug=slug)
    #  except:
    #       return Response("Item not found")
    if request.method=='DELETE':
        if(product_to_delete==True):
            operation=product_to_delete.delete()
        else:
            operation = user_to_delete.delete()
        data={}
        if operation:
            data['success']= 'delete successful'
        else:
            data['failure']='delete failed'
        return Response(data=data)

