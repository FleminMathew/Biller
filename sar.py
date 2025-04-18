import pickle,os,csv,sys 
def addcust(): 
    fh=open("sarang supermarket.dat","ab") 
    cust={} 
    cust["name"]=input("ENTER CUSTOMER'S NAME:") 
    cust["address"]=input("ENTER CUSTOMER'S ADDRESS:") 
    cust["phno"]=int(input("ENTER CUSTOMER'S PHONE NUMBER:")) 
    cust["DOB"]=input("ENTER DATE OF BIRTH:") 
    cust["email"]=input("ENTER CUSTOMER'S MAIL ID:") 
    pickle.dump(cust,fh) 
    fh.close() 
    print("!!!!!ACCOUNT CREATED SUCCESSFULLY!!!!!") 
def displayall(): 
    fh=open("sarang supermarket.dat","rb") 
    try: 
        while True: 
            s=pickle.load(fh) 
            print(s) 
    except EOFError: 
        fh.close() 
def displaycust(phno): 
 
    fh=open("sarang supermarket.dat","rb") 
    found=False 
    try: 
        while True: 
            st=pickle.load(fh) 
            if st["phno"]==phno: 
                print(st) 
                found=True 
    except EOFError: 
        if found==False: 
            print("!! NO SUCH RECORD !!") 
        fh.close() 
def delcust(phno): 
   fh=open("sarang supermarket.dat","rb") 
   fh2=open("temp.dat","wb+") 
   found=False 
   try: 
       while True: 
           st=pickle.load(fh) 
           if st["phno"]==phno: 
               found=True 
               continue 
           else: 
               pickle.dump(st,fh2) 
 
   except EOFError: 
       fh.close() 
       if found==False: 
           print("NO SUCH ACCOUNT") 
   fh2.close() 
   os.remove("sarang supermarket.dat") 
   os.rename("temp.dat","sarang supermarket.dat") 
def delall(): 
    fh=open("sarang supermarket.dat","rb") 
    fh2=open("temp.dat","wb+") 
    found=False 
    try: 
        while True: 
            st=pickle.load(fh) 
            continue 
    except EOFError: 
        fh.close() 
    fh2.close() 
    os.remove("sarang supermarket.dat") 
    os.rename("temp.dat","sarang supermarket.dat") 
def etaddr(phno): 
    fh1=open("sarang supermarket.dat","rb+") 
    fh2=open("temp.dat","wb+") 
    found=False 
 
    try: 
        while True: 
            st=pickle.load(fh1) 
            if st["phno"]==phno: 
                st["address"]=input("ENTER THE NEW ADDRESS:") 
                pickle.dump(st,fh2) 
                found=True 
            else: 
                pickle.dump(st,fh2) 
    except EOFError: 
        fh1.close() 
        if found==False: 
            print("!! NO SUCH ACCOUNT !!") 
    fh2.close() 
    os.remove("sarang supermarket.dat") 
    os.rename("temp.dat","sarang supermarket.dat") 
def edtdob(phno): 
    fh1=open("sarang supermarket.dat","rb+") 
    fh2=open("temp.dat","ab+") 
    found=False 
    try: 
        while True: 
            st=pickle.load(fh1) 
            if st["phno"]==phno: 
 
                st["DOB"]=input("ENTER THE NEW DOB:") 
                pickle.dump(st,fh2) 
                found=True 
            else: 
                pickle.dump(st,fh2) 
    except EOFError: 
        fh1.close() 
        if found==False: 
            print("!! NO SUCH ACCOUNT !!") 
    fh2.close() 
    os.remove("sarang supermarket.dat") 
    os.rename("temp.dat","sarang supermarket.dat") 
def additem(): 
    fh1=open("saitems.csv","a",newline='') 
    st=csv.writer(fh1) 
    ino=input("ENTER ITEM CODE:") 
    iname=input("ENTER NAME:") 
    iprice=float(input("ENTER PRICE:")) 
    iquant=int(input("ENTER QUANTITY:")) 
    st.writerow([ino,iname,iprice,iquant]) 
    print("!!ITEM ADDED SUCCESSFULLY!!") 
    fh1.close() 
def displayitem(cdno): 
    fh2=open("saitems.csv","r",newline='\r\n') 
 
    print("\tITEM CODE | ITEM NAME | PRICE | QUANTITY |")  
    st=csv.reader(fh2) 
    for i in st: 
        if i[0]==cdno: 
            print("\t",i[0]," | ",i[1]," | ",i[2]," | ",i[3]," | ") 
            break 
        else: 
            print("NO SUCH ITEM IN THE STOCK") 
    fh2.close() 
