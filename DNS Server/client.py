import socket

address = ("127.0.0.1",
           50)  # ip address and port  number specified in the server
bufferSize = 1024  # size of buffer for receiving queries' response

UDP_sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)  # Socket Creation: AF_INET for ipv4 addressing, SOCK_DGRAM for UDP

print("Name: Pari, Roll no:2110994779")

while True:
    print("---------------------------------------------------------------------------")
    query = input("Enter hostname/alias name : ")
    UDP_sock.sendto(query.encode(), address)  # query sending to server

    query_response, server_address = UDP_sock.recvfrom(bufferSize)  # receiving server's response
    print("Server Response on you Query : " + str(query_response.decode()))

    # Asking from user to continue or not
    is_next = input("Continue? Y/N: ")
    if is_next != "Y" and is_next != "y":
        break
