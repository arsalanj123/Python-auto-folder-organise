import shutil, os
 
file_extensions=[]
extensions=""
extensions_string = ''
path = ''

def FindExtensions (path):
    print("What folder do you want to organise? Please enter the path below:")
    pathhuman = input("")
    splitinput = pathhuman.split("\\")
    joininput = '\\\\'.join(splitinput)
    path = joininput
    os.chdir(path)
    for filename in os.listdir(path):
        if os.path.isfile(filename):
            filesplit = filename.rsplit('.', 1)
            if len(filesplit) == 2:
                extensions = filesplit[1]
                extensions_string = str(extensions)
                print(filename)
                if os.path.exists(str(path+extensions_string)):
                    shutil.move(filename,(path+'\\'+extensions_string+'\\'+filename))
                else:
                    os.makedirs(path+extensions_string)
                    shutil.move(filename,(path+'\\'+extensions_string+'\\'+filename))
            elif len(filesplit) == 1:
                if os.path.exists(str(path+"unknown")):
                    shutil.move(filename,(path+"\\"+"unknown"+"\\"+filename))
                else: 
                    os.makedirs(path+"unknown")
                    shutil.move(filename,(path+"\\"+"unknown"+"\\"+filename))
    print("Completed!")    
        


print(FindExtensions(path))