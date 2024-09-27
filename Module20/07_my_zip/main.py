# TODO здесь писать код
string =  'abcd'
tpl_num = (10, 20, 30, 40)
result = ((sym, num) for sym, num in zip(string, tpl_num))
print(result)
for elem in result:
    print(elem)

result_add = ((value, tpl_num[index]) for index, value in enumerate(string))
print(result_add)
for elem in result_add:
    print(elem)