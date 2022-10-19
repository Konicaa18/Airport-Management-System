#AIRPORT MANAGEMENT SYSTEM
#FLIGHT DETAILS
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="admin",database="airlines")
mycursor=mydb.cursor()

print("******************WELCOME TO AIRPORT MANAGEMENT SYSTEM******************")
def flight_details():
    print("********************* FLIGHT DETAILS *********************")
    while True:
        print("1.Domestic Flights")
        print("2.International Flights")
        print("3.Go back to the Main Menu")
        choice=int(input("Enter flight type whose details you want to view(1/2)="))
        print("======================================================")
        if choice==1:
            while True:
                print("1.View Airlines")
                print("2.View the details of all available Domestic Flights")
                print("3.View the details of Flights arriving at a specific location")
                print("4.View the details of Flights departing from a specific location")
                print("5.View the details of a specific flight")
                print("6.Go Back to the main menu")
                ch=int(input("Enter your choice(1-6)="))
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                if ch==1:
                    mycursor.execute("select distinct(airlines) from domesticflights")
                    for x in mycursor:
                        print(x)
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                elif ch==2:
                    print('FL_NO',' FLIGHT_NAME','   ','BOARDING','  ARRIVAL','\t',
                    'S_FILL',' ','DATE','\t\t','T_SEATS','AIRLINES','\t','FARE')
                    mycursor.execute("select * from domesticflights")
                    for x in mycursor:
                        print(x[0],' ',x[1],'\t',x[2],'\t ',x[3],'\t',x[4],'\t',x[5],
                        '\t',x[6],'\t',x[7],'\t',x[8])
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                elif ch==3:
                   des=input("Enter your destination:")
                   try:
                       sql="SELECT * FROM domesticflights WHERE ARRIVAL like '{}'".format(des)
                       mycursor.execute(sql)
                       data=mycursor.fetchall()
                       mydb.commit()
                       if data==[]:
                           print("Ooops!!!No flight with this location is available at the moment")
                           print("Contact Head Office for more information.")
                       else:
                           print('FL_NO',' FLIGHT_NAME','   ','BOARDING','  ARRIVAL','\t',
                                 'S_FILL',' ','DATE','\t\t','T_SEATS','AIRLINES','\t','FARE')
                           for i in data:
                               print(i[0],' ',i[1],'\t',i[2],'\t ',i[3],'\t',i[4],'\t',i[5],
                                    '\t',i[6],'\t',i[7],'\t',i[8])
                   except Exception as e:
                       print(e)
                   print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                elif ch==4:
                   des=input("Enter the place of departure:")
                   try:
                       sql="SELECT * FROM domesticflights WHERE DEPARTURE like '{}'".format(des)
                       mycursor.execute(sql)
                       data=mycursor.fetchall()
                       mydb.commit()
                       if data==[]:
                           print("Ooops!!!No flight with this location is available at the moment")
                           print("Contact Head Office for more information.")
                       else:
                           print('FL_NO',' FLIGHT_NAME','   ','BOARDING','  ARRIVAL','\t','S_FILL',
                                 ' ','DATE','\t\t','T_SEATS','AIRLINES','\t','FARE')
                           for i in data:
                               print(i[0],' ',i[1],'\t',i[2],'\t ',i[3],'\t',i[4],'\t',i[5],'\t',
                                     i[6],'\t',i[7],'\t',i[8])
                   except Exception as e:
                       print(e)
                   print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                elif ch==5:
                    f=int(input("Enter the flight number whose details you want to view:"))
                    try:
                       sql="SELECT * FROM domesticflights WHERE FLIGHTNO like {}".format(f)
                       mycursor.execute(sql)
                       data=mycursor.fetchone()
                       if data==None:
                           print("The given flight number does not exist")
                       else:
                           print('FL_NO',' FLIGHT_NAME','   ','BOARDING','  ARRIVAL','\t','S_FILL',
                                 ' ','DATE','\t\t','T_SEATS','AIRLINES','\t','FARE')
                           print(data[0],' ',data[1],'\t',data[2],'\t ',data[3],'\t',data[4],'\t',
                                 data[5],'\t',data[6],'\t',data[7],'\t',data[8])
                    except Exception as e:
                       print(e)
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                
                elif ch==6:
                     return
        elif choice==2:
            while True:
                print("1.View Airlines")
                print("2.View the details of all available International Flights")
                print("3.View the details of Flights arriving at a specific location")
                print("4.View the details of Flights departing from a specific location")
                print("5.View the details of a specific flight")
                print("6.Go Back to the main menu")
                c=int(input("Enter your choice(1-6)="))
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                if c==1:
                    mycursor.execute("select distinct(airlines) from internationalflights")
                    for x in mycursor:
                        print(x)
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                elif c==2:
                    print('FL_NO',' FLIGHT_NAME','   ','BOARDING','  ARRIVAL','\t','S_FILL',
                          ' ','DATE','\t\t','T_SEATS','AIRLINES','\t','FARE')
                    mycursor.execute("select * from internationalflights")
                    for x in mycursor:
                        print(x[0],' ',x[1],'\t',x[2],'\t ',x[3],'\t',x[4],'\t',x[5],
                              '\t',x[6],'\t',x[7],'\t',x[8])
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")                  
                elif c==3:
                   des=input("Enter your destination:")
                   try:
                       sql="SELECT * FROM internationalflights WHERE ARRIVAL like '{}'".format(des)
                       mycursor.execute(sql)
                       data=mycursor.fetchall()
                       mydb.commit()
                       if data==[]:
                           print("Ooops!!!No flight with this location is available at the moment")
                           print("Contact Head Office for more information")
                       else:
                           print('FL_NO',' FLIGHT_NAME','   ','BOARDING','  ARRIVAL','\t','S_FILL',
                                 ' ','DATE','\t\t','T_SEATS','AIRLINES','\t','FARE')
                           for i in data:
                               print(i[0],' ',i[1],'\t',i[2],'\t ',i[3],'\t',i[4],'\t',i[5],'\t'
                                     ,i[6],'\t',i[7],'\t',i[8])
                   except Exception as e:
                       print(e)
                   print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    
                elif c==4:
                    des=input("Enter boarding place:")
                    try:
                        sql="SELECT * FROM internationalflights WHERE departure like '{}'".format(des)
                        mycursor.execute(sql)
                        data=mycursor.fetchall()
                        mydb.commit()
                        if data==[]:
                            print("Ooops!!!No flight with this location is available at the moment")
                            print("Contact Head Office for more information")
                        else:
                           print('FL_NO',' FLIGHT_NAME','   ','BOARDING','  ARRIVAL','\t','S_FILL',
                                 ' ','DATE','\t\t','T_SEATS','AIRLINES','\t','FARE')
                           for i in data:
                               print(i[0],' ',i[1],'\t',i[2],'\t ',i[3],'\t',i[4],'\t',i[5],'\t',
                                     i[6],'\t',i[7],'\t',i[8])
                    except Exception as e:
                       print(e)
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    
                elif c==5:
                    f=int(input("Enter the flight number whose details you want to view:"))
                    try:
                       sql="SELECT * FROM internationalflights WHERE FLIGHTNO like {}".format(f)
                       mycursor.execute(sql)
                       data=mycursor.fetchone()
                       mydb.commit()
                       if data==None:
                           print("The given flight number does not exist")
                       else:
                          print('FL_NO',' FLIGHT_NAME','   ','BOARDING','  ARRIVAL','\t','S_FILL',
                                ' ','DATE','\t\t','T_SEATS','AIRLINES','\t','FARE')
                          print(data[0],' ',data[1],'\t',data[2],'\t ',data[3],'\t',data[4],'\t',
                                data[5],'\t',data[6],'\t',data[7],'\t',data[8])
                    except Exception as e:
                       print(e)
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                elif c==6:
                    return
        elif choice==3:
                return

