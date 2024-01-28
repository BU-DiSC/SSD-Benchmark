# -*- coding: UTF-8 -*-
import os, subprocess, glob, multiprocessing, ntpath, shlex, filecmp, random, string, progressbar
from datetime import datetime
from multiprocessing.pool import ThreadPool

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
#get file with name
def get_file_with_name(wdir, fname):
    wdir = validir(wdir)
    res = glob.glob(wdir+fname)
    return res
    
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
