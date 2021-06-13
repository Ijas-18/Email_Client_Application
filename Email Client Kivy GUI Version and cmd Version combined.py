from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.uix.list import ThreeLineListItem
import mysql.connector
import hashlib                                                      

                                                        #This guidesign string includes all elements of each screen
guidesign = """
ScreenManager:
    Login_page:
    Register_page:
    User_page:
    Send_mail_page:
    Received_mail_page:
    Sent_mail_page:

<Login_page>:
    name:'loginpage'

    email:email
    password:password

    BoxLayout:
        orientation:'vertical'

        MDToolbar:
            title:'Log In to IJ Email Client'
            elevation: 8

        
        MDLabel:

        MDTextField:
            id:email
            hint_text:"Email Id"
            helper_text:"OR register new email id:"
            helper_text_mode:"on_focus"
            pos_hint:{'center_x':0.5,'center_y':0.9}
            size_hint_x:0.8

        MDTextField:
            id:password
            hint_text:"Password"
            helper_text:"OR register new email id:"
            helper_text_mode:"on_focus"
            pos_hint:{'center_x':0.5,'center_y':0.9}
            size_hint_x:0.8
            icon_right: 'eye-off'
            password : True

        MDLabel:
    
    MDRectangleFlatIconButton:
        text:"Login"
        icon:'login'
        pos_hint:{'center_x':0.5,'center_y':0.3}
        on_release:
            root.manager.transition.direction = 'left'
            root.manager.current = 'userpage' if root.validate() == 1 else 'registerpage'
        
    MDRectangleFlatIconButton:
        text:"Register"
        icon:'register'
        pos_hint:{'center_x':0.5,'center_y':0.2}
        on_release:
            root.manager.transition.direction = 'right'
            root.manager.current = 'registerpage'
    

<Register_page>:
    name:'registerpage'
    email:email
    password:password
    
    BoxLayout:
        orientation:'vertical'

        MDToolbar:
            title:'Register Email'
            elevation: 8
        
        MDLabel:

        MDTextField:
            id:email
            hint_text:"Enter New email id to register"
            helper_text:"OR Click login to login"
            helper_text_mode:"on_focus"
            pos_hint:{'center_x':0.5,'center_y':0.9}
            size_hint_x:0.8

        MDTextField:
            id:password
            hint_text:"Enter Password for email"
            pos_hint:{'center_x':0.5,'center_y':0.9}
            size_hint_x:0.8
            icon_right: 'eye-off'
            password:True

        MDLabel:

    MDRectangleFlatIconButton:
        text:"Create Account"
        icon:'table-merge-cells'
        pos_hint:{'center_x':0.5,'center_y':0.3}
        on_release:
            root.manager.transition.direction = 'left'
            root.manager.current = 'loginpage' if root.store() == 1 else 'registerpage'

    MDRectangleFlatIconButton:
        text:"Login"
        icon:'login'
        pos_hint:{'center_x':0.5,'center_y':0.2}
        on_release: 
            root.manager.transition.direction = 'left'
            root.manager.current = 'loginpage'


<User_page>:
    name:'userpage'
    userlabel : userlabel
    usermenubar : usermenubar
    accountlabel : accountlabel
    MDLabel:
        id:userlabel
        text:'Welcome '
        halign:'center'

    
    MDNavigationLayout:
        x: usermenubar.height

        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'

                    MDToolbar:
                        id:usermenubar
                        title:'Account Menu'
                        elevation: 8
                        left_action_items: [["menu",lambda x: navigation.set_state("open")]]
                    Widget:



        MDNavigationDrawer:
            id: navigation
            BoxLayout:
                spacing:'7dp'
                padding:'7dp'
                orientation:'vertical'


                ScrollView:
                    MDList:
                        TwoLineAvatarIconListItem:
                            id:accountlabel
                            text:''
                            secondary_text:''
                            IconLeftWidget:
                                icon:'account-box'
                        OneLineAvatarIconListItem:
                            text: 'Received Mails'
                            font_style:'Caption'
                            on_release: 
                                root.manager.transition.direction = 'up'
                                root.manager.current = 'receivedmailpage'
                            IconLeftWidget:
                                icon: "email-receive"

                        OneLineAvatarIconListItem:
                            text: 'Sent Mails'
                            font_style:'Caption'
                            on_release:
                                root.manager.transition.direction = 'down'
                                root.manager.current = 'sentmailpage'
                            IconLeftWidget:
                                icon: "email-send"

                        OneLineAvatarIconListItem:
                            text: 'Log Out'
                            font_style:'Caption'
                            on_release:
                                root.manager.transition.direction = 'right'
                                root.manager.current = 'loginpage'
                            IconLeftWidget:
                                icon: "logout"


    MDBottomAppBar:
        md_bg_color: 1, 1, 1, 1
        MDToolbar:
            icon: "email-send"
            type: "bottom"
            mode: "end"
            on_action_button:
                root.manager.transition.direction = 'left'
                root.manager.current = 'sendmailpage'


<Send_mail_page>:
    name:'sendmailpage'
    to : to
    sub : sub
    mssg : mssg
    BoxLayout:
        orientation:'vertical'

        MDToolbar:
            title:'Send Email'
            elevation: 8

        MDTextField:
            id:to
            hint_text:"TO"
            pos_hint:{'center_x':0.5,'center_y':0.9}
            size_hint_x:0.8

        MDTextField:
            id:sub
            hint_text:"Subject"
            pos_hint:{'center_x':0.5,'center_y':0.9}
            size_hint_x:0.8

        MDTextField:
            id:mssg
            hint_text:"Message"
            pos_hint:{'center_x':0.5,'center_y':0.9}
            size_hint_x:0.8
            multiline:True
        
        GridLayout:
            cols:2
            spacing : '15dp'
            padding : '10dp'
            pos_hint:{'center_x':0.6,'center_y':0.5}
            MDRectangleFlatIconButton:
                text:"back"
                icon:'keyboard-backspace'
                pos_hint:{'center_x':0.4,'center_y':0.1}
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'userpage'
            
            MDRectangleFlatIconButton:
                id:sendbtn
                text:"Send Mail"
                icon:'send'
                pos_hint:{'center_x':0.4,'center_y':0.1}
                on_press:
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'userpage' if root.send() == 1 else 'sendmailpage'


        MDLabel:


<Received_mail_page>:
    name:'receivedmailpage'
    receivermessage:receivermessage
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title:'Received Mails'
            elevation: 8
        ScrollView:
            MDList:
                id:receivermessage               
    MDRectangleFlatIconButton:
        text:"back"
        icon:'keyboard-backspace'
        pos_hint:{'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.transition.direction = 'down'
            root.manager.current = 'userpage'


<Sent_mail_page>:
    name:'sentmailpage'
    sendermessage:sendermessage
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title:'Sent Mails'
            elevation: 8
        ScrollView:
            MDList:
                id:sendermessage
    MDRectangleFlatIconButton:
        text:"back"
        icon:'keyboard-backspace'
        pos_hint:{'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.transition.direction = 'up'
            root.manager.current = 'userpage'

"""


