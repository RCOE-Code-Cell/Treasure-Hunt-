from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from round.models import Groups
from round.serializers import TotalGroupsSerializer
import jwt
from .models import User

class UpdateGroupView(APIView):
    def put(self, request, group_id):
        token = request.headers.get('Authorization')
        if not token:
            return Response({"error": "Unauthorized!"}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Decode JWT to check if user is staff
        try:
            payload = jwt.decode(token, 'secret', algorithms="HS256")
        except jwt.ExpiredSignatureError:
            return Response({"error": "Token expired!"}, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.InvalidTokenError:
            return Response({"error": "Invalid token!"}, status=status.HTTP_401_UNAUTHORIZED)

        user = User.objects.filter(id=payload['id']).first()
        if not user or not user.is_staff:
            raise PermissionDenied("You do not have permission to perform this action.")

        group = Groups.objects.filter(id=group_id).first()
        if not group:
            return Response({"error": "Group not found!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TotalGroupsSerializer(group, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
