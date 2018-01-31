def character_locator(data , letter):
    l=[]
    for i in range(len(data)):
        if(data[i] == letter):
            l.append(i)
    return l
if __name__ == "__main__":  
    data = input("enter string:  ")
    letter = input("enter letter: ")
    print(character_locator(data,letter))