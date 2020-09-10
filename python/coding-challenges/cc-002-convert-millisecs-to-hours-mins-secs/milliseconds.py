def main():
    milis = input('lütfen milisecond cinsinden sayıyı giriniz: ')
    if milis.lower() == 'exit':
        print("Exiting the program... Good Bye")
        
    elif milis.isdigit():
        
        milis = int(milis)
        second = int(milis / 1000)
        minutes = int(second/ 60)
        minutes2 = int(second%60)
        hour = int(minutes / 60)
        hour2 = int(minutes%60)
        day = int(hour / 24)
        day2 = int(hour % 24)
        print(second, minutes, hour, day)
        if second < 1:
            print(f'just {milis} milliseconds')
            
        elif minutes < 1:
            print(f'{second} second/s')
            
        elif hour < 1 :
            if second > 1:
                print(f'{minutes2} minute/s {second} second/s')
                
            else:
                print(f'{minutes2} minute/s')
                
        elif day < 1 :
            if minutes > 1:
                if second > 1:
                    print(f"{hour2} hour/s {minutes2} minute/s {second} second/s")
                    
                else:
                    print(f"{hour2} hour/s {minutes2} minute/s")
                    
            else:
                if second > 1:
                    print(f"{hour2} hour/s {second} second/s")
                    
                else:
                    print(f"{hour2} hour/s")

        
    else:
        print("Not Valid Entry")
        return main()
                    

main()
