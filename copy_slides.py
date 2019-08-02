# Nicola Blackstock
#Assignment 4 Part 3
#Due Date: June 26th 2019
# UCBE Cyber Security 
import os
import shutil

def pptx_copy():
    dest_path = "/Users/nicolablackstock/Desktop/CyberSecurity/homework/HW_week4_Python/CyberSecurity-Notes/"
    src = "/Users/nicolablackstock/Desktop/UCBBMT201905CYBER4/PowerPoint Presentations/"
   
    files = os.listdir(src)
    for f in files:
       f = str(f)
       if(f.endswith('.pdf') or ('.pptx')):
            week = f[6]
            day = f[9]
           

            from_src = os.path.join(src, f)
            new_folder = os.path.join(dest_path + "Week" + week + '/' "Day" + day)
            print(new_folder)
                
            if not os.path.exists(new_folder):
                os.makedirs(new_folder)
                print(new_folder)


            shutil.copy(from_src, new_folder)
            print ("Copy '" + str(from_src) + "' directory to '" + str(new_folder) + "'")

              
pptx_copy()   