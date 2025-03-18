def Largest_Num(num):
    large=num[0]  # we consider as frist element list as largest

    for i in num: # using for loop we get element from list

        if large<i:  # compare current element to largest element
            large=i  #if condition is True then it replace with current element
    return large     # return largest Element in list


num=[45,27,25,98,67] #input list
print(Largest_Num(num))