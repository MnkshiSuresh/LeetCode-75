'''Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].'''

def product(a):
    b = []
    for i in range(len(a)):
        product_val = 1
        for j in range(len(a)):
            if j != i:
                product_val *= a[j]
        b.append(product_val)

    print(b)

a = [1, 2, 3, 4]
product(a)
