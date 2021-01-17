import socket
from application import app
import multiprocessing

class WebServer(object):
    def __init__(self):
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server_socket.bind(("", 8080))
        tcp_server_socket.listen(128)

        self.tcp_server_socket = tcp_server_socket

    def start(self):
        while True:
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            print(f"new client has connected:{str(ip_port)}")
            p1 = multiprocessing.Process(target=self.request_handler, args=(new_client_socket, ip_port))
            p1.daemon =True

            p1.start()
            new_client_socket.close()




    def request_handler(self, new_client_socket, ip_port ):
        request_data = new_client_socket.recv(1024)
        if not request_data:
            print(f"{str(ip_port)} has disconnected")
            new_client_socket.close()
            return
        response_data = app.application("./static", request_data, ip_port)
        new_client_socket.send(response_data)
        new_client_socket.close()

if __name__ == '__main__':
    ws = WebServer()
    ws.start()