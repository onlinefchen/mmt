from device import *
from library import *

class trigger:
    num = 0
    test_time = 500  # The max trigger time
    result_log = ""
    
    def trigger_init(self, param):
        trigger.result_log = open(param, "w")
        trigger.num = 0
        trigger.test_time = 500
        trigger.result_log.close()
        
    def do_exec_work(self, cmdname, cmd):
        local_device = device()
        local_lib = lib()
        ret = local_device.cmd(cmd)
        time = local_lib.get_exec_time(ret)
        to_write = str(cmdname + " " + str(time) + "\n")
        trigger.result_log.write(to_write);
    
    def do_write_result(self, infolist):
        local_device = device()
        to_write = local_device.get_info_list(infolist)
        trigger.result_log.write(to_write);
        
        
    def trigger(self, resultlog, cmdname, cmd, infolist):
        trigger.result_log = resultlog
        local_trigger = trigger()
        free_trigger = 153600; #freemem less than 150MB
        local_device = device()
        local_lib = lib()
        log_param = str(resultlog)
        trigger.result_log = open(log_param, "a+")
        #active_file = get_first_number(local_device.get_meminfo("Active(file)")) 
        #inactive_file = get_first_number(local_device.get_meminfo("Inactive(file)"))
        
        #Set the trigger here
        mem_free = local_lib.get_str_first_value(local_device.get_device_info("MemFree"))
        if mem_free < free_trigger:
            if int(trigger.num) > trigger.test_time:
                return 1
            trigger.num = int(trigger.num) + 1
            local_trigger.do_write_result(infolist)
            local_trigger.do_exec_work(cmdname, cmd)
            local_device.cmd("echo 10000000 > /d/ion/heaps/sys_heap_shrink")
        trigger.result_log.close()
        return 0
    
# if __name__ == '__main__':
#     local_trigger = trigger()
#     cmdlist = ["cat /proc/meminfo" , "logcat -c" , "cat /d/ion/heaps/sys_heap"]
#     infolist = ["MemFree", "MemAvailable", "slabs_scanned"]
#     local_trigger.trigger("test", cmdlist, infolist)
