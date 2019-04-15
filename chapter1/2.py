mul=lambda n:print (n) if n%2!=0 else True
try:
    n=int(input("Enter The Number->"))
    if isinstance(mul(n),type(None)):
     print("The Number isnt Even")
    elif n==0:
     print("The Number is Zer0 can't say anything")
      
    else:
       print("The Number is Even")  

except:
        print("It is not an Interger.Enter some integer value greater than Zer0")  
        
  

