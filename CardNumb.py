import random


class Uncoder():
    def wor(bins = None):
        if bins == None: bins = ['40587075', '547913', '48934742', '54597475', '54867390', '48009997', '54867378', '52804120', '416496', '41437994', '547942', '48093821', '549445', '52132434', '43031226', '44762409', '552055', '54238896', '52804124', '40378078', '51007092', '43031202', '54711475', '43031278', '523040', '51546426', '55302951', '54867407', '54711488', '488968', '52568956', '52132458', '52568903', '677013', '412477', '53506169', '51007088', '54899913', '54899957', '424646', '54867419', '548792', '677608', '457858', '43008815', '43777290', '40389624', '427414', '42497597', '520138', '48011386', '677059', '44762426', '548386', '48934714', '543645', '544552', '548438', '460065', '48062302', '54711418', '524468', '470675', '5521756778', '48489135', '475764', '55217585', '45658809', '40333076', '48489182']
        basic_nums = '0123456789'
        rand_bin = random.choice(bins)
        residual = 16 - len(rand_bin)
        if residual > 0:
            card = str(rand_bin) + ''.join(random.choices(basic_nums,k=residual))
            random_year = random.randint(2022,2029)
            random_month = str(random.randint(1,12))
            if len(random_month) == 1: random_month = '0' + random_month
            random_cvv = ''.join(random.choices(basic_nums,k=3))
            return f"{card}|{random_month}|{random_year}|{random_cvv}"
        else: return ''

    cards = ''
    choice_user = int(input('Select type of generation that you want \n\t1-Russian Bins\n\t2-Custom Bins from file\n\t=> '))
    if choice_user != 1 and choice_user != 2:
        while choice_user != 1 and choice_user != 2:
            choice_user = int(input('The number you have entered it is not valid\nYou should choose ether 1 or 2\n\t=> '))
        
    count = int(input('Ok, now Enter the count of cards that you want to generate it\n\t=> '))
    if choice_user == 1:
        bins = None
    else:
        bins = open(input('well, Enter now the path of the file that contains the bins\n\t=> '),'r',encoding='utf-8').read().splitlines()

    for i in range(0,count):
        cards += f"{wor(bins)}\n"

    with open('res.txt','w',encoding='utf-8') as file:
        file.write(cards)
        file.close()
    print(f'Successfully generate {count} cards\n\tSaved in res.txt')
Uncoder