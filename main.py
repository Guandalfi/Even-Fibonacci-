list = [1,2]

def fin():
    terc = 0
    even_fin = 0
    while terc < 4000000:
        prim = list[-1]
        segu = list[-2]
        terc = prim + segu
        if terc < 4000000:
            list.append(terc)
            #if terc % 2 == 0:
            #    even_fin += terc
    return
                
fin()
print(f"Sum of even Fibonacci number's: {sum(num for num in list if not num % 2)}")
print(list)
    
  