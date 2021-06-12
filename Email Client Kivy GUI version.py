from kivymd.app import MDApp
from kivy.lang.builder import ScreenManager,Screen




class login_page:
    pass

class register_page:
    pass

class user_page:
    pass

class send_mail_page:
    pass

class received_mail_page:
    pass

class sent_mail_page:
    pass


class EmailClient(MDApp):
    def build(self):
        screengui = Builder.load_string(clientgui)
        return screengui