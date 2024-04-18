
class Integral:

    def __init__(self, func1, x1bound, x2bound):
        self.func1 = func1
        self.x1bound = x1bound
        self.x2bound = x2bound
        self.sum = sum

    def init_func():
        func1 = input("Enter your function f(x):")
        x1bound = input("Enter the lower bound of the integral:")
        x2bound = input("Enter the upper bound of the integral:")
        ...

    def take_integral(x1bound, x2bound, func1):
        sum = 0
        for x in range(x1bound, x2bound, (x2bound - x1bound)/1000):
            sum += func1(x) * ((x2bound - x1bound)/1000)

        return sum

        
        ...

    def print_graph():
        ...

def main():
    ...


if __name__ == '__main__':
    main()
