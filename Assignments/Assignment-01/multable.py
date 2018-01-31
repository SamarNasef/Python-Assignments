def multiplication_table(no):
    l=[]
    l2=[]
    for i in range(1,no+1):
        for j in range(1,i+1):
            l.append(i*j)
        l2.append(l)
        l=[]
    return l2
if __name__ == "__main__":
    num = input("enter no:  ")
    print(multiplication_table(int(num)))