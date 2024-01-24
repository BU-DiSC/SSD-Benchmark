# -*- coding: UTF-8 -*-
"""
Author: JLU
Helper functions for general usage
V1.10
Updated:20230819
"""
import progressbar, shutil, os, subprocess, glob, multiprocessing, ntpath, shlex, filecmp, random, string
import requests as req
from datetime import datetime
from multiprocessing.pool import ThreadPool

resurl = "https://www.asleague.org/res/sra/"
defaultdir = "./"


#get system type
def get_os_type():
    res = str(os.name)
    #return linux for posix(linux is more common) or windows for windows
    if(res == "posix"):
        return "linux"
    elif(res == "nt"):
        return "windows"
    else:
        return 2
        
#obtain file from a remote resource location
def getfile(loc, fname, rurl = resurl): 
    scri = req.get(rurl + fname, allow_redirects=True)
    open(validir(loc) + fname, "wb").write(scri.content)
    return
#obtain a single file
def getfile_d(loc, fname, url):
    scri = req.get(url, allow_redirects=True)
    loc = validir(loc)
    open(loc + fname, "wb").write(scri.content)
    return
#validate url is in correct format
#by default replace all "\" with "/", add "/" at the end if not exist.
#if replace == False, no replace happens. if inputurl ends with "/" or "\" nothing happens, else "/" will be appended.
def validir(inputurl, replace = True):
    if (replace == True):
        inputurl = inputurl.replace("\\", "/")
        if (inputurl[-1] == "/"):
            return inputurl
        return (inputurl + "/")
    else:
        if (inputurl[-1] == "/" or "\\"):
            return inputurl
        return (inputurl + "/")

#replace all \ with /
def valiurl(inputurl):
    inputurl = inputurl.replace("\\", "/")
    #replace all multiple occurance of /
    res = ""
    for i in range(0, len(inputurl)):
        ele = inputurl[i]
        if(ele != "/"):
            res += ele
        elif(ele == "/" and i == 0):
            res += ele
        elif(ele == "/"):
            pre = inputurl[i-1]
            if(pre == "/"):
                #do nothing
                pass
            else:
                res += ele
        else:
            res += ele
    
    return res

#get last folder name in a dir
def get_last_dir_name(wdir):
    return get_base_name(validir(wdir)[:-1])

#validate question ends with :
def valiq(inputq):
    if (inputq[-1] == ":"):
        return inputq
    return (inputq + " :")

