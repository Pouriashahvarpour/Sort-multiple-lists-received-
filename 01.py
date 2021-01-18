k = eval(input("Enter positive number from number of list="))
if(k<=0):
    print("Your number was enter is not positive")
else:
    orginal_list = []
    i = 1
    listt=[]
    while(i<=k):
        print("\r ** If your want Stop entering the number enterd 'end' **")
        while(1):
            new = input("Enter your number is want add= ")
            if (new == 'end' or new =='End'):
                break
            else:
                new = int(new)
                listt.append(new)
            
        i+=1
        if (i == k):
            orginal_list = listt.copy()
    orginal_list.sort()
    print("Mixed and sort list your enterd -->",orginal_list)
