main_list = [1, 5, 3]
sec_list1 = [1, 5, 1, 5]
sec_list2 = [1, 3, 1, 5, 3, 3]

main_list.extend(sec_list1)
print('Кол-во цифр 5 при первом объединении:', main_list.count(5))
for i in range(main_list.count(5)):
    main_list.remove(5)

main_list.extend(sec_list2)
print('Кол-во цифр 3 при втором объединении:', main_list.count(3))
print('Итоговый список:', main_list)
# TODO переписать программу
