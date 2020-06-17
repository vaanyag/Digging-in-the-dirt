
import os
import shutil
from pathlib import Path
import sys


'''
STEP 1
'''
list_files=[]

list_of_main_files=[]

R=[]
list_of_sub_files2=[]   

list_files1=[]

list_of_sub_files=[]
list_of_main_files2=[]


def make_list_of_paths(path_dir):
    
    list_of_files = os.listdir(path_dir)
    for file in list_of_files:
        path = path_dir / Path(file)
        if os.path.isfile(path) == True:
            list_files1.append(path)
            list_of_main_files2.append(path)
        else:
            list_of_sub_files.append(path)
            make_list_of_paths(path)

def first_operation():
  
    find_name = input()

    if find_name == '':
        sys.exit()

    else:
    
        command_type = find_name[0]
        directory = find_name[2:]

        if os.path.isdir(directory) == False:
            print('ERROR')
            first_operation()
        else:

            if command_type!='D' and command_type!='R':
                print ("ERROR")
                first_operation()
            elif command_type == 'D':
                try:
                    list_of_files = os.listdir(directory)
                except OSError:
                    sys.exit()
           
                for file in list_of_files:
                    path0=Path(directory)
                
                    path = path0 / Path(file)
                    if os.path.isfile(path) == True:
                 
                        list_of_main_files.append(path)
                list_of_main_files.sort()
                for files in list_of_main_files:
                    print (files)
                #list_files=list_of_main_files
                return list_of_main_files
           
            elif command_type == 'R':
                path = Path(directory)
                make_list_of_paths(path)
                list_of_files = os.listdir(directory)
               
                for file in list_of_files:
                    path0=Path(directory)
                   
                    path = path0 / Path(file)
                    if os.path.isfile(path) == True:
                      
                        list_of_main_files.append(path)
                list_of_main_files.sort()
                for files in list_of_main_files:
                    list_files.append(files)
                    print(files)
               
                for file in list_of_main_files2:
                    if file not in list_of_main_files:
                        list_of_sub_files2.append(file)

                list_of_sub_files2.sort() 
                for files in list_of_sub_files2:
                    list_files.append(files)
                
                    print (files)
   
    return  list_files
    
'''
STEP 2
'''

list_of_int_files=[]
def second_operation(list_files):
    search_files=input()
    type_of_command = search_files[0]
    
    if search_files=='A':
        for i in list_files:
            list_of_int_files.append(i)
            print (i)
            
    elif type_of_command in ['N', 'E', 'T', '<', '>']:
        commands = search_files.split(' ')
        type_of_command = search_files[0]
        file_name  = search_files[2:]
        
        if file_name=='':
            print('ERROR')
            second_operation(list_files)
            
        else:
            if type_of_command=='N':
                for i in list_files:
                    if file_name == os.path.basename(i): 
                        list_of_int_files.append(i)
                        print (i)
                        
            elif type_of_command=='E':
                if '.' not in file_name:
                    extension_name='.'+file_name
                else:
                    extension_name=file_name
                for i in list_files:
                    if extension_name in os.path.basename(i):
                        list_of_int_files.append(i)
                        print (i)
                        
            elif type_of_command=='T':
                for file in list_files:
                  
                    file1=open(file,"r")
                    try:
                        file1.readline()
                    except:
                        continue
                    else:
                        for line in file1:
                            if file_name in line:
                                list_of_int_files.append(file)
                                print (file)
                    finally:
                        file1.close()
                        
            elif type_of_command=='<':
                try:
                    num_bytes=int(file_name)
                    for file in list_files:
                        if os.path.getsize(file)<num_bytes:
                            list_of_int_files.append(file)
                            print(file)
                except ValueError:
                    print('ERROR')
                    second_operation(list_files)
                        
            elif type_of_command=='>':
                try:
                    num_bytes=int(file_name)
                    for file in list_files:
                        if os.path.getsize(file)>num_bytes:
                            list_of_int_files.append(file)
                            print(file)
                except ValueError:
                    print("ERROR")
                    second_operation(list_files)
    else:
        print("ERROR")
        second_operation(list_files)
        
        
    
    return list_of_int_files

'''
STEP 3
'''

def third_operation(list_of_int_files):
    action=input()
    
    if action=='F':
        for file in list_of_int_files:
            
            try:
                file1=open(file,'r')
                print(file1.readlines(1)[0], end='')                
            except UnicodeDecodeError:
                print('NOT TEXT')
            finally:
                file1.close()
                
    elif action=='T':
        for file in list_of_int_files:
            os.utime(file,None)
            
    elif action=='D':
        for file in list_of_int_files:
            new_name=str(file)+'.dup'
            shutil.copy(file,new_name)
            
    
    else:
        print("ERROR")
        third_operation(list_of_int_files)
    return

if __name__=='__main__':
    
    files_list=first_operation()
    if files_list != []:
        interesting_files=second_operation(files_list)
        if interesting_files != []:
            third_operation(interesting_files)
