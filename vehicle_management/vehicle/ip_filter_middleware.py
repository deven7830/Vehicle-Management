from django.http import HttpResponse


class IPFilterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define your IP filtering logic here
        allowed_ips = ['127.0.0.1']
        if request.META['REMOTE_ADDR'] not in allowed_ips:
            return HttpResponse('Access Denied')

        response = self.get_response(request)

        return response
