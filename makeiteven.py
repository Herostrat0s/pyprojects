def make_even(num):
    if num%2 !=0:
        return num + 1 
    else:
        return num
    
print(make_even(int(input("Please enter a number: "))))