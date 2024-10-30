from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import threading
from selenium.webdriver.common.keys import Keys
import emoji
import os
import requests
import base64
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.service import Service
from PIL import Image
import io
import colorama
colorama.init()


def success_color(string):
    return colorama.Fore.GREEN + string + colorama.Style.RESET_ALL
def error_color(string):
    return colorama.Fore.RED + string + colorama.Style.RESET_ALL
def system_color(string):
    return colorama.Fore.YELLOW + string + colorama.Style.RESET_ALL

def waiting_ui(timeout=5, content=""):
    for i in range(timeout):
        print(
            colorama.Fore.YELLOW + f"\r[{i+1}]" + colorama.Style.RESET_ALL,
            end = colorama.Fore.YELLOW + " -> " + colorama.Style.RESET_ALL
        )
        print(
            colorama.Fore.BLUE + f"{content}" + colorama.Style.RESET_ALL,
            end=""
        )
        time.sleep(1)
    print()


try:
    edge_chromium_path = EdgeChromiumDriverManager().install()
    print(system_color("your edge driver path"))
    print(success_color(f"-> {edge_chromium_path}"))
except:
    input(error_color("đã có lỗi khi cài edge drive vui lòng kiểm tra lại, enter để đóng\n-> "))


print(system_color(" -----------------------------"))
print(system_color("| MODULES CREATED BY PHUTECH  |"))
print(system_color("| facebook -> Programing sama |"))
print(system_color("| github -> @phucoding286     |"))
print(system_color("| youtube -> Phu Tech         |"))
print(system_color(" -----------------------------"))



class LoginCreateSession:
    def __init__(self, email_or_phone, password, group_or_chat):
        options = webdriver.ChromeOptions()
        
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--log-level=3")
        options.add_argument("--headless=old")

        self.browser = webdriver.Chrome(
            options=options,
            keep_alive=True
        )

        self.email_or_phone = email_or_phone
        self.password = password
        self.group_or_chat = group_or_chat

        self.get_to_mes()
        self.login()
        self.check_verify()
        self.pass_notify()
        self.to_group_or_chat()

    def get_to_mes(self):
        self.browser.get("https://www.messenger.com/login/")
    
    def login(self):
        time.sleep(1)
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
                (By.ID, "email")
            )).send_keys(self.email_or_phone)
        except:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
                (By.ID, "email")
            )).send_keys(self.email_or_phone)
        time.sleep(0.2)
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
                (By.ID, "pass")
            )).send_keys(self.password)
        except:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
                (By.ID, "pass")
            )).send_keys(self.password)
        time.sleep(0.2)
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
                (By.ID, "loginbutton")
            )).click()
        except:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
                (By.ID, "loginbutton")
            )).click()

    def check_verify(self):
        waiting_ui(5, "please wait for 5 seconds")
        input(system_color("[!] please verify access (if have) for continue\n-> "))
        self.browser.get("https://www.messenger.com/login/")
        print(system_color("[!] finding any requests for verify..."))
        try:
            try:
                continue_with_acc = WebDriverWait(self.browser, 2.5).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//span[contains(@class, '_2hyt')]")
                    )
                )
            except:
                continue_with_acc = WebDriverWait(self.browser, 2.5).until(
                    EC.presence_of_element_located(
                        (By.XPATH, "//span[contains(@class, '_2hyt')]")
                    )
                )
            try:
                continue_with_acc.click()
            except:
                continue_with_acc.click()
            print(success_color("[*] verified and continue going..."))
        except Exception as e:
            print(success_color("[*] dont have any requests for verify, continue going..."))

    def pass_notify(self):
        print(system_color("[!] finding any requests for sync messages..."))
        try:
            try:
                x1 = WebDriverWait(self.browser, 2.5).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Đóng']")))
            except:
                x1 = WebDriverWait(self.browser, 2.5).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Đóng']")))
            try:
                x1.click()
            except:
                x1.click()
            try:
                x2 = WebDriverWait(self.browser, 2.5).until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'x1lliihq') and text()='Không đồng bộ']")))
            except:
                x2 = WebDriverWait(self.browser, 2.5).until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'x1lliihq') and text()='Không đồng bộ']")))
            try:
                x2.click()
            except:
                x2.click()
            print(success_color("[*] synced messages !"))
        except Exception as e:
            print(success_color("[*] dont haven't any requests for sync messages!"))


    def to_group_or_chat(self):
        print(system_color("[*] going to chat box..."))
        self.browser.get(self.group_or_chat)





