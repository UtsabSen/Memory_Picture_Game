from tkinter import *
from tkinter import messagebox
import random

def main():
    root = Tk()

    n = random.randint(1, 4)

    def about():
        messagebox.showinfo("ABOUT","Name: Utsab Sen\nEmail: utsabsen1999@gmail.com\nLOVELY PROFESSIONAL UNIVERSITY\n<3 INDIA <3")

    if n == 1:
        frame1 = Frame(root)

        img1 = PhotoImage(file="bear.png")
        label1 = Label(frame1, image=img1)
        label1.grid(row=0)

        img2 = PhotoImage(file="book.png")
        label2 = Label(frame1, image=img2)
        label2.grid(row=0, column=1)

        img3 = PhotoImage(file="car.png")
        label3 = Label(frame1, image=img3)
        label3.grid(row=1)

        img4 = PhotoImage(file="chair.png")
        label4 = Label(frame1, image=img4)
        label4.grid(row=1, column=1)
        frame1.pack(side=TOP)

        def des1():
            root.destroy()
            main()

        refresh_button = Button(frame1, text="REFRESH", command= des1)
        refresh_button.grid(row=2)

        def ok1():
            root.destroy()
            root1 = Tk()
            root1.geometry("220x300")

            var_a1 = IntVar()
            var_a2 = IntVar()
            var_a3 = IntVar()
            var_a4 = IntVar()
            var_a5 = IntVar()
            var_a6 = IntVar()
            var_a7 = IntVar()
            var_a8 = IntVar()
            var_a9 = IntVar()
            var_a10 = IntVar()

            var_a = [var_a1, var_a2, var_a3, var_a4, var_a5, var_a6, var_a7, var_a8, var_a9, var_a10]
            x_a = ["Seal", "Bear", "Google", "Book", "Kite", "Car", "Tree", "Chair", "Lion", "Elephant"]
            y_a = 0
            buttons_a = [Checkbutton(root1, text=x_a[i], variable=var_a[i]) for i in range(10)]
            for b in buttons_a:
                b.grid(row=y_a, sticky=W)
                y_a += 1

            def result_1():
                count=0
                if var_a[1].get() == 1:
                    count+=1
                if var_a[3].get() == 1:
                    count+=1
                if var_a[5].get() == 1:
                    count+=1
                if var_a[7].get() == 1:
                    count+=1

                messagebox.showinfo("RESULT", "You've answered %d correct answers" %count)

            submit_button_1 = Button(root1, text="SUBMIT", command=result_1)
            submit_button_1.grid(row=10)

            def back():
                root1.destroy()
                main()

            back_button = Button(root1, text="BACK", command=back)
            back_button.grid(row=10, column=1)

            root1.title("OPTIONS")
            root1.mainloop()

        ok_button_1 = Button(frame1, text="  OK  ", command=ok1)
        ok_button_1.grid(row=2, column=1)

        about_button = Button(frame1, text="ABOUT", command=about)
        about_button.grid(row=3, columnspan=2)


    elif n == 2:
        frame2 = Frame(root)

        img1 = PhotoImage(file="cheetah.png")
        label1 = Label(frame2, image=img1)
        label1.grid(row=0)

        img2 = PhotoImage(file="earth.png")
        label2 = Label(frame2, image=img2)
        label2.grid(row=0, column=1)

        img3 = PhotoImage(file="einstein.png")
        label3 = Label(frame2, image=img3)
        label3.grid(row=1)

        img4 = PhotoImage(file="elephant.png")
        label4 = Label(frame2, image=img4)
        label4.grid(row=1, column=1)

        def des2():
            root.destroy()
            main()

        frame2.pack(side=BOTTOM)
        refresh_button = Button(frame2, text="REFRESH", command=des2)
        refresh_button.grid(row=2)

        def ok2():
            root.destroy()
            root1 = Tk()
            root1.geometry("220x300")

            var_a1 = IntVar()
            var_a2 = IntVar()
            var_a3 = IntVar()
            var_a4 = IntVar()
            var_a5 = IntVar()
            var_a6 = IntVar()
            var_a7 = IntVar()
            var_a8 = IntVar()
            var_a9 = IntVar()
            var_a10 = IntVar()

            var_a = [var_a1, var_a2, var_a3, var_a4, var_a5, var_a6, var_a7, var_a8, var_a9, var_a10]
            x_a = ["Einstein", "Bear", "Earth", "Book", "Kite", "Car", "Tree", "Cheetah", "Lion", "Elephant"]
            y_a = 0
            buttons_a = [Checkbutton(root1, text=x_a[i], variable=var_a[i]) for i in range(10)]
            for b in buttons_a:
                b.grid(row=y_a, sticky=W)
                y_a += 1

            def result_2():
                count=0
                if var_a[0].get() == 1:
                    count+=1
                if var_a[2].get() == 1:
                    count+=1
                if var_a[7].get() == 1:
                    count+=1
                if var_a[9].get() == 1:
                    count+=1

                messagebox.showinfo("RESULT", "You've answered %d correct answers" %count)

            submit_button_2 = Button(root1, text="SUBMIT", command=result_2)
            submit_button_2.grid(row=10)

            def back():
                root1.destroy()
                main()

            back_button = Button(root1, text="BACK", command=back)
            back_button.grid(row=10, column=1)

            root1.title("OPTIONS")

            root1.mainloop()

        ok_button_2 = Button(frame2, text="  OK  ", command=ok2)
        ok_button_2.grid(row=2, column=1)

        about_button = Button(frame2, text="ABOUT", command=about)
        about_button.grid(row=3, columnspan=2)

    elif n == 3:
        frame3 = Frame(root)

        img1 = PhotoImage(file="google.png")
        label1 = Label(frame3, image=img1)
        label1.grid(row=0)

        img2 = PhotoImage(file="guitar.png")
        label2 = Label(frame3, image=img2)
        label2.grid(row=0, column=1)

        img3 = PhotoImage(file="laptop.png")
        label3 = Label(frame3, image=img3)
        label3.grid(row=1)

        img4 = PhotoImage(file="lion.png")
        label4 = Label(frame3, image=img4)
        label4.grid(row=1, column=1)

        frame3.pack()

        def des3():
            root.destroy()
            main()

        refresh_button = Button(frame3, text="REFRESH", command=des3)
        refresh_button.grid(row=2)

        def ok3():
            root.destroy()
            root1 = Tk()
            root1.geometry("220x300")

            var_a1 = IntVar()
            var_a2 = IntVar()
            var_a3 = IntVar()
            var_a4 = IntVar()
            var_a5 = IntVar()
            var_a6 = IntVar()
            var_a7 = IntVar()
            var_a8 = IntVar()
            var_a9 = IntVar()
            var_a10 = IntVar()

            var_a = [var_a1, var_a2, var_a3, var_a4, var_a5, var_a6, var_a7, var_a8, var_a9, var_a10]
            x_a = ["Seal", "Bear", "Laptop", "Book", "Guitar", "Car", "Tree", "Chair", "Lion", "Google"]
            y_a = 0
            buttons_a = [Checkbutton(root1, text=x_a[i], variable=var_a[i]) for i in range(10)]
            for b in buttons_a:
                b.grid(row=y_a, sticky=W)
                y_a += 1

            def result_3():
                count=0
                if var_a[2].get() == 1:
                    count+=1
                if var_a[4].get() == 1:
                    count+=1
                if var_a[8].get() == 1:
                    count+=1
                if var_a[9].get() == 1:
                    count+=1

                messagebox.showinfo("RESULT", "You've answered %d correct answers" %count)

            submit_button_3 = Button(root1, text="SUBMIT", command=result_3)
            submit_button_3.grid(row=10)

            def back():
                root1.destroy()
                main()

            back_button = Button(root1, text="BACK", command=back)
            back_button.grid(row=10, column=1)

            root1.title("OPTIONS")

            root1.mainloop()

        ok_button_3 = Button(frame3, text="  OK  ", command=ok3)
        ok_button_3.grid(row=2, column=1)

        about_button = Button(frame3, text="ABOUT", command=about)
        about_button.grid(row=3, columnspan=2)

    elif n == 4:
        frame4 = Frame(root)

        img1 = PhotoImage(file="mobile.png")
        label1 = Label(frame4, image=img1)
        label1.grid(row=0)

        img2 = PhotoImage(file="plane.png")
        label2 = Label(frame4, image=img2)
        label2.grid(row=0, column=1)

        img3 = PhotoImage(file="table.png")
        label3 = Label(frame4, image=img3)
        label3.grid(row=1)

        img4 = PhotoImage(file="tree.png")
        label4 = Label(frame4, image=img4)
        label4.grid(row=1, column=1)

        frame4.pack()

        def des4():
            root.destroy()
            main()

        refresh_button = Button(frame4, text="REFRESH", command=des4)
        refresh_button.grid(row=2)

        def ok4():
            root.destroy()
            root1 = Tk()
            root1.geometry("220x300")

            var_a1 = IntVar()
            var_a2 = IntVar()
            var_a3 = IntVar()
            var_a4 = IntVar()
            var_a5 = IntVar()
            var_a6 = IntVar()
            var_a7 = IntVar()
            var_a8 = IntVar()
            var_a9 = IntVar()
            var_a10 = IntVar()

            var_a = [var_a1, var_a2, var_a3, var_a4, var_a5, var_a6, var_a7, var_a8, var_a9, var_a10]
            x_a = ["Plane", "Bear", "Google", "Book", "Table", "Car", "Tree", "Mobile", "Chair", "Elephant"]
            y_a = 0
            buttons_a = [Checkbutton(root1, text=x_a[i], variable=var_a[i]) for i in range(10)]
            for b in buttons_a:
                b.grid(row=y_a, sticky=W)
                y_a += 1

            def result_4():
                count=0
                if var_a[0].get() == 1:
                    count+=1
                if var_a[4].get() == 1:
                    count+=1
                if var_a[6].get() == 1:
                    count+=1
                if var_a[7].get() == 1:
                    count+=1

                messagebox.showinfo("RESULT", "You've answered %d correct answers" %count)

            submit_button_4 = Button(root1, text="SUBMIT", command=result_4)
            submit_button_4.grid(row=10)

            def back():
                root1.destroy()
                main()

            back_button = Button(root1, text="BACK", command=back)
            back_button.grid(row=10, column=1)

            root1.title("OPTIONS")

            root1.mainloop()

        ok_button_4 = Button(frame4, text="  OK  ", command=ok4)
        ok_button_4.grid(row=2, column=1)

        about_button = Button(frame4, text="ABOUT", command=about)
        about_button.grid(row=3, columnspan=2)


    root.title("IMAGE")
    root.mainloop()

main()