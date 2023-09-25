import os.path
import subprocess

from PathUtils import ExePath


def GenerateCsharpScript(proto_file, proto_dir, output_dir):
    # 调用protoc命令生成C#脚本
    command = (f"{os.path.join(ExePath(), 'Libs', 'protoc', 'bin', 'protoc.exe')} "
               f"--proto_path={proto_dir} "
               f"--csharp_out={output_dir} {proto_file}")
    subprocess.run(command, shell=True)


def GenerateAllProto2CShap(proto_dir, output_dir):
    # 生成所有proto文件的C#脚本
    for root, dirs, files in os.walk(proto_dir):
        for file in files:
            if file.endswith('.proto'):
                GenerateCsharpScript(os.path.join(root, file), proto_dir, output_dir)

