import time
import threading
import requests


class API:
    _obj = None
    lock = threading.Lock()
    def __new__(cls):
        if cls._obj == None:
            with cls.lock:
                print("Creating an instance......")
                if cls._obj == None:
                    cls._obj=super().__new__(cls)
                    print("instance created.....")
        return cls._obj
    def __init__(self):
        self.url=input("Enter the url:")
        self.rate_limit=int(input("Enter the rate limit:"))
        self.max_retries=int(input("Enter the max retries:"))


    def session(self):
        self.request=requests.Session()
        return self.request.get(self.url)


    def main(self):
        for  _ in range(1,self.max_retries+1):
            try:
                event =threading.Event()
                event.wait(1/self.rate_limit)
                response=self.session()
                print(response.status_code)
            except Exception as e:
                print("Error Occured")





A=API()

print(A.main())

