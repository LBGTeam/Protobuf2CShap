import os.path
import platform
import subprocess

from FileUtils import DeleteDirFiles
from PathUtils import ExePath


def GenerateCsharpScript(proto_file, proto_dir, output_dir):
    # 获取当前操作系统信息
    current_os = platform.system()

    # 根据操作系统执行不同的命令
    if current_os == "Windows":
        command = (f"{os.path.join(ExePath(), 'Libs', 'protoc', 'bin', 'protoc.exe')} "
                   f"--proto_path={proto_dir} "
                   f"--csharp_out={output_dir} {proto_file}")
    elif current_os == "Darwin":
        command = (f"protoc "
                   f"--proto_path={proto_dir} "
                   f"--csharp_out={output_dir} {proto_file}")
    else:
        raise Exception("Unsupported operating system")
        # 调用protoc命令生成C#脚本
    subprocess.run(command, shell=True)


def GenerateAllProto2CShap(proto_dir, output_dir):
    DeleteDirFiles(output_dir)
    # 生成所有proto文件的C#脚本
    for root, dirs, files in os.walk(proto_dir):
        for file in files:
            if file.endswith('.proto'):
                GenerateCsharpScript(os.path.join(root, file), proto_dir, output_dir)


