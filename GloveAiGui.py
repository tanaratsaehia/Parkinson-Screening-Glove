from tkinter import *
from tkinter.filedialog import *
from tkinter import ttk
from datetime import datetime
from csv import writer
from sklearn import svm
import requests
import serial
import pickle

token = 'GVYOEFv4QXiAD65Z1gVbrnosIdqEIzZfdG4b62pe7AN'

root = Tk()
root.title("Parkinson screening glove")
root.geometry("1000x820+550+100")

my_text = Text(root, width=65, height=20, font=("arel", 18), borderwidth=5)
my_text.pack(pady=20)

global count_loop
global savepath
global parCount
global count1
start_count = 0
count1 = 0
parCount = 0
savepath = ""
count_loop = 0
stop = 0
####serial-code############################
def serial_port():
    global choice_port_l
    global choice_port_r
    global choice_hands
    global hand_port
    hand_port = ""
    hand = choice_hands.get()
    right = str(choice_port_r.get())
    left = str(choice_port_l.get())
    if(hand == "Right"):
        #hand_port = str(right)
        return str(right)
    if(hand == "Left"):
        hand_port = str(left)
        return str(left)

def serial_port_write():
    global choice_hands_write
    global hand_port_write
    global choice_port_l
    global choice_port_r
    hand_port_write = None
    hand = choice_hands_write.get()
    right = str(choice_port_r.get())
    left = str(choice_port_l.get())
    if(hand == "Right"):
        hand_port_write = right
    if(hand == "Left"):
        hand_port_write = left
####serial-code#############################
def startLoop():
    global count_loop
    global listX
    global hand_port
    global running
    global count1
    if (count_loop == 0):
        global ser
        
        ser = serial.Serial(serial_port(), 115200)
    if(count1 >= 200):
        global running
        print(serial_port())
        if (running):
            global listX
            global my_text
            global timeNow
            global modeltrained
            global parCount
            now = datetime.now()
            timeNow = now.strftime("%d/%m/%Y %H:%M:%S")
            print(running)
            x = ser.readline()
            
            #strX = x.encode("UTF-8")
            a = x.strip()
            b = str(a)
            b = b.replace("b","")
            b = b.replace("'","")
            listX = b.split('_')
            x = ser.readline()
            #strX = x.encode("UTF-8")
            a = x.strip()
            b = str(a)
            b = b.replace("b","")
            b = b.replace("'","")
            listX = b.split('_')
            
            x1 = float(listX[0])
            y1 = float(listX[1])
            z1 = float(listX[2])
            x2 = float(listX[3])
            y2 = float(listX[4])
            z2 = float(listX[5])
            
            realData = [x1, y1, z1, x2, y2, z2]
            answer = modeltrained.predict([realData])
            
            answerStr = answer[0]
            my_text.insert(END, timeNow)
            my_text.insert(END, "  :  ")
            my_text.insert(END, listX)
            my_text.insert(END, "   ")
            my_text.insert(END, answerStr)
            my_text.insert(END, "\n")
            my_text.see(END)
            
            if answer[0] == 'par':
                global parCount
                parCount += 1
    if (count1 >= 740):
        if(parCount >= 90):
            a = ValueNoti.get()
            if(ValueNoti.get() == 1):
                DayNow = now.strftime("%d/%m/%Y")
                TimeNow = now.strftime("%H:%M:%S")
                State = "PerkinsonDetected!"
                payload = {'message' : f'\nวันที่ {DayNow} เวลา {TimeNow}\nผลการตรวจคือ : {State}','notificationDisabled' : False}
                requests.post('https://notify-api.line.me/api/notify', headers={'Authorization' : 'Bearer {}'.format(token)}, params = payload)
            my_text.insert(END, "\n")
            my_text.insert(END, "----------------->parkinson is detected")
            my_text.insert(END, "\n")
            my_text.see(END)
            del ser
        else:
            a = ValueNoti.get()
            if(ValueNoti.get() == 1):
                DayNow = now.strftime("%d/%m/%Y")
                TimeNow = now.strftime("%H:%M:%S")
                State = "you are normal"
                payload = {'message' : f'\nวันที่ {DayNow} เวลา {TimeNow}\nผลการตรวจคือ : {State}','notificationDisabled' : False}
                requests.post('https://notify-api.line.me/api/notify', headers={'Authorization' : 'Bearer {}'.format(token)}, params = payload)
            my_text.insert(END, "\n")
            my_text.insert(END, "----------------->you are normal")
            my_text.insert(END, "\n")
            my_text.see(END)
            del ser
        running = False
        del ser
        my_text.see(END)
    count1 += 1
    count_loop += 1
    print(count1)
    root.after(10, startLoop)

