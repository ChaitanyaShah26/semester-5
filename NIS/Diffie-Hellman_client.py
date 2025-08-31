import socket

# Diffie-Hellman parameters
p = int(input("Enter the prime number p : "))
g = int(input("Enter the primitive root g : "))

# User input for private key
private_key = int(input("Enter your private key : "))

# Compute public key
public_key = pow(g, private_key, p)

# Connect to server
client = socket.socket()
client.connect(('localhost', 5000))

# Receive server's public key
server_pub_key = int(client.recv(1024).decode())

# Send public key to server
client.send(str(public_key).encode())

# Compute shared secret
shared_key = pow(server_pub_key, private_key, p)
print(f"[Client] Shared Key: {shared_key}")

# If shared key matches expected, print "Hi"
if shared_key == int(input("Enter the expected shared key : ")):
    print("Hi (from Client)")

client.close()