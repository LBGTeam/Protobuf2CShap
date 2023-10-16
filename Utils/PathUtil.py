import os
import sys


def ExePath():
    if hasattr(sys, 'frozen'):
        path_sys = os.path.dirname(sys.executable)
        return path_sys  # 使用pyinstaller打包后的exe目录
    path_py = os.path.dirname(__file__)
    return path_py  # 没打包前的py目录


def CheckPath(path):
    # 获取文件所在路径
    pathDir = os.path.dirname(path)
    # 如果路径不存在就创建路径
    os.makedirs(pathDir, exist_ok=True)
    # 如果路径是文件且文件不存在就创建文件
    if not os.path.exists(path) and os.path.isfile(path):
        with open(path, 'w') as f:
            f.write('')
    return os.path.abspath(path)


RootPath = os.path.abspath(os.path.join(ExePath(), '..'))
SavesPath = CheckPath(os.path.join(RootPath, 'Saves'))
ScriptsPath = CheckPath(os.path.join(RootPath, 'Scripts'))
DefProtosExePath = os.path.join(RootPath, 'Libs', 'protoc', 'bin', 'protoc.exe')
DefProtosPath = CheckPath(os.path.join(RootPath, 'Protos'))
ConfigsPath = CheckPath(os.path.join(SavesPath, 'Config.json'))
