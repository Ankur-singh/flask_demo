def prime(num):
    if num > 1:  
        for i in range(2,num):  
            if (num % i) == 0:  
                return False  
        else:  
            return True  
    else:  
        return False
    
if __name__ == '__main__':
    number = int(input('Enter a number: '))
    print(prime(number))