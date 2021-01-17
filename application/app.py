from application import utils
from application import urls
from application import funs

print(urls.route_dict)
def parse_request(request_data, ip_port):
    request_text =  request_data.decode()
    loc = request_text.find("\r\n")
    request_line = request_text[:loc]
    request_line_list = request_line.split(" ")

    file_path = request_line_list[1]
    print(f" {str(ip_port)} request path: {file_path}")

    if file_path == "/":
        file_path = "/index.html"

    return file_path

def application(current_dir, request_data, ip_port):

    file_path = parse_request(request_data, ip_port)
    resource_path = current_dir+file_path
    response_data = ""
    #dynamic
    if file_path.endswith(".py"):
        if file_path in urls.route_dict:
            response_body = urls.route_dict[file_path]().encode()
            response_data = utils.create_http_response("200 OK", response_body)
        else:
            response_body = "This page Not Found!".encode()
            response_data = utils.create_http_response("404 Not Found", response_body)
    else:
        #static
        try:
            with open(resource_path, "rb") as file:
                response_body = file.read()

                response_data = utils.create_http_response("200 OK", response_body)

        except Exception as e:

            response_body = f"Error! {str(e)}"
            response_body = response_body.encode()
            response_data = utils.create_http_response("404 Not Found", response_body)

    return response_data
