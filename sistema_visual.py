from tkinter import *
from tkinter import ttk
from sistema_criptografia import *
from tkinter import messagebox

# Screen Setup
root = Tk()
root.title("Encryption System")
root.geometry("490x560+610+153")
root.iconbitmap(default='./icon.ico')
root.resizable(width=1, height=1)

def homeScreen():
    def encryption_window():
        encryption_button.destroy()
        decryption_button.destroy()
        background.destroy()

        # Functions
        def get_input():
            output_text.config(text="Encrypted text:  " + encryption(input_label.get(1.0, "end-1c")))

        # Texts
        input_text = Label(text="Enter the text to be encrypted:  ", font=('bold'))
        output_text = Label(root, text="", font=('Calibri 15'))

        # Entry Box
        input_label = Text(root, width=50, height=20, bg="light yellow", )

        # Buttons
        output_button = ttk.Button(root, text="Encrypt", command=get_input)

        # Output screen
        input_text.pack()
        input_label.pack()
        output_button.pack()
        output_text.pack()

        # Function back
        def back_homeScreen_tab01():
            back01_button.destroy()
            input_text.destroy()
            input_label.destroy()
            output_button.destroy()
            output_text.destroy()
            homeScreen()

        # Button back
        back01_button = Button(root, text='Back',command=back_homeScreen_tab01)
        back01_button.place(width=50, height=30, x=220, y=495)

    def decryption_window():
        encryption_button.destroy()
        decryption_button.destroy()
        background.destroy()

        # Entry Box
        input_label = Text(root, width=50, height=20, bg="light blue", )

        # Functions
        def get_input():
            output_text.config(text="Decrypted text:  " + decryption(input_label.get(1.0, "end-1c")))

        # Texts
        input_text = Label(text="Enter the text to be decrypted:  ", font=('bold'))
        output_text = Label(root, text="", font=('Calibri 15'))

        # Buttons
        output_button = ttk.Button(root, text="Decrypt", command=get_input)

        # Output screen
        input_text.pack()
        input_label.pack()
        output_button.pack()
        output_text.pack()

        def back_homeScreen_tab02():
            decryption_button.destroy()
            back02_button.destroy()
            input_text.destroy()
            input_label.destroy()
            output_button.destroy()
            output_text.destroy()
            homeScreen()

        back02_button = Button(root, text='Back', command=back_homeScreen_tab02)
        back02_button.place(width=50, height=30, x=220, y=495)

    # Background
    background = Label(root)
    background.la = PhotoImage(file='./background.png')
    background['image'] = background.la
    background.place(x=-2,y=0)

    #Buttons
    encryption_button = Button(root, bd=20, text="Encrypt", font=('bold'), command=encryption_window)
    encryption_button.place(width=250, height=100, x=125, y=180)

    decryption_button = Button(root, bd=20, text="Decrypt", font=('bold'), command=decryption_window)
    decryption_button.place(width=250, height=100, x=125, y=360)


homeScreen()
root.mainloop()