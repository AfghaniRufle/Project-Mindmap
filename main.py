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
foot = [] 
note = []
n = 0

#MAIN
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
    file_opener.seek(0)

#READ THE TEXT FILE AND MAKE ARRAY
    EXPECTED = 1
    footer_num = 1
    cache_note = ""
    cache = ""

    #READ NOTE
    for read in file_opener : 
        if f"NOTE_{EXPECTED}_END" in read : 
            EXPECTED += 1
            note.append(cache_note)
            cache_note = ""

        cache_note += read

        if f"NOTE_{EXPECTED}_START" in read :
            file_opener.readline()
            footer_num = 1
            foot.append([])
        # READ FOOT IN NOTE   
        if f"FOOT_{footer_num}_START" in read :
            for read in file_opener : 
                if f"FOOT_{footer_num}_END" in read :
                            if read.strip() == '' :
                                break
                            foot[EXPECTED-1].append(cache)        
                            footer_num += 1
                            cache = ""
                            break
                cache += read
            
#READ THE ARRAY AND MAKE PROGRAM

# DEBUGGING
for i in range(len(foot)):              # i = nomor baris
    for j in range(len(foot[i])):       # j = nomor kolom
        print(i, j, foot[i][j])

print(f"TEST : Cache_note : {cache_note}")
