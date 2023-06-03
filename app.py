from binary_search_tree import Build_Tree
from red_black_tree import red_black_tree
from linear_search import linear_search
from binary_search import binary_search
import random
from tkinter import *

random_list = []
def random_fun(range):
    while len(random_list)<int(range):
          r=random.randint(1,100)
          if r not in random_list:
              random_list.append(r)
    print(random_list)
    return(random_list)

# https://stackoverflow.com/questions/73838437/how-do-i-write-code-in-order-to-generate-random-numbers-in-a-way-that-a-random-n

#Create an instance of tkinter frame or window
win= Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")
win.title('Search Algorithm')
# https://www.tutorialspoint.com/what-does-calling-tk-actually-do

frame1 = Frame(win, border=4, relief=RIDGE)
frame1.grid(sticky=E+W)
label1 = Label(frame1, text='Enter Size of Array', background='white')
label1.grid(sticky=E+W)
label1.pack()
entry1 = Entry(frame1, width=10,border=4)
entry1.pack()

frame2 = Frame(win, border=4, relief=RIDGE)
frame2.grid(sticky=E+W)
label2=Label(frame2, text='Create Sequence or Random Series?', background='white')
label2.grid(sticky=E+W)
label2.pack()
#entry2 = Entry(frame2, width=50,border=4)
#entry2.pack()

frame3 = Frame(win, border=4, relief=RIDGE)
frame3.grid(sticky=E+W)
label3=Label(frame3, text='Enter number for the search', background='white')
label3.grid(sticky=E+W)
label3.pack()
entry3 = Entry(frame3, width=50,border=4)
entry3.pack()

frame4 = Frame(win, border=4, relief=RIDGE)
frame4.grid(sticky=E+W)
label4=Label(frame4, text='Select Search Algorithm', background='white')
label4.grid(sticky=E+W)
label4.pack()

frame5 = Frame(win, border=4, relief=RIDGE)
frame5.grid(sticky=E+W)

# https://stackoverflow.com/questions/1441134/tkinter-grid-geometry-manager-size-propagation-with-sticky
# https://www.geeksforgeeks.org/python-creating-a-button-in-tkinter/

def button1():
    output_1 = "Entered Array size: " + str(entry1.get())
    label1.config(text=output_1)

Button1 = Button(frame1, text='Enter', command=button1)
Button1.pack()
# https://www.javatpoint.com/python-tkinter-button


def button2():
    output_2 = "You selected the option " + str(var.get())
    label2.config(text = output_2)

#var = IntVar()
var = StringVar()
var.set(1)

R1 = Radiobutton(frame2, text="Random Series", variable=var, value=0,
                  command=button2)
R1.pack( anchor = W )

R2 = Radiobutton(frame2, text="Enter your Series (separated by spaces)", variable=var, value=1,
                  command=button2)
R2.pack( anchor = W )
# https://www.tutorialspoint.com/python/tk_radiobutton.htm

entry2 = Entry(frame2, width=50,border=4)
entry2.pack()



def button3():
    global label_3
    global output_3
    global random_list
    global array_Size
    array_size = entry1.get()
    s = entry2.get()
    random_list = [int(x) for x in s.split()][:int(array_size)]
# https://stackoverflow.com/questions/6429638/how-to-split-a-string-of-space-separated-numbers-into-integers
    print(random_list)
    if (var.get() == "0"):
        rnd_list = random_fun(array_size)
        print(rnd_list)
        print(s)
        s = ""
        s = ",".join([str(i) for i in rnd_list])
    output_3 = "Your series is:  " + s
    print(output_3)

    if int(array_size) < 50:
        canvas1 = Canvas(frame2, bg='#FFFFFF', width=500, height=500, scrollregion=(0, 0, 500, 500))
        #canvas1.create_window(650, 20, window=e1)
        #button1 = tk.Button(text='Get Results', command=DNS)
        #canvas1.create_window(650, 50, window=button1)
        hbar = Scrollbar(frame2, orient=HORIZONTAL)
        hbar.pack(side=BOTTOM, fill=X)
        hbar.config(command=canvas1.xview)
        vbar = Scrollbar(frame2, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=X)
        vbar.config(command=canvas1.xview)
        canvas1.config(width=400, height=600)
        canvas1.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        canvas1.pack(side=LEFT, expand=True, fill=BOTH)
        # https://compscipal.medium.com/python-tkinter-as-a-java-application-36536176fe83

        label_3=Label(canvas1,text=output_3,wraplength=1000, justify="left")
        label_3.grid(row =6, column = 0)


Button3 = Button(frame2, text='Enter', command=button3)
Button3.pack()


def button4():
    output_4 = "Entered number for search is " + str(entry3.get())
    label3.config(text=output_4)
Button4 = Button(frame3, text='Enter', command=button4)
Button4.pack()



v = IntVar()
v.set(1)
def selection():
    print(v.get())

