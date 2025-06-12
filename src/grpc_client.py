import grpc
import file_extension_pb2 as file_extension_pb2
import file_extension_pb2_grpc as file_extension_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = file_extension_pb2_grpc.FileExtensionStub(channel)
    file_path = input("Enter file path: ")
    request = file_extension_pb2.FilePathRequest(file_path=file_path)
    try:
        response = stub.GetFileExtension(request)
        print(f"Extension: {response.extension}")
    except grpc.RpcError as e:
        print(f"gRPC error: {e.code()} - {e.details()}")

if __name__ == "__main__":
    run()