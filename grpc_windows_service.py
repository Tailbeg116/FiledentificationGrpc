import win32serviceutil
import win32service
import win32event
import servicemanager
import sys
import os

class GrpcServerService(win32serviceutil.ServiceFramework):
    _svc_name_ = "GrpcFileExtensionService"
    _svc_display_name_ = "gRPC File Extension Service"
    _svc_description_ = "A gRPC service to detect file extensions using Magika."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.server = None

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        if self.server:
            self.server.stop(0)

    def SvcDoRun(self):
        import grpc_server  # Import here to avoid issues with service manager
        servicemanager.LogInfoMsg("Starting gRPC File Extension Service...")
        self.server = grpc_server.serve(blocking=False)
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)
        servicemanager.LogInfoMsg("gRPC File Extension Service stopped.")

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(GrpcServerService)