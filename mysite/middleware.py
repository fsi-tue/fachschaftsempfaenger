from datetime import datetime
import pytz

class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-Generated-On'] = datetime.now(pytz.timezone('Europe/Berlin')).strftime("%c")
        return response
