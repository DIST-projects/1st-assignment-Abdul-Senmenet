from xmlrpc.server import SimpleXMLRPCServer

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

server = SimpleXMLRPCServer(("0.0.0.0", 8000))
print("RPC Server running on port 8000...")

server.register_function(add, "add")
server.register_function(multiply, "multiply")

server.serve_forever()
