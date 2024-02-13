import os
import sys

def main():
    checkFirstBoot()

    #if user supplies args use them instead of stored settings
    if not len(sys.argv) == 1:
        setSource(sys.argv[1])
        setTarget(sys.argv[2])
        setWhitelist(sys.argv[3])

    performClean()
 

'''
This functions checks to see if the config files exist, if not it creates them
'''
def checkFirstBoot():
    if not os.path.isfile(f"{os.getcwd()}\\source.txt"):
        if not os.path.isfile(f"{os.getcwd()}\\target.txt"):
            if not os.path.isfile(f"{os.getcwd()}\\whitelist.txt"):
                performStartup()
    
'''
This function gets input from the user, calls functions to create config files, 
and then passes input to the setters
'''
def performStartup():
    source = []
    target = ""
    whitelist = []

    #get all the source directories from user input and put them in a list
    while True:
        temp = input("Please input the path(s) to any directory you would like to clean. When done type 'stop': ")
        if not temp.lower().strip() == "stop":
            source.append(temp)
        else:
            break

    #get target directory from user
    target = input("Please input the directory that files should be sorted in: ")

    #get all files to whitelist from user and store them in a list
    while True:
        temp = input("Please provide name of file you would like to add to white list.\nIf none please enter stop: ")
        if not temp.lower().strip() == "stop":
            whitelist.append(temp)
        else:
            break

    #create the cfg files
    createSource()
    createTarget()
    createWhitelist()    

    #store the paths/files    
    setSource(source)
    setTarget(target)
    setWhitelist(whitelist)

    #creates source file returns nothing
def createSource():
    with open("source.txt", "a") as file:
        return
    #creates target file returns nothing
def createTarget():
    with open("target.txt", "a") as file:
        return
    #creates whitelist file returns nothing
def createWhitelist():
    with open("whitelist.txt", "a") as file:
        return

'''
Takes a list of source directory paths as input and stores them in the config file
'''
def setSource(sources):
    with open("source.txt", "w") as file:
        for path in sources:
            file.write(f"{path},")
'''
Takes a target directory path as input and stores them in the config file
'''
def setTarget(target):
    with open("target.txt", "w") as file:
        file.write(target)

'''
Takes a list of files to be whitelisted as input and stores them in the config file
'''
def setWhitelist(whitelist):
    with open("whitelist.txt", "w") as file:
        for path in whitelist:
            file.write(f"{path},")

'''
Retrieves the source directories as a string from the config file and returns them
Values are seperated by commas
'''
def getSource():
    with open("source.txt", "r") as file:
        return file.readline()
    
'''
Retrieves the target directory as a string from the config file and returns it
'''
def getTarget():
    with open("target.txt", "r") as file:
        return file.readline()
    
'''
Retrieves the whitelisted files as a string from the config file and returns them
Values are seperated by commas
'''       
def getWhitelist():
    with open("whitelist.txt", "r") as file:
        return file.readline()


'''
This is the logic to perform the directory clean 
It creates subdirectories within the target directory, 
and then it moves all the files from the source directory(s)
excluding any whitelisted files
'''
def performClean():
    
    #retrieve settings from config files
    sources = getSource().rstrip(",").split(",")
    targetDir = getTarget()
    whitelist = getWhitelist().rstrip(",").split(",")

    #create sub-directories to sort files into
    try:
        os.mkdir(f"{targetDir}\\office")
        os.mkdir(f"{targetDir}\\office\\excel")
        os.mkdir(f"{targetDir}\\office\\word")
        os.mkdir(f"{targetDir}\\office\\powerpoint")
        os.mkdir(f"{targetDir}\\photos")
        os.mkdir(f"{targetDir}\\videos")
        os.mkdir(f"{targetDir}\\text")
        os.mkdir(f"{targetDir}\\audio")
        os.mkdir(f"{targetDir}\\other")
    except FileExistsError:
        pass
    
    #iterate through all the source directories and check the file against the whitelist then sort
    for sourceDir in sources:
        files = os.listdir(sourceDir)
        for file in files:
            if file in whitelist:
                continue
            else:
                #sort based on extension of file
                extension = file.split(".")[-1]
                match extension:
                    case "docx":
                            os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\office\\word\\{file}")
                    case "doc":
                        os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\office\\word\\{file}")
                    case "pptx":
                        os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\office\\powerpoint\\{file}")
                    case "xlsx":
                        os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\office\\excel\\{file}")
                    case "csv":
                        os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\office\\excel\\{file}")
                    case "txt":
                        os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\text\\{file}")
                    case "rtf":
                        os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\text\\{file}")
                    case "mp4":
                        os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\videos\\{file}")
                    case "mov":
                        os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\videos\\{file}")
                    case "wmv":
                        os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\videos\\{file}")
                    case "jpg":
                        os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\photos\\{file}")
                    case "jpeg":
                        os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\photos\\{file}")
                    case "png":
                        os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\photos\\{file}")
                    case "mp3":
                        os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\audio\\{file}")
                    case "wav":
                        os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\audio\\{file}")
                    case _:
                        os.rename(f"{sourceDir}\\{file}", f"{targetDir}\\other\\{file}")
            

if __name__ == "__main__":
    main()