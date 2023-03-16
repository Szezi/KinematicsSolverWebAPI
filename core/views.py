from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Accounts API Overview': reverse('accounts-overview', request=request),

        'Robotic API Overview': reverse('robot-overview', request=request),

    }

    return Response(api_urls)