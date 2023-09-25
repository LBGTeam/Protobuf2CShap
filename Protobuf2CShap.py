import os

from PathUtils import ExePath
from ProtobufUtils import GenerateAllProto2CShap

if __name__ == '__main__':
    GenerateAllProto2CShap(os.path.join(ExePath(), 'Protos'), os.path.join(ExePath(), 'Scripts'))