class Listener(LoginCreateSession):
    def __init__(self, email_or_phone, password, group_or_chat):
        super().__init__(email_or_phone, password, group_or_chat)

        self.his_inp = ""
        self.current_inp = ""
        self.his_img_value = ""
        self.current_img_value = ""
        self.current_image = None
        self.waiting = True
        self.username = None
        self.sending_img = False
        
        threading.Thread(target=self.listening).start()
        self.waiting_setting_up()

    
    def remove_emoji(self, text):
        return emoji.replace_emoji(text, replace="")
    
    
    def first_input_message_init(self):
        print(system_color("[!] initing messages and images input..."))
        try:
            try:
                message = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '(//div[@class="html-div xexx8yu x4uap5 x18d9i69 xkhd6sd x1gslohp x11i5rnm x12nagc x1mh8g0r x1yc453h x126k92a x18lvrbx"])[last()]')))
            except:
                message = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '(//div[@class="html-div xexx8yu x4uap5 x18d9i69 xkhd6sd x1gslohp x11i5rnm x12nagc x1mh8g0r x1yc453h x126k92a x18lvrbx"])[last()]')))
            message = message.text

            self.his_inp = message
            self.current_inp = message
            
            print(system_color("[!] finding image..."))
            img = None
            try:
                try:
                    img = WebDriverWait(self.browser, 2).until(EC.presence_of_all_elements_located((By.XPATH, "//img[@alt='Open photo' and contains(@class, 'xz74otr xmz0i5r x193iq5w')]")))
                except:
                    img = WebDriverWait(self.browser, 2).until(EC.presence_of_all_elements_located((By.XPATH, "//img[@alt='Mở ảnh' and contains(@class, 'xz74otr xmz0i5r x193iq5w')]")))
                print(success_color("[*] founded an image!"))
            except Exception as e:
                print(error_color("[!] error when find image from box"))

            self.his_img_value = str(img)[-100:]
            self.current_img_value = str(img)[-100:]
        except Exception as e: 
            print(error_color("[!] error when init messages and images input"))
    

    def check_new_message(self):
        try:
            message = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '(//div[@class="html-div xexx8yu x4uap5 x18d9i69 xkhd6sd x1gslohp x11i5rnm x12nagc x1mh8g0r x1yc453h x126k92a x18lvrbx"])[last()]')))
        except:
            message = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '(//div[@class="html-div xexx8yu x4uap5 x18d9i69 xkhd6sd x1gslohp x11i5rnm x12nagc x1mh8g0r x1yc453h x126k92a x18lvrbx"])[last()]')))
        message = message.text

        if message == self.his_inp:
            pass
        else:
            print(system_color('[!] finding username...'))
            username = None
            try:
                try:
                    username = WebDriverWait(self.browser, 2.5).until(EC.presence_of_all_elements_located((By.XPATH, "//span[contains(@class, 'html-span') and contains(@class, 'xdj266r') and contains(@class, 'x11i5rnm') and contains(@class, 'xat24cr') and contains(@class, 'x1mh8g0r') and contains(@class, 'xexx8yu') and contains(@class, 'x4uap5') and contains(@class, 'x18d9i69') and contains(@class, 'xkhd6sd') and contains(@class, 'x1hl2dhg') and contains(@class, 'x16tdsg8') and contains(@class, 'x1vvkbs')]")))
                except:
                    username = WebDriverWait(self.browser, 2.5).until(EC.presence_of_all_elements_located((By.XPATH, "//span[contains(@class, 'html-span') and contains(@class, 'xdj266r') and contains(@class, 'x11i5rnm') and contains(@class, 'xat24cr') and contains(@class, 'x1mh8g0r') and contains(@class, 'xexx8yu') and contains(@class, 'x4uap5') and contains(@class, 'x18d9i69') and contains(@class, 'xkhd6sd') and contains(@class, 'x1hl2dhg') and contains(@class, 'x16tdsg8') and contains(@class, 'x1vvkbs')]")))
            except Exception as e:
                print(error_color("[!] error when find username"))
            if username is not None:
                print(success_color(f"[*] found username -> {username[-1].text}"))
                self.username = username[-1].text
            self.current_inp = message

    
    def check_new_image(self):
        print(system_color("[!] finding image..."))
        img = None
        try:
            try: 
                img = WebDriverWait(self.browser, 2).until(EC.presence_of_all_elements_located((By.XPATH, "//img[@alt='Open photo' and contains(@class, 'xz74otr xmz0i5r x193iq5w')]")))
            except: 
                img = WebDriverWait(self.browser, 2).until(EC.presence_of_all_elements_located((By.XPATH, "//img[@alt='Mở ảnh' and contains(@class, 'xz74otr xmz0i5r x193iq5w')]")))
            print(success_color("[*] founded an image!"))
        except Exception as e:
            print(error_color("[!] error when finding image!"))

        if img is not None:
            try:
                img = img[-1].get_attribute("src")
            except:
                img = img[-1].get_attribute("src")
                    
            if img[:4] == "http":
                img = requests.get(img).content
            else:
                img = base64.b64decode(img[23:])
            if str(img)[-100:] == self.his_img_value:
                pass
            else:
                if self.sending_img:
                    self.current_img_value = str(img)[-100:]
                    self.his_img_value = str(img)[-100:]
                    self.sending_img = False
                else:
                    self.current_image = img
                    self.current_img_value = str(img)[-100:]



    def listening(self):
        print(system_color('[#] listening ...'))
        self.first_input_message_init()
        while True:
            try:
                time.sleep(0.5)
                self.check_new_message()
                self.check_new_image()

                if self.waiting:
                    self.waiting = False

            except Exception as e:
                print(error_color("[!] dont have'nt any message (or error)"))
                continue


    def waiting_setting_up(self):
        time.sleep(1)
        print(system_color('[!] waiting for complete setting up...'))
        while not self.waiting:
            pass
        print(success_color("[*] successed setting up!"))
    



