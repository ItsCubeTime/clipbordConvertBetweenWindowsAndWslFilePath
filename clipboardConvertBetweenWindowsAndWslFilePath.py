import subprocess
import sys
import pathlib
try:
    import clipboard
except:
    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    install('clipboard')
    import clipboard

getWslRootDir=lambda:(pathlib.Path(__file__).parent/'wslRootDir.txt').open("r").readline()
returnVal = ''
inputStr:str = clipboard.paste()
wslRootDir=getWslRootDir()
isWindowsPath=':' in inputStr or inputStr.startswith(wslRootDir)
if isWindowsPath:
    pathDestinationIsOutsideWsl=not inputStr.startswith(wslRootDir)
    inputStr=inputStr.replace('\\','/').replace('//','/')
    if pathDestinationIsOutsideWsl: # @note Eg: C:\Program Files\GIMP 2\bin
                                    # to 
                                    # /mnt/c/Program Files/GIMP 2/bin
        driveLetter=inputStr[:inputStr.find(':')].lower()
        pathWithoutLetter=inputStr[inputStr.find('/'):]
        returnVal='/mnt/'+driveLetter+pathWithoutLetter
        # print(f"{driveLetter}\n{pathWithoutLetter}",sep='\n')
    else: # @note Eg: \\wsl.localhost\Enterprise/home\olliver\Desktop\keyboardLayoutConverter\keyboard-layout-converter
          # to
          # /home/olliver/Desktop/keyboardLayoutConverter/keyboard-layout-converter
        returnVal='/'+inputStr[len(wslRootDir):]

else:
    if inputStr[0]=='/':
        inputStr=inputStr[1:]
    pathDestinationIsOutsideWsl=inputStr.startswith("mnt")
    if pathDestinationIsOutsideWsl: # @note Eg: /mnt/c/PythonPathLibraries/fast-examples
                                    # to
                                    # c:/PythonPathLibraries/fast-examples
        driveLetterStart=1+inputStr.find('/',1)
        driveLetterEnd=inputStr.find('/',driveLetterStart+1)
        driveLetter=inputStr[driveLetterStart:driveLetterEnd]
        returnVal=driveLetter+':/'+inputStr[driveLetterEnd+1:]
        # print(driveLetter,sep="\n")
    else: # @note Eg: /home/olliver/Desktop/keyboardLayoutConverter/keyboard-layout-converter
          # to
          # \\wsl.localhost\Enterprise/home/olliver/Desktop/keyboardLayoutConverter/keyboard-layout-converter
        # print(f"wslRootDir: {wslRootDir}")
        returnVal=(wslRootDir+'/'+inputStr)
        # print(returnVal)
if returnVal[-1]=='/':
    returnVal=returnVal[:-1]
print(f"""\
inputStr: {inputStr}
isWindowsPath: {isWindowsPath}
pathDestinationIsOutsideWsl: {pathDestinationIsOutsideWsl}
returnVal: {returnVal}""")
clipboard.copy(returnVal)