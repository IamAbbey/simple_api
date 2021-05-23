from rest_framework import generics, status
from rest_framework.response import Response

from .models import UUIDData
from .serializers import UUIDDataSerializer


class UUIDDataListView(generics.ListAPIView):
    """
    Returns all active UUIDData
    """

    queryset = UUIDData.objects.all()
    serializer_class = UUIDDataSerializer

    def get_queryset(self):
        self.serializer_class.create(self, {})
        return super().get_queryset()

    def list(self, request, *args, **kwargs):
        """
        GET verb, to return all active posts
        """
        queryset = self.get_queryset()
        serializer = UUIDDataSerializer(queryset, many=True)
        return Response(
            {
                "success": True,
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
