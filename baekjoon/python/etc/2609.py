
a,b=map(int,input().split());m=a*b
while b: a,b=b,a%b
print(a,m//a,sep="\n")
