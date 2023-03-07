import socket

# Define IP address and port to listen on
ip_address = '127.0.0.1'
port = 53 # DNS uses port 53
 

# Create UDP socket and bind to IP address and port number.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip_address, port)) 

# Define a dictionary of DNS records
dns_records = {
    'example.com': '192.168.1.1',
    'google.com': '172.217.14.174',
    'facebook.com': '69.63.176.13'
}

# Loop to handle incoming DNS requests
while True:
    print("Waiting for Client request...")
    # Receive DNS request and address from client
    data, address = sock.recvfrom(512)
    if data:
        print("Data has been received.")
    # Decode DNS request from bytes to string format.
    query = data.decode()

    # Extract domain name from DNS request
    domain_name = query.split()[0][:-1]

    # Check if domain name exists in DNS records
    if domain_name in dns_records:
        # Build DNS response
        response = f'{query} {dns_records[domain_name]}'
        # Send DNS response to client
        sock.sendto(response.encode(), address)
    else:
        # If domain name not found, return error message
        error = f'{query} ERROR'
        sock.sendto(error.encode(), address)
