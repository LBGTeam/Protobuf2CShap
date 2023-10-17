import os
import shutil

from Utils.LogUtil import ShowLog


def DeleteDirFiles(dir_path, ignore_Dir=None, ignore_File=None):
    if os.path.exists(dir_path):
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if ignore_File is not None and file in ignore_File:
                    continue
                os.remove(os.path.join(root, file))
                ShowLog(f'删除文件: {os.path.join(root, file)}')
            for mDir in dirs:
                if ignore_Dir is not None and mDir in ignore_Dir:
                    continue
                os.rmdir(os.path.join(root, mDir))
                ShowLog(f'删除目录: {os.path.join(root, mDir)}')


def CopyDirFiles(origin_oath, target_path, ignore_Dir=None, ignore_File=None):
    if os.path.exists(origin_oath):
        for root, dirs, files in os.walk(origin_oath):
            for file in files:
                if ignore_File is not None and file in ignore_File:
                    continue
                # 构建源文件路径和目标文件路径
                source_file = os.path.join(root, file)
                target_file = os.path.join(target_path, file)
                # 复制文件
                shutil.copy2(source_file, target_file)
                ShowLog(f'复制文件: {source_file} -> {target_file}')
            for mDir in dirs:
                if ignore_Dir is not None and mDir in ignore_Dir:
                    continue
                # 构建源目录路径和目标目录路径
                source_dir = os.path.join(root, mDir)
                target_dir = os.path.join(target_path, mDir)
                # 复制目录
                shutil.copytree(source_dir, target_dir)
                ShowLog(f'复制目录: {source_dir} -> {target_dir}')


def WriteFileContent(file_path, content):
    # 如果文件不存在就创建文件
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write(content)
            f.close()
            ShowLog(f'创建文件: {file_path}')
    # 如果文件存在就覆盖文件内容
    with open(file_path, 'w') as f:
        f.write(content)
        f.close()
        ShowLog(f'写入文件: {file_path}')
