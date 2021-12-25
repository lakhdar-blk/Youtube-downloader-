from tkinter import * 
from tkinter import ttk

from PIL import ImageTk, Image
from tkinter import filedialog
from download import download

def read_data():

    global  url_input, location_input, Listb, t

    url         = url_input.get()
    location    = location_input.get()
    typef       = Listb.get()
    
    status      = download(url, location, typef)
    t = canvas1.create_text(340, 220, text="Please wait...", fill="Black", font=('Helvetica 13 bold'), state='hidden')
    
    #if the file was downloaded successfuly then the response will be 1, 0 otherwise. 
    print(status)


def browse_button():
    
    global folder_path, location_input, canvas1
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    location_input.delete(0,END)
    location_input.insert(0, filename)
    

if __name__ == "__main__":
        
        window = Tk()

        window.title("Python-Youtube downloader ")
        window.configure(width=600, height=300)
        window.configure(bg='lightgray')
        window.eval('tk::PlaceWindow . center')
        window.resizable(False, False)

        canvas1 = Canvas(window, width=635, height=300, bg='white')
        canvas1.pack(fill = "both", expand = True)
        img = ImageTk.PhotoImage(Image.open("bg.jpg")) 
        canvas1.create_image( 0, 0, image = img, anchor = "nw")

        canvas1.create_text(100, 45, text="Video URL:", fill="Yellow", font=('Helvetica 13 bold'))
        url_input = Entry(canvas1, width=40, font=("Helvetica", 14))
        url_input.place(x=170,y=30)
        """
        typetx = Label(canvas1, text="File Type:", font=("Helvetica", 13))
        typetx.place(x=40,y=90)"""

        canvas1.create_text(90, 100, text="File type:", fill="Black", font=('Helvetica 13 bold'))
        Listb = ttk.Combobox(canvas1, 
                        values=["Audio", 
                                "Video",], font=('Helvetica 13 bold'))
        Listb.current(0)
        Listb.config(state = "readonly")
        Listb.place(x=170,y=90)

        canvas1.create_text(90, 150, text="Location:", fill="Black", font=('Helvetica 13 bold'))

        location_input = Entry(canvas1, width=33, font=("Helvetica", 14))
        location_input.place(x=170,y=135)




        folder_path = StringVar()
        browse = Button(canvas1, text="Browse", width=7, font=("Helvetica", 10), command=browse_button)
        browse.place(x=550,y=135)

        #t = canvas1.create_text(340, 220, text="Please wait...", fill="Black", font=('Helvetica 13 bold'),)

        down = Button(canvas1, text="Download", width=15, font=("Helvetica", 11), bg="Green", fg="White", command=read_data)
        down.place(x=265,y=260)


        window.mainloop()

