while True:
    n = input("lütfen milisecond cinsinden bir tam sayı değeri giriniz:")
    milisec = 1000
    sec = 60*milisec
    mint = sec*60
    hours = mint*60
    days = 24*hours
    millis=input("Enter time in milliseconds ")
    if millis.lower() == 'exit':
        print("Exiting the program... Good Bye")
    if not millis.isdigit():
        print('please enter a valid number: ')
    # time = input("Input time in seconds: ")
    # day = time // (24 * 3600)
    # time = time % (24 * 3600)
    # hour = time // 3600
    # time %= 3600
    # minutes = time // 60
    # time %= 60
    # seconds = time
    # print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))

    #if not n.isdigit():
    #    return 'lütfen bir tam sayı giriniz'

    if n/milisec < 1:
        print('sadece milisaniye')
        break
    elif n/milisec > 1 and n/milisec < sec:
        print('şu kadar seconds')
        break
    elif n/sec > 1 and n/sec < mint:
        if n%sec < 1:
            print("şu kadar dakika")
            break
        else:
            print("şu kadar dakika şu kadar saniye")
            break
    elif n/mint > 1 and n/mint < hours:
        if n%mint < 1:
            print("şu kadar saat")
            break
        elif n%mint > 1 and n%mint < :

        else:
            print("şu kadar dakika şu kadar saniye") 