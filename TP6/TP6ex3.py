def ajouter_elt(lst=[0,1,2], elt=3):
    lst.append(elt)
    return lst

print(ajouter_elt())
#a [0, 1, 2, 3]

#b
print(ajouter_elt())
print(ajouter_elt())
#[0, 1, 2, 3, 3]
#[0, 1, 2, 3, 3, 3]

#c
def ajouter_carac(ch ="abc", elt = "d"):
    return ch + elt
#d
print(ajouter_carac())
#abcd

#e
print(ajouter_carac())
print(ajouter_carac())
#abcd
#abcd