class cmdversion():                                             #1st email client version code modified
    email = ''
    password = ''
    def database():
        try:
            global mydb
            mydb = mysql.connector.connect(host="remotemysql.com",
                                        user="Kek5nLJNbQ",
                                        password="SDn1G50OHW",
                                        database="Kek5nLJNbQ")
            return 1
        except :
            return 0

    def validatecredentials(self,email,password):
        self.email = email
        self.password = password
        if (cmdversion.database() == 1):
            sql = "SELECT Email, Password FROM Email_Client_User_Database WHERE Email = %s and Password = %s"
            emps = (email,password)
            mycursor = mydb.cursor()
            mycursor.execute(sql,emps)
            myresult = mycursor.fetchall()
            for x in myresult:
                if(x == emps):
                    return 1
                else:
                    return 0
        else:
            return 0

    def storecredentials(self,email,password):
        if (cmdversion.database() == 1):
            try:
                mycursor = mydb.cursor()
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
                return 0
        else:
            return 0

    def sendmail(self,to,sub,mssg):
        if (cmdversion.database() == 1):
            mycursor = mydb.cursor()
            sender = cmdversion.asterik_to_underscore(self.email)
            sender = sender.split(".com")
            receiver = cmdversion.asterik_to_underscore(to)
            receiver = receiver.split(".com")
            subject = sub
            message = mssg
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
            
            return 1
        else:
            return 0
    
    def view_receivedmail(self):
        if (cmdversion.database() == 1):
            mycursor = mydb.cursor()
            receiver = cmdversion.asterik_to_underscore(self.email)
            receiver = receiver.split(".com")
            sql7 = "SELECT %s FROM Email_Client_Receivers"%(receiver[0])
            mycursor.execute(sql7)

            mail_no = mycursor.fetchall()

            receivedmessages = []

            for d in mail_no:
                sql8 = 'SELECT Mail_message FROM Email_Client_Messages WHERE Mail_no =%s'
                mycursor.execute(sql8,d)
                message = mycursor.fetchall()
                try:
                    real_message = message[0][0].rsplit('   ')
                    sender = cmdversion.underscore_to_asterik(real_message[0]) +".com"
                    subject = real_message[2]
                    msgstring = ''
                    for m in range(3,len(real_message)):
                        msgstring += real_message[m]
                    combined = [sender,subject,msgstring]
                    receivedmessages.append(combined)    
                except IndexError:
                    pass
            return receivedmessages  

        else:
            pass
    
    def view_sentmail(self):
        if (cmdversion.database() == 1):
            mycursor = mydb.cursor()
            sender = cmdversion.asterik_to_underscore(self.email)
            sender = sender.split(".com")
            sql8 = "SELECT %s FROM Email_Client_Senders"%(sender[0])
            mycursor.execute(sql8)

            mail_no = mycursor.fetchall()
            sentmessages = []

            for h in mail_no:
                sql9 = 'SELECT Mail_message FROM Email_Client_Messages WHERE Mail_no =%s'
                mycursor.execute(sql9,h)
                message = mycursor.fetchall()
                try:
                    real_message = message[0][0].rsplit('   ')
                    receiver = cmdversion.underscore_to_asterik(real_message[1])+".com" 
                    subject = real_message[2]
                    msgstring = ''
                    for n in range(3,len(real_message)):
                        msgstring += real_message[n]
                    combined = [receiver,subject,msgstring]
                    sentmessages.append(combined)
                except IndexError:
                    pass
            return sentmessages
        else:
            return 0

    def asterik_to_underscore(j):
        name = j.rsplit("@")
        name = name[0]+'_'+name[1]
        return name

    def underscore_to_asterik(u):
        name = u.rsplit("_")
        name = name[0]+'@'+name[1]
        return name




