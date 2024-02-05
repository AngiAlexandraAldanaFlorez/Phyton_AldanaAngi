def Money():
    print('---- Change Money to coins of 10, 5 and 1 ----')
    print('----------------------------------------------')


    n = int(input("How much money do you want to exchange? "))
    
    if 0 < n < 1000:
        d = n // 10
        p = n % 10
        e = p // 5
        c = p % 5 

        list=[]
        for i in range(d):
            list.append("10")
        for i in range(e):
            list.append("5")
        for i in range(c):
            list.append("1")
        print(list)
    else: 
        print("invalid money number")

Money()