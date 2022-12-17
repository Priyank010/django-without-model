from .serializers import *
from rest_framework.views import APIView
from .tests import *
from rest_framework.response import Response


class myDataView(APIView):

    def get(self, request):

        linkedin = 'https://www.linkedin.com/in/priyank-desai-2b89a41a3/'
        github = 'https://github.com/Priyank010'
        my_website = 'https://priyank010.github.io/#home'
        medium = 'https://priyankdesai515.medium.com/'

        data_obj = myData(linkedin,github,my_website,medium)
        serializer_class = myDataSerializer(data_obj)
        return Response(serializer_class.data)