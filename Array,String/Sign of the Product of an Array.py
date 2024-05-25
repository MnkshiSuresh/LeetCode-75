def signFunct(prod):
    if prod<0:
        print("-")
    elif prod>0:
        print("+")    
    else:
        print("0") 
   



array = input("enter your array elements with a space gap: ")
arr = array.split()
prod = 1
for i in range(0,len(arr)):
    prod = prod*int(arr[i])
signFunct(prod)
  
