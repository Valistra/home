print ("Vvedite a")
a = float (input ())
print ("Vvedite b")
b = float (input ())
print ("Vvedite c")
c = float (input ())
d = b*b-4*a-c
print ("D = ", d)    
if d<0:
    print ("Kornei net")
if d>0:
    x1= (-b+d**0.5)/(2*a)
    x2= (-b-d**0.5)/(2*a)
    print ("x1= ", x1)
    print ("x2= ", x2)
if d==0:
    x=-b/(2*a)
    print ("x1= ", x1)
    

print ("End")
input()