#write a specific file to a system location with content
def writefile(filename, content, print_progress = True):
    res = open(filename, "w")
    if(print_progress):
        lenf1 = len(content)
        bar = progressbar.ProgressBar(maxval=lenf1, \
        widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        bar.start()
        cnt = 0
        for i in content:
            res.write(str(i))
            res.write("\n")
            cnt += 1
            bar.update(cnt)
        bar.finish()
    else:
        for i in content:
            res.write(str(i))
            res.write("\n")
    res.close()
    
#remove a single line from the file
def rm_lines_from(lines, file):
    nfname = file + "_temp"
    with open(file, "r") as file_input:
        with open(nfname, "w") as output:
            for line in file_input:
                if line.strip("\n") != lines:
                    output.write(line)
    move_file_to_file(nfname, file)
    return True

#append one line to the file
def append_line(fdir, line):
    file = open(fdir, 'a')
    file.write(line)
    file.close()
    return

#add to the log file
def add_to_log(fdir, content, print_c = True, enable_log = True, prefix_cus = ""):
    prefix = "[" + get_datetime(4) + "] " + prefix_cus + " "
    line = prefix + content
    if(print_c):
        print(line)
    else:
        pass
    
    if(enable_log):
        file = open(fdir, 'a')
        #write new line first
        file.write("\n")
        file.write(line)
        file.close()
    else:
        pass
    return

#serialize command
def serialize_cmd(cmd):
    if(cmd == []):
        return ''
    else:
        res = ''
        for i in cmd:
            res += i
            res += ' '
        #remove last space
        res = res[:-1]
        return res
    return ''

#clear terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

#replace a string in file from a to b
def replace_in_file(fdir, old_string, new_string):
    nfname = fdir + "_temp"
    with open(fdir, "r", encoding="utf-8") as file_input:
        with open(nfname, "w", errors='ignore') as output:
            for line in file_input:
                new_line = line.replace(old_string, new_string)
                output.write(new_line)
    
    move_file_to_file(nfname, fdir)    
#return content of a single file as list
def get_list_from_file(fdir):
    file1 = open(fdir, 'r')
    Lines = file1.read().splitlines()
    return Lines

#return left stripped list of a single file
def get_list_from_file_lstrip(fdir):
    file1 = open(fdir, 'r')
    Lines = file1.read().splitlines()
    res = []
    for i in Lines:
        res.append(i.lstrip())
    return res
    
#Exit python with provided error message 
def exit_with_err(emsg):
    print(emsg)
    exit(1)

#get list of folders in directory, only folder name without path will be returned
def get_folder_list(wdir):
    res = []
    wdir = validir(wdir)
    if(check_exist(wdir)):
        flist = os.listdir(wdir)
        for i in flist:
            j = valiurl(wdir + i)
            if(os.path.isdir(j)):
                res.append(i)
    else:
        return None
    return res

#get list of folders in directory, returns absolute path of those folders
def get_folder_list_abs(wdir):
    res = []
    wdir = validir(wdir)
    if(check_exist(wdir)):
        flist = os.listdir(wdir)
        for i in flist:
            j = valiurl(wdir + i)
            if(os.path.isdir(j)):
                res.append(wdir + i)
    else:
        return None
    return res

#get list of files in directory, return file name
def get_file_list(wdir, white_list = []):
    res = []
    wdir = validir(wdir)
    if(check_exist(wdir)):
        flist = os.listdir(wdir)
        for i in flist:
            if(i not in white_list):
                res.append(i)
    else:
        return None
    return res
#get list of files in directory, return absolute path
def get_file_list_abs(wdir, white_list = []):
    res = []
    wdir = validir(wdir)
    if(check_exist(wdir)):
        flist = os.listdir(wdir)
        for i in flist:
            if(i not in white_list):
                res.append(wdir + i)
    else:
        return None
    return res

#Clean quit, remove temp file & __pycache__
def clean_quit(sdir = defaultdir, stopexe = False):
    rdir = validir(sdir)
    rmdir = rdir + "__pycache__/"
    #remove __pycache__
    flist = os.listdir(sdir)
    #print(flist)
    if("__pycache__/" in flist):
        shutil.rmtree(rmdir)
    else:
        pass
    if(stopexe == True):
        exit()
    else:
        pass
#get a folder's size
def get_dir_size(directory):
    """Returns the `directory` size in bytes."""
    total = 0
    try:
        # print("[+] Getting the size of", directory)
        for entry in os.scandir(directory):
            if entry.is_file():
                # if it's a file, use stat() function
                total += entry.stat().st_size
            elif entry.is_dir():
                # if it's a directory, recursively call this function
                total += get_dir_size(entry.path)
    except NotADirectoryError:
        # if `directory` isn't a directory, get the file size then
        return os.path.getsize(directory)
    except PermissionError:
        # if for whatever reason we can't open the folder, return 0
        return 0
    return total

#Check if folder valid
def check_dir_valid(inputdir):
    #print(inputdir)
    if (os.path.isdir(inputdir)):
        size = get_dir_size(inputdir)
        #print(size)
        if (size > 0):
            return True
        else:
            return False
    else:
        return False

#Check if file valid
def check_file_valid(inputdir):
    if (os.path.isfile(inputdir)):
        size = os.stat(inputdir).st_size
        if (size > 0):
            return True
        else:
            return False
    else:
        return False
        
#Check if valid
#if inputed a file, return true if it exist & size > 0, else false
#if folder inputed, return if exist with size >0, else false
def check_valid(inputdir):
    dstat = check_dir_valid(inputdir)
    fstat = check_file_valid(inputdir)
    return dstat or fstat


#check if a directory is a file or folder or non exist
def check_file_type(wdir):
    detf = os.path.isfile(wdir)
    detd = os.path.isdir(wdir)
    if(detf and detd):
        return "error"
    elif(not detf and not detd):
        return "non-exist"
    elif(detf):
        return "file"
    elif(detd):
        return "dir"
    else:
        return "error"
    
    return "error"

#Check if exist
def check_exist(inputdir):
    return os.path.exists(inputdir)

#Check if dir exist
def check_dir_exist(inputdir):
    return os.path.exists(inputdir) and os.path.isdir(inputdir)

#Check if file exist
def check_file_exist(inputdir):
    return os.path.isfile(inputdir)

#check if a dir empty
def check_dir_empty(inputdir):
    if(os.path.isdir(inputdir)):
        size = get_dir_size(inputdir)
        #print(size)
        if (size == 0):
            return True
        else:
            return False
    else:
        return False
    return False

#Check if a dir exist & empty
def check_empty_dir(inputdir):
    if (check_exist(inputdir) and os.path.isdir(inputdir)):
        lendir = len(os.listdir(inputdir))
        #print(lendir)
        if (lendir == 0):
            return True
        else:
            return False
    else:
        return False
#check if a directory is writable
def check_dir_writable(inputdir):
    write = ["This is a writable test..."]
    tfname = "write_test.txt"
    inputdir = validir(inputdir)
    if(check_dir_exist(inputdir)):
        fdir = inputdir + tfname
        try:
            writefile(fdir, write)
        except:
            return False
        if(check_file_exist(fdir)):
            os.remove(fdir)
            if(check_file_exist(fdir)):
                return False
            else:
                return True
        else:
            return False
    else:
        return False
    
    return False

        
#Check if a dir non-exist or empty
def check_dir_non_exist_or_empty(inputdir):
    if(check_exist(inputdir)):
        #print(check_exist(inputdir))
        if (check_empty_dir(inputdir)):
            #print(check_empty_dir(inputdir))
            return True
        else:
            return False
    else:
        return True    
#Create if dir not exist
def create_dir_if_not_exist(inputdir, msg = "Folder Created: ", Print = True, appenddir = True):
    inputdir = validir(inputdir)
    exist = os.path.exists(inputdir)
    if (not exist):
        os.makedirs(inputdir)
        if(Print):
            if(appenddir):
                print(msg + str(inputdir))
            else:
                print(msg)
        else:
            pass
    else:
        pass
    return

#print a warning message says input is invalid 
def warn_input():
    print("Invalid input!. Please check your input!")
    return

#get user input and check if in the range. wlist is a list of STRINGS specify the allowance range. 
def get_input(question, wlist = [], check = True, warn = 'Invalid input.'):
    usri = ""
    if (check):
        usri = input(question)
        while (usri not in wlist):
            print(warn)
            usri = input(question)
    else:
        usri = input(question)
    return usri

#Check if a string represents integer
def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
#check if a string represents float
def is_float(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False
    
#get current date as yyyy_mm_dd
def get_date():
    today = datetime.today()
    d = today.strftime("%y_%m_%d")
    return d

#get current date and time as yyyy_mm_dd_hh_mm_ss
def get_datetime(style = 0):
    now = datetime.now()
    if(style == 0):    
        dt_string = now.strftime("%Y_%m_%d_%H_%M_%S")
    elif(style == 1):
        dt_string = now.strftime("%Y_%m_%d_%H%M%S")
    elif(style == 2):
        dt_string = now.strftime("%Y%m%d_%H%M%S")
    elif(style == 3):
        dt_string = now.strftime("%Y-%m-%d-%H-%M-%S")
    elif(style == 4):
        dt_string = now.strftime("%m/%d %H:%M:%S")
    elif(style == 5):
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    return dt_string

#get current time HH_MM_SS
def get_time(style = 0):
    now = datetime.now()
    if (style == 0):
        dt_string = now.strftime("%H_%M_%S")
    elif(style == 1):
        dt_string = now.strftime("%H:%M:%S")
    return dt_string   
 
#run a system command, accepting list of arguments
def run_cmd(fcmd, shell = False):
    #os.system(fcmd)
    #print("cmd called")
    if(shell):
        print(serialize_cmd(fcmd))
        c = subprocess.call(serialize_cmd(fcmd), shell=True)
        return c
    else:
        c = subprocess.call(fcmd)
        return c
    return None
    
def run_cmd_timeout(fcmd, shell = False, tout = 0):
    #os.system(fcmd)
    #print("cmd called")
    if(shell):
        print(serialize_cmd(fcmd))
        if(tout != 0):
            c = subprocess.call(serialize_cmd(fcmd), shell=True, timeout=tout)
        else:
            c = subprocess.call(serialize_cmd(fcmd), shell=True)
        return c
    else:
        if(tout != 0):
            c = subprocess.call(fcmd, timeout=tout)
        else:
            c = subprocess.call(fcmd)
        return c
    return None
    
#run a system command, returning output printed to console
# returns return code and captured output
def run_cmd_and_get_output(fcmd):
    result = subprocess.run(fcmd, stdout=subprocess.PIPE)   
    return_code = result.returncode
    print_content = ""
    os_type = get_os_type()
    if(os_type == "windows"):
        print_content = result.stdout.decode('gbk')
    elif(os_type == "linux"):
        print_content = result.stdout.decode('utf-8')
    else:
        print_content = result.stdout.decode('utf-8')
    return return_code, print_content.splitlines()

#run a system command without wait for complete. accepting list of argumetns
def run_cmd_without_waiting(fcmd):
    subprocess.popen(fcmd)
    return

#move a folder to another folder
def move_dir(ori, dest):
    shutil.move(ori,dest)
    return 

#move a folder to another folder
def move_dir_linux(ori, dest):
    cmd = []
    ori = validir(ori)
    dest = validir(dest)
    #check if dest exist
    if(check_dir_exist(dest)):
        #base name
        base_name = get_last_dir_name(ori)
        dest_dir = dest + base_name
        remove_dir_linux(dest_dir)
        cmd = ["mv", "-f", ori, dest_dir]
    else:
        cmd = ["mv", "-f", ori, dest]
    #exe
    run_cmd(cmd)
    return
    
#remove a folder
def remove_dir(wdir):
    if(check_dir_exist(wdir)):
        shutil.rmtree(wdir)
    else:
        pass
    
    return


#remove a folder linux
def remove_dir_linux(wdir):
    wdir = validir(wdir)
    if(check_dir_exist(wdir)):
        cmd = ["rm", "-rf", wdir]
        run_cmd(cmd)
    else:
        pass
    
    return

#remove a file
def remove_single_file(wdir):
    try:
        os.remove(wdir)
    except OSError as e:  ## if failed, report it back to the user ##
        print ("Error: %s - %s." % (e.filename, e.strerror))
    return

#remove a file linux
def remove_single_file_linux(wdir):
    if(check_file_exist(wdir)):
        cmd = ["rm", "-rf", wdir]
        run_cmd(cmd)
    else:
        pass
    
    return

#remove a file or a dir
def remove_file_or_dir(wdir):
    wdir = valiurl(wdir)
    ftype = check_file_type(wdir)
    if(ftype == "dir"):
        remove_dir(wdir)
    elif(ftype == "file"):
        remove_single_file(wdir)
    else:
        #file not exist
        return None

#remove a file or a dir
def remove_file_or_dir_linux(wdir):
    cmd = ["rm", "-rf", wdir]
    run_cmd(cmd)
    return

#removea list of file or folder
def remove_list_of_file_or_folder(rlist):
    for i in rlist:
        j = valiurl(i)
        remove_file_or_dir(j)
    return

#removea list of file or folder linux
def remove_list_of_file_or_folder_linux(rlist):
    for i in rlist:
        j = valiurl(i)
        remove_file_or_dir_linux(j)
    return

#remove file with in a dir but keep that dir
def empty_dir(wdir):
    wdir = validir(wdir)
    remove_dir(wdir)
    create_dir_if_not_exist(wdir)
    return

#remove file with in a dir but keep that dir untouched.
def empty_dir_windows(wdir):
    flist = get_file_with_name(wdir, "*")
    remove_list_of_file_or_folder(flist)
    return

#empty list of dir
def empty_list_of_dir(wlist):
    for i in wlist:
        empty_dir(i)
    return

#empty list of dir windows, this one will remove all contents within the folder. will not remove and recreate main dir.
def empty_list_of_dir_windows(wlist):
    for i in wlist:
        empty_dir_windows(i)
    return
#copy a file to another directory overwrite
def copy_file_to(ori, dest):
    shutil.copy(ori, dest)
    return

#copy a file to another directory or file linux & overwrite
def copy_file_to_linux(ori, dest):
    cmd = ["cp", "-rf", ori, dest]
    run_cmd(cmd)
    return

#copy a list of file to another directory
def copy_list_of_file_to(olist, dest):
    for i in olist:
        copy_file_to(i, dest)
    return

#copy a list of file to another directory linux 
def copy_list_of_file_to_linux(olist, dest):
    for i in olist:
        copy_file_to_linux(i, dest)
    return

#copy a directory to another directory, no overwrite
def copy_dir_to(ori, dest):
    shutil.copytree(ori, dest)
    return

#copy a directory to another directory, overwrite
def copy_dir_to_linux(ori, dest):
    try:
        ori = validir(ori)
        dest = validir(dest)
        cmd = ["cp", "-r", ori, dest]
        run_cmd(cmd)
        return 
    except:
        return 


#copy a directory to another directory, overwrite
def copy_dir_to_overwrite(ori, dest):
    ori = validir(ori)
    dest = validir(dest)
    #remove if exist
    if(check_dir_exist(dest)):
        #remove
        remove_dir(dest)
    else:
        pass
    #start copying
    copy_dir_to(ori, dest)
    
    return

#copy a directory to another directory, overwrite
def copy_dir_to_overwrite_linux(ori, dest):
    ori = validir(ori)
    dest = validir(dest)
    cmd = ["cp", "-rf", ori, dest]
    run_cmd(cmd)
    return

#Move a file to another directory & overwrite
def move_file_to(ori, dest):
    dest = validir(dest)
    shutil.move(ori, dest)
    return

#Move a file to another directory & overwrite linux
def move_file_to_linux(ori, dest):
    cmd = ["mv", "-f", ori, dest]
    run_cmd(cmd)
    return

#Move a file to overwrite another file. if its a directory, it will be placed there.
def move_file_to_file(ori, dest):
    if(check_file_exist(dest)):
        remove_single_file(dest)
    else:
        pass
    shutil.move(ori, dest)
    return

#Move a file to overwrite another file. if its a directory, it will be placed there. linux
def move_file_to_file_linux(ori, dest):
    cmd = ["mv", "-f", ori, dest]
    run_cmd(cmd)
    return

#Move a file to another directory
def move_file_to_dir(ori, dest, fname):
    ot = validir(ori) + fname
    move_file_to(ot, dest)
    return

#Move a file to another directory linux
def move_file_to_dir_linux(ori, dest, fname):
    ot = validir(ori) + fname
    move_file_to_linux(ot, dest)
    return

#Move a list of file to another directory
def move_list_of_file_to(olist, dest):
    for i in olist:
        move_file_to(i, dest)
    return

#Move a list of file to another directory linux
def move_list_of_file_to_linux(olist, dest):
    for i in olist:
        move_file_to_linux(i, dest)
    return

#move a list of file or folder to another directory
def move_list_of_file_or_folder(rlist, dest):
    dest = validir(dest)
    create_dir_if_not_exist(dest)
    
    for i in rlist:
        if(check_file_exist(i)):
            move_file_to(i, dest)
        elif(check_dir_exist(i)):
            move_dir(i, dest)
        else:
            #pass if not exist
            pass
    return

#move a list of file or folder to another directory linux
def move_list_of_file_or_folder_linux(rlist, dest):
    dest = validir(dest)
    create_dir_if_not_exist(dest)
    
    for i in rlist:
        if(check_file_exist(i)):
            move_file_to_linux(i, dest)
        elif(check_dir_exist(i)):
            move_dir_linux(i, dest)
        else:
            #pass if not exist
            pass
    return

#compare two directories
def compare_dir(dir1, dir2):
    det = False
    cmp = filecmp.dircmp(dir1, dir2)
    dfile = cmp.diff_files
    
    if(len(dfile) == 0):
        det = True
    else:
        return False
    
    if(len(cmp.left_only) == 0 and len(cmp.right_only) == 0):
        det = True
    else:
        return False
    return det

#get file with name
def get_file_with_name(wdir, fname):
    wdir = validir(wdir)
    res = glob.glob(wdir+fname)
    return res

#get base name of a file, no path
def get_base_name(fname):
    return(ntpath.basename(fname))

#get directory of a file dir
def get_dir_name(fdir):
    if(fdir != ""):
        
        return validir(os.path.dirname(os.path.realpath(fdir)))
    else:
        return ""
    
#get all files in specific directory
def read_dir(wdir):
    return os.listdir(wdir)

#get system cpu count
def get_cpu_num():
    return(multiprocessing.cpu_count())

#split based on space preserve quotes
def split_on_space_with_quote(fline):
    return shlex.split(fline, posix=False)

#split based on space remove quotes
def split_on_space_without_quote(fline):
    return shlex.split(fline, posix=True)

def split_on_tab(fline):
    return fline.split("\t")

#Create process pool and execute based on provided list of commands
def run_cmd_pool(cmdlist, nworker = 4):
    pool = ThreadPool(nworker)
    for i in cmdlist:
        pool.apply_async(run_cmd, (i,))
    pool.close()
    pool.join()
    return

#Compare two list, sequence not matter
def compare_lists_no_srict(alist, blist):
    a = alist.sort()
    b = blist.sort()
    if(a == b):
        return True
    else:
        return False
    return False

#Return the difference part between the new list than old list while reatain the sequence.
def get_new_list_diff(old, new):
    res = []
    for i in new:
        if(i not in old):
            res.append(i)
        else:
            pass
    
    return res

#return current disk total, used, available
def get_disk_info(wdir):
    stat = shutil.disk_usage(wdir)
    total = stat[0]
    used = stat[1]
    freed = stat[2]
    used_p = used/total
    freed_p = freed/total
    return total, used, freed, used_p, freed_p

#return current disk total, used, available,  used percent, free space percent in gb
def get_disk_info_gb(wdir):
    stat = shutil.disk_usage(wdir)
    total = from_byte_to_gb(stat[0])
    used = from_byte_to_gb(stat[1])
    freed = from_byte_to_gb(stat[2])
    used_p = used/total
    freed_p = freed/total
    return total, used, freed, used_p, freed_p

#get file size in bytes
def get_file_size(wdir):
    size = os.path.getsize(wdir)
    return size

#get file size in gb
def get_file_size_gb(wdir):
    size = from_byte_to_gb(os.path.getsize(wdir))
    return size

#get file size in mb
def get_file_size_mb(wdir):
    size = from_byte_to_mb(os.path.getsize(wdir))
    return size

#get file size in mb
def get_file_size_kb(wdir):
    size = from_byte_to_kb(os.path.getsize(wdir))
    return size
#get folder size in gb
def get_folder_size_gb(wdir):
    return from_byte_to_gb(get_dir_size(wdir))

#get folder size in mb
def get_folder_size_mb(wdir):
    return from_byte_to_mb(get_dir_size(wdir))

#return tb in size from byte input
def from_byte_to_tb(byte):
    return byte/(1024**4)

#return gb in size from byte input
def from_byte_to_gb(byte):
    return byte/(1024**3)

#return mb in size from byte input
def from_byte_to_mb(byte):
    return byte/(1024**2)

#return kb in size from byte input
def from_byte_to_kb(byte):
    return byte/(1024)

#add double parenthesis 
def add_quote(slink):
    cmd = "\"" + slink + "\""
    return cmd

#convert a dictionary to list
def dict_to_keylist(dictionary):
    res = []
    for i in dictionary:
        res.append(dictionary[i])
    return res

#rename a file or directory
def rename_file_or_directory(ori, dest):
    if(not check_exist(ori)):
        return False
    else:
        pass
    os.rename(ori, dest)
    return True

def ask_and_check_dir(question, default=""):
    det = True
    while (det):
        df = ""
        if (default == ""):
            df = "无"
        else:
            df = default
        qdir = input(question + "默认[" + df + "]: ")
        if (qdir == ""):
            qdir = default
        else:
            pass

        if (check_dir_exist(qdir)):
            return validir(qdir)
        else:
            print("无效的目录.")
    return None

def ask_and_check_file(question, default=""):
    det = True
    while (det):
        df = ""
        if (default == ""):
            df = "None"
        else:
            df = default
        qdir = input(question + "Default[" + df + "]: ")
        if (qdir == ""):
            qdir = default
        else:
            pass

        if (check_file_exist(qdir)):
            return qdir
        else:
            print("Invalid file.")
    return None

#get index of the minimum element of a list
def get_idx_of_min_element(ilist):
    if(len(ilist) == 0):
        print("list length = 0, unable to find min element.")
        return -1;
    idx = 0
    res = ilist[0]
    num = 0
    for i in ilist:
        if(i < res):
            res = i
            idx = num
        num += 1
    return idx

#assign list of folders to X number of lists based on their size
def get_LB_folders_size(list_of_target, folder_list_abs, exp_index = [], progress = True):
    res = []
    res_size = []
    #initialize lists
    num_sep = len(list_of_target)
    #initialize idx
    if(exp_index == []):
        for i in range(num_sep):
            exp_index.append(1.0)

    for i in range(num_sep):
        res.append([])
        res_size.append(int(get_dir_size(list_of_target[i]) * exp_index[i]))
    #initialize and add to dictionary
    dict = {}
    if(progress):
        lenf1 = len(folder_list_abs)
        bar = progressbar.ProgressBar(maxval=lenf1, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        bar.start()
        cnt = 0
        for i in folder_list_abs:
            dict.update({i:get_dir_size(i)})
            cnt += 1
            bar.update(cnt)
        bar.finish()
    else:
        for i in folder_list_abs:
            dict.update({i:get_dir_size(i)})

    #sort the dictionary from higher to lower
    for w in sorted(dict, key=dict.get, reverse=True):
        #get placement index
        idx = get_idx_of_min_element(res_size)
        res[idx].append(w)
        res_size[idx] += int(dict[w] * exp_index[idx])

    return res, res_size

#get size in human-readable format
def get_size_readable_format(file_size_byte, round_bit = 2):
    res = ""
    #start checking byte
    if (file_size_byte < 1024):
        res = str(file_size_byte) + " Bytes"
    #checking for KB
    elif(file_size_byte < 1024**2):
        res = str(round(from_byte_to_kb(file_size_byte), round_bit)) + " KB"
    #checking MB
    elif(file_size_byte < 1024**3):
        res = str(round(from_byte_to_mb(file_size_byte), round_bit)) + " MB"
    #checking GB
    elif (file_size_byte < 1024 ** 4):
        res = str(round(from_byte_to_gb(file_size_byte), round_bit)) + " GB"
    #checking TB
    else:
        res = str(round(from_byte_to_tb(file_size_byte), round_bit)) + " TB"

    return res

#get size of a list of file/folders, need absolute path
def get_size_list_of_file_or_folder(flist):
    total = 0
    for i in flist:
        total += get_dir_size(i)
    return total

#remove duplicates from a list
def remove_duplicate_from_list(listA):
    res = []
    for i in listA:
        if(i not in res):
            res.append(i)
    return res

#check input for y or n
def check_yes_no(userinput, default = True):
    if(userinput == ""):
        return default
    elif(userinput == "Y" or userinput == "y"):
        return True
    elif(userinput == "N" or userinput == "n"):
        return False
    else:
        return -1
#check input valid for y or n
def ask_user_for_Y_or_N(default_question = "Use Y for yes or N for no, default Y. 使用Y继续或使用N退出, 默认Y [Y/N]:", default = True):
    det = True
    while(det):
        t = input(default_question)
        tr = check_yes_no(t, default)
        if(tr == -1):
            print("Invalid Input 无效的输入")
        else:
            return tr

#ask for option with default provided
#question: string, the question asked
#default: string, the default value when no response provided
#important: boolean, type confirm to confirm important options
#valid_func: func, provided validation function
#valids: list of str, provided valid options
def ask_with_default(question, default = "", valids = [], important = False, valid_func = None, invalids = []):
    det = True
    #format the question
    qd = question + " [Default " + default + "]: "
    if(default == ""):
        qd = question

    while(det):
        t = input(qd)
        #replace t with default when empty
        if(t == ""):
            t = default
        #check validity list
        if (valids != [] and str(t) not in valids):
            print("[ERROR] Invalid answer, not in allowed list. ")
            continue
        #check customized validation
        if(valid_func != None):
            if(not valid_func(t)):
                print("[ERROR] Verification failed.")
                continue
        #check if invalids
        if(invalids != [] and t in invalids):
            print("[ERROR] Invalid value.")
            continue
        #confirm important if set
        if(important):
            print("You provided: " + qd)
            tt = input("Please confirm by type 'confirm' or 'CONFIRM'")
            if(tt != "confirm" and tt != "CONFIRM"):
                print("Invalid confirmation.")
                continue

        #verification passed, return result
        return t

#check if a provided string is ip
def is_ip(ip):
    #separate based on .
    ip_split = ip.split(".")
    #length has to be exactly 4
    if(len(ip_split) != 4):
        return False
    #check each components to be integer between 0 and 255 inclusive
    for i in ip_split:
        #check integer
        if(not is_int(i)):
            #not integer
            return False
        #check value if int
        i = int(i)
        if(i < 0 or i > 255):
            return False
    #input str is ip
    return True

#get length n of random characters
def get_random(length, enable_str = True, enable_int = True, enable_symbol = True, enable_capital = True):
    if(length == 0):
        return ""
    int_list = "0123456789"
    char_list_upper = string.ascii_uppercase
    char_list_lower = string.ascii_lowercase
    symbol_list = "`~!@#$%^&*()_+-=[]|}{;':,./<>?"
    choice = ""
    if(enable_str):
        choice += char_list_lower
    if(enable_capital):
        choice += char_list_upper
    if(enable_int):
        choice += int_list
    if(enable_symbol):
        choice += symbol_list
    return ''.join(random.sample(choice,length))