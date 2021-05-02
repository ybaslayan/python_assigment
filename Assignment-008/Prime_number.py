number = input("Please enter a positive integer number : ")


if number.isdigit():
    number = int(number)
    x = number-1
    while x>1:
        if number%x==0:
            print('{} is not a prime number!'.format(number))
            break
        else:
            x-=1
    else:
        print('{} is a prime number!'.format(number))
else:
    print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")