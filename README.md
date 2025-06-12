# gRPC File Extension Service

This project provides a gRPC service to identify the file extension of a given file path using the Magika library. It is designed for efficient inter-process communication, such as integration with C# or other languages, without the need to hit HTTP endpoints.

## Project Structure

```
fastapi-file-extension-service
├── proto
│   └── file_extension.proto         # Protobuf definition for the gRPC service
├── src
│   ├── grpc_server.py               # gRPC server implementation
│   ├── grpc_client.py               # Example gRPC client
│   ├── file_extension_pb2.py        # Generated protobuf code
│   └── file_extension_pb2_grpc.py   # Generated gRPC code
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd fastapi-file-extension-service
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   - On Windows:
     ```
     python -m venv venv
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **(If needed) Generate gRPC code from proto:**
   ```
   python -m grpc_tools.protoc -I=proto --python_out=src --grpc_python_out=src proto/file_extension.proto
   ```

## Usage

### Start the gRPC Server

```
python src/grpc_server.py
```

The server will listen on port `50051` by default.

### Run the Example gRPC Client

```
python src/grpc_client.py
```

You will be prompted to enter a file path, and the client will display the detected file extension.

## gRPC Service Definition

- **Service:** `FileExtension`
- **Method:** `GetFileExtension`
  - **Request:** `FilePathRequest` (contains `file_path: string`)
  - **Response:** `FileExtensionResponse` (contains `extension: string`)

See [`proto/file_extension.proto`](proto/file_extension.proto) for details.

## Integration

You can call this gRPC service from any language that supports gRPC (such as C#, Java, Go, etc.) using the provided proto definition.

## License

This project is licensed under the MIT License.