cmd = cmdversion()                                          #creates a instace of cmdversion class

class Login_page(Screen):                                           #each class is created to control each screens
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    def validate(self):
        if(cmd.validatecredentials(self.email.text,self.password.text) ==1 ):
            return 1
        else:
            return 0    

class Register_page(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    def store(self):
        if(cmd.storecredentials(self.email.text,self.password.text) ==1 ):
            return 1
        else:
            return 0  
    
class User_page(Screen):
    userlabel = ObjectProperty(None)
    accountlabel = ObjectProperty(None)
    def on_enter(self, *args):
        user_name = cmd.email.split('@')
        self.userlabel.text = 'Welcome ' + user_name[0]
        self.accountlabel.text = '' + user_name[0]
        self.accountlabel.secondary_text = '' + cmd.email

class Send_mail_page(Screen):
    to : ObjectProperty(None)
    sub : ObjectProperty(None)
    mssg : ObjectProperty(None)
    def send(self):
        if(cmd.sendmail(self.to.text,self.sub.text,self.mssg.text) == 1):
            return 1
        else:
            return 0

class Received_mail_page(Screen):
    receivermessage : ObjectProperty(None)
    def on_enter(self,*args):
        msg = cmd.view_receivedmail()
        for i in range(len(msg)):
            self.receivermessage.add_widget(ThreeLineListItem(text="{}".format(msg[i][0]),secondary_text = "{}".format(msg[i][1]),tertiary_text = "{}".format(msg[i][2])))
    
    def on_leave(self, *args):
        self.receivermessage.clear_widgets(children=None)
    
class Sent_mail_page(Screen):
    sendermessage : ObjectProperty(None)
    def on_enter(self,*args):
        msg = cmd.view_sentmail()
        for i in range(len(msg)):
            self.sendermessage.add_widget(ThreeLineListItem(text="{}".format(msg[i][0]),secondary_text = "{}".format(msg[i][1]),tertiary_text = "{}".format(msg[i][2])))

    def on_leave(self, *args):
        self.sendermessage.clear_widgets(children=None)

class screenmanage(ScreenManager):
    pass


class EmailClientApp(MDApp):                                        #Extends the prebuilt MDApp class 
    def build(self):                                                #Builds the gui
        self.theme_cls.primary_palette = 'Cyan'
        sm = ScreenManager()                                                #creates a instance of screen manager to switch between screens
        sm.add_widget(Login_page(name = 'loginpage'))
        sm.add_widget(Register_page(name= 'registerpage'))
        sm.add_widget(User_page(name = 'userpage'))
        sm.add_widget(Send_mail_page(name = 'sendmailpage'))
        sm.add_widget(Received_mail_page(name = 'receivedmailpage'))
        sm.add_widget(Sent_mail_page(name = 'sentmailpage'))                        #adds all screens
        screengui = Builder.load_string(guidesign)                                  #loads the instructions and elements of each screen
        return screengui                                                                


EmailClientApp().run()              #program stars here