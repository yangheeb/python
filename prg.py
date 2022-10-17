Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a,b=10,20
b
20
a==b
False
a>=b
False
c=True
type(c)
<class 'bool'>
x,y=7,20
y%x>=b/a
True
c
True
x>=y and c
False
y//x==b-a and a!=b
False
x=5.7
int(x)
5
round(x)
6
round(5.8763,2)
5.88
round(5.8975,2)
5.9
x
5.7
y
20
x+y
25.7
x
5.7
str(x)
'5.7'
data="경영정보학과"
data
'경영정보학과'
data[0]
'경'
data[4]
'학'
v='Donga'
v
'Donga'
v[2]
'n'
data+v
'경영정보학과Donga'
data+700
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    data+700
TypeError: can only concatenate str (not "int") to str
data+str(700)
'경영정보학과700'
v
'Donga'
v*10
'DongaDongaDongaDongaDongaDongaDongaDongaDongaDonga'
v+10
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    v+10
TypeError: can only concatenate str (not "int") to str
print(v,data)
Donga 경영정보학과
print(v,'\n',data)
Donga 
 경영정보학과
print(v,'\t',data)
Donga 	 경영정보학과
int("100")
100
str(100)
'100'
v.upper()
'DONGA'
v.lower()
'donga'
v.find('a')
4