def on_stop():
    global running
    global ser
    global listX
    listX = None
    running = False
    del ser

def on_start():
    global running
    global count_loop
    global count1
    global parCount
    parCount = 0
    count1 = 0
    count_loop = 0
    running = True
    model()
    serial_port()
    startLoop()

def clear():
    my_text.delete(1.0, END)

def loadmodel():  
    global linearModel_r
    global polyModel_r
    global rbfModel_r
    global linearModel_l
    global polyModel_l
    global rbfModel_l
    folderpath = str(askdirectory())
    print(folderpath)
    
    loaded_model_linear_r = pickle.load(open(f'{folderpath}/finalized_model_linear_right.sav', 'rb'))
    loaded_model_poly_r = pickle.load(open(f'{folderpath}/finalized_model_poly_right.sav', 'rb'))
    loaded_model_rbf_r = pickle.load(open(f'{folderpath}/finalized_model_rbf_right.sav', 'rb'))
    loaded_model_linear_l = pickle.load(open(f'{folderpath}/finalized_model_linear_left.sav', 'rb'))
    loaded_model_poly_l = pickle.load(open(f'{folderpath}/finalized_model_poly_left.sav', 'rb'))
    loaded_model_rbf_l = pickle.load(open(f'{folderpath}/finalized_model_rbf_left.sav', 'rb'))
    #I:\My Drive\GloveAi\finalized_model_linear_left.sav
    linearModel_r = loaded_model_linear_r
    polyModel_r  = loaded_model_poly_r
    rbfModel_r = loaded_model_rbf_r
    linearModel_l = loaded_model_linear_l
    polyModel_l = loaded_model_poly_l
    rbfModel_l = loaded_model_rbf_l
    
    my_text.insert(END, "\n")
    my_text.insert(END, "Model loaded from : ")
    my_text.insert(END, f"{folderpath}")
    my_text.insert(END, "\n")
    my_text.see(END)

def model():
    global modeltrained
    global choice_hands
    global choice_kernel
    global linearModel_r
    global polyModel_r
    global rbfModel_r
    global linearModel_l
    global polyModel_l
    global rbfModel_l
    kernel = choice_kernel.get()
    hand = choice_hands.get()
    #"Linear", "Poly", "RBF"
    if(hand == "Right"):
        if(kernel == "Linear"):
            modeltrained = linearModel_r
        if(kernel == "Poly"):
            modeltrained = polyModel_r
        if(kernel == "RBF"):
            modeltrained = rbfModel_r
    if(hand == "Left"):
        if(kernel == "Linear"):
            modeltrained = linearModel_l
        if(kernel == "Poly"):
            modeltrained = polyModel_l
        if(kernel == "RBF"):
            modeltrained = rbfModel_l

def window_setting():
    global folderpath
    window_setting = Tk()
    window_setting.title("Setting path file")
    window_setting.geometry("300x250")
    Label(window_setting, text="Folder path model Ai", font=("arel", 14)).grid(row=0, columnspan=2, padx=10, pady=10, sticky=W)
    Label(window_setting, text="Path : ", font=("arel", 10)).grid(row=1, padx=20, sticky=W)
    Label(window_setting, text=folderpath, font=("arel", 10)).grid(row=1, column=0, columnspan=3, padx=63, sticky=W)
    window_setting.mainloop()
#Help_toolbar
def how_to_use():
    how_to_use = Tk()
    how_to_use.title("How to use")
    how_to_use.geometry("300x250")
    Label(how_to_use, text="please read this link in you browser", font=("arel", 10)).grid(row=1, padx=20, sticky=W)
    #Label(how_to_use, text=fileopen_r, font=("arel", 10)).grid(row=1, column=0, columnspan=3, padx=63, sticky=W)
    Label(how_to_use, text="Left : ", font=("arel", 10)).grid(row=2, padx=20, sticky=W)
    #Label(how_to_use, text=fileopen_l, font=("arel", 10)).grid(row=2, column=0, columnspan=3, padx=55, sticky=W)
    how_to_use.mainloop()
