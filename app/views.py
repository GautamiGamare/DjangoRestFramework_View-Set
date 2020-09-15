from rest_framework.viewsets import ViewSet
from app.serializers import ProductSerializer
from app.models import ProductModel
from rest_framework.response import Response

class Product(ViewSet):
    def list(self,request): #List method will bahave like get() Will read all values
        qs = ProductModel.objects.all()
        ps = ProductSerializer(qs,many=True)
        return Response(ps.data)

    def create(self,request): #will bahave as post
        res = request.data
        ps = ProductSerializer(data=res)
        if ps.is_valid():
            ps.save()
            msg = {'data':'Data is saved'}
        else:
            msg = {'error':ps.errors}
        return Response(msg)

    def retrieve(self,request,pk=None):
        try:
            qs = ProductModel.objects.get(pid=pk)
            ps = ProductSerializer(qs)
            return Response(ps.data)
        except ProductModel.DoesNotExist:
            msg = {'data':'Product Not Found'}
            return Response(msg)

    def update(self,request,pk=None):
        qs = ProductModel.objects.get(pid=pk)
        try:
            ps = ProductSerializer(qs,request.data,partial=True)
            if ps.is_valid():
                ps.save()
                msg = {'data':'Product is Saved'}
            else:
                msg = {'error':'Error while Saving Product'}
            return Response(msg)
        except ProductModel.DoesNotExist:
            msg = {'error':'Product ID: Not Found'}
            return Response(msg)

    def destroy(self,request,pk=None):
        res = ProductModel.objects.filter(pid=pk).delete()
        if res[0]!=0:
            msg = {'data':'Product ID is deleted'}
        else:
            msg = {'error':'Product ID is not available'}
        return Response(msg)

