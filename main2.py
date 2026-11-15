
dat_read = ""
expect = 1
with open("datafile.txt",'r') as f : 
    for line in f : 
        if f"FOOT_{expect}_START" in line : 
            #f.readline() ada loop coy
            for line in f :
                if f"FOOT_{expect}_END" in line : 
                    break
                dat_read += line

print(dat_read)
        


        