def add():
    print("***************ADDING RECORDS IN THE FLIGHT CHART*******************")
    while True:
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("Where do you want to enter the records?")
        print("1.Enter records in DomesticFlights")
        print("2.Enter records in InternationalFlights")
        print("3.Go back to the Main Menu")
        ftype=int(input("Enter your choice="))
        print("======================================================")
        if ftype==1:
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",password="admin",database="airlines")
                mycursor=mydb.cursor()
                while True:
                    flightno=int(input("Enter flight number:"))
                    flname=input("Enter flight name:")
                    departure=input("Enter departure city:")
                    arrival=input("Enter arrival city:")
                    noofpassengers=0
                    date=input('Enter the date of departure:')
                    totalseats=300
                    airlines=input("Enter name of the airlines:")
                    fare=int(input("Enter flight fare:"))
                    economy=0;business=0;firstclass=0
                    sql="insert into domesticflights(flightno,flname,departure,arrival,\
                    noofpassengers,date,totalseats,airlines,fare,economy,business,firstclass)values({},'{}','{}','{}',{},{},'{}','{}',{},{},{},{})".format(flightno,flname,departure,arrival,noofpassengers,date,totalseats,airlines,fare,economy,business,firstclass)
                    mycursor.execute(sql)
                    print("\n!!!Successfully inserted the record!!!")
                    ans=input(" Do you want to enter more(y/n)?")
                    if ans in 'Nn':
                        break
                mydb.commit()
            except Exception as e:
                print(e)
                
        elif ftype==2:
            try:
                mydb=mysql.connector.connect(host="localhost",user="root",password="admin",database="airlines")
                mycursor=mydb.cursor()
                while True:
                    flightno=int(input("Enter flight number:"))
                    flname=input("Enter flight name:")
                    departure=input("Enter boarding country:")
                    arrival=input("Enter destination:")
                    noofpassengers=0
                    date=input('Enter date of departure:')
                    totalseats=300
                    airlines=input("Enter name of the airlines:")
                    fare=int(input("Enter flight fare:"))
                    economy=0;business=0;firstclass=0
                    sql="insert into internationalflights(flightno,flname,departure,\
                    arrival,noofpassengers,date,totalseats,airlines,fare,economy,business,\
                    firstclass)values({},'{}','{}','{}',{},{},'{}','{}',{},{},{},\
                    {})".format(flightno,flname,departure,arrival,noofpassengers,date,\
                                totalseats,airlines,fare,economy,business,firstclass)
                    mycursor.execute(sql)
                    print("!!!Successfully inserted the record!!!")
                    ans=input("You want to enter more(y/n)?")
                    if ans in 'nN':
                        break
                mydb.commit()
            except Exception as e:
                print(e)
        elif ftype==3:
            print("TERMINATING")
            return
        else:
            print("WRONG CHOICE")


