
data = ["1", "5",
        "mom: upper-upper-lower-middle class",
        "dad: middle-middle-middle-lower-middle class", 
        "queenelizabeth: upper-upper-upper class",
        "chair: lower-lower class",
        "unclebob: middle-middle-lower-middle class"]




def tierlister(data):
    people_1 = data[-int(data[1]):]
    people_2 = []
    people_dic = {}

    for i in people_1:
        people_2.append(i.split())
        people_dic[people_2[people_1.index(i)][0]] = people_2[people_1.index(i)][1].split("-")

    max_detail = 0
    for x,y in people_dic.items():
        if max_detail < len(y): #Finding the furthest detail.
            max_detail = len(y)
        num_class_val = ""
        for i in y[::-1]: #Go through the list reversed
            if i == "upper":
                num_class_val += "2"
            elif i == "middle":
                num_class_val += "1"
            elif i == "lower":
                num_class_val += "0"
        people_dic[x] = num_class_val

    for x,y in people_dic.items(): #get the same amount of detail
        if len(y) < max_detail:
            people_dic[x] = int(y + "1"*(max_detail-len(y)))
        else:
            people_dic[x] = int(y)

    tierlist = sorted(people_dic, key=people_dic.get, reverse=True)
    
    for i in tierlist:
        print(i.replace(":",""))
    print("="*30)
tierlister(data)