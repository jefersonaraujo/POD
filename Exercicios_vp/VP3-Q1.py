#1) Suponha  que  você tenha um dada  sequência  de  n  elementos,  S,  contendo inteiros distintosque   estão   listados   em   ordem   crescente.   Dado   um   número   k, implementeum   algoritmorecursivo  para  encontrar  dois  inteiros  em  S, tais que  soma seja  igual  a  k,  se  existir tal par


def compare(S,k):
    array = []
    # temp = -1
    for i in range(len(S)):
        for j in range(len(S)):
            #print(S[i],S[j]+1)
            temp = S[i]+S[j]
            #print(S[i],S[j])
            if temp == k:
                #print(temp)
                print(S[i],"+ ",S[j]," = ",k)
                #array.insert(S[i],S[j]+1)

    return array

sequence = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(compare(sequence,12))
