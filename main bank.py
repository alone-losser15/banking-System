def menu():
    while True:
        
        print()
        print('1.CREATE BANK ACCOUNT')
        print()
        print('2.TRANSACTION')
        print()
        print('3.CUSTOMER DETAILS')
        print()
        print('4.TRANSACTION DETAILS')
        print()
        print('5.DELETE ACCOUNT')
        print()
        print('6.QUIT')
        print()
        n=int(input('Enter your CHOICE='))
        print()
        if n == 1:
            acc_no=int(input('Enter your ACCOUNT NUMBER='))
            print()
            acc_name=input('Enter your ACCOUNT NAME=')
            print()
            ph_no=int(input('Enter your PHONE NUMBER='))
            print()
            add=(input('Enter your place='))
            print()
            cr_amt=float(input('Enter your credit amount='))
            V_SQLInsert="INSERT  INTO customer_details values (" +  str (acc_no) + ",' " + acc_name + " ',"+str(ph_no) + ",' " +add + " ',"+ str (cr_amt) + " ) "
            cur.execute(V_SQLInsert)
            print()
            print('Account Created Succesfully!!!!!')
            conn.commit()
        elif n == 2:
             ####
            
            acct_no=int(input('Enter Your Account Number='))
            cur.execute('select * from customer_details where acct_no='+str (acct_no))
            data=cur.fetchall()
            count=cur.rowcount
            conn.commit()
            if count == 0:
                print()
                print('Account Number Invalid Sorry Try Again Later    \n ORCREATE YOUR ACCOUNT FIRST ')
                print()
            else:
                
                print()
                print('1.WITHDRAW AMOUNT')
                print()
                print('2.ADD AMOUNT')
                print()
                x=int(input('Enter your CHOICE='))
                print()
                if x == 1:
                    amt=float(input('Enter withdrawl amount='))
                    cr_amt=0
                    cur.execute('update customer_details set   cr_amt=cr_amt-'+str(amt) +  ' where acct_no=' +str(acct_no) )
                    V_SQLInsert="INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(acct_no,dt.datetime.today(),amt,cr_amt) 
                    cur.execute(  V_SQLInsert)
                    conn.commit()
                    print()
                    print('Account Updated Succesfully!!!!!')   
                if x== 2:
                    amt=float(input('Enter amount to be added='))
                    cr_amt=0
                    cur.execute('update customer_details set  cr_amt=cr_amt+'+str(amt) +  ' where acct_no=' +str(acct_no) )
                    V_SQLInsert="INSERT  INTO transactions values ({} , '{}' , {} , {}) ".format(acct_no,dt.datetime.today(),cr_amt,amt)
                    cur.execute(  V_SQLInsert)
                    conn.commit()
                    print()
                    print('Account Updated Succesfully!!!!!')
        elif n == 3:
            acct_no=int(input('Enter your account number='))
            print()
            cur.execute('select * from customer_details where acct_no='+str(acct_no) )
            if cur.fetchone() is  None:
                print()
                print('Invalid Account number')
            else:
                cur.execute('select * from customer_details where acct_no='+str(acct_no) )
                data=cur.fetchall()
                for row in data:
                    print('ACCOUNT NO=',acct_no,'     ACCOUNT NAME=',row[1],'    PHONE NUMBER=',row[2],'     ADDRESS=',row[3],'    credit amt=',row[4])
                    print()
                    
            conn.commit()
        elif n == 4:
            acct_no=int(input('Enter your account number='))
            print()
            cur.execute('select * from customer_details where acct_no='+str(acct_no) )
            if cur.fetchone() is  None:
                print()
                print('Invalid Account number')
            else:
                cur.execute('select * from transactions where acct_no='+str(acct_no) )
                data=cur.fetchall()
                for row in data:
                    print('ACCOUNT NO=',acct_no,'     DATE=',row[1],'      WITHDRAWAL AMOUNT=',row[2],'     AMOUNT ADDED=',row[3])
                    print()
                      
        elif n == 5:
            print('DELETE YOUR ACCOUNT')
            acct_no=int(input('Enter your account number='))
            cur.execute('delete from customer_details where acct_no='+str(acct_no) )
            print('ACCOUNT DELETED SUCCESFULLY')
        elif n == 6:
            print('THANK YOU PLEASE VISIT AGAIN')
            break
        else:
            print('choose the right option!!!!!!!!!!!!')
     
     
    
                                               

               
#MAIN
import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='1234')
if conn.is_connected():
     print('connected succesfully')
cur=conn.cursor()
cur.execute("create database if not exists bank")
cur.execute("use bank")
cur.execute('create table if not exists customer_details(acct_no bigint(25) primary key,acct_name varchar(25) ,phone_no bigint(25) check(phone_no>11),address varchar(45),cr_amt float(10,2) )')
cur.execute('create table if not exists transactions(acct_no int(11),date date ,withdrawal_amt float(10,2),amount_added float(10,2) )')
cur.execute('create table if not exists user_table(username varchar(25) primary key,passwrd int(10) not null )')
conn.commit()
print("******DATABASE IS STABILIS AND TABLES WERE CREATED************")

print('=========================WELCOME TO STARK BANK============================================================')
import datetime as dt
print(dt.datetime.now())
print('1.REGISTER')
print()
print('2.LOGIN')
print()
print('0.exit')

while True:
    
    n=int(input('enter your choice='))
    print()

    if n== 1:
        cur.execute("select * from user_table")
        v=cur.fetchall()
        count=cur.rowcount
        conn.commit()
        if count<2:
            name=input('Enter the Username=')
            print()
            passwd=int(input('Enter a numeric Password='))
            print()
            V_SQLInsert="INSERT  INTO user_table (passwrd,username) values (" +  str (passwd) + ",' " + name + " ') "
            cur.execute(V_SQLInsert)
            conn.commit()
            print()
            print('USER created succesfully')
            menu()
        else:
            print()
            print("*************maximum number of users is defined \n******* so, go through the login way   ")
    elif n==2 :
        name=input('Enter your Username=')
        print()
        passwd=int(input('Enter your Password='))
        V_Sql_Sel="select * from user_table where passwrd='"+str (passwd)+"' and username=  ' " +name+ " ' "
        cur.execute(V_Sql_Sel)
        if cur.fetchone() is  None:
            print()
            print('Invalid username or password')
        else:
            print()
            menu()
    elif n == 0:
        break
    else:
        print("choose a appropriate option:")
     
     