class Sender(Listener):
    def __init__(self, email_or_phone, password, group_or_chat):
        super().__init__(email_or_phone, password, group_or_chat)

    def send_message(self, inp=None, inp_down_line=None):
        try:
            try:
                send_msg = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//p[@class='xat24cr xdj266r']")))
            except:
                send_msg = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//p[@class='xat24cr xdj266r']")))

            if inp is not None:
                inp = " ".join(inp.split())
                try:
                    send_msg.send_keys( self.remove_emoji(inp+" ") )
                except:
                    send_msg.send_keys( self.remove_emoji(inp+" ") )
                time.sleep(0.2)
                try:
                    send_msg.send_keys(Keys.ENTER)
                except:
                    send_msg.send_keys(Keys.ENTER)

            elif inp_down_line is not None:
                for inp in inp_down_line:
                    try:
                        send_msg.send_keys( self.remove_emoji(inp+" ") )
                    except:
                        send_msg.send_keys( self.remove_emoji(inp+" ") )
                    try:
                        send_msg.send_keys(Keys.SHIFT, Keys.ENTER)
                    except:
                        send_msg.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(0.2)
                try:
                    send_msg.send_keys(Keys.ENTER)
                except:
                    send_msg.send_keys(Keys.ENTER)

                print(success_color("[*] send message is successed!"))

        except Exception as e:
            print(error_color("[!] error when send messgae!"))
        self.his_inp = self.current_inp
    

    def send_image(self, img_path: str = "./image_model/output_image.png", message=None):
        self.sending_img = True
        try:
            upload_image = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@type="file" and contains(@class, "x1s85apg")]')))
        except:
            upload_image = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@type="file" and contains(@class, "x1s85apg")]')))
        time.sleep(0.2)
        try:
            upload_image.send_keys(os.path.abspath(img_path))
        except:
            upload_image.send_keys(os.path.abspath(img_path))
        time.sleep(0.2)
        try:
            send_msg = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//p[@class='xat24cr xdj266r']")))
        except:
            send_msg = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, "//p[@class='xat24cr xdj266r']")))
        time.sleep(0.2)
        try:
            send_msg.send_keys(" " if message == None else message)
        except:
            send_msg.send_keys(" " if message == None else message)
        time.sleep(0.2)
        try:
            send_msg.send_keys(Keys.ENTER)
        except:
            send_msg.send_keys(Keys.ENTER)





class MesChat(Sender):
    def __init__(self, email_or_phone, password, group_or_chat):
        super().__init__(email_or_phone, password, group_or_chat)
    
    def new_message_listen(self):
        if self.his_inp != self.current_inp:
            self.his_inp = self.current_inp
            return self.current_inp
        else:
            return None
    
    def new_image_listen(self, return_file=False, file_path="./meschat_img.png", return_byte=True):
        if self.current_img_value != self.his_img_value:
            self.his_img_value = self.current_img_value
            if return_file:
                img = io.BytesIO(self.current_image)
                img = Image.open(img)
                img.save(file_path)
                return "had return image file"
            elif return_byte:
                return self.current_image
        else:
            return None



if __name__ == "__main__":
    meschat = MesChat(
        email_or_phone="demo@s.com",
        password="demo",
        group_or_chat="" # link group or chat box
    )

    while True:
        new_message = meschat.new_message_listen()
        if new_message is not None:
            if new_message in ["hi", "Hi"]:
                meschat.send_message("hello, how are you?")
            elif new_message in ['send image', 'send img']:
                meschat.send_image("./test.jpg")
            else:
                meschat.send_message("what do you mean?")
            continue
        new_image = meschat.new_image_listen(return_file=True)
        if new_message is not None:
            pass
