while len(men) > 0:         #kommentera ut relevanta komplexiteter
    raggare = men[0]
    PI = raggare.personIndex
    currpref = int(raggare.pref[0])/2 - 1
    ragg = women[int(currpref)]

    currcoup = []
    for i in c:                         #n
        if i[1] is ragg:
            currcoup.append(i)
            break

    if len(currcoup) == 0:
        raggare.pref = raggare.pref[1:]
        make_couple(raggare, ragg)
        men = men[1:]
        c = sorted(c, key=lambda couple: couple[0].personIndex)
    else:
        cTemp = currcoup[0]
        for p in cTemp[1].pref:         #n

            if raggare.personIndex == int(p):
                c.remove(cTemp)         #n?     vi är i en for-loop -->n*n = n^2
                raggare.pref = raggare.pref[1:]
                make_couple(raggare, ragg)
                c = sorted(c, key=lambda couple: couple[0].personIndex)
                men = men[1:]
                men.append(cTemp[0])
                break

            if cTemp[0].personIndex == int(p):
                men[0].pref = men[0].pref[1:]
                break