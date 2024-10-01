# TODO здесь писать код
def str_to_lst(str):
    return str.split('\n')
zen = open('zen.txt', 'r')
zen_str = zen.read()
zen_lst = str_to_lst(zen_str)
zen.close()
for elem in zen_lst[::-1]:
    print(elem)