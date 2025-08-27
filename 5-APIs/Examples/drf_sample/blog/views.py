from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import BlogPost, Task
from .serializers import BlogPostSerializer, TaskSerializer


# Name the class according to what it's supposed to do
class BlogPostListCreate(APIView):

    # List all Blog Posts
    def get(self, request):
        # Retrieve all posts
        blog_posts = BlogPost.objects.all()

        # Use the serialzer to convert the data to JSON
        serializer = BlogPostSerializer(blog_posts, many=True)

        # Return a response
        return Response(serializer.data)  # JSON
        
    def post(self, request):
        # Deserialize the incoming data
        serializer = BlogPostSerializer(data=request.data)

        # Validate the data
        if serializer.is_valid():

            # Save the new post
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            
            # return validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Name the class according to the model its working with
class TaskViewSet(ViewSet):
    
    authentication_classes = [TokenAuthentication]
    permissions_classes = [IsAuthenticated]

    # Declare the queryset as a class attribute
    queryset = Task.objects.all()

    # Gets the full list of tasks
    def list(self, request):
        # Serialize the objects
        serializer = TaskSerializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Retrieves a single object
    def retrieve(self, request, pk=None):
        task = get_object_or_404(self.queryset, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)


