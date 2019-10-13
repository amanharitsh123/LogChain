import time

def file_monitor(FILE, typ, q):
    prev = ''
    while True:
        file_pt = open(FILE,'r')
        lines = file_pt.readlines()
        i = -1
        if lines[i] == prev:
            time.sleep(1)
            continue
        else:
            t = prev
            prev = lines[-1]
            for line in lines[::-1]:
                if line == t:
                    break
                q.put((typ,line))