def abuot_toolbar():
    global fileopen_r
    global fileopen_l
    abuot_toolbar = Tk()
    abuot_toolbar.title("Setting path file")
    abuot_toolbar.geometry("300x250")
    Label(window_setting, text="CSV path to train Ai", font=("arel", 14)).grid(row=0, columnspan=2, padx=10, pady=10, sticky=W)
    Label(window_setting, text="Right : ", font=("arel", 10)).grid(row=1, padx=20, sticky=W)
    Label(window_setting, text=fileopen_r, font=("arel", 10)).grid(row=1, column=0, columnspan=3, padx=63, sticky=W)
    Label(window_setting, text="Left : ", font=("arel", 10)).grid(row=2, padx=20, sticky=W)
    Label(window_setting, text=fileopen_l, font=("arel", 10)).grid(row=2, column=0, columnspan=3, padx=55, sticky=W)
    abuot_toolbar.mainloop()
####Command################################################
def new_window():
    pass

def start_write():
    global running_write
    global count_loop_write
    global choice_hands_write
    global choice_state
    global hand
    global state
    global start_count
    hand = choice_hands_write.get()
    state = choice_state.get()
    running_write = True
    count_loop_write = 0
    start_count += 1
    serial_port_write()
    startloop_write()

def stop_write():
    global running_write
    global ser
    global listX
    global count_loop_write
    count_loop_write = 0
    listX = None
    running_write = False
    del ser
    print(ser)

def reset_write():
    stop_write()
    stop_write()

def clear_write():
    my_text_write.delete(1.0, END)

def startloop_write():
    global count_loop_write
    global hand
    global state
    global hand_port_write
    
    if (count_loop_write == 0):
        global ser
        ser = serial.Serial(hand_port_write, 9600)
    if(count_loop_write >= 60):
        if (running_write):
            global listX
            global my_text_write
            global write_win
            global savepath
            now = datetime.now()
            timeNow = now.strftime("%d/%m/%Y %H:%M:%S")
            x = ser.readline()
            #strX = x.encode("UTF-8")
            a = x.strip()
            b = str(a)
            b = b.replace("b","")
            b = b.replace("'","")
            listX = b.split('_')
            x = ser.readline()
            #strX = x.encode("UTF-8")
            a = x.strip()
            b = str(a)
            b = b.replace("b","")
            b = b.replace("'","")
            listX = b.split('_') 
            x1 = float(listX[0])
            y1 = float(listX[1])
            z1 = float(listX[2])
            x2 = float(listX[3])
            y2 = float(listX[4])
            z2 = float(listX[5])
            gloveData = []
            gloveData.append(x1)
            gloveData.append(y1)
            gloveData.append(z1)
            gloveData.append(x2)
            gloveData.append(y2)
            gloveData.append(z2)
            gloveData.append(hand)
            gloveData.append(state)
            with open(savepath, 'a', newline='') as f_object:
                writer_ojbect = writer(f_object)
                writer_ojbect.writerow(gloveData)
                f_object.close()
            my_text_write.insert(END, timeNow.time())
            my_text_write.insert(END, "  :  ")
            my_text_write.insert(END, listX)
            my_text_write.insert(END, "   ")
            my_text_write.insert(END, hand)
            my_text_write.insert(END, "   ")
            my_text_write.insert(END, state)
            my_text_write.insert(END, "\n")
    count_loop_write += 1
    print(count_loop_write)
    my_text_write.see(END)
    write_win.after(12, startloop_write)

def writewin():
    global timeNow
    global listX
    global count_loop_write
    global my_text_write
    global savepath
    global write_win
    global choice_state
    global choice_hands_write
    savepath = askopenfilename()
    timeNow = datetime.now()
    write_win = Toplevel()
    write_win.title("Write data to csv file")
    write_win.geometry("900x800")
    
    my_text_write = Text(write_win, width=65, height=20, font=("arel", 16), borderwidth=5)
    my_text_write.pack(pady=20)
    
    label_frame = Frame(write_win)
    label_frame.pack()
    Label(label_frame, text=f"              Save to : {savepath}", font=("arel", 16)).grid(row=0, column=0)
    print(savepath)
    
    Label(label_frame, text="Hands", font=("arel", 12)).grid(row=1, column=0, sticky=W, pady=10)
    global choice_hands_write
    choice_hands_write = StringVar(value="Chose hands")
    combo_hands = ttk.Combobox(label_frame, textvariable=choice_hands_write)
    combo_hands["values"] = ("Right", "Left")
    combo_hands.grid(row=2, column=0, sticky=W )

    Label(label_frame, text="Parkinson state", font=("arel", 12)).grid(row=1, column=1, padx=4, sticky=W)
    choice_state = StringVar(value="Chose state")
    combo_state = ttk.Combobox(label_frame, textvariable=choice_state)
    combo_state["values"] = ("par", "normal")
    combo_state.grid(row=2, column=1, padx=5, sticky=W )
    
    button_frame = Frame(write_win)
    button_frame.pack()
    btn = Button(button_frame, text="Write", font=30, command=start_write)
    btn.grid(row=0, column=0, pady=25)
    btn2 = Button(button_frame, text="Stop", font=30, command=stop_write)
    btn2.grid(row=0, column=1, padx=50)
    btn3 = Button(button_frame, text="Clear", font=30, command=clear_write)
    btn3.grid(row=0, column=2)
    btn4 = Button(button_frame, text="Reset", font=30, command=reset_write)
    btn4.grid(row=1, column=1)

