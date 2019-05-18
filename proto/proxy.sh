#! /bin/sh

# full directory name of current script
SCRIPT_PATH="$( cd "$(dirname -- "$0")" ; pwd -P )"
#echo "$SCRIPT_PATH"

PROTO_PATH="$SCRIPT_PATH/proxy.proto"
#echo "$PROTO_PATH"

if [ -f "$PROTO_PATH" ]; then
  PROTOC_COMM='python -m grpc_tools.protoc -I'$SCRIPT_PATH' --python_out='$SCRIPT_PATH' --grpc_python_out='$SCRIPT_PATH' '$PROTO_PATH
  echo "Executing command:"
  echo "    "$PROTOC_COMM
  $PROTOC_COMM
  echo "Execution returned code: $?"
else
  echo "'$PROTO_PATH' definition not found"
fi

