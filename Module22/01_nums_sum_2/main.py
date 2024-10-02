# TODO здесь писать код
numbers = open('numbers.txt', 'r')
summ_num = 0
for i_line in numbers:
    nums = i_line.split()
    for num in nums:
        summ_num += int(num)
numbers.close()
answer = open('answer.txt', 'w')
answer.write(str(summ_num))
answer.close()
