import time
from queue import Queue
from .file_monitor import file_monitor
from threading import Thread 

# Logs to save:
# 1) Auth(ssh) /var/log/auth.log
# 2) bash_history ~/.bash_history
# 3) httpd logs /var/log/httpd/
# 4) system messages /var/log/syslog
# 5) dmseg logs /var/log/dmesg

dic  = {
    'auth':'/var/log/auth.log',
    'bash_history':'/home/amanharitsh/.bash_history',
    'sys':'/var/log/syslog',
    'dmseg':'/var/log/dmesg'
}


FILE = '/var/log/auth.log'

# Starting Threads

def start_monitor(q):
    
    # Starting each thread with FILE and Type Parameter
    for typ,FILE in dic.items():
        t1 = Thread(target = file_monitor, args =(FILE, typ, q )) 
        t1.start()

    
