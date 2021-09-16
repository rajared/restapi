from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import*
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin,DestroyModelMixin,UpdateModelMixin



""""functionbased view"""
@api_view(['GET'])
def home(request):
    return Response({"status":200,"message":'yes'})
@api_view(['GET'])
def get1(request):
    music=Musician.objects.all()
    serialize_data=MusicSerializer(music,many=True)
    return Response({"status":200,"payload":serialize_data.data})
@api_view(['POST'])
def post1(request):
    music=Musician.objects.all()
    serialize_data=MusicSerializer(data=request.data)
    if serialize_data.is_valid():
        serialize_data.save()
    return Response(serialize_data.data)
@api_view(['POST'])
def update1(request,id):
    music=Musician.objects.get(id=id)
    serialize_data=MusicSerializer(instance=music,data=request.data)
    if serialize_data.is_valid():
        serialize_data.save()
    return Response(serialize_data.data)
@api_view(['DELETE'])
def delete1(request,id):
    music=Musician.objects.get(id=id)
    music.delete()
    return Response('item is delete')


""""""""""""""""class based views"""""""""""""''"""""""""
class Music_get_list_or_create_operations_view(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Musician.objects.all()
    serializer_class=MusicSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class Music_urd_operations_view(GenericAPIView,DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin):
    queryset=Musician.objects.all()
    serializer_class=MusicSerializer
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)




