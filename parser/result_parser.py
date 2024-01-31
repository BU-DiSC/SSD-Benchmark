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
res = [",Threads,IOPS,Bandwidth(MB/s),Latency(usec/msec),CPU"]
read_dir= "E:/Code/fio-bench/fio-bench-config/results/p4510_legacy/"
output = "./bench_result.csv"
list_of_file = get_file_with_name(read_dir, pattern)
t = []
#preprocess
for i in list_of_file:
    t.append(validir(i)[:-1])
list_of_file = t
#print (list_of_file)


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
                clat_raw = round(float(seg[1].split(",")[2].split("=")[1]))
                if(seg[0].split("(")[1].split(")")[0] == "usec"):
                    clat = str(clat_raw) + " " + seg[0].split("(")[1].split(")")[0]
                elif((seg[0].split("(")[1].split(")")[0] == "msec")):
                    #clat = str(clat_raw * 1000) + " " + seg[0].split("(")[1].split(")")[0]
                    clat_raw *= 1000
                    clat = str(clat_raw) + " " + "usec"
                elif ((seg[0].split("(")[1].split(")")[0] == "nsec")):
                    # clat = str(clat_raw * 1000) + " " + seg[0].split("(")[1].split(")")[0]
                    clat_raw /= 1000
                    clat = str(round(clat_raw)) + " " + "usec"
            elif(seg[0].split("(")[0] == "bw"):
                if(seg[0].split("(")[1].split(")")[0] == "KiB/s"):
                    bw_raw = str(round(float(seg[1].split(",")[3].split("=")[1])/1024))
                    bw = bw_raw + " MiB/s"
                elif(seg[0].split("(")[1].split(")")[0] == "MiB/s"):
                    bw_raw = str(round(float(seg[1].split(",")[3].split("=")[1])))
                    bw = bw_raw + " " + seg[0].split("(")[1].split(")")[0]
            elif (seg[0] == "iops"):
                iops = str(round(float(seg[1].split(",")[2].split("=")[1])))
            elif(seg[0] == "cpu"):
                cpu = str(round((float(seg[1].split(",")[0].split("=")[1][:-1]) + float(seg[1].split(",")[1].split("=")[1][:-1])) * int(threads)))
        res = str(block_size) + " " + rwmode + " [Threads]: " + str(threads) + " [IOPS]: " + iops + " [Bandwidth]: " + str(bw) + " [Latency]: " + clat + " [CPU]: " + cpu
        csv_entry = ",".join([str(block_size) + " " + rwmode,str(threads),iops,str(bw_raw),str(clat_raw),cpu])
    except:
        res = filename
        csv_entry = "None"

    return res, csv_entry, str(block_size) + " " + rwmode, int(threads)

#serialize for output
def serialize(input_dict, initial_list = []):
    out = initial_list
    for key in input_dict:
        for i in input_dict[key]:
            out.append(i[1])
    return out

#sort list
def sort_list(unsort_list, idx):
    return sorted(unsort_list, key = lambda x:x[idx])

#temp result
tr = {}
#extract elements from list and add to dict
for i in list_of_file:
    t = proc_file((i))
    key = t[2]
    print(t[0])
    #res.append(t[1])
    if(key in tr):
        val = tr.get(key)
        val.append([t[3],t[1]])
        tr[key] = val
    else:
        tr[key] = [[t[3],t[1]]]

#sort the dict based on threads
for key in tr:
    tr[key] = sort_list(tr[key],0)

#prepare for output
res = serialize(tr,res)
#output file
writefile(output, res)