def displayallit(): 
    fh2=open("saitems.csv","r",newline='\r\n') 
    print("\tITEM CODE | ITEM NAME | PRICE | QUANTITY |") 
    st=csv.reader(fh2) 
    for i in st: 
       print("\t",i[0]," | ",i[1]," | ",i[2]," | ",i[3]," | ") 
    fh2.close() 
def editprice(cdno): 
    fh2=open("saitems.csv","r",newline='\r\n') 
    temp=[] 
    st=csv.reader(fh2) 
    for i in st: 
        print(i) 
        if i[0]==cdno: 
            i[2]=float(input("ENTER THE NEW PRICE:")) 
 
            temp.append(i) 
        else: 
            temp.append(i)   
    fh2.close()  
    fh3=open("saitems.csv","w") 
    es=csv.writer(fh3) 
    for j in temp: 
        es.writerow(j) 
        print("ITEM UPDATED SUCCESSFULLY") 
    fh3.close() 
def editquant(cdno): 
    fh2=open("saitems.csv","r",newline='\r\n') 
    temp=[] 
    st=csv.reader(fh2) 
    for i in st: 
        print(i) 
        if i[0]==cdno: 
            i[3]=int(input("ENTER THE NEW QUANTITY:")) 
            temp.append(i)   
        else: 
            temp.append(i)   
    fh2.close()  
    fh3=open("saitems.csv","w") 
    es=csv.writer(fh3) 
 
    for j in temp: 
        es.writerow(j) 
    print("ITEM UPDATED SUCCESSFULLY") 
    fh3.close() 
def editcode(cdno): 
    fh2=open("saitems.csv","r",newline='\r\n') 
    temp=[] 
    st=csv.reader(fh2) 
    for i in st: 
        print(i) 
        if i[0]==cdno: 
            i[0]=input("ENTER THE NEW CODE:") 
            temp.append(i)   
        else: 
            temp.append(i)   
    fh2.close()  
    fh3=open("saitems.csv","w") 
    es=csv.writer(fh3) 
    for j in temp: 
        es.writerow(j) 
    print("ITEM UPDATED SUCCESSFULLY") 
    fh3.close() 
def delitem(cdno): 
   fh2=open("saitems.csv","r",newline='\r\n') 
 
   temp=[] 
   st=csv.reader(fh2) 
   for i in st: 
       print(i) 
       if i[0]==idno: 
           continue 
       else: 
           temp.append(i) 
   fh3=open("saitems.csv","w") 
   es=csv.writer(fh3) 
   for j in temp: 
       es.writerow(j) 
   fh3.close()     
   print("ITEM DELETED SUCCSESSFULLY")  
     
