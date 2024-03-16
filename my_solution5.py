#это файл с решением задачи 5
f_r = open('C:/Users/olimp/git_megapolis/languages.txt', encoding='utf-8').readlines()
#открываем файл предоставленный в задаче
headlines = f_r.pop(0).strip().split('$')
headlines[0] = 'title'
#определяем заголовки в исходном файле
f_r = [i.strip().split('$') for i in f_r]
# превращаем файл в список
dicc = {'unknown': []}
#инициализация словоря
for i in f_r:
    if i[headlines.index("creators")] in dicc.keys():
        dicc[i[headlines.index("creators")]].append(i[headlines.index("title")])
        # запись в словарь если элемент уже существует
    elif i[headlines.index("creators")] == "":
        dicc['unknown'].append(i[headlines.index("title")])
        # запись если автор не указан
    else:
        dicc[i[headlines.index("creators")]] = [i[headlines.index("title")]]
        # добавление нового ключа в словарь

a = dicc['unknown']
for i in range(10):
    print('unknown', a[i])
# вывод в заданном формате
