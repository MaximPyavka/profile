from datetime import datetime
#from profile.models import RequestInfo


class StoreRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.timestamp = datetime.now()
        print(request.timestamp)
        response = self.get_response(request)
        exec_time = datetime.now() - request.timestamp
        with open("profile.log", "a") as log:
            log.write("Request - {}, execution time - {}, IP - {}\n".format(response, exec_time, request.META.get("REMOTE_ADDR")))

            """RequestInfo.objects.create(response=response, exec_time=exec_time)
        for i in RequestInfo.objects.all():
            print(i.response, i.exec_time)
        #print(exec_time)
        #print(response)"""
        return response
