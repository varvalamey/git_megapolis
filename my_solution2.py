#это файл с решением задачи 2
def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j][headlines.index("title")] > array[j+1][headlines.index("title")]:
                a = array[j]
                b = array[j+1]

                array[j] = b
                array[j+1] = a
    return array
# алгоритм сортировки пузырьком для двумерного массива


f_r = open('C:/Users/olimp/git_megapolis/languages.txt', encoding='utf-8').readlines()
#открываем файл предоставленный в задаче
headlines = f_r.pop(0).strip().split('$')
headlines[0] = 'title'
#определяем заголовки в исходном файле
f_r = [i.strip().split('$') for i in f_r]
# превращаем файл в список
k =bubble_sort(f_r)[0:5]
# сортируем массив с помощью bubble_sort
for i in k:
    print(f'{i[headlines.index("title")]} – год создания {i[headlines.index("appeared")]} - {i[headlines.index("book_count")]}')
# выводим данные в необходимом формате

