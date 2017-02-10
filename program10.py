principle=int(input("enter the principle amount:"))
rate=int(input("enter the rate:"))
time=int(input("enter the time:"))
def simple_interest(principle,time,rate):
    A=principle*(1+rate*time)
    print("total simple interest:",A)
simple_interest(principle,time,rate) 
