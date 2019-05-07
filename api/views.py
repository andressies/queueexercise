from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from api.queue_datastructure import Queue
import json

# initialize a 'Doe' family
queue = Queue(mode='FIFO')
queue2 = Queue(mode='LIFO')

"""
The MembersView will contain the logic on how to:
 GET, POST, PUT or delete family members
"""
class QueueView(APIView):
    def get(self, request):
        queue.dequeue()
        result = json.dumps(queue.get_all())
        # fill this method and update the return
        
        return Response(result, status=status.HTTP_200_OK)

    def post(self, request):
        asdf = queue.enqueue(json.loads(request.body))

        # add a new member to the queue
        result = json.dumps(asdf)
        return Response(result, status=status.HTTP_200_OK)

class QueueAllView(APIView):
    def get(self, request):
        # respond a json with all the queue items
        result = json.dumps(queue.get_all())
        return Response(result, status=status.HTTP_200_OK)