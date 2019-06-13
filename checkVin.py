import re

def replace_all(txt, r_dict):
    for k, v in r_dict.items():
        txt = txt.replace(k, v)
    return txt

# def find_any(txt, f_list):
#     for l in f_list:
#         if txt.find(l) > -1:
#             return True
#     return False

def isValidVin(vin):
    vin = vin.upper()
    available_symbol_pattern = re.compile(r'[^A-HJ-NPR-Z0-9]')
    # check_number_pattern = re.compile(r'[^0-9X]')
    if len(vin) < 17:   #or find_any(vin, ['I', 'O', 'Q']) == True
        return -1
    if re.search(available_symbol_pattern, vin) or not(vin[-4:].isdigit()):
        return -2
    # if re.search(check_number_pattern,vin[8]):
    #     return -3
    widths = [8,7,6,5,4,3,2,10,'-',9,8,7,6,5,4,3,2]    
    eq = {'A':'1','B':'2','C':'3','D':'4','E':'5','F':'6','G':'7','H':'8','J':'1','K':'2','L':'3','M':'4','N':'5','P':'7','R':'9','S':'2','T':'3','U':'4','V':'5','W':'6','X':'7','Y':'8','Z':'9'}
    check_num = vin[8]
    if not(check_num.isdigit()) and check_num != 'X':
        check_num = eq[check_num]
    print(check_num)
    new_vin = replace_all(vin, eq)
    # print(new_vin)
    count = 0
    for i in range(0,17):
        if widths[i] == '-':
            continue
        count += int(new_vin[i]) * widths[i]
    # print(count)
    if ((count % 11) < 10 and (count % 11) == int(check_num)) or ((count % 11) == 10 and check_num == 'X'):
        return 1
    return 0

def checkVin():
    vin = input('Введите vin для проверки, для выхода введите символ(!): ')
    while vin != '!':
        checked = isValidVin(vin)
        if checked == 0:
            print('Vin не является валидным так как результирующий символ не совпадает')
        if checked == -1:
            print('Колисечство введенных символов не достаточно для проверик Vin')
        if checked == -2:
            print('Vin содержаться недопустимые символы')
        if checked == -3:
            print('Vin результирующий символ нельзя проверить')
        if checked == 1:
            print('Vin является валидным')
        vin = input('Введите vin для проверки, для выхода введите символ(!): ')

if __name__ == '__main__':
    checkVin()

    # print(isValidVin('XW7BF3HK90S117684'))
    # print(isValidVin('jh2pc35051m200020'))
    # print(isValidVin('X896377R7K0AR3039'))