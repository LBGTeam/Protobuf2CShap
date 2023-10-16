import os

from Utils import JsonUtil, PathUtil


class ConfigData:
    def __init__(self):
        self.JsonPath = PathUtil.ConfigsPath
        self.config = self.LoadJsonData()
        if not os.path.exists(self.JsonPath):
            self.InitJsonData()

    def InitJsonData(self):
        self.ProtoExePathData(PathUtil.DefProtosExePath)
        self.ProtoPathData(PathUtil.DefProtosPath)
        self.OutScriptsPathData('')

    def LoadJsonData(self):
        return JsonUtil.LoadJsonData(self.JsonPath)

    def ProtoExePathData(self, value=None):
        return self.JsonData('ProtoExePath', value)

    def ProtoPathData(self, value=None):
        return self.JsonData('ProtoPath', value)

    def OutScriptsPathData(self, value=None):
        return self.JsonData('OutScriptsPath', value)

    def JsonData(self, key, value=None):
        if value is not None:
            self.config[key] = value
            JsonUtil.SaveJsonData(self.JsonPath, self.config)
            return value
        if key in self.config.keys():
            return self.config[key]
        return None

    def SaveJsonData(self, jsonData):
        JsonUtil.SaveJsonData(self.JsonPath, jsonData)


CfgData = ConfigData()
