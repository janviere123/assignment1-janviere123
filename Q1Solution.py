start=int(input("enter starting time :\n"))
end=int(input("enter ending time:\n"))
if start>end or start>24 or end>24:
        print("invalid input")
          exist(1)
 total_amount=0
    #total amount
while start<end:
       if 0<=start<7 or 21<=start<24:
               total_amount=total_amount+500
       elif 7<=start<10 or 19<=start<21:
               total_amount=total_amount+1000
       elif 10<=start<19
               total_amount=total_amount+1500
       else
               pass
        start =start+1
print(f"\n total_amount to be paid is {total_amount}")
        
