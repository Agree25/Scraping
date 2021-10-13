from typing import final
import PyPDF2
import re
import fitz
from pathlib import Path
pdf = PyPDF2.PdfFileReader('CauseListFile_3LZM6YNU0EL.PDF')
file = 'CauseListFile_3LZM6YNU0EL.PDF'
size = pdf.getNumPages()
url_regex = r"([-a-zA-Z0-9&])"

case = input()
year = input()
Petitioner = input()
Respondent = input()

str = ""
text = ""

with fitz.open(file) as pdf:
    text = ""
    no = 1
    for page in pdf:
        print(no)
        # extract text of each PDF page
        text = page.getText()
       
        t = 7
        judge_content = ""
        flag = 0
        cause = ""
        finall=""
        error_1_p = 1
        error_1 = 0
        save=0
        judge_count=0
        if('MATTERS LISTED FOR' in text):
        
            for line in text.splitlines():

#--------------------------------------------------------------------------------------------------------------------#
                if Petitioner in line.strip() or Respondent in line.strip():
                    #print(line)
                    if(judge_content!=""):
                        with open("judge.txt", "w", encoding='utf-8') as f:
                            f.write(judge_content)
                    
                    save = 1

                    break
#--------------------------------------------------------------------------------------------------------------------#
                if('MATTERS LISTED FOR' in line.strip()):
                    
                    flag = 1
                    t = 7
                    judge_count = 0
                    judge_content = ""
                    judge_content += cause
                    judge_content += '\n'
                # if case is also on same page break to handle case with 2 judge on same page


#--------------------------------------------------------------------------------------------------------------------#
                if(error_1 == 1):   # for handling problem faced during judge name coming in 3 lines instead of 1
                    if(error_1_p==1):
                        error_1_p=0
                    else:
                        judge_content+=line.strip()
                        judge_content+='\n'
                        error_1=0
                        judge_count += 1
                    continue

#--------------------------------------------------------------------------------------------------------------------#
                if(('CAUSE LIST' in line or "LIST" in line ) and flag==0):   #to read only first line

                    finall += line.strip(" ")
                   
                    temp =list(finall.split(" "))
                 
                    cause=""
                    co=1
                    error_1_p=1
                    error_1=0
                    for i in temp:
                        if(i!=""):
                            if co==1:  #date
                                cause+="Date: "
                                cause+=i
                                cause +="\n"
                                co+=1
                            elif co==2:
                                co+=1
                            elif co==3:
                                cause+=i
                                cause+=" Cause List"
                                break
                            
                            
#--------------------------------------------------------------------------------------------------------------------#
                if(flag and t > 0):
                   
                    if('COURT NO' in line.strip()):
                        judge_content += line.strip()
                        judge_content += '\n'
                        t -= 1
                    elif('MATTERS LISTED FOR' in line.strip()):
                        judge_content += line.strip()
                        judge_content += '\n'
                        t -= 1
                    elif('DIVISION' in line.strip()):
                        judge_content += line.strip()
                        judge_content += '\n'
                        t -= 1
                    elif(("HON’BLE" in line.strip() or "HON'BLE" in line.strip()) and judge_count<=1):  # "HON’BLE"
                        
                        vector=list(line.split())
                        #print(vector)
                        if(len(vector)==2):   # judge name error
                            judge_content += line.strip()
                            judge_content+=" "
                            error_1=1
                        else:
                            if(vector[0] == "HON’BLE" or vector[0] == "HON'BLE"):
                                judge_count += 1
                                judge_content += line.strip()
                                judge_content += '\n'
                        t -= 1
                    else:
                        t -=1
                
            # print()
            # print(judge_content)
            # print(save)
            # print()
            if(save==0):
                with open("judge.txt", "w", encoding='utf-8') as f:
                        f.write(judge_content)
        
#--------------------------------------------------------------------------------------------------------------------#
        list_no=""
        txt = re.search(url_regex, text)
        if(txt != None and case in text and year in text and Petitioner in text and Respondent in text):
            for line in text.splitlines():
               
                if(case in line and year in line):
                    list_no=line
                    
                    

            #str += text
            point = ""
            for i in list_no:
                if i == ".":
                    break
                else:
                    point += i
            item=""
            item += "Item No:"
            item+=point
            print(item)
            
            
            break
                    
        no += 1
#-------------------------------------------------------------------------------------------------------------------------#

# for i in cause:
#     print(i)

# with open("CauseListFile.txt", "w", encoding='utf-8') as f:
#     f.write(str)

