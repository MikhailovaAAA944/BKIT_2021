# используется для сортировки
from operator import itemgetter

class Programm:
    def __init__(self, id, nam, price, comp_id):
        self.id = id
        self.nam = nam
        self.price = price
        self.comp_id = comp_id

class Comp:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Programm_Comp:
    def __init__(self, comp_id, programm_id):
        self.comp_id = comp_id
        self.programm_id = programm_id

comps = [Comp(1, 'Acer'),
    Comp(2, 'Lenovo'),
    Comp(3, 'Asus'),]

programms = [Programm(1, 'MC Office', 5800, 2),
    Programm(2, 'UTorrent', 0, 3),
    Programm(3, 'PDF Converter', 350, 3),
    Programm(4, 'Access', 4990, 2),
    Programm(5, 'Translator', 750, 1),]

programm_comps = [Programm_Comp(1,1),
    Programm_Comp(1,5),
    Programm_Comp(3,3),
    Programm_Comp(2,1),
    Programm_Comp(1,4),]

def main():
    one_to_many = [(m.nam, m.price, o.name)
        for o in comps
        for m in programms
        if m.comp_id == o.id]
    
    many_to_many_temp = [(o.name, mo.comp_id, mo.programm_id)
        for o in comps
        for mo in programm_comps
        if o.id == mo.comp_id]

    many_to_many = [(m.nam, m.price, comp_name) 
        for comp_name, comp_id, programm_id in many_to_many_temp
        for m in programms if m.id == programm_id]

    print('Задание Г1')
    res_11 = [(o.name,list(nam for nam,_,name in one_to_many if name == o.name)) for o in comps if o.name[0] == 'А'] 
    print(res_11)

    print('\nЗадание Г2')
    res_12_unsorted = []
    # Перебираем все компьютеры
    for o in comps: 
        # Список программ компьютера
        o_programms = list(filter(lambda x: x[2] == o.name, one_to_many))
        # Если компьютер не пустой
        if len(o_programms) > 0:
            res_12_unsorted.append((o.name, max(o_programms, key=lambda x: x[1])[1]))

    # Сортировка по максимальной стоимости
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание Г3')
    res_13 = []
    # Перебираем все компьютеры
    for programm,_,comp in many_to_many:
        res_13.append((programm, comp))
    res_13 = sorted(res_13, key=itemgetter(1))
    print(res_13)

if __name__ == '__main__':
    main() 
    