R3 = Radiobutton(frame4, text="Linear Search", variable=v, value=1,
                  command=selection)
R3.pack( anchor = W )
R4 = Radiobutton(frame4, text="Binary Search", variable=v, value=2,
                  command=selection)
R4.pack( anchor = W )
R5 = Radiobutton(frame4, text="Binary Search Tree", variable=v, value=3,
                  command=selection)
R5.pack( anchor = W )
R6 = Radiobutton(frame4, text="Red Black Tree", variable=v, value=4,
                  command=selection)
R6.pack( anchor = W )
R7 = Radiobutton(frame4, text="Comparision of Runtime", variable=v, value=5,
                  command=selection)
R7.pack( anchor = W )
# https://www.tutorialspoint.com/python/tk_radiobutton.htm

ret_value=-1
index_return=''
#v = IntVar()
#v.set(1)

def button5():
    global label_5
    e=entry3.get()
    value=int(e)
    print("number value is : ",value)
    print("random list is",random_list)
    if (v.get() == 1):
        # Linear Search
        ret_value1, s1 = linear_search(random_list, value)
        print(ret_value1)

        index_return1 = str(ret_value1)
        if ret_value1 != -1:
            label_5 = Label(frame5,text="Linear Search: Found at index :  " + index_return1 + " \n and runtime for linear search algorithm is " + s1,
                             font=("Helvetica"))
        else:
            label_5 = Label(frame5,text="Linear Search: Key not found in Array \n and runtime for linear search algorithm is " + s1,
                             font=("Helvetica"))

    elif (v.get() == 2):
        # Binary Search
        ret_value2, sorted_arr, s2 = binary_search(random_list, value)
        print(ret_value2)

        index_return2 = str(ret_value2)
        if ret_value2 != -1:
            label_5 = Label(frame5, text="Binary Search: For Sorted array: " + str(
                sorted_arr) + " \nFound at index -> " + index_return2 + " \nand runtime for binary search algorithm is " + s2,
                            font=("Helvetica"))
        else:
            label_5 = Label(frame5, text="Binary Search: Key not found in Array: " + str(
                sorted_arr) + " \n and runtime for binary search algorithm is " + s2, font=("Helvetica"))

    elif (v.get() == 3):
        # Binary Search Tree
        ret_value3, s3 = Build_Tree(random_list, value)

        if ret_value3 != -1:
            label_5 = Label(frame5,
                             text="Binary Search Tree: Key Found \nand runtime for binary search algorithm is " + s3,
                             font=("Helvetica"))
        else:
            label_5 = Label(frame5,
                             text="Binary Search Tree: Key not found in Tree \nand runtime for binary search algorithm is " + s3,
                             font=("Helvetica"))

    elif (v.get() == 4):
        # Red Black Trees
        ret_value4, s4 = red_black_tree(random_list, value)

        if ret_value4 != -1:
            label_5 = Label(frame5,
                             text="Red Black Tree: Key Found \nand runtime for binary search algorithm is " + s4,
                             font=("Helvetica"))
        else:
            label_5 = Label(frame5,
                             text="Red Black Tree: Key not found in Tree \nand runtime for binary search algorithm is " + s4,
                             font=("Helvetica"))
    else:
        ret_value1, s1 = linear_search(random_list, value)
        index_return1 = str(ret_value1)

        ret_value2, sorted_arr, s2 = binary_search(random_list, value)
        index_return2 = str(ret_value2)

        ret_value3, s3 = Build_Tree(random_list, value)

        ret_value4, s4 = red_black_tree(random_list, value)

        if ret_value1 != -1 and ret_value2 != -1 and ret_value3 != -1 and ret_value3 != -1 and ret_value4 != -1:
            text1 = "Linear Search: Found at index -> " + index_return1 + " \n and runtime for linear search algorithm is " + s1 + "\n Binary Search: Found at index -> " + index_return2 + " \n and runtime for binary search algorithm is " + s2 + "\n Binary Search Tree: Key Found \n and runtime for binary search algorithm is " + s3 + "\n Red Black Tree: Key Found \n and runtime for binary search algorithm is " + s4

            label_5 = Label(frame5, text=text1, font=("Helvetica"))
        else:
            text2 = "Binary Search: Key not found in Array \n and runtime for binary search algorithm is " + s2 + "\n Binary Search: Key not found in Array \n and runtime for binary search algorithm is " + s2 + "\n Binary Search Tree: Key not found in Tree \n and runtime for binary search algorithm is " + s3 + "\n Red Black Tree: Key not found in Tree \n and runtime for binary search algorithm is " + s4
            label_5 = Label(frame5, text=text2, font=("Helvetica"))
        print(
            "Linear Search " + s1 + "\n Binary Search " + s2 + "\n Binary Seach Tree " + s3 + "\n Red Black Tree " + s4)
    print(v)

    label_5.pack()



Button5 = Button(frame5, text='Search', command=button5)
Button5.pack()


win.mainloop()





