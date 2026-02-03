import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://16.171.10.19:8000/")

try:
    print(server.add(2, 3))
except Exception as e:
    print("RPC Error:", e)


print("Addition:", server.add(10, 5))
print("Multiplication:", server.multiply(4, 6))
