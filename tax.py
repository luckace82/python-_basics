a=12000
tax1=0
if a<=10000:
    tax=0
elif a<=20000:
    tax=(a-10000)*0.1
else:
    tax=10000*0.1+(a-20000)*0.2 
print("the tax you need to pay is : RS",tax)        
       
    
