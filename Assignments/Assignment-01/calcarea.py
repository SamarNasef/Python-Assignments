
def calcarea(shape,dim1,dim2=0):
    area=0
    if(shape == 't'):
        area=0.5*dim1*dim2
    elif(shape == 's'):
        area=dim1*dim1
    elif(shape == 'r'):
        area=dim1*dim2
    elif(shape == 'c'):
        area=2*3.14*dim1
    return area

if __name__ =="__main__":
    shape=input("enter shape(t,r,s,c): ")
    if(shape in ['t','r']):
        dim1=int(input("enter dim1: "))
        dim2=int(input("enter dim2: "))
        print(calcarea(shape,dim1,dim2))
    elif(shape in ['s','c']):
        dim=int(input("enter dim: "))
        print(calcarea(shape,dim))
    else:
        print("wrong shape")


