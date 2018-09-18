from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from .permissions import IsOwner
from .serializers import EntrySerializer, UserSerializer, CategorySerializer
from .models import Entry, Category


# Create your views here.
class CreateView(generics.ListCreateAPIView):
    """
    This class defines the create behaviour of our rest API
    """
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """
        Save the POST data when creating a new entry
        """
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    This class handles the http GET, PUT and DELETE requests.
    """
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)


class UserView(generics.ListAPIView):
    """
    View to list the users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """
    View to retrieve a user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryView(generics.ListAPIView):
    """
    View to handle listing of categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
