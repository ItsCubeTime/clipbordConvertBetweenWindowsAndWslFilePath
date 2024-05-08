# clipbordConvertBetweenWindowsAndWslFilePath
Takes whatever is in your clipboard, tries to figure out whether its a Linux or Windows style path, then tries to figure out if the path leads somewhere within the WSL environment or not and finally converts from the current path style (Windows path to Linux style and vise versa) to the other - and then puts the result in your clipboard.

# Usage & Examples:
1. Set the contents of`wslRootDir.txt` to where your WSL is mounted:
![image](https://github.com/ItsCubeTime/clipbordConvertBetweenWindowsAndWslFilePath/assets/20190653/fd3596f7-a617-4665-bbcc-929136d2ed92)
2. Go into your WSL environtment and copy any file path:
![image](https://github.com/ItsCubeTime/clipbordConvertBetweenWindowsAndWslFilePath/assets/20190653/189a90d3-1580-4aa8-a726-2b3cdb75c502)
So you have something like: `/mnt/c/Program Files/Google/Chrome/` in your clipboard.
3. Run `clipbordConvertBetweenWindowsAndWslFilePath.exe` (or `python clipbordConvertBetweenWindowsAndWslFilePath.py`).
4. You should now have the Windows equalent path in your clipboard instead, eg: `c:/Program Files/Google/Chrome`
5. ???
6. Profit

I recommend creating a shortcut for the script and placing it in `C:\ProgramData\Microsoft\Windows\Start Menu\Programs`. That way you can just press the Windows key, type "clipboard Convert" and press enter every time you want to make a conversion.
