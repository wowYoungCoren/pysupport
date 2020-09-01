import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
import os

BASE_DIR = "Results/"

def readFile():
    # 文件路径
    root = tk.Tk()
    # 选取文件夹
    root.withdraw()
    # 选取文件
    file = filedialog.askopenfilename()

    _, _, extension = executePath(file)
    data = None
    if extension == ".xlsx" or extension == ".xls":
        # 读取文件
        data = pd.read_excel(file)
    elif extension == ".txt" or extension == ".csv":
        # 读取文件（不带列名）
        data = pd.read_csv(file, header=None)
    # if file != '':
    #     data = pd.read_excel(Filepath)  # 读取文件

    return data



def executePath(filename):
    (filepath,tempfilename) = os.path.split(filename);
    (shotname,extension) = os.path.splitext(tempfilename);
    return filepath, shotname, extension


if __name__ == '__main__':
    readFile()