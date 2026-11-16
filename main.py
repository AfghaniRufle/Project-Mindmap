import tkinter
import keyboard
import os

def check_line_boot() : 
    pass 

def check_out_end(read) : 
    setpoint = "PROG_END"
    return read == setpoint

def print_error(type) : 
    print(type)
text = [] 
note = []
n = 0

EXPECTED = 1
with open("datafile.txt",'r') as file_opener : 
#Check dulu validitasnya 
    read = file_opener.readline()
    if not ('PROG_START' in read) : 
        print("INVALID CODE TEXT CODE 1-0")
        pass
    for read in file_opener :
        last = read.strip()
    if not(last == 'PROG_END') : 
        print("INVALID CODE TEXT CODE 1-1")
        pass
#READ
    file_opener.seek(0)
    EXPECTED = 1
    cache_note = ""
    cache = ""
    #READ PROGRAM/NOTE
    for read in file_opener : 
        if f"NOTE_{EXPECTED}_START" in read :
            if f"NOTE_{EXPECTED}_END" in read : 
                EXPECTED += 1
            footer_num = 1
            text.append([])
            for read in file_opener : 
                cache_note += read
                if f"FOOT_{footer_num}_START" in read :
                    cache = ""
                    # READ FOOT IN NOTE
                    for read in file_opener : 
                        if check_out_end(read) : print_error("ERROR IN FOOTREADER")
                        if f"FOOT_{footer_num}_END" in read :
                            if not(read.strip() == '') :
                                text[EXPECTED-1].append(cache)
                            footer_num += 1
                            break
                        cache += read
                        
#fungsi_untuk_membuat_GUI dan lain lain

# DEBUGGING
for i in range(len(text)):              # i = nomor baris
    for j in range(len(text[i])):       # j = nomor kolom
        print(i, j, text[i][j])
