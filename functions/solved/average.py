# write a function  that returns the arithmetic average for a list of numbers
def average_function(list_num):
    sum=0
    for i in range(list_num):
        sum=sum+list_num[i]
    average=sum/len(list_num)
    return average


# Test your function 
