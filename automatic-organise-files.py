import shutil, os, time, re

file_extensions=[]
extensions=""
extensions_string = ""
path = ""
Starttime = 0 
Endtime = 0

def OrganiseFolderbyExtensions ():
    Starttime = time.time()
    #Ask user for input for the Path in the OS
    print("What folder do you want to organise? Please enter the path below: \n")
    
    #Input for Path variable
    pathhuman = input("")
    print("\nYou have provided the path: "+pathhuman+"\n")

    #run function to convert normal path to python-readable path
    path = PathStringConversion(pathhuman)
    print("The PathStringConversion Function changed the user provided path to: "+path+"\n")

    #move to directory as path
    os.chdir(path)

    #Count files
    print("There are "+CountFiles(path)+" number of files in this folder"+"\n")

    if CountFiles(path) == "0":
        print("There are no files in this folder\n")
    else:
        print("Started Working on the "+CountFiles(path)+" files\n")
        
        #looping through files in the directory
        for filename in os.listdir(path):
            
            #find only files
            if os.path.isfile(filename):
                print("Initiaing work on file: "+filename)
                
                #split file name from last dot
                filesplit = filename.rsplit('.', 1)

                # if split file name has two variables (it means there is an extension in the file name)
                if len(filesplit) == 2:
                    #select the files extension from the index value which is 1
                    extensions = filesplit[1]
                    #convery it to string
                    extensions_string = str(extensions)

                    #if a folder named of the file's extension exists then just move the file from current folder to the extension-named folder
                    if os.path.exists(str(".\\"+extensions_string)):
                        print("The Folder "+path+"\\"+extensions_string+" already exists")
                        
                        #stringing up the new path
                        newpath = os.path.join(".\\"+extensions_string+'\\'+filename)
                        #If file already exists move the file with an incremented value
                        if os.path.exists(newpath):                                
                            #file already exists
                            print ("File "+filename+" is already present in "+path+"\\"+extensions_string+"\n")
                            print ("Copying the file with an incremental value of the current present")
                            #run the filename increment function which will increment the filename with a number
                            filenameincrement = Incrementsamefilename(filename)
                            filenameincrementnewpath = os.path.join(".\\"+extensions_string+'\\'+filenameincrement)
                            #move the file to the folder with a new name and delete the file in the current folder
                            shutil.move(filename, filenameincrementnewpath)
                            print ("Copied the file with an incremental value to "+path+filenameincrement)                            
                            print ("File processing completed!"+'\n')                          
                        else:
                            #move the file to the new path
                            shutil.move(filename,newpath)
                            print ("File "+filename+" is moved to "+path+"\\"+extensions_string)
                            print ("File processing completed!"+'\n')                        

                    #if the extension-named folder does not exist, create it and then move the file
                    else:
                        print("The folder "+path+"\\"+extensions_string+" does not exist, therefore it will be created")
                        
                        os.makedirs(str(".\\"+extensions_string))
                        print("The Folder "+path+"\\"+extensions_string+" is created")
                        
                        #stringing up the new path
                        newpath = os.path.join(".\\"+extensions_string+'\\'+filename)
                        #If file already exists move the file with an incremented value
                        if os.path.exists(newpath):                                
                            #File already exists
                            print ("File "+filename+" is already present in "+path+"\\"+extensions_string+"\n")
                            print ("Copying the file with an incremental value of the current present")
                            #run the filename increment function which will increment the filename with a number
                            filenameincrement = Incrementsamefilename(filename)
                            filenameincrementnewpath = os.path.join(".\\"+extensions_string+'\\'+filenameincrement)
                            #move the file to the folder with a new name and delete the file in the current folder
                            shutil.move(filename, filenameincrementnewpath)
                            print ("Copied the file with an incremental value to "+path+filenameincrement)                            
                            print ("File processing completed!"+'\n')                        
                        else:
                            #move the file to the new path
                            shutil.move(filename,newpath)
                            print ("File "+filename+" is moved to "+path+"\\"+extensions_string)
                            print ("File processing completed!"+'\n')

                #if the file split has only one index value after splitting, it means this file has no extension
                elif len(filesplit) == 1:
                    print("This file does not contain an extension")
                    
                    #if folder named "unknown" exists, then put the file in that folder
                    if os.path.exists(str(".\\unknown")):
                        print("The Folder "+path+"\\\\unknown is already present")
                        
                        #stringing up the new path
                        newpath = os.path.join(".\\unknown"+"\\\\"+filename)
                        #If file already exists move the file with an incremented value
                        if os.path.exists(newpath):                                
                            #File already exists
                            print ("File "+filename+" is already present in "+path+"\\\\unknown\n")
                            print ("Copying the file with an incremental value of the current present")
                            #run the filename increment function which will increment the filename with a number
                            filenameincrement = Incrementsamefilename(filename)
                            filenameincrementnewpath = os.path.join(".\\"+"unknown"+'\\'+filenameincrement)
                            #move the file to the folder with a new name and delete the file in the current folder
                            shutil.move(filename, filenameincrementnewpath)
                            print ("Copied the file with an incremental value to "+path+filenameincrement)                            
                            print ("File processing completed!"+'\n')                        
                        else:
                            #move the file to the new path
                            shutil.move(filename,newpath)
                            print ("File "+filename+" moved to "+path+"\\unknown")
                            print ("File processing completed!"+'\n')

                    else: 
                        #otherwise create the folder and then move the file
                        print("The folder "+path+"\\\\unknown does not exist, therefore it will be created")
                        
                        #make the unknown directory
                        os.makedirs(str(".\\unknown"))
                        print("The folder "+path+"\\\\unknown is created")
                        
                        #stringing up the new path
                        newpath = os.path.join(".\\unknown"+"\\\\"+filename)
                        #If file already exists move the file with an incremented value
                        if os.path.exists(newpath):                                
                            #File already exists
                            print ("File "+filename+" is already present in "+path+"\\\\unknown\n")
                            print ("Copying the file with an incremental value of the current present")
                            #run the filename increment function which will increment the filename with a number
                            filenameincrement = Incrementsamefilename(filename)
                            filenameincrementnewpath = os.path.join(".\\"+extensions_string+'\\'+filenameincrement)
                            #move the file to the folder with a new name and delete the file in the current folder
                            shutil.move(filename, filenameincrementnewpath)
                            print ("Copied the file with an incremental value to "+path+filenameincrement)                            
                            print ("File processing completed!"+'\n')                                                
                        else:
                            #move the file to the new path
                            shutil.move(filename,newpath)
                            print ("File "+filename+" moved to "+path+"\\\\unknown")
                            print ("File processing completed!"+'\n')
                        
    #Completed
    print("The Folder has been Processed!\n")

    Endtime = time.time()
    TotalTime = Endtime - Starttime
    TotalTimeinseconds = TotalTime/60 
    print(f"The Program took {TotalTimeinseconds} seconds to complete!")

