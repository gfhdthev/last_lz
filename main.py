#gfhdthev
#файл для объединения двух заданий


#импортируем модули
import pyramid
import Archimed

def main():
    mod = input('Ксли хотите использовать прграмму по нахождению объема введите P, если пловучесть объекта, то A: ')
    if mod.lower() == 'p':
        pyramid.main()
        main()
    elif mod.lower() == 'a':
        Archimed.main()
        main()
    else:
        return 1

if __name__ == '__main__':
    main()