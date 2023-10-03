def getColorName(r, g, b, csv):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(r- int(csv.loc[i,"R"])) + abs(g- int(csv.loc[i,"G"]))+ abs(b- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname 
    