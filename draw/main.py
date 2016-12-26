from device import *
from pc import *
from trigger import *
from view import *


def init_exec_env(param):
    local_linux = linux()
    local_device = device()
    local_linux.cmd("adb reboot bootloader")
    print "update image .... begin"
    local_linux.exec_bat(param)
    print "wait for device ..."
    local_device.wait_device("")
    print "install apk ..."
    local_linux.exec_bat("D:/Test-Tool/all_in_one/install.bat")
    print "push ..."
    local_linux.cmd("adb push iontest /data")
    local_linux.cmd("adb shell chmod +x /data/iontest")
    local_linux.cmd("adb reboot")
    local_device.wait_device("")

def do_test(test, infolist, exec_cmd):
    i = 0
    times = 100000
    local_trigger = trigger()
    apklist = test + "apklist.txt"
    local_device.get_apk_list(apklist)
    file_apk_list = open(apklist)
    apk_list = file_apk_list.readlines()
    local_trigger.trigger_init(test)
    for i in range(times):
        for line in apk_list:
            print "start apk " + line
            local_device.run_one_apk(line)
            ret = local_trigger.trigger(test, "iontest" , exec_cmd, infolist)
            if int(ret) > 0:
                break
        if int(ret) > 0:
            break
    file_apk_list.close()

if __name__ == '__main__':
    local_device = device()
    local_view = view()
    exec_cmd = "time ./data/iontest --alloc --len 536870912 -h 1 -f 8"
    infolist = ["slabs_scanned", "pgscan_kswapd_dma", "pgscan_kswapd_normal", "compact_migrate_scanned", "compact_free_scanned",
                "allocstall", "compact_success", "compact_stall" ,"compact_daemon_wake","pgsteal_kswapd_dma", "pgsteal_kswapd_normal", "pswpin" , "pswpout",
                "allocstall", "compact_daemon_wake", "compact_success"]
        
    first_test = "4+0.5"
    sec_test = "2+2"
    #init_exec_env("D:/Chicago/first/image/update_sec_hi3660.bat")
    do_test(first_test, infolist, exec_cmd)
    #init_exec_env("D:/Chicago/secound/image/update_sec_hi3660.bat")
    do_test(sec_test, infolist, exec_cmd)
    local_view.draw_compare_figure(first_test, sec_test, "", "memory.png")
