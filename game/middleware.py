from rest_framework.response import Response


class GameMiddleware:

    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        return self._get_response(request)

    def process_exception(self, request, exception):
        return Response({
            'success': False,
            'message': str(exception),
        }, status=417)
