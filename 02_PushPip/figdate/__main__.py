from figdate import figlet_date
import sys
import locale

if __name__ == '__main__':
    
    locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
    
    if len(sys.argv) == 3:
        print(figlet_date(sys.argv[1], sys.argv[2]))
    
    elif len(sys.argv) == 2:
        print(figlet_date(format=sys.argv[1]))
    
    else:
        print(figlet_date())