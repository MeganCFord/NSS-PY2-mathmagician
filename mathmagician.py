import time
import math

class Mathmagician():

    def __init__(self):
        self.number = 0
        self.show_menu()

    def show_menu(self):
        menu = "============MENU==========\n1 = fibonacci numbers\n2 = integers\n3 = prime numbers\nctrl+c to exit\n"
        print(menu)

        func_to_run = input("which function would you like to run? ")
        # make sure the input is in the menu.
        if func_to_run not in ("1", "2", "3"):
            print("please press 1, 2, or 3")

        elif func_to_run == "1":
            # make sure the number of iterations entered is a number.
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
            # make sure the number of iterations entered is a number.
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
            # make sure the number of iterations entered is a number.
            while True:
                try:
                    iterations = int(input("how many prime numbers would you like to print? "))
                except ValueError:
                    print("please input a digit!")
                    continue
                else:
                    self.prime(int(iterations))

    def prime(self, iterations):
        '''
        prints a number of prime numbers in order, then re-displays the menu.
        argument: number of prime numbers to print.
        '''
        self.number = 2
        # keeps track of how many prime numbers we've output.
        counter = 1
        potential_number = 2
        while counter <= iterations:
            # assume the potential number is prime.
            isPrime = True
            # using a square root here to reduce the number of iterations.
            for n in range(2, int(math.sqrt(potential_number) + 1)):
                # iterate to check if any numbers divide into the potential number. If there's no divider the prime indicator will stay true.
                if potential_number % n == 0:
                    isPrime = False
                    break
            # will be true if the iteration didn't find any dividers.
            if isPrime:
                # technically could just print the potential number here- self.number helps with testing.
                self.number = potential_number
                time.sleep(0.3)
                print(self.number)
                counter += 1
            potential_number += 1
        # once the counter and iterations are equal, the menu will re-show.
        time.sleep(.6)
        self.show_menu()

    def fibonacci(self, iterations):
        '''
        prints a number of fibonacci numbers, beginning with 1, in order, then re-displays the menu.
        argument: number of numbers to print.
        '''
        # TODO: make a generator for this. this list iterator works really quickly on really large iterations, but a generator works just as well.
        self.number = 1
        print(self.number)

        fib_list = [1, 1]
        # iterations -1 here because we printed out the first iteration above.
        for x in range(iterations-1):
            # grab the last number in the fib_list
            self.number = fib_list[-1]
            time.sleep(0.3)
            print(self.number)
            # add the two numbers together and add it to the end of the list,
            fib_list.append(fib_list[-1]+fib_list[-2])
            # then take off the first (oldest) number from the list.
            fib_list.remove(fib_list[-3])
        # when the range limit is hit, then re-show the menu. 
        time.sleep(.6)
        self.show_menu()

    def integer(self, iterations):
        '''
        prints a number of integers starting with 1.
        argument: number of numbers to print.
        '''
        self.number = 0
        for math in range(iterations):
            #add one to the number and print it until the range limit is hit.
            self.number +=1
            time.sleep(0.3)
            print(self.number)
        #when the range limit is hit, re-show the menu.
        time.sleep(.6)
        self.show_menu()



if __name__ == '__main__':
    start = Mathmagician()
