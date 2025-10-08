import socket
import ssl

serv=socket.socket()
serv.bind(('0.0.0.0',4423))
serv.listen(5)

certfile='localhost.crt'
keyfile="localhost.key"

context=ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=certfile,keyfile=keyfile)
print("server is listening on port 4423")

while True:
    soc,addr=serv.accept()
    conn=context.wrap_socket(soc,server_side=True)
    try:
        data=conn.recv(1024)
        if data:
            print("recived ",data.decode())
            conn.send(b"hello client")
    except ssl.SSLERROR as e:
        print("ssl error",e)
    finally:
        conn.close()
        