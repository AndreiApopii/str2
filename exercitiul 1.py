cuvantul=str(input("introdu cuvantul :"))
a=str(input("introdu o litera :"))
if len(a)==1:
    for i in cuvantul:
        x=cuvantul.replace(i,a)
        print(x)