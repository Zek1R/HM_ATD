from array import *
from os import system
from time import *
from Merge import *

#       TABLE OF ARRAY TYPE

# 'b'	signed char	        int	    1
# 'B'	unsigned char	    int	    1
# 'h'	signed short	    int	    2
# 'H'	unsigned short	    int	    2
# 'i'	signed int	        int	    2
# 'I'	unsigned int	    int	    2
# 'l'	signed long	        int	    4
# 'L'	unsigned long	    int	    4
# 'q'	signed long long	int	    8
# 'Q'	unsigned long long	int	    8
# 'f'	float	            float	4
# 'd'	double	            float	8


class ATD:
    def __init__(self, name, code_type):
        self.type_table = {'i': 'int',
                          'f': 'float'}
        self.code_type = code_type
        self.name = name
        self.arr = array(code_type)
        self.current_index = 0
    

    def arr_add(self):
        
        value = input("Введите значение > ")
        for x in value:
            if not x in ['1','2','3','4','5','6','7','8','9','0','.',',']:
                print(f"TypeError. Your value >{x}< is not a {self.type_table[self.code_type]} type")   
                sleep(0.2)
                return 
        

        if ('.' in value) or (',' in value):
            value = float(value)
        else:
            value = int(value)
        
        # print(str(type(value)).split("'")[1] == self.type_table[self.code_type])

        if str(type(value)).split("'")[1] == self.type_table[self.code_type]:
            self.current_index += 1 
            self.arr.append(value)
            
        else:
            print(f"TypeError. Your value >{value}< is not a {self.type_table[self.code_type]} type")
            sleep(0.5)
            return 
            
        
    def arr_pop(self):
        if len(self.arr) == 0:
            print("Массив пустой")
            sleep(0.5)
            return
        x = self.arr.pop(0)
        return x
    
    
    def arr_sort(self):
        self.arr = merge_sort(self.arr)


    def arr_print(self):
        system('cls')
        print("name:", self.name)
        data = '['
        for x in self.arr:
            data += str(x) + ', '
        data += ']'
        data = data.replace(", ]", "]")
        print(data)


    def get_info(self):
        info = str(self.name) + '   ' + f'({self.type_table[self.code_type]})'
        return info
    

    def comands(self):
        self.arr_print()
        cmd = input("[1] - Добавить новый элемент\n[2] - Удалить последний элемент (pop)\n[3] - Сортировка массива\n[0] - Выход\nВведите команду\n>")
        for x in cmd:
            if not x in ['0', '1', '2', '3']:
                print("Неверная команда")
                break
        
        if cmd ==  '0':
            return False
        elif cmd == '1':
            self.arr_add()
        elif cmd == '2':
            self.arr_pop()
        elif cmd == '3':
            self.arr_sort()
        return True
    
        

# test = ATD('Test_ATD', input("Input DataType > "))
# test.arr_add(input("[i] - integer\n[f] - float\nInput > "))
# test.arr_add(input("[i] - integer\n[f] - float\nInput > "))
# test.arr_pop()
# test.arr_print()
# test.add('2')
# test.add(3)


class App:
    def __init__(self):
        self.arrays = []
    
    def make_array(self):
        system('cls')
        name = input("Введите имя нового массива > ")
        t = False
        while not t:
            code_type = input("\n[i] - integer\n[f] - float\n\nInput array DataType > ")
            if code_type == 'i' or code_type == 'f':
                print(f"Массив {name} создан")
                t = True
            else:
                print("Ошибка. Тип неверный тип данных.")
        arr = ATD(name, code_type)
        self.arrays.append(arr)
    

    def edit_atd(self):
        #print(len(self.arrays))
        t = True
        while t:
            self.print_atd()
            num = input("Введите номер массива (0 - Отменить ввод)\n> ")
            if num == '0':
                return system('cls')
            chk = False
            for x in num:
                if x not in [str(i) for i in range(10)]:
                    print("Неправильный номер")
                    sleep(0.5)
                    system('cls')
                    break
                chk = True
            if chk == True:
                num = int(num) - 1
                if (num > len(self.arrays) - 1) or (num < 0):
                    print("Неправильный номер")
                    sleep(0.5)
                    system('cls')
                else:
                    t = False

        e = True
        while e:
            e = self.arrays[num].comands()
            

    def print_atd(self):
        if len(self.arrays) != 0:
            for x in range(len(self.arrays)):
                print(f'[{x+1}] - {self.arrays[x].get_info()}')
        else:
            print("Не создано ни одного массива.")
        print('-'*len("Не создано ни одного массива."))


    def comand(self):
        system('cls')
        self.print_atd()

        print("\n[1] - Создать новый массив\n[2] - Редактировать массив\n[0] - Выход из программы\n")
        cmnd = input("Введите команду > ")
        
        if cmnd == '0':
            return False
        elif cmnd == '1':
            self.make_array()
            system("cls")
        elif cmnd == '2':
            system("cls")
            self.edit_atd()
        else:
            print("Неправильная команда")
            sleep(0.500)
            system("cls")
        return True

app = App()
t = True
while t:
    t = app.comand()


# app.print_arrays()
# app.make_array()
# app.arrays[0].arr_add()
# app.arrays[0].arr_add()
# app.arrays[0].arr_add()
# app.arrays[0].arr_add()
# app.arrays[0].arr_add()
# app.arrays[0].arr_print()