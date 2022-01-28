import os, random
import webbrowser


def filepicker():
    basedir = 'C\\Users'
    try:
        userinput01 = input('Input the directory to use: ')
        try:
            userinput01_stripped = userinput01.strip('"')
            basedir = userinput01_stripped
        except Exception as b:
            print(b)
    except Exception as c:
        print(c)
    loop = True
    while loop == True:
        print('\n\nType dir to change current directory.\n\n')
        userinput02 = input('open random file? Y/N: ')
        if userinput02 == 'Y' or userinput02 == 'y':
            try:
                file = random.choice([x for x in os.listdir(basedir) if os.path.isfile(os.path.join(basedir, x))])
                print('Opening Random File {}...'.format(file))
                webbrowser.open(os.path.join(basedir, file))
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
                userinput03 = input('Input the new directory to use: ')
                try:
                    basedir = userinput03
                except Exception as f:
                    print(f)
            except Exception as g:
                print(g)
        else:
            print('Select valid option')
def main():
    print('Random File Picker V.2')
    try:
        filepicker()
    except Exception as h:
        print(h)
if __name__ == '__main__':
    main()
