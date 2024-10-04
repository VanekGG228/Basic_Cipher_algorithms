from tkinter import *
from tkinter import messagebox as mb
from proc import *
from Vijener import *
from Railway import *


class MyRadioButton(Radiobutton):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.configure(font=("Arial", 12))

def encrypt(s:str,key:str,func1,func2):
    if selected_cipher.get()=="1":
        new_key=''
        for i in key:
            if i>='0' and i<='9':
                new_key+=i
        if not new_key:
            mb.showerror(title='KEY PROBLEM',message='The Key is empty') 
            return "0"
        new_key=int(new_key)   
        result =func1(s,new_key)
    else:
        new_key=''
        for i in key:
            if is_russian_letter(i):
                new_key+=i

        if not new_key:
            mb.showerror(title='KEY PROBLEM',message='The Key is empty')
            return "0"        
        new_key = progress_key(new_key, len(s))
        result = func2(s,new_key) 
    return result

def get_text():
    text = text_widget.get("1.0", "end-1c")  
    return text

def handle_text()->int:
    clear_text(text_widget_shifr)

    result = word_processing(get_text())
    key =key_entry.get()
    
    code = encrypt(result,key,Railway,Vijener)
    if code=="0":
        return 1

    text_widget_shifr.config(state=NORMAL)
    text_widget_shifr.insert("end",code)
    text_widget_shifr.config(state=DISABLED)
    return 0



def deciph_text()->int:
    clear_text(text_widget_shifr)

    result = word_processing(get_text())
    key =key_entry.get()
    
    code = encrypt(result,key,decipher,decipher_Vijener)
    if code=="0":
        return 1
    
    text_widget_shifr.config(state=NORMAL)
    text_widget_shifr.insert("end",code)
    text_widget_shifr.config(state=DISABLED)
    return 0



def clear_text(widget):
    widget.config(state=NORMAL)
    widget.delete(1.0,'end')
    widget.config(state=DISABLED)



def open_text():
    filetypes = (('text files','*.txt'),('All files','*.*'))
  
    error= FALSE
    file_path = filedialog.askopenfilename(filetypes=filetypes)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
            if len(file_content) == 0:
                mb.showerror(title="Error", message="File is NULL")
    except:
      
        error = TRUE
    if not error:
        text_widget.delete(1.0,'end')
        text_widget.insert(1.0, file_content)


def save_to_file(data):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w",encoding="utf-8") as file:
            file.write(data)
            print("Data saved to", file_path)

def save():
    save_to_file(text_widget_shifr.get("1.0", "end-1c"))

root = Tk()

root.title('Kryptography')
root.geometry("700x700+450+0")


f_entry =Frame(root,borderwidth=1, relief=SOLID, padx=10,pady=10)
f_entry.pack()
key_label = Label(f_entry,text = 'Enter key',font=('Arial',13))
key_label.pack(anchor=NW)


key_entry = Entry(f_entry,width=50)
key_entry.pack(anchor=NW)


f_temp=Frame(f_entry,pady=5)
f_temp.pack(anchor=NW)



text_widget = Text(root, height=10, width=50,font=('Arial',15))
text_widget.pack()

shifr='Railway'

selected_cipher =StringVar(value="1")

railway_btn = MyRadioButton(text='Railway', value="1", variable=selected_cipher)
railway_btn.pack()
  
vijener_btn = MyRadioButton(text='Vijener(progeressive key)', value="2", variable=selected_cipher )
vijener_btn.pack()


f_top =Frame(root,pady=10)
f_top.pack()


f_widgets =Frame(root,pady=10)
f_widgets.pack()

f_widget1 =Frame(f_widgets,pady=10)
f_widget1.pack()


label1= Label(f_widget1,text ="Cipher",font=(15))
label1.pack()

text_widget_shifr = Text(f_widget1, height=10, width=50,font=('Arial',15))
text_widget_shifr.pack()
text_widget_shifr.config(state=DISABLED)



get_text_button = Button(f_top, text="Get cipher", command=handle_text,font=('Arial',13))
get_text_button.pack(side = LEFT)


decipher_button = Button(f_top, text="Decipher", command=deciph_text,font=('Arial',13))
decipher_button.pack(side = LEFT)

save_cipher_button = Button(f_top, text="Save cipher", command=save,font=('Arial',13))
save_cipher_button.pack(side = LEFT)


open_button = Button(f_top, text="Open file", command=open_text,font=('Arial',13))
open_button.pack()


root.mainloop()
