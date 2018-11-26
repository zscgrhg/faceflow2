pip freeze > requirements.txt

python -m grpc_tools.protoc --proto_path=./protos --python_out=./faces --grpc_python_out=./faces ./protos/facematrix.proto