import cmath

memory = 0

calculations = []


# functions of calculator
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def reciproc(a):
    return 1 / a


def modulo(a, b):
    return a % b


def power(a, b):
    return a ** b


def squareroot(a):
    return cmath.sqrt(a)


def switch_sign(a):
    return -1 * a


# memory functions
def add_to_memory(a, m):
    m += a
    return m


def subtract_from_memory(a, m):
    m -= a
    return m


def memory_clean(m):
    m = 0
    return m


def memory_set(a, m):
    m = a
    return m


def memory_reminder(m):
    print("Stored memory:" + str(m))
    return m


def calc_clean(c):
    c.clear()
    return c


def entry_clear(c):
    try:
        c.pop()
        return c
    except IndexError:
        pass


# main function executions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulo,
    '^': power,
    "SQRT": squareroot,
    "RECP": reciproc,
    "SIGN": switch_sign
}

memory_ops = {
    "MC": memory_clean,
    "MR": memory_reminder,
    "MS": memory_set,
    "M+": add_to_memory,
    "M-": subtract_from_memory,
    "C": calc_clean,
    "CE": entry_clear
}


def choose_operation(a):
    numbers = []
    global calculations
    for n in operations:
        if n in a:
            if n == 'SQRT' or n == 'RECP' or n == 'SIGN':
                b = int(a.replace(n, ''))
                calculations.append(operations[n](b))
                print(operations[n](b))

            else:
                curr_num = a.split(n)
                for i in curr_num:
                    numbers.append(eval(i))
                calculations.append(operations[n](numbers[0], numbers[1]))
                print(operations[n](numbers[0], numbers[1]))


def memory_operation(mi):
    global memory, calculations
    for n in memory_ops:
        if n == mi:
            if n == 'M+' or n == 'M-' or n == 'MS':
                memory = memory_ops[n](calculations[-1], memory)
            elif n == "C" or n == "CE":
                calculations = memory_ops[n](calculations)
            else:
                memory = memory_ops[n](memory)


while True:
    user_input = input("\nWhat are you going to do?\n")
    if user_input == 'quit':
        break
    choose_operation(user_input)

    memory_input = input("Any memory operations?\n")
    if memory_input == 'no':
        continue
    memory_operation(memory_input)
    print(f"Calculations list:{calculations}")
