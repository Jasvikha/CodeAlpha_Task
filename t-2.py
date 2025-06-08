
d={"aapl":180,"tsl":100,"mer":50}
u={}
s=int(input("Enter how many stocks you want to buy- "))
for i in range(0,s):
  sn=input("stock name- ")
  sq=int(input("quantity- "))
  total=sq*d[sn]
print(f"Total investment is ${total}")