ans="y" 
while ans=="Y" or ans=="y": 
    print("\t*******MAIN MENU*******") 
    print("\t1.CUSTOMER\n\t2.BILLING\n\t3.STOCK REGISTER") 
    ch=int(input("ENTER YOUR CHOICE(1~3)")) 
    if ch==1: 
        print("CUSTOMER MENU") 
        print("1.ADD CUSTOMER\n2.SHOW CUSTOMER\n3.DELETE CUSTOMER\n4.EDIT CUSTOMER") 
        cu=int(input("ENTER YOUR CHOICE(1~4)")) 
        if cu==1: 
            addcust() 
        elif cu==2: 
            an="Y" 
            while an=="Y" or an=="y": 
                print("DISPLAY MENU") 
                print("1.DISPLAY ALL\n2.DISPLAY A CUSTOMER") 
                c=int(input("ENTER YOUR CHOICE(1~2)")) 
                if c==1: 
                    displayall() 
                elif c==2: 
                    phno=int(input("ENTER CUSTOMER'S PHONE NUMBER:")) 
                    displaycust(phno) 
                else: 
                    print("INVALID CHOICE!!!!") 
                an=input("DO YOU WISH TO CONTINUE WITH DISPLAY MENU?(Y/N)") 
        elif cu==3: 
            an="Y" 
            while an=="Y" or an=="y": 
                print("DELETE CUSTOMER MENU ") 
                print("1.DELETE ALL\n2.DELETE A CUSTOMER") 
                c=int(input("ENTER YOUR CHOICE(1~2)")) 
 
                if c==2: 
                    pno=int(input("ENTER THE CUSTOMER'S PHONE NUMBER YOU WANT TO DELETE:")) 
                    delcust(pno)                  
                elif c==1: 
                    delall()                   
                else: 
                    print("INVALID CHOICE") 
                an=input("DO YOU WISH TO CONTINUE WITH DELETE CUSTOMER MENU?(Y/N)") 
        elif cu==4: 
            a="y" 
            while a=="Y" or a=="y": 
                print("EDIT CUSTOMER MENU") 
                print("1.EDIT DOB\n2.EDIT ADDRESS") 
                c=int(input("ENTER YOUR CHOICE")) 
                if c==2: 
                    pno=int(input("ENTER THE CUSTOMER'S PHONE NUMBER YOU WANT TO DELETE:")) 
                    etaddr(pno) 
                elif c==1: 
                    pno=int(input("ENTER THE CUSTOMER'S PHONE NUMBER YOU WANT TO EDIT:")) 
                    edtdob(pno) 
                else: 
 
                    print("INVALID CHOICE") 
                a=input("DO YOU WISH TO CONTINUE WITH EDIT CUSTOMER MENU?(Y/N)") 
    elif ch==3: 
        an="Y" 
        while  an=="Y" or an=="y": 
            print("STOCK MENU ") 
            print("1.ADD ITEM\n2.DISPLAY STOCK\n3.UPDATE/EDIT STOCK\n4.DELETE ITEM") 
            c=int(input("ENTER YOUR CHOICE(1~4)")) 
            if c==1: 
                an="y" 
                while an=="Y" or an=="y": 
                    additem() 
                    an=input("DO YOU WISH TO ADD MORE ITEMS(Y/N)") 
            elif c==2: 
                aq="Y" 
                while aq=="Y" or aq=="y": 
                    print("DISPLAY STOCK") 
                    print("1.DISPLAY A ITEM\n2.DISPLAY ALL") 
                    cs=int(input("ENTER YOUR CHOICE(1~2)")) 
                    if cs==1: 
                        ae="Y" 
                        while ae=="Y" or ae=="y": 
                            idno=input("ENTER THE ITEM CODE YOU WANT TO DISPLAY:") 
 
                            displayitem(idno) 
                            ae=input("DO YOU WISH TO CONTINUE TO DISPLAY A ITEM(Y/N)") 
                    elif cs==2: 
                        ae="Y" 
                        while ae=="Y" or ae=="y": 
                            displayallit() 
                            ae=input("DO YOU WISH TO CONTINUE TO DISPLAY ALL(Y/N)") 
                    else: 
                        print("INVALID CHOICE") 
                    aq=input("DO YOU WISH TO CONTINUE WITH DISPLAYMENU(Y/N)") 
            elif c==3: 
                ak="y" 
                while ak=="y" or ak=="Y": 
                    print("1.EDIT PRICE\n2.EDIT QUANTITY\n3.EDIT ITEM CODE") 
                    ec=int(input("Enter your choice(1~3)")) 
                    if ec==1: 
                        idno=input("ENTER THE ITEM CODE YOU WANT TO EDIT:") 
                        editprice(idno) 
                    elif ec==2: 
                        idno=input("ENTER THE ITEM CODE YOU WANT TO EDIT:") 
                        editquant(idno) 
                    elif ec==3: 
 
                        idno=input("ENTER THE ITEM CODE YOU WANT TO EDIT:") 
                        editcode(idno) 
                    else: 
                        print("INVALID CHOICE")   
                    ak=input("DO YOU WISH TO CONTINUE TO UPDATE ITEMS(Y/N)") 
            elif c==4: 
                ak="y" 
                while ak=="y" or ak=="Y": 
                    idno=input("ENTER THE ITEM CODE YOU WANT TO DELETE:") 
                    delitem(idno) 
                    ak=input("DO YOU WISH TO CONTINUE TO DELETE ITEM(Y/N)") 
            else: 
                print("INVALID CHOICE") 
            an=input("DO YOU WISH TO CONTINUE WITH STOCK MENU(Y/N)") 
    elif ch==2: 
        ad="y" 
        while ad=="y" or ad=="y": 
            print("BILL MENU") 
            print("1.NEW BILL\n2.CANCEL BILL\n3.DISPLAY BILL") 
            c=int(input("ENTER YOUR CHOICE(1~3)")) 
            if c==1: 
                ai="y" 
                billno=0 
                while ai=="y" or ai=="Y": 
 
                    pass 
                    fh=open("sarang supermarket.dat","rb") 
                    fh4=open("sarangbill.dat'","ab") 
                    cs=int(input("ENTER THE CUSTOMER'S PHONE NO:")) 
                    bill={} 
                    bill["bno"]=int(input("ENTER THE BILL NO:")) 
                    billno=bill["bno"] 
                    bill["bdate"]=input("ENTER THE DATE:") 
                    it=[] 
                    quant=[] 
                    pr=[] 
                    try: 
                        while True: 
                            st=pickle.load(fh) 
                            if st["phno"]==cs: 
                                bill["custtname"]=st["name"] 
                                print(bill["custtname"]) 
                                a="y" 
                                while a=="y": 
                                    item=input("ENTER THE ITEM NO:") 
                                    fh2=open("saitems.csv","r",newline='\r\n') 
                                    temp=[] 
                                    st=csv.reader(fh2) 
                                    for i in st: 
 
                                        if i[0]==item: 
                                            qu=int(input("ENTER THE QUANTITY:")) 
                                            if int(i[3])-qu<10: 
                                                print("INSUFFICIENT PRODUCT") 
                                                temp.append(i)     
                                            else: 
                                                it.append(i[1]) 
                                                quant.append(qu) 
                                                i[3]=str(int(i[3])-qu) 
                                                temp.append(i) 
                                                p=float(i[2])*qu 
                                                pr.append(p) 
                                        else: 
                                            temp.append(i) 
                                    fh3=open("saitems.csv","w") 
                                    es=csv.writer(fh3) 
                                    for j in temp: 
                                        es.writerow(j) 
                                    print("ITEM UPDATED SUCCESSFULLY") 
                                    fh3.close() 
                                    bill["iname"]=it 
                                    bill["iquant"]=quant 
                                    bill["iprice"]=pr 
                                    print(bill) 
 
                                    a=input("DO YOU WISH TO ADD MORE ITEMS(Y/N)") 
                                     
                    except EOFError: 
                        fh.close() 
                    pickle.dump(bill,fh4) 
                    fh4.close() 
                    ai=input("DO YOU WANT TO CONTINUE BILLING") 
                else: 
                    fh4=open("sarangbill.dat'","rb") 
                    print("\t\t\tBILL") 
                    try: 
                        while True: 
                            st=pickle.load(fh4) 
                            if bill["bno"]==billno: 
                                item=st["iname"] 
                                price=st["iprice"] 
                                s=sum(price) 
                                quant=st["iquant"] 
                                print("\tBill No:",st["bno"]) 
                                print("\tCustomer Name:",st["custtname"]) 
                                print("\tDate:",st["bdate"]) 
                                print("\t| Sno | Rate |      Items    | Quantity | Price |") 
                                for i in range(len(item)): 
 
                                    print("\t| ",(i+1)," | ",price[i]//quant[i]," | ",item[i],"     | ",quant[i]," | ",price[i]) 
                                print("\tGRAND TOTAL:",s) 
                                print("\t\t   THANK YOU    ") 
                                print("\t\t   VISIT AGAIN  ") 
                    except EOFError: 
                        fh4.close() 
            elif c==2: 
                fh4=open("sarangbill.dat'","rb") 
                fh5=open("tempit.dat","ab") 
                bno=int(input("ENTER THE BILL NO YOU WANT TO DELETE")) 
                try: 
                    while True: 
                        st=pickle.load(fh4) 
                        if st["bno"]==bno: 
                            it=st["iname"] 
                            quant=st["iquant"] 
                            n=len(it) 
                            fh2=open("saitems.csv","r",newline='\r\n') 
                            sb=csv.reader(fh2) 
                            temp=[] 
                            for i in it: 
                                for j in sb: 
                                    if i==j[1]: 
 
                                        j[3]=str(int(j[3])+quant[it.index(i)]) 
                                        temp.append(j) 
                                    elif j not in temp: 
                                        pass 
                                    else: 
                                        temp.append(j) 
                                print("ITEM UPDATED SUCCESSFULLY") 
                                fh2.seek(0) 
                            fh3=open("saitems.csv","w") 
                            es=csv.writer(fh3) 
                            es.writerows(temp) 
                            fh3.close() 
                        else: 
                            pickle.dump(st,fh5) 
                except EOFError: 
                    fh4.close() 
                print("BILL CANCELLED SUCCESSFYLLY!!!") 
                fh5.close() 
                os.remove("sarangbill.dat'") 
                os.rename("tempit.dat","sarangbill.dat'") 
            elif c==3: 
                a="y" 
                while a=="y" or a=="Y": 
                    bno=int(input("ENTER THE BILL NO YOU WANT TO DISPLAY")) 
 
                    fh6=open("sarangbill.dat'","rb") 
                    try: 
                        while True: 
                            st=pickle.load(fh6) 
                            if st["bno"]==bno: 
                                print(st) 
                    except EOFError: 
                        fh6.close() 
                    a=input("DO YOU WISH TO DISPLAY MORE BILLS?") 
            else: 
                print("INVALID CHOICE") 
            ad=input("DO YOU WANT TO CONTINUE WITH BILL MENU(Y/N)") 
    else: 
        print("INVALID CHOICE") 
    ans=input("DO YOU WISH TO CONTINUE WITH MAIN MENU?(Y/N)") 
else: 
    print("!! MAIN MENU CLOSING !!") 
    sys.exit(0)