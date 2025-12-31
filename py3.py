y=int(input("Enter the final year:"))
i=datetime.datetime.now().year
for i in range(i,y+1):
     if(i%4==0 and i%100!=0 or i%400==0):
        print(i)
