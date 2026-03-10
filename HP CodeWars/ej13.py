preg=input()
t=input().split(":")
if preg=="Métrica":
    s=t[0]//3600+t[1]//60+t[2]
    hm=s//10000
    mm=s%100//100
    sm=s%10000