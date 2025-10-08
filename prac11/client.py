import socket
import ssl

soc=socket.socket()
server_ip="127.0.0.1"
server_port=4423
soc.connect((server_ip,server_port))

context=ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.check_hostname=False
context.verify_mode=ssl.CERT_NONE
conn=context.wrap_socket(soc,server_hostname=server_ip)

try:
    conn.send(b"hello server")
    response=conn.recv(1024)
    print("server response:",response.decode())
except ssl.SSLERROR as e:
    print("ssl error",e)
finally:
    conn.close()
        