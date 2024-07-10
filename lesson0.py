"1st program"
print((9**0.5)*5)
"2nd program"
print(9,99>9.98,1000!=1000.1)
"3rd program"
num = 1234
a = num % 10
b = (num % 100) // 10
c = (num % 1000) //100
d = (num % 10000) // 1000
num = 5678
e = num % 10
f = (num % 100) // 10
g = (num % 1000) //100
k = (num % 10000) // 1000
num1 = (c*10+b) + (g*10+f)
print(num1)
"4th program"
num = 13.42
a = num*100%10# 2
b= (num*100%100)//10# 4
c = (num *100% 1000) //100# 3
d = (num*100 % 10000) // 1000# 1
num = 42.13
e = num*100%10# 3
f = (num*100%100)//10# 1
g = (num *100% 1000) //100# 2
h = (num*100 % 10000) // 1000# 4
print((d*10+c)==(f*10+e) or (b*10+a)==(h*10+g))