from rest_framework.views import APIView
from rest_framework.response import Response

class RBACAuthorizationView(APIView):
   def post(self, request):
        permissions = request.data.get('permissions', [])
        endpoint = request.data.get('endpoint')

        print("from the other project yay")

        if endpoint in permissions:
            return Response("Authorized", status=200)
        else:
            return Response("Unauthorized", status=403)