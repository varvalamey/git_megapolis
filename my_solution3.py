#python

#это файл с решением задачи 3
f_r = open('C:/Users/olimp/git_megapolis/languages.txt', encoding='utf-8').readlines()
#открываем файл предоставленный в задаче
headlines = f_r.pop(0).strip().split('$')
headlines[0] = 'title'
#определяем заголовки в исходном файле
f_r = [i.strip().split('$') for i in f_r]
# превращаем файл в список
print('Введите год:')
a = input()
while a != '0000':
    language = list(filter(lambda x: x[headlines.index("appeared")] == a, f_r))
    # делаем список из языков, которые были созданы в заданном году
    if language:
        for i in language:
            print(f'В {a} был создан {i[headlines.index("title")]} его создатель: {i[headlines.index("creators")]}')
            # вывод в заданном формате
    else:
        print("В этом году не было создано ЯП")
    print('Введите год:')
    a = input()