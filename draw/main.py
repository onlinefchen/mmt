from device import *
from pc import *
from trigger import *
from view import *


def init_first_env():
    local_windows = windows()
    local_device = device()
    local_windows.cmd("adb reboot bootloader")
    print "update image .... begin"
    local_windows.exec_bat("D:/Chicago/first/image/update_sec_hi3660.bat")
    print "wait for device ..."
    local_device.wait_device("")
    print "install apk ..."
    local_windows.exec_bat("D:/Test-Tool/all_in_one/install.bat")
    print "push ..."
    local_windows.cmd("adb push iontest /data")
    local_windows.cmd("adb shell chmod +x /data/iontest")
    local_windows.cmd("adb reboot")
    local_device.wait_device("")

def init_second_env():
    local_windows = windows()
    local_windows.cmd("adb reboot bootloader")
    print "update image .... begin"
    local_windows.exec_bat("D:/Chicago/second/image/update_sec_hi3660.bat")
    print "wait for device ..."
    #local_windows.cmd("adb reboot bootloader")
    #local_windows.cmd("fastboot flash boot Z:\work\hione\out\target\product\hi3660\sec_boot.img reboot")
    local_device.wait_device("")
    print "install apk ..."
    local_windows.exec_bat("D:/Test-Tool/all_in_one/install.bat")
    local_windows.cmd("adb push iontest /data")
    local_windows.cmd("adb shell chmod +x /data/iontest")
    local_windows.cmd("adb reboot")
    local_device.wait_device("")
    
if __name__ == '__main__':
    times = 1000
    local_trigger = trigger()
    local_device = device()
    local_view = view()

    file_apk_list = open("./apk.txt")
    infolist = ["slabs_scanned", "pgscan_kswapd_dma", "pgscan_kswapd_normal", "compact_migrate_scanned", "compact_free_scanned",
                "allocstall", "compact_success", "compact_stall" ,"compact_daemon_wake","pgsteal_kswapd_dma", "pgsteal_kswapd_normal", "pswpin" , "pswpout",
                "allocstall", "compact_daemon_wake", "compact_success"]
    exec_cmd = "time ./data/iontest --alloc --len 536870912 -h 1 -f 8"
    result_old = "orig.txt"
    result_new = "new.txt"
    
    init_first_env()
    local_device.get_apk_list("./apk.txt")
    apk_list = file_apk_list.readlines()
    local_trigger.trigger_init(result_old)
    for i in range(times):
        for line in apk_list:
            print "start apk .." + line
            local_device.run_one_apk(line)
            ret = local_trigger.trigger(result_old, "iontest" , exec_cmd, infolist)
            if int(ret) > 0:
                break
        if int(ret) > 0:
            break

    init_second_env()
    local_device.get_apk_list("./apk.txt")
    apk_list = file_apk_list.readlines()
    local_trigger.trigger_init(result_new)
    for i in range(times):
        for line in apk_list:
            print "start apk .." + line
            local_device.run_one_apk(line)
            ret = local_trigger.trigger(result_new, "iontest" , exec_cmd, infolist)
            if int(ret) > 0:
                break
        if int(ret) > 0:
            break
     
    local_view.draw_compare_figure(result_old, result_new, "", "memory.png")
