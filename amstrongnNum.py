n=int(input('Enter no :'))
lst=[]
def amstrong(n):
    if n>0:
        r=n%10
        ni = amstrong(n//10)
        re=r**3
        lst.append(re)
amstrong(n)
no=0
for i in lst:
    no= no+i
if n==no:
    print("Num is amstrog ")
else:
    print('num is not amstrong')

