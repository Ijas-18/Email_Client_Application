import mysql.connector
import hashlib
import getpass


def database():
    try:
        global mydb
        mydb = mysql.connector.connect(host="remotemysql.com",
                                       user="Kek5nLJNbQ",
                                       password="SDn1G50OHW",
                                       database="Kek5nLJNbQ")
        return 1
    except :
        print("cant connect to database check network and try again")
        return 0


def storecredentials(email,password):
    try:
        sql = "INSERT INTO Email_Client_User_Database(Email,password) VALUES (%s,%s)"
        val = (email,password)
        mycursor.execute(sql,val)
        mydb.commit()
        name = email.split("@")
        name[1] = name[1].split(".com")
        sql2 = "ALTER TABLE Email_Client_Senders ADD COLUMN {}_{} TEXT NULL".format(name[0],name[1][0])
        mycursor.execute(sql2)
        mydb.commit()
        sql4 = "ALTER TABLE Email_Client_Receivers ADD COLUMN {}_{} TEXT NULL".format(name[0],name[1][0])
        mycursor.execute(sql4)
        mydb.commit()
        return 1
    except mysql.connector.errors.IntegrityError:
        print("Error Email may already have been registered choose any new email or if it is your's go and try to login")
        return 0



def validatecredentials(email,password):
    sql = "SELECT Email, Password FROM Email_Client_User_Database WHERE Email = %s and Password = %s"
    emps = (email, password)
    mycursor.execute(sql,emps)
    myresult = mycursor.fetchall()
    for x in myresult:
        if(x == emps):
            return 1
        else:
            return 0



def user(email,user_name):
    print("\n\t  Hii %s Glad to see you login  "%(user_name))
    while(1):
        try:
            print("\nEnter 1 to send email, 2 to view received email, 3 to view sent mails, 4 to logout")
            u_choice = 0
            u_choice = int(input("Enter your choice:"))
            if (u_choice == 1):
                sendmail(email)
                continue
            elif(u_choice == 2):
                view_receivedmail(email)
                continue
            elif(u_choice == 3):
                view_sentmail(email)
                continue
            elif(u_choice == 4):
                break
            else:
                print("\n Enter correct option\n ")
                continue
            return 
        except ValueError:
            print("\n Enter correct option \n")
        except :
            print("\n An Error has been occured \n")
            

def sendmail(sender):
    sender = asterik_to_underscore(sender)
    sender = sender.split(".com")
    receiver = input("Enter receipient Email:")
    receiver = asterik_to_underscore(receiver)
    receiver = receiver.split(".com")
    subject = input("Enter Subject of Mail:")
    message = input("Enter message:")
    sub_mssg = "From:%s   To:%s   Subject:%s   Message:%s"%(sender[0],receiver[0],subject,message)
    
    hash_message = sender[0]+receiver[0]+subject+message
    hash_encode = hashlib.sha256(hash_message.encode())
    message_no = hash_encode.hexdigest()
    
    sql3 = "INSERT INTO Email_Client_Messages(Mail_no,Mail_message) VALUES (%s,%s)"
    val3 = (message_no,sub_mssg)
    mycursor.execute(sql3,val3)
    mydb.commit()

    sql5_un = 'INSERT INTO Email_Client_Senders(%s)'%(sender[0])
    sql5 = sql5_un+' VALUES (%s)'
    val5 = (message_no,)
    mycursor.execute(sql5,val5)
    mydb.commit()


    sql6_un = 'INSERT INTO Email_Client_Receivers(%s)'%(receiver[0])
    sql6 = sql6_un+' VALUES (%s)'
    val6 = (message_no,)
    mycursor.execute(sql6,val6)
    mydb.commit()
    
    print("\n Mail Sent successfuly \n")
    return 1



def view_receivedmail(receiver):
    print("The received mails are:")
    receiver = asterik_to_underscore(receiver)
    receiver = receiver.split(".com")
    sql7 = "SELECT %s FROM Email_Client_Receivers"%(receiver[0])
    mycursor.execute(sql7)

    mail_no = mycursor.fetchall()
    for d in mail_no:
        sql8 = 'SELECT Mail_message FROM Email_Client_Messages WHERE Mail_no =%s'
        mycursor.execute(sql8,d)
        message = mycursor.fetchall()
        try:
            real_message = message[0][0].rsplit('   ')
            print("\n" +underscore_to_asterik(real_message[0]) +".com\n" +real_message[2])
            for m in range(3,len(real_message)):
                print(real_message[m],end=' ')
            print("\n\n")
        except IndexError:
            pass
       

def view_sentmail(sender):
    print("The sent mails are:")
    sender = asterik_to_underscore(sender)
    sender = sender.split(".com")
    sql8 = "SELECT %s FROM Email_Client_Senders"%(sender[0])
    mycursor.execute(sql8)

    mail_no = mycursor.fetchall()
    count = 0
    for h in mail_no:
        sql9 = 'SELECT Mail_message FROM Email_Client_Messages WHERE Mail_no =%s'
        mycursor.execute(sql9,h)
        message = mycursor.fetchall()
        try:
            real_message = message[0][0].rsplit('   ')
            print("\n" +underscore_to_asterik(real_message[1])+".com \n" +real_message[2])
            for n in range(3,len(real_message)):
                print(real_message[n],end=' ')
            print("\n\n")
        except IndexError:
            pass
        
        

    
def asterik_to_underscore(j):
    name = j.rsplit("@")
    name = name[0]+'_'+name[1]
    return name

def underscore_to_asterik(u):
    name = u.rsplit("_")
    name = name[0]+'@'+name[1]
    return name
    




    
print("\n\t Hii There Welcome to Email Client \n")

while(1):
    if(database()==1):
        mycursor = mydb.cursor()
        pass
    else:
        break
    try:
        print("Enter 1 for Registering New Email, 2 for Login, 3 for Exit:")
        choice = int(input("\nEnter your choice:"))
        
        if(choice == 1):
            user_email = input("Enter Email:")
            user_password = getpass.getpass("Enter password:(Entered password will not be visible on screen)")
            check_stored = 0
            check_stored = storecredentials(user_email,user_password)
            if (check_stored == 1):
                print("\n\nsuccess\n\nEmail and password registered")
            else:
                print("Cant register try again")
                
        elif(choice == 2):
            user_email = input("Enter Email:")
            user_password = getpass.getpass("Enter password:(Entered password will not be visible on screen)")
            check_stored = 0
            check_stored = validatecredentials(user_email,user_password)
            if (check_stored == 1):
                user_name = user_email.rsplit("@")
                user(user_email,str(user_name[0]))
                print("\n Successfully Logged Out \n")
                continue
            else:
                print("\n Can't find your email check your credentials or try to register new account \n")
             
        elif(choice == 3):
            print("\n\t  ********THank You*********\n")
            mycursor.close()
            mydb.close()
            break
        
        else:
            print("Enter correct choice")
            pass

        
    except ValueError:
        print("\n Enter correct option \n")
        pass
    except :
        print("\n An Error has been occured \n")
        pass






        
