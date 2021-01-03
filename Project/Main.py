import numexpr as ne

lower_bound = float(input("Start: "))
upper_bound = float(input("Stop: "))
step_size = int(input("Step: "))
method = int(input("Enter 1 for traps / 2 for simps13 / 3 for simps38: "))
function = input("Enter function as numexpr notation: ")

def f(x):
    function1 = ne.evaluate(function)
    return function1    

if (method == 1):
    def traps (a, b, n):
        h = (b-a)/ n
        sum = f(a) + f(b)
        for i in range (1,n):
            x = a + i*h
            sum = sum + 2 * f(x)
        integration = (sum * h)/2
        return integration
    print (traps(lower_bound, upper_bound, step_size))
    

elif(method == 2):
    def simps13 (a, b, n):
        h = ((b-a)/n)
        sum = f(a) + f(b)
        for i in range(1,n):
            x = a + i*h
            if i%2 ==0:
                sum = sum + 2*f(x)
            else:
                sum = sum + 4*f(x)
        integration = sum * h/3
        return integration
    print (simps13(lower_bound, upper_bound, step_size))

else:
    def simps38 (a, b, n):
        h = (b-a)/n
        sum = f(a) + f(b)
        for i in range (1,n):
            x = a + i*h
            if i%3 == 0:
                sum = sum + 2*f(x)
            else:
                sum = sum + 3*f(x)
        integration = sum * 3*h/8
        return integration
    print (simps38(lower_bound, upper_bound, step_size))