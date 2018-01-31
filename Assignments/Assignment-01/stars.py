def mario_pyramid(num):
    row = ""
    for i in range(num):
        for j in range(i,num):
            row += " "
        for k in range(0,i+1) :
            row += "*"
        row += "\n"
    return row

if __name__ == "__main__":
    num = int(input("enter no: "))
    print(mario_pyramid(num))