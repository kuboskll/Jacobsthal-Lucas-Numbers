dizi = [2,1] #dizi tanımladık
k=int(input("Sayi Giriniz: "))
if k%2==0:
    for x in range(1,k):
        if x%2==0:
            sonuc=(2**(x+1))+((-1)**(k+1))    
            dizi.append(sonuc)
        else:
            sonuc=(2**(x+1))+((-1)**(k+1))
            sonuc=sonuc+2
            dizi.append(sonuc) #diziye aktardık  
else:
    for x in range(1,k):
        if x%2==0:
            sonuc=(2**(x+1))+((-1)**(k+1))    
            dizi.append(sonuc-2)
        else:
            sonuc=(2**(x+1))+((-1)**(k+1))
            sonuc=sonuc+2
            dizi.append(sonuc-2) #diziye aktardık
    
print(dizi)
