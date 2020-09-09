from tkinter import *
# ---------------------------------------------------- FLames Implementation -------------------------------------------------------------

name_1 = []
name_2 = []
count = 0
flag = True


print("# --------------------- FLames Implementation ---------------------")
while(flag):
    name1 = input ( "Enter the boy's name : " )
    name1 = name1.lower()
    name1 = name1.replace(" ", "")

    while(name1.isalpha() == False):
        print("The Entered name contains invalid characters. \nEnter the string again")
        name1 = input ( "Enter the boy's name : " )
        name1 = name1.lower()
        name1 = name1.replace(" ", "")


    name2 = input ( "Enter the girl's name : " )
    name2 = name2.lower()
    name2 = name2.replace(" ", "")

    while(name2.isalpha() == False):
        print("The Entered name contains invalid characters. \nEnter the string again")
        name2 = input ( "Enter the boy's name : " )
        name2 = name2.lower()
        name2 = name2.replace(" ", "")

    if name1 != name2:
        flag = False
    else:
        print("Same names have been entered")



class Flames:

# -------------------------------------------------------- Initialization ---------------------------------------------------------------

    def __init__(self, name1 = name1, name2 = name2):
        self.name1 = name1
        self.name2 = name2

# ----------------------------------------- Cancellation of Comman letters between 2 names -----------------------------------------------

    def cancel_comman_letters(self):

        global name_1 
        global name_2 

        name_1 = []
        name_2 = []
        
        for i in self.name1 :
            name_1.append(i)

        for j in self.name2 :
            name_2.append(j)

        for i in range (len(name_1)):

            for j in range (len(name_2)):

                if name_1[i] == name_2[j]:
                    name_1[i] = '$'
                    name_2[j] = '$'

        # print (name_1)
        # print (name_2)

# ------------------------------------------- Count the remaining letters left in the names ----------------------------------------------

    def letter_count(self):

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

    def flames(self):
        print("Performing Flames...")
        global count
        nc = count
        flames = ['f', 'l', 'a', 'm', 'e', 's']
        alter = []
        i = 0
        
        remain = 0
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
                    print("They are FRIENDs")
                if flames[0] == 'l':
                    print("They are LOVEd by each other")
                if flames[0] == 'a':
                    print("One has AFFECTION towards the other")
                if flames[0] == 'm':
                    print("They will marry each other")
                if flames[0] == 'e':
                    print("They are ENEMIES")
                if flames[0] == 's':
                    print("SISTER!!!!")
                
                flag_check = False
                    


# --------------------------------------------------------- Function Calls --------------------------------------------------------------

X = Flames()
X.cancel_comman_letters()
X.letter_count()
X.flames()

# ---------------------------------------------------------------- GUI -------------------------------------------------------------------

GUI = Tk()
GUI.geometry ( "500x500" )
GUI.resizable ( 0, 0 )
GUI.title ( "FLAMES" )
Label ( text = "Boy's Name : " ).grid(row = 0)
Label ( text = "Girl's Name : " ).grid(row = 1)

entry1 = Entry(GUI)
entry2 = Entry(GUI)

entry1.grid(row = 0, column = 1)
entry2.grid(row = 1, column = 1)
GUI.mainloop()
