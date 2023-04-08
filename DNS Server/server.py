import socket

print("DNS Server Started!!")
print("Name: Pari, Roll no:2110994779")
# ip address and port number
address = ("127.0.0.1", 50)
# size of buffer for receiving queries
bufferSize = 1024

UDP_sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)  # Socket Creation: AF_INET for ipv4 addressing, SOCK_DGRAM for UDP
UDP_sock.bind(address)  # binding socket to ip and port

type_A = {"http://www.abc.com": "10.0.0.1", "http://www.def.com": "20.0.0.1",
          "http://www.ghi.com": "30.0.3.3"}  # Type A records
type_CNAME = {"http://www.g.com": "http://www.google.com",
              "http://www.n.com": "http://www.netflix.com",
              "http://www.y.com": "http://www.youtube.com",
              "http://www.a.com": "http://www.amazon.com",
              "http://www.s.com": "http://www.spotify.com"}  # CNAME records

while True:
    print("---------------------------------------------------------------------------")
    print("Listening for client at ip=" + address[0] + " and port=" + str(address[1]) + " ...")
    query, client_address = UDP_sock.recvfrom(bufferSize)  # receiving client's query
    print("Client query: " + query.decode())

    # checking type of query: A or CNAME and preparing response
    URL = query.decode()
    if URL in type_A.keys():
        response = "A," + type_A[URL]
    elif URL in type_CNAME.keys():
        response = "CNAME," + type_CNAME[URL]
    else:
        response = "None"

    UDP_sock.sendto(response.encode(), client_address)  # response sending to client
