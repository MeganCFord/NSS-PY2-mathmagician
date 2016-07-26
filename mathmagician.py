class Mathmagician():

    def __init__(self):
        self.number = 0

    def show_menu(self):
        print("the menu will print here \n")

        func_to_run = input("which function would you like to run?")
        if func_to_run not in ("1", "2", "3"):
            print("please press 1, 2, or 3")
        elif int(func_to_run) == 1:
            iterations = input("how many times would you like to run the fibonacci sequence?")
            self.fibonacci(int(iterations))
        elif int(func_to_run) == 2:
            iterations = input("how many times would you like to run the integer sequence?")
            self.integer(int(iterations))
        elif int(func_to_run) == 3:
            iterations = input("how many times would you like to run the prime number sequence?")
            self.prime(int(iterations))
            

    def fibonacci(self, iterations):
        self.number = 1
        print(self.number)

        fib_list = [1, 1]
        for x in range(iterations-1):
            self.number = fib_list[-1]
            print(self.number)
            fib_list.append(fib_list[-1]+fib_list[-2])
            fib_list.remove(fib_list[-3])


    def integer(self, iterations):
        self.number = 0
        for math in range(iterations):
            self.number +=1
            print(self.number)

    def prime(self, iterations):
        pass


if __name__ == '__main__':
    thing = Mathmagician()
    thing.show_menu()
