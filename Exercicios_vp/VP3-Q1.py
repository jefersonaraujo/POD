#1) Suponha  que  você tenha um dada  sequência  de  n  elementos,  S,  contendo inteiros distintosque   estão   listados   em   ordem   crescente.   Dado   um   número   k, implementeum   algoritmorecursivo  para  encontrar  dois  inteiros  em  S, tais que  soma seja  igual  a  k,  se  existir tal par


def compare(S,k):
    array = []
    slots =[]
    # temp = -1
    for i in range(len(S)):
        for j in range(len(S)):
            #print(S[i],S[j]+1)
            temp = S[i]+S[j]
            #print(S[i],S[j])
            if temp == k:
                #print(temp)
                #print(S[i],"+ ",S[j]," = ",k)
                #slots.append([S[i],S[j]])
                array.append([S[i],S[j]])

    return array

sequence = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
k=12
print("As combinações de soma para :",k, "São:\n")
print(compare(sequence,12))
