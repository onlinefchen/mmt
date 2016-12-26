import os
import subprocess

class windows:
    def cmd(self, cmd):
        try:
            ret = os.popen(cmd).readlines()
        except:
            print "exec error"
        return "".join(ret).replace('\r', '') #return a string
    
    def exec_bat(self, bat_path):
        cur_dir = os.getcwd()
        bat = os.path.basename(bat_path)
        image_dir = os.path.dirname(bat_path)
        os.chdir(image_dir)
        bat_run = subprocess.Popen(bat, stdin=subprocess.PIPE)
        bat_run.communicate("")
        self.cmd("adb wait-for-device")
        os.chdir(cur_dir)

class linux:
    def cmd(self, Param):
        list = os.popen(Param).readlines()
        for line in list:
            line.strip("\n")
            line.strip("\r")
            #print len(list)
            return list

            
#if __name__ == '__main__':
    ##local_windows = windows()
    ##ret = local_windows.cmd("adb shell cat /proc/meminfo")
    #local_windows = windows()
    #ret = local_windows.cmd("adb shell cat /proc/meminfo")
    #print ret.split()
