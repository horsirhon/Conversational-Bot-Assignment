import os
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import main
import subprocess
import util


class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("550x280")

        self.login_button_main_window = util.get_button(self.main_window, 'login', 'green', self.login)
        self.login_button_main_window.place(x=360, y=20)

        self.register_new_user_button_main_window = util.get_button(self.main_window, 'register new user', 'gray',
                                                                    self.register_new_user, fg='black')
        self.register_new_user_button_main_window.place(x=360, y=100)

        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=20, y=20, width=320, height=240)

        self.add_webcam(self.webcam_label)

        self.db_dir = './db'
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)

        self.log_path = './log.txt'
        self.html_open = False

    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)
        self.label = label
        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()
        frame = cv2.resize(frame, (320, 240))
        self.most_recent_capture_arr = frame
        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
        self.most_recent_capture_pil = Image.fromarray(img_)
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        self.label.imgtk = imgtk
        self.label.configure(image=imgtk)

        self.label.after(20, self.process_webcam)

    def login(self):
        unknown_log_path = './tmp.jpg'
        cv2.imwrite(unknown_log_path, self.most_recent_capture_arr)

        output = str(subprocess.check_output(['face_recognition', self.db_dir, unknown_log_path]))
        name = output.split(',')[1][:-5]
        print(name)
        user_known = name not in ['unknown_person',  'no_persons_found' ]
        
        if user_known:
            if not self.html_open:
                print("Hello Osahon, How can i help you today?")
                main.text_to_speech("Hello Osahon, How can i help you today?")
                main.generate_responses()
                self.html_open = True
        else:
            if self.html_open:
                self.html_open = False
        os.remove(unknown_log_path)

    def register_new_user(self):
        self.register_new_user_window = tk.Toplevel(self.main_window)
        self.register_new_user_window.geometry("550x280")

        self.accept_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Accept', 'green', self.accept_register_new_user)
        self.accept_button_register_new_user_window.place(x=360, y=20)

        self.try_again_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Try again', 'red', self.try_again_register_new_user)
        self.try_again_button_register_new_user_window.place(x=360, y=100)

        self.capture_label = util.get_img_label(self.register_new_user_window)
        self.capture_label.place(x=10, y=0, width=320, height=240)


        self.add_img_to_label(self.capture_label)

        self.entry_text_register_new_user = util.get_entry_text(self.register_new_user_window)
        self.entry_text_register_new_user.place(x=750, y=150)

        self.text_label_register_new_user = util.get_text_label(self.register_new_user_window, 'Please, \ninput username:')
        self.text_label_register_new_user.place(x=750, y=70)

    def try_again_register_new_user(self):
        self.register_new_user_window.destroy()

    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)
        self.register_new_user_capture = self.most_recent_capture_arr.copy()


    def start(self):
        self.main_window.mainloop()

    def accept_register_new_user(self):
        name = self.entry_text_register_new_user.get(1.0, "end-1c")
        cv2.imwrite(os.path.join(self.db_dir, '{}.jpg'.format(name)), self.register_new_user_capture)

        util.msg_box('Success!', 'User was registered successfully!')

        self.register_new_user_window.destroy()


if __name__ == "__main__":
    app = App()
    app.start()
