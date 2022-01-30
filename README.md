# Random-File-Picker
Wanted to open random mp3 files. Based on a Stack Overflow Comment. Made in Jan. 2022
- V.1 Notes: It open any random File inside a folder, but not in the subfolders of chosen folder. Typing folder location with quotations causes an error. not case sensitive, does not diferentiate between '/' and '\\'
- V.2 Change Notes: Typing folder with quotes, or straight copy pasting from Explorer.exe is now fine, it no longer causes causes an error.
- V.2 Folder with EXE Notes: Compiled using pyinstaller, requires entire folder. Mildly tested on PC it was made on. Made 03:53 2022.01.28
- V.2.1 Change Notes: Fixed error with directory changing. Exe version mildly tested on PC it was made on. Made 2022.01.28 04:00
- V.2.3.1 Change Notes: Moved from webbrowser function to os.startfile. Added quick directories: music and pictures, using getpass function. Program creates a log text file when it runs into an error. Now on program startup it prints program version, and the time when program started.
- .

- Been using V.2.1 for 4 hours. No errors so far, Some songs repeat occasionally, but that is because it is true random.
- Tested V.2.1 on 3 other computers that run windows, and don't have python installed. Program worked on both windows 10 machines, but not windows 7.
- .
- .
- Note: File_and_folder_crawler has a random function as well. 
- .
- How to use: start program, type in directory of choice when prompted. Example: "C:/Users/example/music" press Enter. press y, then enter. It will open a random file in the folder you chose, example: a random .mp3 file inside C:/Users/example/music.
- .
- V.2.3.1 Quick directory notes: when changing directory, typing music, makes music folder the base directory. typing documents, make documents into base directory. typing pictures, makes pictures into the base directory.
- .
- Type n and press enter, to exit the program
