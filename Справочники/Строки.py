# str.lower() # - вернет копию строки str, в которой все символы будут преобразованы в нижний регистр

# str.find() # - находит первое вхождение указанного значения

# str.rfind() # - возвращает индекс последнего совпадения подстроки sub в строке str

# str.replace('a', 'b') # - вернет копию строки, в которой все вхождения подстроки "a" заменены на подстроку "b"

# str.upper() # - вернет копию строки str с символами, преобразованными в верхний регистр

# list.pop(i) # - позволяет получить элемент по индексу удаляя его из последовательности


from collections import Counter


def top3(st):
    counter_top3 = Counter(st.replace(' ', '')).most_common(3)
    print(counter_top3)
    return ', '.join([f'{letter} - {cnt}' for letter, cnt in counter_top3])

top3("fdklsfjlsdfjdsfjdjfdsnfkndsfaskdkokwjqopjewqekqwjfuihplvkcxjnvbhfqwel;kdfldskfgjewjf;fdkljfd")