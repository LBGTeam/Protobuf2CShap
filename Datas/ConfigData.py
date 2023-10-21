import os

from PyUtils import JsonUtil, PathUtil


SavesPath = PathUtil.CheckPath(os.path.join(PathUtil.RootPath, 'Saves'), True)
ProtosPath = PathUtil.CheckPath(os.path.join(PathUtil.RootPath, 'Protos'), True)
CShapScriptsPath = PathUtil.CheckPath(os.path.join(PathUtil.RootPath, 'CShapScripts'), True)
PythonScriptsPath = PathUtil.CheckPath(os.path.join(PathUtil.RootPath, 'PythonScripts'), True)
DefProtosExePath = os.path.join(PathUtil.RootPath, 'Libs', 'protoc', 'bin', 'protoc.exe')
DefProtosPath = PathUtil.CheckPath(os.path.join(PathUtil.RootPath, 'Protos'), True)
ConfigsPath = PathUtil.CheckPath(os.path.join(SavesPath, 'Config.json'))


class ConfigData:
    def __init__(self):
        self.JsonPath = ConfigsPath
        self.config = self.LoadJsonData()
        if not os.path.exists(self.JsonPath):
            self.InitJsonData()

    def InitJsonData(self):
        self.ProtoExePathData(DefProtosExePath)
        self.ProtoPathData(DefProtosPath)
        self.OutCShapScriptsPathData('')
        self.OutPythonScriptsPathData('')
        self.ProtosIdsNameData('client_gen.proto')
        self.ProtoClientPatternData(r'^client_|common\.proto$')
        self.ProtoMsgPatternData(r'message\s+(\w+(?:REQ|ACK|PUSH))')
        self.ProtoModuleImportPrefixData('Network.ProtoPB2')
        self.ProtoIdMapData('ProtoGen.py')

    def LoadJsonData(self):
        return JsonUtil.LoadJsonData(self.JsonPath)

    def ProtoExePathData(self, value=None):
        return self.JsonData('ProtoExePath', value)

    def ProtoPathData(self, value=None):
        return self.JsonData('ProtoPath', value)

    def OutCShapScriptsPathData(self, value=None):
        return self.JsonData('OutCShapScriptsPath', value)

    def OutPythonScriptsPathData(self, value=None):
        return self.JsonData('OutPythonScriptsPath', value)

    def ProtoClientPatternData(self, value=None):
        return self.JsonData('ProtoClientPattern', value)

    def ProtosIdsNameData(self, value=None):
        return self.JsonData('ProtosIdsName', value)

    def ProtoMsgPatternData(self, value=None):
        return self.JsonData('ProtoMsgPattern', value)

    def ProtoModuleImportPrefixData(self, value=None):
        return self.JsonData('ProtoModuleImportPrefix', value)

    def ProtoIdMapData(self, value=None):
        return self.JsonData('ProtoIdMap', value)

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
