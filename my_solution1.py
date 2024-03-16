#это файл с решением задачи 1
f_r = open('C:/Users/olimp/git_megapolis/languages.txt', encoding='utf-8').readlines()
#открываем файл предоставленный в задаче
headlines = f_r.pop(0).strip().split('$')
headlines[0] = 'title'
#определяем заголовки в исходном файле
f_r = [i.strip().split('$') for i in f_r]
# превращаем файл в список

f_w = open('C:/Users/olimp/git_megapolis/program.csv', mode='w', encoding='utf-8')
#открываем файл для записи в формате csv
f_w.write(';'.join([headlines[headlines.index("title")], headlines[headlines.index("appeared")], headlines[headlines.index("book_count")]]))
#добавляем в файл необходимые заголовки
for i in f_r:
    f_w.write('\n')
    f_w.write(';'.join([i[headlines.index("title")], i[headlines.index("appeared")], i[headlines.index("book_count")]]))
f_w.close()
# добавили все значения из файла f_r и закрыли файл для записи

count = len(list(filter(lambda x: x[headlines.index("type")] == 'язык запросов', f_r)))
#подсчет количества элементов в списке, который отфильтрован в оригинальном файле по хначению поля type "язык запросов"
print(f'Количество языков запросов равно: {count}')

#дополнительный вывод задачи