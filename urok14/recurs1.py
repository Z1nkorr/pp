def print_10_hello(i):
    print(f"{i} + hello")
    i+=1
    if i <= 10:

        print_10_hello(i)

    print(f"{i} - hello")

print_10_hello(0)