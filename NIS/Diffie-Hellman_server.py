import socket

# Diffie-Hellman parameters
p = int(input("Enter the prime number p : "))
g = int(input("Enter the primitive root g : "))

# User input for private key
private_key = int(input("Enter your private key : "))

# Compute public key
public_key = pow(g, private_key, p)

# Start TCP server
server = socket.socket()
server.bind(('localhost', 5000))
server.listen(1)
print("[*] Waiting for connection...")

conn, addr = server.accept()
print(f"[+] Connected to {addr}")

# Send public key to client
conn.send(str(public_key).encode())

# Receive client's public key
client_pub_key = int(conn.recv(1024).decode())

# Compute shared secret
shared_key = pow(client_pub_key, private_key, p)
print(f"[Server] Shared Key: {shared_key}")

# If shared key matches expected, print "Hi"
if shared_key == int(input("Enter the expected shared key : ")):
    print("Hi (from Server)")

conn.close()
server.close()