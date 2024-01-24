# -*- coding: UTF-8 -*-
import os, subprocess, glob, multiprocessing, ntpath, shlex, filecmp, random, string
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
