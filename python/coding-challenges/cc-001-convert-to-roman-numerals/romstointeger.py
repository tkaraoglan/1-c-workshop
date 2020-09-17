
def int_to_rome(a = input("lütfen 0 ile 4000 arası bir sayı giriniz:")):
    import sys
    try:
        if a.lower() == "exit":
            sys.exit()
        
        a = int(a)
        if not 0 < a <4000:
            print("lütfen belirtilen aralıkta bir sayı giriniz")
            sys.exit()
        b = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
        c = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        d= []
        for i in range(len(b)):
            count = int((a/b[i]))
            d.append(count*c[i])
            a -= count * b[i]
        print("".join(d))
    except ValueError:
        return "lütfen tam sayı bir değer giriniz: "

    
int_to_rome()