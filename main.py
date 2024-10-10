def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number * factorial(number - 1)
    
def TrailingZeros(number):
    count = 0 
    i = 5 
    while(number // i != 0): # 120 (120//24 which is not equal to zero because the answer is 24)
        count += int(number/i) # count will increase to 24 because 120/5 is 24 
        i = i*5 # it means 5 multilply by 5 (it will check by 5 then 25 then 125 and so on )
    return count     
    
    # fac = factorial(number)
    # print(fac)
    # count = 0
    # while(fac%10==0):
    #     count = count + 1
    #     fac = fac /10
    # return count    


if __name__ == '__main__':
    number = (int(input("Enter the number: ")))


    # fac = factorial(number)
    # print(f"the factorial number is {fac}")
    print(TrailingZeros(number))