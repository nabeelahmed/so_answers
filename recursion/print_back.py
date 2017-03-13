def print_backward(num):
    if num == 10:
        return 
    num += 1
    print(num)
    print_backward(num)
    print("yeah")   
    print(num)
    print()

print_backward(6)
