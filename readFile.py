import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
import os

BASE_DIR = "Results/"

def readFile():
    # 文件路径
    root = tk.Tk()
    root.withdraw()  # 选取文件夹
    file = filedialog.askopenfilename()  # 选取文件

    _, _, extension = executePath(file)
    data = None
    if extension == ".xlsx" or extension == ".xls":
        data = pd.read_excel(file)  # 读取文件
    elif extension == ".txt" or extension == ".csv":
        data = pd.read_csv(file, header=None)  # 读取文件
    # if file != '':
    #     data = pd.read_excel(Filepath)  # 读取文件

    return data



def executePath(filename):
    (filepath,tempfilename) = os.path.split(filename);
    (shotname,extension) = os.path.splitext(tempfilename);
    return filepath, shotname, extension


if __name__ == '__main__':
    readFile()