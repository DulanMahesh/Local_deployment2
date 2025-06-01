'''Create a function called return_distincts() that receives 3integers as parameters.
If the sum of the 3 numbers is greater than 15, it must returnthe highest number.
If the sum of the 3 numbers is less than 10, it must return thelowest number.
If the sum of the 3 numbers is a value between 10 and 15(included), then it must return the number with theintermediate value.'''

def return_distincts(num1,num2,num3):
    total=[]

    total.append(num1)
    total.append(num2)
    total.append(num3)

    if num1+num2+num3 >15:
        return max(total)
    elif num1+num2+num3 <10:
        return min(total)
    elif (num1 + num2 + num3) >= 10 and (num1 + num2 + num3) <= 15:
        total_sorted =sorted(total) # to get the middle number in a list with 3 numbers, first we sort the list
        return total_sorted[1] # then we call the index of 1


print(return_distincts(6,1,4))












