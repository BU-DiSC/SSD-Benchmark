from helper import *
pattern="*_*_*.txt"
match_dict = {
    "seq":"sequential",
    "rand":"random",
    "w":"write",
    "r":"read",
    "4k":"4k",
    "4m":"4m",
    "8k":"8k",
    "128k":"128k"
}
#change this to where results are
read_dir="./results/zns_4t/"
list_of_file = get_file_with_name(read_dir, pattern)
t = []
#preprocess
for i in list_of_file:
    t.append(validir(i)[:-1])
list_of_file = t
print (list_of_file)


#function to process a result file
def proc_file(filedir):
    flist = get_list_from_file(filedir)
    filename = filedir.split("/")[-1].split(".")[0].split("_")
    block_size = match_dict[filename[0]]
    rwmode = match_dict[filename[1]]
    threads = filename[2]
    #remove all spaces
    t = []
    try:
        for i in flist:
            tr = i.replace(" ", "")
            #split by colon
            seg = tr.split(":")
            if(seg[0].split("(")[0] == "clat"):
                clat = str(round(float(seg[1].split(",")[2].split("=")[1]))) + " " + seg[0].split("(")[1].split(")")[0]
            elif(seg[0].split("(")[0] == "bw"):
                if(seg[0].split("(")[1].split(")")[0] == "KiB/s"):
                    bw = str(round(float(seg[1].split(",")[3].split("=")[1])/1024)) + " MiB/s"
                elif(seg[0].split("(")[1].split(")")[0] == "MiB/s"):
                    bw = str(round(float(seg[1].split(",")[3].split("=")[1]))) + " " + seg[0].split("(")[1].split(")")[0]
            elif (seg[0] == "iops"):
                iops = str(round(float(seg[1].split(",")[2].split("=")[1])))
            elif(seg[0] == "cpu"):
                cpu = str(round((float(seg[1].split(",")[0].split("=")[1][:-1]) + float(seg[1].split(",")[1].split("=")[1][:-1])) * int(threads)))
        res = str(block_size) + " " + rwmode + " [Threads]: " + str(threads) + " [IOPS]: " + iops + " [Bandwidth]: " + str(bw) + " [Latency]: " + clat + " [CPU]: " + cpu
    except:
        res = filename
    return res


for i in list_of_file:
    print(proc_file(i))