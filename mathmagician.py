import time
import math

class Mathmagician():

    def __init__(self):
        self.number = 0

    def show_menu(self):
        menu = "============MENU==========\n1 = fibonacci numbers\n2 = integers\n3 = prime numbers\nctrl+c to exit\n"
        print(menu)

        func_to_run = input("which function would you like to run? ")
        if func_to_run not in ("1", "2", "3"):
            print("please press 1, 2, or 3")

        elif func_to_run == "1":
            while True:
                try:
                    iterations = int(input("how many fibonacci numbers would you like to print? "))
                except ValueError:
                    print("please input a digit!")
                    continue
                else:
                    self.fibonacci(int(iterations))
                    break
        elif func_to_run == "2":
            while True:
                try:
                    iterations = int(input("how many integers would you like to print? "))
                except ValueError:
                    print("please input a digit!")
                    continue
                else:
                    self.integer(int(iterations))
                    break
        elif func_to_run == "3":
            while True:
                try:
                    iterations = int(input("how many prime numbers would you like to print? "))
                except ValueError:
                    print("please input a digit!")
                    continue
                else:
                    self.prime(int(iterations))

    def prime(self, iterations):
        counter = 1
        potential_number = 2
        self.number = 2
        while counter <= iterations:
            isPrime = True
            for n in range(2, int(math.sqrt(potential_number) + 1)):
                if potential_number % n == 0:
                    isPrime = False
                    break
            if isPrime:
                self.number = potential_number
                time.sleep(0.3)
                print(self.number)
                counter += 1
            potential_number += 1
        time.sleep(.6)
        self.show_menu()

    def fibonacci(self, iterations):
        self.number = 1
        print(self.number)

        fib_list = [1, 1]
        for x in range(iterations-1):
            self.number = fib_list[-1]
            time.sleep(0.3)
            print(self.number)
            fib_list.append(fib_list[-1]+fib_list[-2])
            fib_list.remove(fib_list[-3])
        time.sleep(.6)
        self.show_menu()

    def integer(self, iterations):
        self.number = 0
        for math in range(iterations):
            self.number +=1
            time.sleep(0.3)
            print(self.number)
        time.sleep(.6)
        self.show_menu()



if __name__ == '__main__':
    thing = Mathmagician()
    thing.show_menu()
