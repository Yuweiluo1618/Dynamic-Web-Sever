import time
from application import urls
import re
import pymysql

def router(path):
    def function_out(func):
        urls.route_dict[path] = func
        def function_in():
            return func()
        return function_in
    return function_out

@router("/index.py")
def index():
    try:
        with open("./dynamic/index.html", "r") as file:
            file_text = file.read()

            conn = pymysql.connect(host="localhost", user="root", password="", database="jing_dong")
            cur = conn.cursor()
            cur.execute("select * from goods")
            data_from_database = str(cur.fetchall())
            cur.close()
            conn.close()
            print(file_text)
            file_text = re.sub("1", data_from_database, file_text)

    except Exception as e:
            file_text = str(e)

    return file_text



@router("/center.py")
def center():
    return "This is Center"

@router("/gettime.py")
def gettime():
    return f"This is Time {time.ctime()}"
