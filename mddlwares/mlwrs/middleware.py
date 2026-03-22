import time

class RequestTimeMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("Request Timed Middleware Constructor1 called")

    def __call__(self,request):
        start_time=time.time()
        print("Before View MW1")
        response=self.get_response(request)
        
        print("After View MW1")
        end_time=time.time()
        print(f"Request took {start_time - end_time} seconds")
        return response


class RequestTimeMiddleware2:
    def __init__(self,get_response):
        self.get_response=get_response
        print("Request Timed Middleware2 Constructor called")

    def __call__(self,request):
        start_time=time.time()
        print("Before View MW2")
        response=self.get_response(request)
        
        print("After View MW2")
        end_time=time.time()
        print(f"Request took {start_time - end_time} seconds")
        return response


class RequestTimeMiddleware3:
    def __init__(self,get_response):
        self.get_response=get_response
        print("Request Timed Middleware3 Constructor called")

    def __call__(self,request):
        start_time=time.time()
        print("Before View MW3")
        response=self.get_response(request)
        
        print("After View MW3")
        end_time=time.time()
        print(f"Request took {start_time - end_time} seconds")
        return response
