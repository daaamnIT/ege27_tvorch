def max_Sum(seq):
    max_rem = [-1] * 6                                              #массив максимальных чисел
    max_pair_rem = [-1] * 6                                         #массив максимальных пар
    max_trip_rem = [-1] * 6                                         #массив максимальных троек
    result = -1
    for i in range(len(seq)):
        curr_num = seq[i]
        print(max_rem, max_pair_rem, max_trip_rem, result, curr_num)

        for j in range(6):
            if (curr_num + j) % 6 == 0:
                result = max(result, curr_num + max_trip_rem[j])    #ищем максимальный результат

        for j in range(6):                                          #ищем максимальную тройку на позицию j
            max_trip_rem[(curr_num + j) % 6] = max(max_trip_rem[(curr_num + j) % 6], curr_num + max_pair_rem[j])

        for j in range(6):                                          #ищем максимальную пару на позицию j
            max_pair_rem[(curr_num + j) % 6] = max(max_pair_rem[(curr_num + j) % 6], curr_num + max_rem[j])

        max_rem[curr_num % 6] = max(max_rem[curr_num % 6], curr_num)#обновляем массив максимальных чисел
    print(max_rem, result)                                          # выводим результат
    return result
    
def main():
    sequence = []
    with open('27_1a.txt', 'r') as file:                # считываем данные
        num_of_str = file.readline()                    # записываем
        for i in range(int(num_of_str)):                # проходим по всем данным
            sequence.append(int(file.readline()))

    # sequence = [6, 4, 13, 11, 10, 8]
    print("Результат:", max_Sum(sequence))              # выводим результат


if __name__ == '__main__':
    main()

# Идея:
# Сделать такие массивы сумм пар двоек и троек, чтобы на i-той позиции этих массивов был записан остаток от деления этой
# суммы на i. Также будет массив, в котором будут хранится на i-той позиции максимальные суммы, которые при делении на 6
# дают остаток i. Это означает, что для каждого чилса мы сможем быстро находить максимальную сумму пары и тройки.
# Следовательно по числу мы можем быстро составить четверку с максимальной суммой.
