from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.views import APIView
from core.serializer import CoinPriceSz
from core.models import Coin, CoinPrice


class Prices(APIView):
    def get(self,request):
        date = request.query_params.get('date', None)
        offset = request.query_params.get('offset', 0)
        limit = request.query_params.get('limit', 100)

        if date is None:
            data = CoinPrice.objects.all()
            count = CoinPrice.objects.count()
            if int(offset) > count:
                return Response(status=HTTP_400_BAD_REQUEST, data={'error': 'offset is greater than the number of records'})
            data = data[offset:limit+offset]
            serializer = CoinPriceSz(data, many=True)

        else:
            data = CoinPrice.objects.filter(time__date=date)
            count = data.count()
            if int(offset) > count:
                return Response(status=HTTP_400_BAD_REQUEST, data={'error': 'offset is greater than the number of records'})
            data = data[offset:offset+limit]
            serializer = CoinPriceSz(data, many=True)
        response = {
            'url': request.build_absolute_uri(),
            'next': request.build_absolute_uri(request.path + '?offset=' + str(offset + limit) + '&limit=' + str(limit)),
            'count':count,
            'data': serializer.data,
        }            
        return Response(response, status=HTTP_200_OK)