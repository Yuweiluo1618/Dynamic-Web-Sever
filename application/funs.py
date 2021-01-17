import time
from application import urls

def router(path):
    def function_out(func):
        urls.route_dict[path] = func
        def function_in():
            return func()
        return function_in
    return function_out

@router("/index.py")
def index():
    return "This is Index"

@router("/center.py")
def center():
    return "This is Center"

@router("/gettime.py")
def gettime():
    return f"This is Time {time.ctime()}"
