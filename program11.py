principle=int(input("enter the principle amount:"))
rate=float(input("enter the rate:"))
time=int(input("enter the time:"))
n=int(input("enter the n:"))
def compound_interest(principle,time,rate,n):
    r=(rate/100)
    A=principle*(1+r/n)**(n*time)
    print("total compound interest:",A)
compound_interest(principle,time,rate,n) 
