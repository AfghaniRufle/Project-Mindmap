
text = []
y = 0
def blakon() : 
    global y
    y += 1 
    return f"UYAYAYA_{y}"

text.append([])
text.append([])
text.append([])
text.append([])
text.append([])
text[0].append(blakon())
text[0].append(blakon())
text[3].append(blakon())
text[4].append(blakon())

for i in range(len(text)):              # i = nomor baris
    for j in range(len(text[i])):       # j = nomor kolom
        print(i, j, text[i][j])




"""
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
"""


        