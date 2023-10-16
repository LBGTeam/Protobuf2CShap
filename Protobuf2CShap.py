import sys

from ProtobufUtils import GenerateAllProto2Scripts, GenerateAllProtoIds
from Utils import  LogUtil

if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == '-g':
            GenerateAllProtoIds()
        else:
            LogUtil.ShowLog('参数错误')
    else:
        GenerateAllProto2Scripts()
