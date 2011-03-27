class Connector:
    EventHAndler = None
    def HandleResponse(self,eventInfo):pass
    def SetEventHandler(self,func):
        self.eventHandler=func
    def Start(self):pass
    def Stop(self):pass
    def GetResponseObject(self):pass
