import tkinter as tk
from tkinter import messagebox as mb
from functools import partial  
# ---------------------------------------------------- FLames Implementation -------------------------------------------------------------

name_1 = []
name_2 = []
count = 0
flag = True

# -------------------------------------------------------- Initialization ---------------------------------------------------------------

def Editing():

    # mb.showerror("Error", "Hello")
    name1 = str(entry1.get())
    name1 = name1.lower()
    name1 = name1.replace(" ", "")
    
    name2 = str(entry2.get())
    name2 = name2.lower()
    name2 = name2.replace(" ", "")

    if(name1.isalpha() == False or name2.isalpha() == False):
        Str = "The Entered name contains invalid characters. \nEnter the string again"
        # Result.config(text = "%s" %Str) 
        mb.showerror("Error",Str)
        return 

    if name1 == name2:
        Str = "Same names have been entered"
        # Result.config(text = "%s" %Str)
        mb.showerror("Error",Str) 
        return 
    
    cancel_comman_letters(name1, name2)
    letter_count()
    flames()
    

# ----------------------------------------- Cancellation of Comman letters between 2 names -----------------------------------------------

def cancel_comman_letters(name1, name2):

    global name_1 
    global name_2 

    name_1 = []
    name_2 = []
        
    for i in name1 :
        name_1.append(i)

    for j in name2 :
        name_2.append(j)

    for i in range (len(name_1)):

        for j in range (len(name_2)):

            if name_1[i] == name_2[j]:
                name_1[i] = '$'
                name_2[j] = '$'

        # print (name_1)
        # print (name_2)
        # return name_1, name_2

# ------------------------------------------- Count the remaining letters left in the names ----------------------------------------------

def letter_count():

    global count
    count = 0

    for i in range (len(name_1)):
        if name_1[i] != '$':
            count = count + 1
            
    for j in range (len(name_2)):
        if name_2[j] != '$':
            count = count + 1

    # print (count)

# ---------------------------------------------------- Finding the answer in FLAMES ------------------------------------------------------

def flames():
    print("Performing Flames...")
    global count
    nc = count
    flames = ['f', 'l', 'a', 'm', 'e', 's']
    alter = []
    i = 0
    
    flag_check = True

    while flag_check == True:
        if i != count:
            i = i + 1

        if i == count:
            flames[i-1] = '*'
            i = i - 1

            for j in range (i, len(flames)):
                if flames[j] != '*':
                    alter.append(flames[j])
            for j in range (0, i):
                if flames[j] != '*':
                    alter.append(flames[j])

            flames = []
            for k in range (len(alter)):
                flames.append(alter[k])
            alter = []
            i = 0

            count = nc
        if i == len(flames):
            p = i
            count = count - p
            i = 0

        if len(flames) == 1:
            if flames[0] == 'f':
                # print("They are FRIENDs")
                mb.showinfo("Result", "They are FRIENDs")
            if flames[0] == 'l':
                # print("They are LOVEd by each other")
                mb.showinfo("Result", "They are LOVEd by each other")
            if flames[0] == 'a':
                # print("One has AFFECTION towards the other")
                mb.showinfo("Result", "One has AFFECTION towards the other")
            if flames[0] == 'm':
                mb.showinfo("Result","They will marry each other")
            if flames[0] == 'e':
                mb.showinfo("Result","They are ENEMIES")
            if flames[0] == 's':
                mb.showinfo("Result","SISTER!!!!")
            
            flag_check = False
                    


# --------------------------------------------------------- Function Calls --------------------------------------------------------------


# cancel_comman_letters(name1, name2)
# letter_count(name1, name2)
# flames(name1, name2)

# ---------------------------------------------------------------- GUI -------------------------------------------------------------------

GUI = tk.Tk()
GUI.geometry ( "450x350" )

winWidth = GUI.winfo_reqwidth()
winHeight = GUI.winfo_reqheight()
# print(winWidth,"     " ,winHeight)

posRight = int(GUI.winfo_screenwidth()/2 - winWidth)
posLeft = int(GUI.winfo_screenheight()/2 - winHeight)
# print(posRight," ",posLeft)

GUI.geometry( "+{}+{}" .format(posRight, posLeft))

GUI.resizable ( 0, 0 )
GUI.title ( "FLAMES" )

BN = tk.StringVar()
GN = tk.StringVar()

tk.Label( GUI, text = "Boy's Name : " ).place( x = 120, y = 50 )  
tk.Label( GUI, text= "Girl's Name : " ).place( x = 120, y = 80 )

entry1 = tk.Entry(GUI, textvariable = BN)
entry1.place( x = 210, y = 50 )

entry2 = tk.Entry(GUI, textvariable = GN)
entry2.place( x = 210, y = 80 )

Result = tk.Label(GUI)
Result.grid( row = 5, column = 5)

tk.Button(GUI, text = "Submit",activebackground = "pink", activeforeground = "blue", command = Editing).place(x = 200, y = 120)  


GUI.mainloop()
