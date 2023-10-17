from files.models import File
from files.serializers import FileSerializer
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class UploadView(APIView):
    """ File upload view """
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            file_instance = File.objects.create(file=request.FILES['file'])
            serializer = FileSerializer(file_instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print('error')
            return Response({'error_message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