def booking():
    def pdata():
        print("==============================================================================")
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='airlines')
            mycursor=mydb.cursor()
            pname=input("Enter your name:")
            arrival=input("Enter your Destination:")
            sql="SELECT * FROM domesticflights WHERE arrival like '{}'".format(arrival)
            mycursor.execute(sql)
            data=mycursor.fetchall()
            mydb.commit()
            if data==[]:
                print("SORRY!!!..NO FLIGHT AVAILABLE FOR",arrival,". CONTACT HEAD OFFICE")
            else:
                print("==============================================================================")
                print("The available flights are:")
                sql="SELECT FLIGHTNO,FLNAME,DEPARTURE FROM DOMESTICFLIGHTS WHERE ARRIVAL='{}'".format(arrival)
                print()
                print("FLIGHT_NO,FLIGHT_NAME,DEPARTURE")
                mycursor.execute(sql)
                for i in mycursor:
                    print(i)
                a=int(input("Do you want to confirm the booking ? Enter 1 for yes:"))
                if a==1:
                    print()
                    flightno=int(input("Enter flight number="))
                    print()
                    data="SELECT * FROM DOMESTICFLIGHTS WHERE flightno={}".format(flightno)
                    mycursor.execute(data)
                    b=mycursor.fetchall()
                    for i in b:
                        if i[4]>=i[6]:
                            print("SORRY!!! SEATS FOR THIS FLIGHT ARE ALREADY BOOKED.LOOK FOR SOME ANOTHER FLIGHT.")
                            break
                        else:
                            pid=int(input("Enter passenger id:"))
                            departure=input("Enter boarding place=")
                            print ("please choose a class type\n")
                            s=0
                            print ("FOLLOWING ROOMS ARE AVAILABLE:-")
                            print ("1. type First class---->rs 8000 PN\-")
                            print ("2. type Business class---->rs 6000 PN\-")
                            print ("3. type Economy class---->rs 4000 PN\-")
                            flag=0
                            while flag!=1:
                                x=int(input("Enter Your Choice:"))
                                if(x==1):
                                    if i[11]<60:
                                        print ("you have opted First class")
                                        s=8000
                                        sql="update domesticflights set firstclass=firstclass+1 where flightno={}".format(flightno)
                                        mycursor.execute(sql)
                                        flag=1
                                    else:
                                        print("SEATS OF FIRST CLASS ARE ALREADY FILLED!!!.LOOK FOR SOME ANOTHER SEAT")
                                        flag=0
                                elif(x==2):
                                    if i[10]<120:
                                        print ("you have opted Business class")
                                        s=6000
                                        sql="update domesticflights set business=business+1 where flightno={}".format(flightno)
                                        mycursor.execute(sql)
                                        flag=1
                                    else:
                                        print("SEATS OF BUSINESS CLASS ARE ALREADY FILLED!!!.LOOK FOR SOME ANOTHER SEAT")
                                        flag=0
                                    
                                elif(x==3):
                                    s=0
                                    if i[9]<120:
                                        print ("you have opted Economy class")
                                        s=4000
                                        sql="update domesticflights set economy=economy+1 where flightno={}".format(flightno)
                                        mycursor.execute(sql)
                                        flag=1
                                    else:
                                        print("SEATS OF ECONOMY CLASS ARE ALREADY FILLED!!!.LOOK FOR SOME ANOTHER SEAT")
                                        flag=0                                    
                            print ("AMOUNT PAYABLE =",s,"\n")
                            CLAS=input("Enter class=")
                            sql="INSERT INTO pdata(pid,pname,departure,arrival,flightno,class)values({},'{}','{}','{}',{},'{}')".format(pid,pname,departure,arrival,flightno,CLAS)
                            mycursor.execute(sql)
                            mydb.commit()
                            print("Your PassengerId is:",pid)
                            print("****************TICKET RESERVATION SUCCESSFULLY COMPLETED*******************")
                            sql1="UPDATE DOMESTICFLIGHTS SET NOOFPASSENGERS=NOOFPASSENGERS+1 WHERE FLIGHTNO={}".format(flightno)
                            mycursor.execute(sql1)
                            mydb.commit()
        except Exception as e:
            print(e)

    def pidata():
        print("==============================================================================")
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='airlines')
            mycursor=mydb.cursor()
            pname=input("Enter your name:")
            arrival=input("Enter your Destination:")
            sql="SELECT * FROM internationalflights WHERE arrival like '{}'".format(arrival)
            mycursor.execute(sql)
            data=mycursor.fetchall()
            mydb.commit()
            if data==[]:
                print("SORRY!!!..NO FLIGHT AVAILABLE FOR",arrival,". CONTACT HEAD OFFICE")
            else:
                print("==============================================================================")
                print("The available flights are:")
                sql="SELECT FLIGHTNO,FLNAME,DEPARTURE FROM INTERNATIONALFLIGHTS WHERE ARRIVAL='{}'".format(arrival)
                print()
                print("FLIGHT_NO,FLIGHT_NAME,DEPARTURE")
                mycursor.execute(sql)
                for i in mycursor:
                    print(i)
                print("==============================================================================")
                a=int(input("Do you want to confirm the booking.Enter 1 for yes:"))
                if a==1:
                    print()
                    pid=int(input("Enter passenger id:"))
                    flightno=int(input("Enter flight number="))
                    departure=input("Enter boarding country=")
                    print()
                    data="SELECT * FROM INTERNATIONALFLIGHTS WHERE flightno={}".format(flightno)
                    mycursor.execute(data)
                    b=mycursor.fetchall()
                    for i in b:
                        if i[4]>=i[6]:
                            print("SORRY!!! SEATS FOR THIS FLIGHT ARE ALREADY BOOKED.LOOK FOR SOME ANOTHER FLIGHT.")
                            break
                        else:
                            print ("please choose a class type\n")
                            s=0
                            print ("FOLLOWING ROOMS ARE AVAILABLE:-")
                            print ("1. type First class---->rs 80000 PN\-")
                            print ("2. type Business class---->rs 60000 PN\-")
                            print ("3. type Economy class---->rs 40000 PN\-")
                            
                            flag=0
                            while flag!=1:
                                x=int(input("Enter Your Choice:"))
                                if(x==1):
                                    if i[11]<60:
                                        print ("you have opted First class")
                                        s=80000
                                        sql="update internationalflights set firstclass=firstclass+1 where flightno={}".format(flightno)
                                        mycursor.execute(sql)
                                        flag=1
                                    else:
                                        print("SEATS OF FIRST CLASS ARE ALREADY FILLED!!!.LOOK FOR SOME ANOTHER SEAT")
                                        flag=0
                                elif(x==2):
                                    if i[10]<120:
                                        print ("you have opted Business class")
                                        s=60000
                                        sql="update internationalflights set business=business+1 where flightno={}".format(flightno)
                                        mycursor.execute(sql)
                                        flag=1
                                    else:
                                        print("SEATS OF BUSINESS CLASS ARE ALREADY FILLED!!!.LOOK FOR SOME ANOTHER SEAT")
                                        flag=0
                                    
                                elif(x==3):
                                    s=0
                                    if i[9]<120:
                                        print ("you have opted Economy class")
                                        s=40000
                                        sql="update internationalflights set economy=economy+1 where flightno={}".format(flightno)
                                        mycursor.execute(sql)
                                        flag=1
                                    else:
                                        print("SEATS OF ECONOMY CLASS ARE ALREADY FILLED!!!.LOOK FOR SOME ANOTHER SEAT")
                                        flag=0                                    
                            print ("AMOUNT PAYABLE =",s,"\n")
                            CLAS=input("Enter class=")
                            sql="INSERT INTO pIdata(pid,pname,departure,arrival,flightno,class)values({},'{}','{}','{}',{},'{}')".format(pid,pname,departure,arrival,flightno,CLAS)
                            mycursor.execute(sql)
                            mydb.commit()
                            print("Your PassengerId is:",pid)
                            print("****************TICKET RESERVATION SUCCESSFULLY COMPLETED*******************")
                            sql1="UPDATE INTERNATIONALFLIGHTS SET NOOFPASSENGERS=NOOFPASSENGERS+1 WHERE FLIGHTNO={}".format(flightno)
                            mycursor.execute(sql1)
                            mydb.commit()                    
        except Exception as e:
            print(e)            

    print("***************** WELCOME TO AIRLINES RESERVATION SYSTEM *******************")
    print("\n1.RESERVATION FOR DOMESTIC AIRLINES")
    print("2.RESERVATION FOR INTERNATIONAL AIRLINES")
    print("3.EXIT")
    ch=int(input("Enter your choice(1-3):"))
    if ch==1:
        pdata()
    elif ch==2:
        pidata()
    elif ch==3:
        print("TERMINATING")
    else:
        print("WRONG CHOICE")

    mydb.commit()



