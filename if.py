"""done = -1

if done:
    print("yes")   
else:
    print("no")  # else part will execute at the time of value is 0 or empty string or false 


done1 = True
done2 = False
done3 = any([done1,done2]) #if we are using any keyword it will return true
print(done3)"""

name = False
country = "india"
if name == "kishore":
    print("this is wrong")
elif name == True:
    print("this is correct")
elif country == "india":
    print("he's from india")
else:
    print("you entered wrongly")
