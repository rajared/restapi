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
class Musiclistview(GenericAPIView,ListModelMixin):
    queryset=Musician.objects.all()
    serializer_class=MusicSerializer
    def get(self,request):
        return self.list(request)
class Musicgetview(GenericAPIView,RetrieveModelMixin):
    queryset=Musician.objects.all()
    serializer_class=MusicSerializer
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
class Musiccreateview(GenericAPIView,CreateModelMixin):
    queryset=Musician.objects.all()
    serializer_class=MusicSerializer
    def post(self,request,**kwargs):
        return self.create(request,**kwargs)
class Musicdestroyview(GenericAPIView,DestroyModelMixin):
    queryset=Musician.objects.all()
    serializer_class=MusicSerializer
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)
class Musicupdateview(GenericAPIView,UpdateModelMixin):
    queryset=Musician.objects.all()
    serializer_class=MusicSerializer
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)


