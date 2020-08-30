from time import sleep
print("Наш новый телеграм @youcanhackit")
print("DDoSer")
print("Url сайта:")
x = input()
print("Количество потоков:")
input()
print("Кол-во запросов для каждого потока:")
w = input()

while True:
   print("Запрос на " + x + " выполнен")
   sleep(50 / int(w))
