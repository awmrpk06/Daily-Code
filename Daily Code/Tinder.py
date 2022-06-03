from tkinter import N


def Tinder(guys_pref, gal_pref, n):
    pair = [9]*n
    taken = [False]*n
    for i in range(n):
        for j in range(n):
            guy_name, value = list(guys_pref.items())[i]
            girl_name = value[j]
            girl_index = list(gal_pref.keys()).index(girl_name)
            diff = j + gal_pref.get(girl_name).index(guy_name)
            if not taken[girl_index]:
                if pair[i] == 9:
                    pair[i] = [guy_name, girl_name, diff, j]
                else:
                    if pair[i][2] > diff:
                        pair[i] = [guy_name, girl_name, diff, j]
            else:
                for z, v in enumerate(pair):
                    if girl_name == v[1]:
                        taken_diff = v[2]
                        break
                if taken_diff > diff:
                    pair[i] = [guy_name, girl_name, diff, j]
                    j = 0
                    i = z
                    pair[z] = 9
        if not taken[list(gal_pref.keys()).index(pair[i][1])] :
            taken[list(gal_pref.keys()).index(pair[i][1])] = True           
    return pair
guy_preferences = {
    'andrew': ['caroline', 'abigail', 'betty'],
    'bill': ['caroline', 'betty', 'abigail'],
    'chester': ['betty', 'caroline', 'abigail'],
}

gal_preferences = {
    'abigail': ['andrew', 'bill', 'chester'],
    'betty': ['bill', 'andrew', 'chester'],
    'caroline': ['bill', 'andrew', 'chester']
}
print(Tinder(guy_preferences, gal_preferences, 3))