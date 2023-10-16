import sys

from ProtobufUtils import GenerateAllProto2CShap
from Utils import PathUtil, LogUtil
from Datas.ConfigData import CfgData

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '-p':
            if len(sys.argv) > 2:
                GenerateAllProto2CShap(sys.argv[2], sys.argv[3])
            else:
                GenerateAllProto2CShap(sys.argv[2], PathUtil.ScriptsPath)
        else:
            LogUtil.ShowLog('参数错误')
    else:
        GenerateAllProto2CShap(CfgData.ProtoPathData(), PathUtil.ScriptsPath)
