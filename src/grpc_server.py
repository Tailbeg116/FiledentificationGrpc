import grpc
from concurrent import futures
import time
import os

from magika import Magika

import file_extension_pb2 as file_extension_pb2
import file_extension_pb2_grpc as file_extension_pb2_grpc

# Efficiently load Magika model once
magika_model = Magika()

class FileExtensionServicer(file_extension_pb2_grpc.FileExtensionServicer):
    def GetFileExtension(self, request, context):
        file_path = request.file_path
        if not os.path.exists(file_path):
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('File not found')
            return file_extension_pb2.FileExtensionResponse()
        if not os.path.isfile(file_path):
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details('Provided path is not a file')
            return file_extension_pb2.FileExtensionResponse()
        try:
            res = magika_model.identify_path(file_path)
            extension = res.output.extensions[0] if res.output.extensions else ""
            return file_extension_pb2.FileExtensionResponse(extension=extension)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return file_extension_pb2.FileExtensionResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    file_extension_pb2_grpc.add_FileExtensionServicer_to_server(FileExtensionServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server running on port 50051...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()