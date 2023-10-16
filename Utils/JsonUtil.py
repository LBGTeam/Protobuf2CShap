import json
import os

from Utils.LogUtil import ShowLog


def LoadJsonData(filePath):
    jsonData = {}
    if os.path.exists(filePath):
        with open(filePath, 'r') as f:
            jsonData = json.load(f)
    ShowLog(f'加载Json文件: {filePath}')
    return jsonData


def SaveJsonData(filePath, jsonData):
    # 获取文件夹路径
    folderPath = os.path.dirname(filePath)
    # 如果文件夹不存在，则创建文件夹
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    with open(filePath, 'w') as f:
        json.dump(jsonData, f, indent=4, ensure_ascii=False)
    ShowLog(f'保存Json文件: {filePath}')