def p_details():
    print("********************* PASSENGER DETAILS *********************")
    while True:
        print("1.View records of passengers travelling through Domestic Flights")
        print("2.View records of passengers travelling through International Flights")
        print("3.Go back to the Main Menu")
        choice=int(input("Enter your choice(1/3)="))
        print("======================================================")
        if choice==1:
            while True:
                print("1.View Passenger id's of all passengers")
                print("2.View the details of all passengers travelling through Domestic Flights")
                print("3.View the details of passengers arriving at a specific location")
                print("4.View the details of passengers boarding from a specific location")
                print("5.View the details of a specific passenger")
                print("6.View the details of passengers travelling through a particular flight")
                print("7.Go Back to the main menu")
                ch=int(input("Enter your choice(1-7):"))
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                if ch==1:
                    mycursor.execute("select pid from pdata")
                    for x in mycursor:
                        print(x)
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                elif ch==2:
                    print("P_ID","NAME",'\t',"DEPARTURE",'\t',"ARRIVAL",'\t',"F_NO",'\t',"CLASS")
                    mycursor.execute("select * from pdata")
                    for x in mycursor:
                        print(x[0],x[1],'\t',x[2],'\t','\t',x[3],'\t',x[4],'\t',x[5])
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                elif ch==3:
                   des=input("Enter destination:")
                   try:
                       sql="SELECT * FROM pdata WHERE ARRIVAL like '{}'".format(des)
                       mycursor.execute(sql)
                       data=mycursor.fetchall()
                       mydb.commit()
                       if data==[]:
                           print("No passenger with this destination is mentioned in the office records")
                       else:
                           print("P_ID","NAME",'\t',"DEPARTURE",'\t',"ARRIVAL",'\t',"F_NO",'\t',"CLASS")
                           for i in data:
                               print(i[0],i[1],'\t',i[2],'\t','\t',i[3],'\t',i[4],'\t',i[5])
                   except Exception as e:
                       print(e)
                   print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                elif ch==4:
                   des=input("Enter boarding place:")
                   try:
                       sql="SELECT * FROM pdata WHERE DEPARTURE like '{}'".format(des)
                       mycursor.execute(sql)
                       data=mycursor.fetchall()
                       mydb.commit()
                       if data==[]:
                           print("No passenger with this destination is mentioned in the office records")
                       else:
                           print("P_ID","NAME",'\t',"DEPARTURE",'\t',"ARRIVAL",'\t',"F_NO",'\t',"CLASS")
                           for i in data:
                               print(i[0],i[1],'\t',i[2],'\t','\t',i[3],'\t',i[4],'\t',i[5])
                   except Exception as e:
                       print(e)
                   print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                elif ch==5:
                    f=int(input("Enter the passenger id of the passenger whose details you want to view:"))
                    try:
                       sql="SELECT * FROM pdata WHERE pid like {}".format(f)
                       mycursor.execute(sql)
                       data=mycursor.fetchone()
                       mydb.commit()
                       if data==None:
                           print("The given passenger id does not exist in the office records")
                       else:
                           print("P_ID","NAME",'\t',"DEPARTURE",'\t',"ARRIVAL",'\t',"F_NO",'\t',"CLASS")
                           print(data[0],data[1],'\t',data[2],'\t','\t',data[3],'\t',data[4],'\t',data[5])
                    except Exception as e:
                       print(e)
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                
                elif ch==6:
                    f=int(input("Enter the flight number:"))
                    try:
                       sql="SELECT * FROM pdata WHERE flightno like {}".format(f)
                       mycursor.execute(sql)
                       data=mycursor.fetchall()
                       mydb.commit()
                       if data==[]:
                           print("The given flight number does not exist in the office records")
                       else:
                           print("P_ID","NAME",'\t',"DEPARTURE",'\t',"ARRIVAL",'\t',"F_NO",'\t',"CLASS")
                           for i in data:
                               print(i[0],i[1],'\t',i[2],'\t','\t',i[3],'\t',i[4],'\t',i[5])
                    except Exception as e:
                       print(e)
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                
                elif ch==7:
                     return
        elif choice==2:
            while True:
                print("1.View Passenger id's of all passengers")
                print("2.View the details of all passengers travelling through International Flights")
                print("3.View the details of passengers arriving at a specific location")
                print("4.View the details of passengers boarding from a specific location")
                print("5.View the details of a specific passenger")
                print("6.View the details of passengers travelling through a particular flight")
                print("7.Go Back to the main menu")
                c=int(input("Enter your choice(1-7):"))
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                if c==1:
                    mycursor.execute("select pid from pidata")
                    for x in mycursor:
                        print(x)
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                elif c==2:
                    print("P_ID","NAME",'\t',"DEPARTURE",'\t',"ARRIVAL",'\t',"F_NO",'\t',"CLASS")
                    mycursor.execute("select * from pidata")
                    for x in mycursor:
                        print(x[0],x[1],'\t',x[2],'\t','\t',x[3],'\t',x[4],'\t',x[5])
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    
                elif c==3:
                   des=input("Enter destination:")
                   try:
                       sql="SELECT * FROM pidata WHERE ARRIVAL like '{}'".format(des)
                       mycursor.execute(sql)
                       data=mycursor.fetchall()
                       mydb.commit()
                       if data==[]:
                           print("No passenger with this destination is mentioned in the office records")
                       else:
                           print("P_ID","NAME",'\t',"DEPARTURE",'\t',"ARRIVAL",'\t',"F_NO",'\t',"CLASS")
                           for i in data:
                               print(i[0],i[1],'\t',i[2],'\t','\t',i[3],'\t',i[4],'\t',i[5])
                   except Exception as e:
                       print(e)
                   print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    
                elif c==4:
                   des=input("Enter boarding place:")
                   try:
                       sql="SELECT * FROM pidata WHERE DEPARTURE like '{}'".format(des)
                       mycursor.execute(sql)
                       data=mycursor.fetchall()
                       mydb.commit()
                       if data==[]:
                           print("No passenger with this destination is mentioned in the office records")
                       else:
                           print("P_ID","NAME",'\t',"DEPARTURE",'\t',"ARRIVAL",'\t',"F_NO",'\t',"CLASS")
                           for i in data:
                               print(i[0],i[1],'\t',i[2],'\t','\t',i[3],'\t',i[4],'\t',i[5])
                   except Exception as e:
                       print(e)
                   print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    
                elif c==5:
                    f=int(input("Enter the passenger id of the passenger whose details you want to view:"))
                    try:
                       sql="SELECT * FROM pidata WHERE pid like {}".format(f)
                       mycursor.execute(sql)
                       data=mycursor.fetchone()
                       mydb.commit()
                       if data==None:
                           print("The given passenger id does not exist in the office records")
                       else:
                           print("P_ID","NAME",'\t',"DEPARTURE",'\t',"ARRIVAL",'\t',"F_NO",'\t',"CLASS")
                           print(data[0],data[1],'\t',data[2],'\t','\t',data[3],'\t',data[4],'\t',data[5])
                    except Exception as e:
                       print(e)
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                elif c==6:
                    f=int(input("Enter the flight number:"))
                    try:
                       sql="SELECT * FROM pidata WHERE flightno like {}".format(f)
                       mycursor.execute(sql)
                       data=mycursor.fetchall()
                       mydb.commit()
                       if data==[]:
                           print("The given flight number does not exist in the office records")
                       else:
                           print("P_ID","NAME",'\t',"DEPARTURE",'\t',"ARRIVAL",'\t',"F_NO",'\t',"CLASS")
                           for i in data:
                               print(i[0],i[1],'\t',i[2],'\t','\t',i[3],'\t',i[4],'\t',i[5])
                    except Exception as e:
                       print(e)
                    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                    
                elif c==7:
                    return
        elif choice==3:
                return


