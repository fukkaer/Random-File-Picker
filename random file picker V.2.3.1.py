import os, random
import webbrowser
import time
import getpass

#current_user is the user that is currently logged in

current_user = getpass.getuser()

basedir = 'C:\\users'

#this is a test to see if Exception handling can/will write to an error log file
#try:
#    raise ValueError('test')
#except Exception as ex:
#    added_error = str(ex)
#    write_error = open('random_log.txt', 'a')
#    write_error.write(added_error)
#    write_error.write(':::')
#    write_error.write(time.strftime('%X %x'))
#    write_error.write('\n')
#    write_error.close()

#quick_dir has quick paths to folders like music or documents

def quickdir():
    global basedir
    try:
        userinput_quickdir01 = input('Input Directory to use: ')
        try:
            if userinput_quickdir01 == 'music' or userinput_quickdir01 == 'Music' or userinput_quickdir01 == 'm':
                music_dir_list = ['C://Users/', current_user, '/music']
                music_dir = ''.join(music_dir_list)
                try:
                    music_dir_stripped = music_dir.strip('"')
                    basedir = music_dir_stripped
                except Exception as s:
                    print(s)
                    write_Error = open('Random_file_picker_log.txt','a')
                    added_Error = str(s)
                    write_Error.write(added_Error,':::')
                    write_Error.write(time.strftime('%X %x'))
                    write_Error.write('\n')
                    write_Error.close()
            elif userinput_quickdir01 == 'pictures' or userinput_quickdir01 == 'pics' or userinput_quickdir01 == 'Pictures' or userinput_quickdir01 == 'p':
                basedir_pics = ["C://Users/", current_user, "/Pictures"]
                pics_dir = ''.join(basedir_pics)
                try:
                    basedir_pics_stripped = pics_dir.strip('"')
                    basedir = basedir_pics_stripped
                except Exception as t:
                    print(t)
                    try:
                        write_Error = open('Random_file_picker_log.txt','a')
                        added_Error = str(t)
                        write_Error.write(added_Error,':::')
                        write_Error.write(time.strftime('%X %x'))
                        write_Error.write('\n')
                        write_Error.close()
                    except Exception as u:
                        print('Error adding Error t to log')
                        print(u)
            elif userinput_quickdir01 == 'documents' or userinput_quickdir01 == 'docs' or userinput_quickdir01 == 'Documents' or userinput_quickdir01 == 'd':
                basedir02 = ["C://Users/", current_user, "\Documents"]
                docs_dir = ''.join(basedir02)
                try:
                    basedir02_stripped = docs_dir.strip('"')
                    basedir = basedir02_stripped
                except Exception as i:
                    print(i)
                    try:
                        write_Error = open('Random_file_picker_log.txt','a')
                        added_Error = str(i)
                        write_Error.write(added_Error,':::')
                        write_Error.write(time.strftime('%X %x'))
                        write_Error.write('\n')
                        write_Error.close()
                    except Exception as j:
                        print('Error adding Error i to log')
                        print(j)
            elif userinput_quickdir01 != 'music' or userinput_quickdir01 != 'pictures' or userinput_quickdir01 != 'documents':
                try:
                    userinput_quickdir01_stripped = userinput_quickdir01.strip('"')
                    basedir = userinput_quickdir01_stripped
                except Exception as k:
                    print(k)
                    try:
                        write_Error = open('Random_file_picker_log.txt','a')
                        added_Error = str(k)
                        write_Error.write(added_Error,':::')
                        write_Error.write(time.strftime('%X %x'))
                        write_Error.write('\n')
                        write_Error.close()
                    except Exception as l:
                        print('Error adding Error k to log')
                        print(l)
        except Exception as m:
            print(m)
            try:
                write_Error = open('Random_file_picker_log.txt','a')
                added_Error = str(m)
                write_Error.write(added_Error,':::')
                write_Error.write(time.strftime('%X %x'))
                write_Error.write('\n')
                write_Error.close()
            except Exception as n:
                print('Error adding Error m to log')
                print(n)
    except Exception as o:
        print(o)
        try:
            write_Error = open('Random_file_picker_log.txt','a')
            added_Error = str(o)
            write_Error.write(added_Error,':::')
            write_Error.write(time.strftime('%X %x'))
            write_Error.write('\n')
            write_Error.close()
        except Exception as p:
            print('Error adding Error o to log')
            print(p)

#filepicker() function opens the random file and calls on quickdir() when the you type dir

def filepicker():
    global basedir
    try:
        quickdir()
    except Exception as q:
        print(q)
        try:
            write_Error = open('Random_file_picker_log.txt','a')
            added_Error = str(q)
            write_Error.write(added_Error,':::')
            write_Error.write(time.strftime('%X %x'))
            write_Error.write('\n')
            write_Error.close()
        except Exception as r:
            print('Error adding Error q to log')
            print(r)
    loop = True
    while loop == True:
        print('\n\nType dir to change current directory.\n\n')
        userinput02 = input('open random file? Y/N: ')
        if userinput02 == 'Y' or userinput02 == 'y':
            try:
                file = random.choice([x for x in os.listdir(basedir) if os.path.isfile(os.path.join(basedir, x))])
                print('Opening Random File {}...'.format(file))
                os.startfile(os.path.join(basedir, file))
            except Exception as d:
                print(d)
        elif userinput02 == 'n' or userinput02 == 'N':
            try:
                loop = False
                break
            except Exception as e:
                print(e)
        elif userinput02 =='dir'or userinput02 == 'directory' or userinput02 == 'basedir' or userinput02 == 'basedirectory' or userinput02 == 'base directory':
            try:
                quickdir()
            except Exception as g:
                print(g)
        else:
            print('Select valid option')

#start_print() function is the text that gets printed when the program starts

def start_print():
    print('Random File Picker V.2.3.1')
    print(time.strftime('%X %x'))
    print('\n\n')
#main() is the main function
def main():
    start_print()
    try:
        filepicker()
    except Exception as h:
        print(h)
if __name__ == '__main__':
    main()
