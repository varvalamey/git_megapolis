#это файл с решением задачи 1
f_r = open('C:/Users/olimp/git_megapolis/languages.txt', encoding='utf-8').readlines()
#открываем файл предоставленный в задаче
headlines = f_r.pop(0).strip().split('$')
headlines[0] = 'title'
#определяем заголовки в исходном файле
f_r = [i.strip().split('$') for i in f_r]
# превращаем файл в список
a = list(set(list([i[headlines.index('type')] for i in f_r])))
#создаем список с уникальными значениями типов данных заданных в оригинальном файле
for i in a:
    print(f"{sum([int(i[headlines.index('book_count')]) for i in list(filter(lambda x: x[headlines.index('type')] == i, f_r))])} книг содержится в библиотеке по типу {i}")
    # вывод в заданном формате с помощью суммирования данных в фильтрованном по нужному типу списке
