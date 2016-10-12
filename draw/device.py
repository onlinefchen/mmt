from pc import *
from library import *
from operator import *
import time

class device:
    meminfo = ""
    vmstat = ""
    camera = ""
    def cmd(self, cmd, dev = None):
        if dev is None:
            adb_cmd = 'adb shell "%s"' % (cmd)
        else:
            adb_cmd = 'adb -s %s "%s"' % (dev, cmd)
        try:
            ret = os.popen(adb_cmd).readlines()
        except:
            print "adb_shell exec error"
            raise Exception("adb port not connected!")
        #return "".join(ret)
        return "".join(ret).replace('\r', '')
    
    # init the device info meminfo and vmstat
    def init_device_info(self):
        local_windows = windows()
        device.meminfo = local_windows.cmd("adb shell cat /proc/meminfo")
        device.vmstat = local_windows.cmd("adb shell cat /proc/vmstat")
        
    def get_device_info(self, single_info):
        local_windows = windows()
        local_device = device()
        local_lib = lib()
        local_device.init_device_info()
        for var in device.meminfo.split('\n'):
            if var.find(single_info) >= 0:
                number = int(local_lib.get_str_first_value(var))
                return number
        
        for var in device.vmstat.split('\n'):
            if var.find(single_info) >= 0:
                number = int(local_lib.get_str_first_value(var))
                return number
    
    def get_info_list(self, infolist):
        local_device = device()
        valuelist = []
        for i in range(len(infolist)):
            info = local_device.get_device_info(str(infolist[i]))
            valuelist.append(str(infolist[i]) + " " + str(info) + " ")
        valuelist.append(" ")
        return str("".join(valuelist))
    
    def run_one_apk(self, param):
        local_device = device()
        exec_param = 'am start -n %s' % (param)
        #print exec_param
        local_device.cmd(exec_param)
        return 0
    
    def stop_one_apk(self, param):
        local_device = device()
        exec_param = 'am force-stop %s' % (param)
        #print exec_param
        local_device.cmd(exec_param)
        return 0
    
    def get_apk_list(self, Param):
        local_window = windows()
        print "monkey..."
        ret = local_window.cmd("adb shell monkey --port 88888888 -v -v")
        print "monkey... end"
        file_apk_list = open(Param, 'w')
        apk_activity = ""
        apklist = []
        for line in ret.split('\n'):
            if line.find('Using main activity') >= 0:
                apk_activity = line.split()[5]
                apk_package = line.split()[8].strip(')')
                apklist.append(apk_package + '/' + apk_activity)
        for i in range(len(apklist)):
            if apklist[i].find('huawei.camera') >= 0 or apklist[i].find('huawei.camera') >= 0:
                device.camera = apklist[i]
                continue
            print apklist[i]
            file_apk_list.write(apklist[i] + "\n")
        #print device.camera
    
    def wait_device(self,param):
        local_windows = windows()
        local_windows.cmd("adb wait-for-device") 
        while True: 
            out = local_windows.cmd("adb shell getprop service.bootanim.exit") 
            if contains("".join(out), "1"): 
                break
            time.sleep(1)
        local_windows.cmd("adb shell svc power stayon true") 
        local_windows.cmd('adb shell input keyevent 82')
        local_windows.cmd('adb shell input keyevent 82')
        
        

# if __name__ == '__main__':
#     local_device = device()
#     local_device.get_apk_list("./tmplist.txt")
#     MemAvailable = local_device.get_device_info("MemAvailable")
#     compact_success = local_device.get_device_info("compact_success")
#     print MemAvailable + compact_success 
#       
#     info_list = ["MemFree", "MemAvailable", "slabs_scanned"]
#     ret = local_device.get_info_list(info_list)
#     local_device.run_one_apk("com.android.gallery3d/com.huawei.gallery.app.HwCameraPhotoActivity")
#     print ret
    
