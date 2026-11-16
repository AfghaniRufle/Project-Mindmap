import tkinter
import keyboard
import os

def check_line_boot() : 
    pass 

text = [] 
n = 0

EXPECTED = 1
with open("datafile.txt",'r') as file_opener : 
#Check dulu validitasnya 
    read = file_opener.readline()
    if not ("PROG_START" in read) : 
        print("INVALID CODE TEXT CODE 1")
        pass
    for read in file_opener :
        last = read.strip
    if not(last == "PROG_END") : 
        print("INVALID CODE TEXT CODE 1")
        pass
#READ
    file_opener.seek(0)
    EXPECTED = 1
    cache_note = ""
    cache = ""
    for read in file_opener : 
        if f"NOTE_{EXPECTED}_START" in read :
            if f"NOTE_{EXPECTED}_END" in read : 
                text.append()
                EXPECTED += 1

            footer_num = 1
            text.append([])
            for read in file_opener : 
                cache_note += read
                if f"FOOT_{footer_num}_START" in read :
                    cache = ""
                    for read in file_opener : 
                        if f"FOOT_{footer_num}_END" in read :
                            text[EXPECTED-1].append(cache)
                            footer_num =+ 1
                            break
                        cache += read
                        
#fungsi_untuk_membuat_GUI dan lain lain

# DEBUGGING
for r1 in text : 
    for r2 in r1 : 
        print(r2)
