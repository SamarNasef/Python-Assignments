def remove_vowels(sen):
    tmp = sen
    for i in range(len(sen)):
        if( sen[i] in ['a','e','o','u','i','A','O','E','U','I']):
            sen2 = tmp.replace(sen[i],'')
            tmp = sen2
    return sen2
if __name__ == "__main__":
    data = input("enter sentence:  ")
    remove_vowels(data)

