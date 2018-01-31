def create_dict(l):
    d={}
    keys=[]
    values=[]
    for i in range(len(l)):
        keys.append(l[i][0])
        values.append(l[i])
        if(keys[i] in d):
            d[keys[i]].append(values[i])
        else:
            tmp_dict={keys[i]:[values[i]]}
        d.update(tmp_dict)
    return d

if __name__ == "__main__":
    l=["samar","eman","hhh","sara","sss"]
    print(create_dict(l))


