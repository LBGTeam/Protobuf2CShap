import os
import shutil

from Utils.LogUtil import ShowLog


def DeleteDirFiles(dir_path):
    if os.path.exists(dir_path):
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                os.remove(os.path.join(root, file))
                ShowLog(f'删除文件: {os.path.join(root, file)}')
            for mDir in dirs:
                os.rmdir(os.path.join(root, mDir))
                ShowLog(f'删除目录: {os.path.join(root, mDir)}')


def CopyDirFiles(origin_oath, target_path):
    if os.path.exists(origin_oath):
        for root, dirs, files in os.walk(origin_oath):
            for file in files:
                # 构建源文件路径和目标文件路径
                source_file = os.path.join(root, file)
                target_file = os.path.join(target_path, file)
                # 复制文件
                shutil.copy2(source_file, target_file)
                ShowLog(f'复制文件: {source_file} -> {target_file}')
            for mDir in dirs:
                # 构建源目录路径和目标目录路径
                source_dir = os.path.join(root, mDir)
                target_dir = os.path.join(target_path, mDir)
                # 复制目录
                shutil.copytree(source_dir, target_dir)
                ShowLog(f'复制目录: {source_dir} -> {target_dir}')
