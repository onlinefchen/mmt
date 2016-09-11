import os
from curses.ascii import isdigit
from lib import *
from app import *
from view import *
from linux_cmd import linux

class device:
    
    meminfo = ""
    vmstat = ""
    
    def init_device_info(self, Param):
        local_linux = linux()
        device.meminfo = local_linux.cmd("adb shell cat /proc/meminfo")
        device.vmstat = local_linux.cmd("adb shell cat /proc/vmstat")
        #print device.meminfo
        #print device.vmstat
        
    def get_device_info(self, Param):
        local_lib = lib()
        local_device = device()
        local_device.init_device_info("");
        #print "get info " + Param
        i = 0
        for i in range(len(device.meminfo)):
            #print "look " + Param + " in meminfo " +  str(device.meminfo[i])
            if Param in str(device.meminfo[i]):
                number = int(local_lib.get_str_first_value(device.meminfo[i]))
                #print number
                #print Param + str(number) + " " + "in meminfo"
                return number
        i = 0
        for i in range(len(device.vmstat)):
            #print "look " + Param + " in  vmstat " +  str(device.vmstat[i])
            if Param in str(device.vmstat[i]):

                number = int(local_lib.get_str_first_value(device.vmstat[i]))
                #print number
                #print Param + str(number) + " " + "in vmstat"
                return number

            
    def get_list_info(self, infolist):
        local_device = device()
        valuelist = []
        for i in range(len(infolist)):
            info = local_device.get_device_info(str(infolist[i]))
            valuelist.append(str(infolist[i]) + " " + str(info) + " ")
        return str("".join(valuelist))
        
                    
if __name__ == '__main__':
    local_device = device()
    local_app = app()
    local_view = view()
    orig = "without"
    new = "withpatch"
    app_list = open("./littleapp.txt").readlines()
    orig_log = open(orig, "a+")
    new_log = open(new, "a+")
    infolist = ["nr_free_pages","nr_inactive_anon","nr_active_anon","nr_inactive_file", 
                "nr_active_file", "nr_unevictable", "nr_mlock", "nr_anon_pages", 
                "nr_mapped", "nr_file_pages", "compact_migrate_scanned", "compact_isolated", 
                "pgrefill_dma32", "pgrefill_normal", "pgsteral_kswapd_dma32", "pgsteal_kswapd_normal",
                "pgsteal_direct_dma32", "pgsteal_direct_normal", "pgscan_kswapd_dma32", "pgscan_kswapd_normal",
                "pgscan_direct_dma32", "pgscan_direct_normal", "slabs_scanned", "unevictable_pgs_munlocked",
                "MemFree", "MemAvailable", "slabs_scanned"]
#     infolist = ["slabs_scanned", "pgscan_direct_normal", "pgscan_kswapd_normal", "MemFree"]
#     infolist = ["slabs_scanned"]
    
#     for i in range(len(app_list)):
#         local_app.lunch_app(app_list[i])
#         to_write = local_device.get_list_info(infolist)
#         orig_log.write(str(to_write) + "\n")
#     orig_log.close()
#         
#     for i in range(len(app_list)):
#         local_app.lunch_app(app_list[i])
#         to_write = local_device.get_list_info(infolist)
#         new_log.write(str(to_write) + "\n")
#     new_log.close()
        
    local_view.draw_compare_figure(orig, new)