def cancel():
    def cancel_Dticket():
        import mysql.connector
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='airlines')
        mycursor=mydb.cursor()
        a=int(input("Do you want to view the passenger names along with their details.Enter 1 for yes."))
        if a==1:
            mycursor.execute("select * from pdata")
            data=mycursor.fetchall()
            print("P_ID","NAME",'\t',"DEPARTURE",'\t',"ARRIVAL",'\t',"F_NO",'\t',"CLASS")
            for i in data:
                print(i[0],i[1],'\t',i[2],'\t','\t',i[3],'\t',i[4],'\t',i[5])
        else:
            b=int(input("Do you want to view the passenger id's of all registered passengers.Enter 1 for yes."))
            if b==1:
                print("Passenger id's of the registered passengers are----->>>>>>")
                mycursor.execute("select pid from pdata")
                for x in mycursor:
                    print(x)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='airlines')
            mycursor=mydb.cursor()
            pid=int(input("Enter passenger id whose details is to be deleted="))
            sql="delete from pdata where pid=%s"
            sid=(pid,)
            no=int(input("Enter the flight number for confirmation:"))
            mycursor.execute(sql,sid)
            mydb.commit()
            sql="update domesticflights set noofpassengers=noofpassengers-1 where flightno={}".format(no)
            mycursor.execute(sql)
            print("1.FIRSTCLASS \t 2.BUSINESS \t 3.ECONOMY")
            CLASS=int(input("Choose your registered class(1-3)>>:"))
            if CLASS==1:
                sql1="update domesticflights set firstclass=firstclass-1 where flightno={}".format(no)
            elif CLASS==2:
                sql1="update domesticflights set business=business-1 where flightno={}".format(no)
            elif CLASS==3:
                sql1="update domesticflights set economy=economy-1 where flightno={}".format(no)
            mycursor.execute(sql1)
            mydb.commit()
            print("Reservation for passenger with passenger id",pid,"has been cancelled")
        except Exception as e:
            print(e)
        mydb.commit()

    def cancel_Iticket():
        import mysql.connector
        mydb=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='airlines')
        mycursor=mydb.cursor()
        a=int(input("Do you want to view the passenger names along with their details.Enter 1 for yes."))
        if a==1:
            mycursor.execute("select * from pidata")
            data=mycursor.fetchall()
            print("P_ID","NAME",'\t',"DEPARTURE",'\t',"ARRIVAL",'\t',"F_NO",'\t',"CLASS")
            for i in data:
                print(i[0],i[1],'\t',i[2],'\t','\t',i[3],'\t',i[4],'\t',i[5])
        else:
            b=int(input("Do you want to view the passenger id's of all registered passengers.Enter 1 for yes."))
            if b==1:
                print("Passenger id's of the registered passengers are----->>>>>>")
                mycursor.execute("select pid from pidata")
                for x in mycursor:
                    print(x)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        try:
            mydb=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='airlines')
            mycursor=mydb.cursor()
            pid=int(input("Enter passenger id whose details is to be deleted="))
            sql="delete from pidata where pid=%s"
            sid=(pid,)
            no=int(input("Enter the flight number for confirmation:"))
            mycursor.execute(sql,sid)
            mydb.commit()
            sql="update internationalflights set noofpassengers=noofpassengers-1\
                 where flightno={}".format(no)
            mycursor.execute(sql)
            print("1.FIRSTCLASS \t 2.BUSINESS \t 3.ECONOMY")
            CLASS=int(input("Choose your registered class(1-3)>>"))
            if CLASS==1:
                sql1="update internationalflights set firstclass=firstclass-1 \
                      where flightno={}".format(no)
            elif CLASS==2:
                sql1="update internationalflights set business=business-1\
                      where flightno={}".format(no)
            elif CLASS==3:
                sql1="update internationalflights set economy=economy-1\
                      where flightno={}".format(no)
            mycursor.execute(sql1)
            mydb.commit()
            print("Reservation for passenger with passenger id",pid,"has been cancelled")
        except Exception as e:
            print(e)
        mydb.commit()
        
    while True:
        print("**************************** FLIGHT RESERVATION CANCELLATION ******************************")
        print("1.DOMESTIC AIRLINES RESERVATION CANCELLATION")
        print("\n2.INTERNATIONAL AIRLINES RESERVATION CANCELLATION ")
        print("\n3.Go back to the Main Menu")
        ch=int(input("Enter from where do you want to delete the records?:"))
        print("======================================================")
        if ch==1:
            cancel_Dticket()
        elif ch==2:
            cancel_Iticket()
        elif ch==3:
            return
        else:
            print("WRONG CHOICE")
            
############################ MAIN PROGRAM ################################    
while True:
    print("==========================================================================")
    print("1.VIEW DETAILS OF AVAILABLE FLIGHTS")
    print("2.ADD RECORDS IN THE FLIGHT CHART")
    print("3.TICKET RESERVATION")
    print("4.VIEW PASSENGER DETAILS")
    print("5.CANCELLATION OF A BOOKED FLIGHT")
    print("6.EXIT\n")
    print("==========================================================================")
    ch=int(input("Enter your choice(1-6)="))
    print("===========================================================================")
    if ch==1:
        flight_details()
    elif ch==2:
        add()
    elif ch==3:
        booking()
    elif ch==4:
        p_details()
    elif ch==5:
        cancel()
    elif ch==6:
        print("************ THANK YOU *****************")
        break
    else:
        print("WRONG CHOICE")
