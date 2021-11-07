#!/usr/bin/env python

import BaseHTTPServer
import SimpleHTTPServer
import ssl

# Variables you can modify
# https://192.168.250.72:4509
bind_to_address = '192.168.250.80'
server_port = 4509
ssl_key_file = "server1.example.com.key"
ssl_certificate_file = "server1.example.com.pem"


# Don't modify anything below

httpd = BaseHTTPServer.HTTPServer(
    (bind_to_address, server_port), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, server_side=True,
                               keyfile=ssl_key_file,
                               certfile=ssl_certificate_file)
httpd.serve_forever()
