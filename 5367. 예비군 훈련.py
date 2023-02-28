person = list(input().split())

if person[0] == '0':
    print(0)
else:
    if person[-1] == 'Private':
        if int(person[0])>= 1 and int(person[0])<=4:
            if person[2] == 'Y':
                print(28)
            else:
                if person[1] != 'ROKAF':
                    print(32)
                else:
                    print(28)
        else:
            print(20)

    else:
        print(28)