#Function to convert the windows provided path to python-readable path with double slashes        
def PathStringConversion(pathtoconvert):
    
    #Split the path with "\" Divider
    splitinput = pathtoconvert.split("\\")
    
    #Join the split words in the list back but with 2 "\" as the path to be provided in python has to be double forward slash
    joininput = '\\\\'.join(splitinput)
    
    #Assign joininput to path again for the main function
    pathconverted = os.path.join(joininput)
    return pathconverted



#Function for counting files in the directory
def CountFiles(pathforfilecount):
    os.chdir(pathforfilecount)
    Totalfiles = 0
    TotalFilesString = '0'
    for filename in os.listdir(pathforfilecount):
        #find only files
        if os.path.isfile(filename):
            Totalfiles = Totalfiles + 1
            TotalFilesString = str(Totalfiles)
    return TotalFilesString

#if same file exists in the to-copy folder provide the oldfilename and it will generate a new for the file with (1) at the end but before the extension(if present) like test(1).jpeg 
def addnumberatendoffilename(oldfilename):
    #split file by last dot
    filesplit = oldfilename.rsplit('.', 1)
    #see if the filename has an extension 
    if len(filesplit) == 2:
        #take the  file's extension which is number 1 in index
        extension = filesplit[1]
        #take filename without extension which is number 0 in index
        filenamestringwithoutextension = filesplit[0]
        #combine filename and extension with (1) in middle with a dot
        newfilename = filenamestringwithoutextension+"(1)."+extension
    #see if the filename has no extension 
    elif len(filesplit) == 1:
        filenamestringwithoutextension = filesplit[0]
        #combine filename with (1) in middle with a dot
        newfilename = filenamestringwithoutextension+"(1)"
    #return the new named file
    return newfilename

