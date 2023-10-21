import os.path
import platform
import re
import subprocess

from PyUtils import FileUtil, LogUtil
from Datas import ConfigData
from Datas.ConfigData import CfgData


def GenerateCsharpScript(proto_file, proto_dir, output_dir):
    # 获取当前操作系统信息
    current_os = platform.system()

    # 根据操作系统执行不同的命令
    if current_os == "Windows":
        command = (f"{CfgData.ProtoExePathData()} "
                   f"--proto_path={proto_dir} "
                   f"--csharp_out={output_dir} {proto_file}")
    elif current_os == "Darwin":
        command = (f"protoc "
                   f"--proto_path={proto_dir} "
                   f"--csharp_out={output_dir} {proto_file}")
    else:
        raise Exception("Unsupported operating system")
    # 调用protoc命令生成C#脚本
    try:
        subprocess.run(command, shell=True)
        LogUtil.ShowLog(f"调用protoc命令生成C#脚本: {proto_file}")
    except Exception as e:
        LogUtil.ShowLog(f"调用protoc命令生成C#脚本失败: {e}")


def GeneratePythonScript(proto_file, proto_dir, output_dir):
    # 根据操作系统执行不同的命令
    command = (f'python -m grpc_tools.protoc '
               f'--proto_path={proto_dir} '
               f'--python_out={output_dir} '
               f'{proto_file}')
    # 调用protoc命令生成Python脚本
    try:
        subprocess.run(command, shell=True)
        LogUtil.ShowLog(f"调用protoc命令生成Python脚本: {proto_file}")
    except Exception as e:
        LogUtil.ShowLog(f"调用protoc命令生成Python脚本失败: {e}")


def GenerateAllProto2Scripts():
    GenerateAllProto2CShap(CfgData.ProtoPathData(), ConfigData.CShapScriptsPath)
    GenerateAllProto2Python(CfgData.ProtoPathData(), ConfigData.PythonScriptsPath)


def GenerateAllProto2CShap(proto_dir, output_dir):
    FileUtil.DeleteDirFiles(output_dir)
    # 生成所有proto文件的C#脚本
    for root, dirs, files in os.walk(proto_dir):
        for file in files:
            if file.endswith('.proto'):
                GenerateCsharpScript(os.path.join(root, file), proto_dir, output_dir)
    FileUtil.DeleteDirFiles(CfgData.OutCShapScriptsPathData(), None, None, ['.meta'])
    FileUtil.CopyDirFiles(ConfigData.CShapScriptsPath, CfgData.OutCShapScriptsPathData())


def GenerateAllProto2Python(proto_dir, output_dir):
    FileUtil.DeleteDirFiles(output_dir, None, [CfgData.ProtoIdMapData()])
    # 生成所有proto文件的Python脚本
    for root, dirs, files in os.walk(proto_dir):
        for file in files:
            if file.endswith('.proto'):
                GeneratePythonScript(os.path.join(root, file), proto_dir, output_dir)
    # 修改Python脚本中的import语句
    for root, dirs, files in os.walk(ConfigData.PythonScriptsPath):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                # 使用正则表达式匹配并替换import语句
                content = re.sub(r'import (\w+_pb2) as (\w+)',
                                 rf'import {CfgData.ProtoModuleImportPrefixData()}.\1 as \2', content)

                with open(os.path.join(root, file), 'w', encoding='utf-8') as f:
                    f.write(content)
    FileUtil.DeleteDirFiles(CfgData.OutPythonScriptsPathData(), ['__pycache__'])
    FileUtil.CopyDirFiles(ConfigData.PythonScriptsPath, CfgData.OutPythonScriptsPathData())


def GenerateAllProtoIds():
    proto_dir = CfgData.ProtoPathData()
    # 生成所有proto文件的ID
    ids = {}
    for root, dirs, files in os.walk(proto_dir):
        for file in files:
            if (re.match(CfgData.ProtoClientPatternData(), file)
                    and CfgData.ProtosIdsNameData() not in file
                    and file.endswith('.proto')):

                ids[file] = ReadProtoFile(os.path.join(root, file))
    # 根据ids生成一个proto文件，里面是所有协议的枚举
    with open(os.path.join(proto_dir, CfgData.ProtosIdsNameData()), 'w', encoding='utf-8') as f:
        f.write('syntax = "proto3";\n\n')
        f.write('package myproto;\n\n')
        f.write('enum ID {\n')
        f.write('\tNONE = 0;\n')
        importDes = f"from {CfgData.ProtoModuleImportPrefixData()} import {CfgData.ProtosIdsNameData()[:-6]}_pb2,"
        messageMapDes = f"MessageMap = {{"
        idIndex = 0
        for key, value in ids.items():
            if len(value) > 0:
                idIndex += 1
                f.write(f'\n\t// {key}\n')
                for i in range(len(value)):
                    f.write(f'\tMsg_{value[i]} = {idIndex * 1000 + i};\n')
                protoName = f'{key[:-6]}_pb2'
                genProtoName = f'{CfgData.ProtosIdsNameData()[:-6]}_pb2'
                importDes += f' {protoName},'
                for msg in value:
                    messageMapDes += f'\n\t{genProtoName}.Msg_{msg}: {protoName}.{msg}(),'
                LogUtil.ShowLog(f'生成协议ID: {key}')
        # 去掉最后一个逗号
        importDes = importDes[:-1]
        messageMapDes = messageMapDes[:-1]

        messageMapDes += '\n}\n'
        FileUtil.WriteFileContent(os.path.join(ConfigData.PythonScriptsPath, CfgData.ProtoIdMapData()),
                                   f'{importDes}\n\n{messageMapDes}')
        f.write('}\n')


def ReadProtoFile(proto_file):
    # 读取proto文件,并且将所有的msg的名字提取出来
    with open(proto_file, 'r', encoding='utf-8') as f:
        message_names = re.findall(CfgData.ProtoMsgPatternData(), f.read())
    return message_names
