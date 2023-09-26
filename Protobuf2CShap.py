import os
import sys

from PathUtils import ExePath
from ProtobufUtils import GenerateAllProto2CShap

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '-p':
            if len(sys.argv) > 2:
                GenerateAllProto2CShap(sys.argv[2], sys.argv[3])
            else:
                GenerateAllProto2CShap(sys.argv[2], os.path.join(ExePath(), 'Scripts'))
    else:
        GenerateAllProto2CShap(os.path.join(ExePath(), 'Protos'), os.path.join(ExePath(), 'Scripts'))
