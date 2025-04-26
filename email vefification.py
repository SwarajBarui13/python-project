k,d,x=0,0,2
email=input("Enter Your emial:")

if len(email)>6:
    if email[0].isalpha():
        if (email.count("@")==1) and ("@" in email):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i.isspace():
                        k=1 
                    elif i.isalnum:
                        x=0
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="@" or i==".":
                        continue
                    else:
                        d=1

                if k==1 or d==1:
                    print("please check your email")
                else:
                    print("Your email is right")
            else:
                print("please check your email,the position of . is not correct")
        else:
            print("please check your email,the position of @ is not correct")
    else:
        print("Your email is wrong,please check")
else:
    print("Your email is wrong,please check")

print("your email is sucessfully verified")