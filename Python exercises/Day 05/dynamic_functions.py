#excercise 1
#check the given number has 3 digits
def check_3_digits(num):

    return num in range(100,1000)

sum = 367+456
result =check_3_digits(sum)
print(result)

#exercise2
#check all the numbers from a list, include in a list if a numbers has 3 digits

def check_3_digits_inlist(numlist):
    numwith3digits=[]
    for n in numlist:
        if n in range(100,1000):
            numwith3digits.append(n)
    print(f"3 digit numbers found{numwith3digits}")

check_3_digits_inlist([341,44,567,7,999])


#exercise3
#solution for exercise2 in another way

def chk_3_digits_inlist(numlist):
    numwith3digits=[]
    for n in numlist:
        if n in range(100,1000):
            numwith3digits.append(n)
        else:
            pass
    return numwith3digits

print(chk_3_digits_inlist([34,44,678,56,789]))



