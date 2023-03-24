import random 
def InputData(n):
    global num
    num = []
    for i in range(n):
        num = num + [random.randint(-30, 50)]
    return num

def Insertsort():
    # run an outer loop i from 1 to len(num) to repeat the process of insertion sort
    for i in range(1,len(num)):

        # x to be inserted at proper place
        x=num[i]

        # run an inner while loop j for insertion sort from i-1 to 0
        j=i-1
        while j>=0:

            # now check if the value of x is less than num[j] then shift the number num[j] towards right else break the inner loop j
            if x<num[j]:
                num[j+1]=num[j]
            else:
                break
            j=j-1

        # outside the body of inner loop j insert the value of x at num[j+1] position
        num[j+1]=x

    # print the sorted list
    print('\n\nList after Insertion Sort')
    for n in num:
        print(n,end=' ')

# define a list
InputData(n=int(input("Nhap so phan tu: ")))
print('List before Insertion Sort')
for n in num:
    print(n,end=' ')
Insertsort()