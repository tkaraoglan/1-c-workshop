while True:
    n = input("lütfen milisecond cinsinden bir tam sayı değeri giriniz:")
    milisec = 1000
    sec = 60*milisec
    mint = sec*60
    hours = mint*60
    days = 24*hours


    #if not n.isdigit():
    #    return 'lütfen bir tam sayı giriniz'

    if n/milisec < 1:
        print('sadece milisaniye')
        break
    elif n/milisec > 1 and n/milisec <sec:
        print('şu kadar seconds')
        break
    elif n/sec > 1 and n/sec < mint:
        if n%60000 < 1:
            print("şu kadar dakika")
            break
        else:
            print("şu kadar dakika şu kadar saniye")
    elif n/mint > 1 and n/mint < hours:
        if n%60000 < 1:
            print("şu kadar dakika")
            break
        else:
            print("şu kadar dakika şu kadar saniye") 