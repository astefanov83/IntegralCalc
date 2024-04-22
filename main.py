
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
        
        return func1, x1bound, x2bound

    def take_integral(x1bound, x2bound, func1):

        curr2 = x1bound
        tot = 0

        for i in range(0, 10000):

            step = float((x2bound - x1bound)/10000)

            copyoffunc = func1
            curr = 0

            for letter in range(len(copyoffunc)):
                if copyoffunc[letter] == 'x': 
                    copyoffunc = copyoffunc[:letter] + str(curr2 + step) + copyoffunc[letter + 1:]

            curr2 += step
            curr = (eval(copyoffunc))*(step)
            print("ran")
            tot += curr

        return tot

    def print_graph():
        ...

def main():
    func, lo, hi = Integral.init_func()

    print(Integral.take_integral(int(lo), int(hi), func))

    

if __name__ == '__main__':
    main()