#increment file number by 1 number at end if the file already has a number at the end showing its already a copy of another file in the folder. Functionality for only 2 letter digits max till 99.
#For 3 letter digits add with lastfivecharacters = filenamestringwithoutextension[-5:] and its following code.
def Incrementsamefilename(oldfilename):
    filesplit = oldfilename.rsplit('.', 1)
    # if split file name has two variables (it means there is an extension in the file name)
    if len(filesplit) == 2:
        #select the filename from the index value which is 0
        filenamestringwithoutextension = filesplit[0]
        #select the extension of the file (index 1)
        extension = filesplit[1]
        #select last three characters from the string of filename without extension - used for 1 digit numbers
        lastthreecharacters = filenamestringwithoutextension[-3:]
        #select last four characters from the string of filename without extension - used for 2 digit numbers
        lastfourcharacters = filenamestringwithoutextension[-4:]
        #search for 1 digit encapsulated with ()
        if re.search(r"\(\d\)", lastthreecharacters):
            #take the digit number and increment it by 1
            nextdigit = int(lastthreecharacters[-2]) + 1
            #convert to string
            nextdigitstr = str(nextdigit)
            #add brackets to the number string 
            nextdigitwithbrackets = str("("+nextdigitstr+")")
            #add the brackated number string to the filename-without-last-3-characters which has the increment number removed, add the incremented-number and extension
            newincrementfilename = filenamestringwithoutextension[:-3]+nextdigitwithbrackets+"."+extension
        #search for 2 digit encapsulated with ()
        elif re.search(r"\(\d\d\)", lastfourcharacters):
            #get only the numbers from the string
            digits = int(''.join(list(filter(str.isdigit, lastfourcharacters))))
            #take the digit number and increment it by 1
            nextdigit = digits + 1
            #convert to string
            nextdigitstr = str(nextdigit)
            #add brackets to the number string 
            nextdigitwithbrackets = str("("+nextdigitstr+")")
            #add the brackated number string to the filename-without-last-3-characters which has the increment number removed, add the incremented-number and extension
            newincrementfilename = filenamestringwithoutextension[:-4]+nextdigitwithbrackets+"."+extension
        #if there is no 1 or 2 digit encapsulated with () then file is probably without any number hence run addnumbertoendfilename to add a number to it and return new filename
        else:
            newincrementfilename = addnumberatendoffilename(oldfilename)
    #if the filename does not have extension then filesplit length will only give 1, if so then this code runs 
    elif len(filesplit) == 1:
        #select the filename from the index value which is 0
        filenamestringwithoutextension = filesplit[0]
        #select last three characters from the string of filename without extension - used for 1 digit numbers
        lastthreecharacters = filenamestringwithoutextension[-3:]
        #select last four characters from the string of filename without extension - used for 2 digit numbers
        lastfourcharacters = filenamestringwithoutextension[-4:]
        #search for 1 digit encapsulated with ()      
        if re.search(r"\(\d\)", lastthreecharacters):
            #take the digit number and increment it by 1
            nextdigit = int(lastthreecharacters[-2]) + 1
            #convert to string
            nextdigitstr = str(nextdigit)
            #add brackets to the number string 
            nextdigitwithbrackets = str("("+nextdigitstr+")")
            #add the brackated number string to the filename-without-last-3-characters which has the increment number removed, add the incremented-number
            newincrementfilename = filenamestringwithoutextension[:-3]+nextdigitwithbrackets
        #search for 2 digit encapsulated with ()
        elif re.search(r"\(\d\d\)", lastfourcharacters):
            #get only the numbers from the string
            digits = int(''.join(list(filter(str.isdigit, lastfourcharacters))))
            #take the digit number and increment it by 1
            nextdigit = digits + 1
            #convert to string
            nextdigitstr = str(nextdigit)
            #add brackets to the number string 
            nextdigitwithbrackets = str("("+nextdigitstr+")")
            #add the brackated number string to the filename-without-last-3-characters which has the increment number removed, add the incremented-number
            newincrementfilename = filenamestringwithoutextension[:-4]+nextdigitwithbrackets
            #if there is no 1 or 2 digit encapsulated with () then file is probably without any number hence run addnumbertoendfilename to add a number to it and return new filename
        else:
            newincrementfilename = addnumberatendoffilename(oldfilename)
    return newincrementfilename

OrganiseFolderbyExtensions()