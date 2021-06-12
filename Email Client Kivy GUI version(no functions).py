from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
import mysql.connector
import hashlib
import getpass


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

    BoxLayout:
        orientation:'vertical'

        MDToolbar:
            title:'Email Client'
            elevation: 8

        
        MDLabel:

        MDTextField:
            hint_text:"Enter Registered Email Id"
            helper_text:"OR Click register and register new email id:"
            helper_text_mode:"on_focus"
            pos_hint:{'center_x':0.45,'center_y':0.5}
            size_hint_x:0.4

        MDTextField:
            hint_text:"Enter Password"
            helper_text:"OR Click register and register new email id:"
            helper_text_mode:"on_focus"
            pos_hint:{'center_x':0.45,'center_y':0.5}
            size_hint_x:0.4

        MDLabel:
    
    MDRectangleFlatIconButton:
        text:"Login"
        icon:'login'
        pos_hint:{'center_x':0.45,'center_y':0.3}
        on_press: root.manager.current = 'userpage'
        
    MDRectangleFlatIconButton:
        text:"Register"
        icon:'register'
        pos_hint:{'center_x':0.45,'center_y':0.2}
        on_press: root.manager.current = 'registerpage'
    

<Register_page>:
    name:'registerpage'
    BoxLayout:
        orientation:'vertical'

        MDToolbar:
            title:'Register Email'
            elevation: 8
        
        MDLabel:

        MDTextField:
            hint_text:"Enter New email id to register"
            helper_text:"OR Click login to login"
            helper_text_mode:"on_focus"
            pos_hint:{'center_x':0.45,'center_y':0.5}
            size_hint_x:0.4

        MDTextField:
            hint_text:"Enter Password for email"
            pos_hint:{'center_x':0.45,'center_y':0.5}
            size_hint_x:0.4

        MDLabel:

    MDRectangleFlatIconButton:
        text:"Create Account"
        icon:'table-merge-cells'
        pos_hint:{'center_x':0.45,'center_y':0.3}
        on_press: root.manager.current = 'loginpage'

    MDRectangleFlatIconButton:
        text:"Login"
        icon:'login'
        pos_hint:{'center_x':0.45,'center_y':0.2}
        on_press: root.manager.current = 'loginpage'


<User_page>:
    name:'userpage'
    MDLabel:
        text:'Welcome user'
        halign:'center'

    
    MDNavigationLayout:
        x: usermenubar.height

        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'

                    MDToolbar:
                        id:usermenubar
                        title:'user account'
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
                            text:'Users name'
                            secondary_text:'Users email'
                            IconLeftWidget:
                                icon:'account-box'
                        OneLineAvatarIconListItem:
                            text: 'Received Mails'
                            font_style:'Caption'
                            on_release: root.manager.current = 'receivedmailpage'
                            IconLeftWidget:
                                icon: "email-receive"

                        OneLineAvatarIconListItem:
                            text: 'Sent Mails'
                            font_style:'Caption'
                            on_release: root.manager.current = 'sentmailpage'
                            IconLeftWidget:
                                icon: "email-send"


    MDBottomAppBar:
        md_bg_color: 1, 1, 1, 1
        MDToolbar:
            icon: "email-send"
            type: "bottom"
            mode: "end"
            on_action_button:root.manager.current = 'sendmailpage'




<Send_mail_page>:
    name:'sendmailpage'
    BoxLayout:
        orientation:'vertical'

        MDToolbar:
            title:'Send Email'
            elevation: 8
            right_action_items: [["send"]]

            MDRectangleFlatIconButton:
                text:"back"
                icon:'keyboard-backspace'
                pos_hint:{'center_x':0.2,'center_y':0.1}
                on_press: root.manager.current = 'userpage'

        MDTextField:
            hint_text:"TO"
            pos_hint:{'center_x':0.3,'center_y':0.9}
            size_hint_x:0.4

        MDTextField:
            hint_text:"Subject"
            pos_hint:{'center_x':0.3,'center_y':0.9}
            size_hint_x:0.4

        MDTextField:
            hint_text:"Message"
            pos_hint:{'center_x':0.3,'center_y':0.9}
            size_hint_x:0.4
            multiline:'True'

        MDLabel:


<Received_mail_page>:
    name:'receivedmailpage'
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title:'Received Mails'
            elevation: 8
            left_action_items: [["keyboard-return"]]
        ScrollView:
            MDList:
                ThreeLineAvatarIconListItem:
                    text:'Users name'
                    secondary_text:'Users email'
                    tertiary_text:"ff"
                    IconLeftWidget:
                        icon:'message-arrow-left'

<Sent_mail_page>:
    name:'sentmailpage'
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title:'Sent Mails'
            elevation: 8
            left_action_items: [["keyboard-return"]]
        ScrollView:
            MDList:
                ThreeLineAvatarIconListItem:
                    text:'Users name'
                    secondary_text:'Users email'
                    tertiary_text:"gg"
                    IconLeftWidget:
                        icon:'message-arrow-right'

"""




class Login_page(Screen):
    pass

class Register_page(Screen):
    pass

class User_page(Screen):
    pass

class Send_mail_page(Screen):
    pass

class Received_mail_page(Screen):
    pass

class Sent_mail_page(Screen):
    pass

class screenmanage(ScreenManager):
    sm = ScreenManager()
    sm.add_widget(Login_page(name = 'loginpage'))
    sm.add_widget(Register_page(name= 'registerpage'))
    sm.add_widget(User_page(name = 'userpage'))
    sm.add_widget(Send_mail_page(name = 'sendmailpage'))
    sm.add_widget(Received_mail_page(name = 'receivedmailpage'))
    sm.add_widget(Sent_mail_page(name = 'sentmailpage'))

class EmailClientApp(MDApp):
    def build(self):
        screengui = Builder.load_string(guidesign)
        return screengui

EmailClientApp().run()