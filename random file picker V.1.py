import os, random
import webbrowser
basedir = "C:\\Users"

#file = random.choice([x for x in os.listdir(basedir) if os.path.isfile(os.path.join(basedir, x))])

#print('Opening File {}...'.format(file))
#webbrowser.open(os.path.join(basedir, file))

print('Random File Picker V.1.0')
try:
    userinput03 = input('input Directory to use without quotations: ')
    try:
        basedir = userinput03
    except Exception as e:
        print(e)
except Exception as f:
    print(f)
loop = True
while loop == True:
    print('\n\nType dir to change directory currently used.\n\n')
    userinput = input('open random file? y/n: ')
    if userinput == 'y':
        try:
            file = random.choice([x for x in os.listdir(basedir) if os.path.isfile(os.path.join(basedir, x))])
            print('Opening File {}...'.format(file))
            webbrowser.open(os.path.join(basedir, file))
        except Exception as a:
            pront(a)
    elif userinput == 'n':
        try:
            loop = False
            break
        except Exception as b:
            print(b)
    elif userinput =='dir' or userinput == 'di' or userinput == 'diir' or userinput == 'ddir' or userinput == 'dirr' or userinput == 'directory' or userinput == 'basedir' or userinput == 'basedirectory' or userinput == 'base directory':
        try:
            userinput02 = input('input new directory location without quotations: ')
            try:
                basedir = userinput02
            except Exception as c:
                print(c)
        except Exception as d:
            print(d)
    else:
        print('select valid option')
input('press ENTER to exit')

#create file type checking so no unwanted file types are opened, ex. .kra or .webp
