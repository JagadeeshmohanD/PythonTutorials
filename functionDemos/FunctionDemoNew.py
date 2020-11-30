def print_name(*args):
    print(args)
    print(args[3])
    # for name in args:
    #     print(name)

print_name("Python","Java","C#","JavaScript","Ruby")


def get_sum_of_all_number(*args):
    print(sum(args))

def get_min_number(*args):
    print(min(args))

def get_max_number(*args):
    print(max(args))

get_sum_of_all_number(10,30,60)
get_min_number(20,10,80)
get_max_number(100,150,850)