def reset():
    on_stop()
    on_stop()

####Command################################################
menu_root = Menu()
root.config(menu=menu_root)

menuitem_file = Menu()
menuitem_file.add_command(label="New window", command=new_window)
menuitem_file.add_command(label="Load model", command=loadmodel)
menuitem_file.add_command(label="Write data", command=writewin)
#menuitem_file.add_command(label="Train Ai left hand", command=chosefile_l)
menuitem_file.add_command(label="Show setting", command=window_setting)

menuitem_help = Menu()
menuitem_help.add_command(label="How to use program" ,command=how_to_use)
menuitem_help.add_command(label="About")

menu_root.add_cascade(label="File", menu=menuitem_file)
menu_root.add_cascade(label="Help", menu=menuitem_help)

label_frame = Frame(root)
label_frame.pack()

Label(label_frame, text="Serial ports", font=("arel", 18)).grid(row=0, columnspan=2, sticky=W)

Label(label_frame, text="Right", font=("arel", 12)).grid(row=1, column=0, sticky=W)
choice_port_r = StringVar(value="Chose port")
combo_r = ttk.Combobox(label_frame, textvariable=choice_port_r, width=10)
combo_r["values"] = ("COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "COM10", "COM11", "COM12", "COM13", "COM14", "COM15", "COM16", "COM17", "COM18", "COM19", "COM20")
combo_r.grid(row=2, column=0 )

Label(label_frame, text="Left", font=("arel", 12)).grid(row=1, column=1, sticky=W, padx=4)
choice_port_l = StringVar(value="Chose port")
combo_l = ttk.Combobox(label_frame, textvariable=choice_port_l, width=10)
combo_l["values"] = ("COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "COM10", "COM11", "COM12", "COM13", "COM14", "COM15", "COM16", "COM17", "COM18", "COM19", "COM20")
combo_l.grid(row=2, column=1, padx=5 )

Label(label_frame, text="Hands", font=("arel", 18)).grid(row=0, column=2, padx=30, sticky=W)
choice_hands = StringVar(value="Chose Hands")
combo_hands = ttk.Combobox(label_frame, textvariable=choice_hands, width=10)
combo_hands["values"] = ("Right", "Left")
combo_hands.grid(row=1, column=2, padx=32, pady=5)

Label(label_frame, text="Kernel", font=("arel", 18)).grid(row=0, column=3, sticky=W)
choice_kernel = StringVar(value="Chose kernel")
combo_kernel = ttk.Combobox(label_frame, textvariable=choice_kernel)
combo_kernel["values"] = ("Linear", "Poly", "RBF")
combo_kernel.grid(row=1, column=3, padx=1)

ValueNoti = IntVar()
CheckBtnNoti = Checkbutton(label_frame, text="LineNotify", font=28, padx=15, variable=ValueNoti, onvalue=1, offvalue=0)
CheckBtnNoti.grid(row=1, column=4, padx=1)

button_frame = Frame(root)
button_frame.pack()

btn = Button(button_frame, text="Start", font=30, command=on_start)
btn.grid(row=0, column=0, pady=25)

btn2 = Button(button_frame, text="Stop", font=30, command=on_stop)
btn2.grid(row=0, column=1, padx=50)

btn3 = Button(button_frame, text="Clear", font=30, command=clear)
btn3.grid(row=0, column=2)

btn4 = Button(button_frame, text="Reset", font=30, command=reset)
btn4.grid(row=1, column=1)

root.mainloop()


#pyinstaller GloveAiGui.py --onefile --windowed 
