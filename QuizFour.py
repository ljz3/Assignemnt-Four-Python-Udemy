# 1) Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.

def norm_funct(funct):
    print(funct(10))


# 2) Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.

norm_funct(lambda data: data + 3)


# 3) Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed.     

def norm_funct_inf(funct, *args):
    for arg in args:
        print(funct(arg))

norm_funct_inf(lambda data: data + 1, 2, 3, 4, 10)


# 4) Format the output of your “normal” function such that numbers look nice and are centered in a 20 character column.

def norm_funct_format(funct, *args):
    for arg in args:
        print("After function: {:^20}".format(funct(arg)))

norm_funct_format(lambda data: data + 1, 2, 3, 4, 10)