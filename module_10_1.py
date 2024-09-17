from datetime import datetime
from time import sleep
from threading import Thread
import time

def wite_words(word_count, *file_name):
    with open(*file_name, 'w', encoding='utf-8') as file:
        for i in range(1,word_count +1):
            file.write(f'Какое-то слово № {i} \n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')

start = time.time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
end = time.time()
time_res = end - start
print(f'Работа потоков: {round(time_res,4)} секунд(ы)')

first = Thread(target=wite_words, args=(10, 'example5.txt'))
second = Thread(target=wite_words, args=(30, 'example6.txt'))
third = Thread(target=wite_words, args=(200, 'example7.txt'))
fourth = Thread(target=wite_words, args=(100, 'example8.txt'))
start_1 = time.time()
first.start()
second.start()
third.start()
fourth.start()

first.join()
second.join()
third.join()
fourth.join()
end_1 = time.time()
time_res_1 = end_1 - start_1
print(time_res_1)