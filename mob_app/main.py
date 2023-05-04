import glob
import json
import random
from datetime import datetime
from pathlib import Path
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from hoverable import HoverBehavior

Builder.load_file("design.kv")


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"
    
    def login(self, un, pw):
        with open("users.json") as file:
            users = json.load(file)
            if un in users and users[un]["password"] == pw:
                self.manager.current = "login_screen_success"
            else:
                self.ids.wrong_login.text = "Wrong password or username!"
                
    def f_pw_redirection(self):
        self.manager.current = "forgot_my_password_screen"


class SignUpScreen(Screen):
    def add_user(self, uname, pword):
        if uname != "" and pword != "":
            with open("users.json") as file:
                users = json.load(file)
            
            users[uname] = {
                "username": uname,
                "password": pword,
                "created": datetime.now().strftime("%Y-%m-%d %H-%M-%S")
            }

            with open("users.json", 'w') as file:
                json.dump(users, file)

            self.manager.current = "sign_up_screen_success"


class SignUpScreenSuccess(Screen):
    def switch_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"


class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"
    
    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob("*.txt")
        available_feelings = [Path(filename).stem for filename in available_feelings]
        if feel in available_feelings:
            with open(f"{feel}.txt", encoding="utf8") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling"


class ForgottenPWScreen(Screen):
    def pw_recovery(self, un):
        with open("users.json") as file:
            users = json.load(file)
            if un in users:
                key = users[un]["password"]
                self.ids.password1.text = f"Your password is {key}"
            else:
                self.ids.password1.text = "You need to sign up first!"
    
    def redirect(self, un):
        with open("users.json") as file:
            users = json.load(file)
            if un in users:
                self.manager.transition.direction = 'right'
                self.manager.current = "login_screen"
            else:
                self.manager.current = "sign_up_screen"


class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
