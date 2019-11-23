#Convert_xlsx_to_csv
# Tach sheet thanh tung file va ghi du lieu doc du lieu tung file va ghi vao 1 file khac
import pandas as pd
import numpy as np
from pprint import pprint
import re
import os,fnmatch
import datetime 
import shutil
import openpyxl
import xlsxwriter
import xlrd
import csv
import glob
from xlrd import open_workbook
from xlwt import Workbook

#xac dinh thoi gian

files=[]
listOfFiles = os.listdir('.')# lay danh sach file
pattern = "*.xlsx"# lay file cua excel
for entry in listOfFiles:
	if fnmatch.fnmatch(entry, pattern):
		files.append(entry)
export_time= files.pop(0)# xuat ra chuoi
	#loc thoi gian va dinh dang Y-m-d
date_1 = re.search(r"(\d{4})(\d{2})(\d{2})",export_time)
date_2 = date_1.group(1)+"-"+date_1.group(2)+"-"+date_1.group(3)


#CHIA NHO file excel thanh nhieu file
def split_file():
	rb = open_workbook('Billing check for date_20190905_MSC.xlsx')
	for a in range(10): #for example there're only 5 tabs/sheets
	    rs = rb.sheet_by_index(a)
	    new_book = Workbook()
	    new_sheet = new_book.add_sheet('Sheet 1')
	    for row in range(rs.nrows):
	        for col in range(rs.ncols):
	            new_sheet.write(row, col, rs.cell(row, col).value)
	    new_book.save("C:/PythonCode"+"/Chiafile/" + str(a) + ".xls")

#them cot
def add_colum(fileName):
		trans=pd.read_excel(fileName)
		df_len = len(trans)
		Date = [date_2 for i in range(df_len)]
		trans['Date'] = Date
		trans.to_excel(fileName)
#Duyet cac file 		
def batchProcess(dirPath):
	files=[]
	listOfFiles = os.listdir(dirPath)# lay danh sach file
	pattern = "*.xls"# lay file cua excel
	for entry in listOfFiles:
	    if fnmatch.fnmatch(entry, pattern):
	            files.append(entry)
	for file in files:
		add_colum(os.path.join(dirPath, file))
#Chuyen xlxs to csv
def convert_csv():
	# set working directories for files
	starting_folder=('C:/PythonCode/Chiafile/')
	save_folder = ('C:/PythonCode/')

	#create list of excel file names from folder  
	files = []
	for file in os.listdir(starting_folder):
	    filename = os.fsdecode(file)
	    files.append(filename)

	# create list for file names to be saved as csv
	save_files = [w.replace('xlsx','csv') for w in files]

	#loop through csv files to format and save to new location
	for i in range(len(files)):
	    #reads unformatted excel file into dataframe
	    df = pd.read_excel(starting_folder+files[i])
	    #save to csv for db loading
	    df.to_csv(save_folder+save_files[i]+'.csv',index = False, encoding='utf-8') 
def main():
	#time_stamp()
	#split_file()
	#batchProcess('C:/PythonCode/Chiafile')
	convert_csv()
if __name__ == "__main__":
	
	main()
    
