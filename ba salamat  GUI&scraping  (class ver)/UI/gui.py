import sys
from tkinter import messagebox
from tkinter.font import BOLD
from turtle import width
sys.path.insert(0,'C:/Users/MohammadReza/Desktop/webscraping/BaSalamUpdated')
#----------------------------------------------------------------------------optional odule
import os
os.system('cls')
#----------------------------------------------------------------------------requirment
from tkinter import *
from tkinter import ttk
from DAL.dbmanager import Database_manager
from DAL.product import product
from DAL.dbmanager import Database_manager
#-----------------------

################################### main program############################################
class User_interface:
    def __set_size(self,body,width,height):
        w=width
        h=height
        x=self.main_form.winfo_screenwidth()
        y=self.main_form.winfo_screenheight()
        xs=(x/2)-(w/2)
        ys=(y/2)-(h/2)
        body.geometry("%dx%d+%d+%d"%(w,h,xs,ys))
    def __init__(self,products) -> None:
        self.list_of_products=products
        self.main_form=Tk()
        self.main_form.title('فروشگاه اینترنتی با سلام')
        # self.main_form.iconbitmap("")
        self.__set_size(self.main_form,800,300)
        self.main_form.resizable(width=False,height=False)

        #--------------------------------------------------------------------------------------create label $ buttons
        self.label_1=Label(self.main_form,text="به فروشگاه اینترنتی باسلام خوش امدید",font=("tahoma",18,BOLD))
        self.Button_left=Button(self.main_form,text=" نمایش محصولات ",font=("tahoma",15))
        self.Button_right=Button(self.main_form,text=" درج محصولات ",font=("tahoma",15))
        #---------------------------------------------------------------------------------------sticking widgths
        self.Button_left.grid(row=1,column=0,padx=10)
        self.Button_right.grid(row=1,column=3,padx=10)
        self.label_1.grid(row=0,column=1,columnspan=2,pady=20)
        #---------------------------------------------------------------------------------------bind functions
        self.Button_left.bind("<Enter>",lambda event : self.__enter(event,'left'))
        self.Button_right.bind("<Enter>",lambda event : self.__enter(event,'right'))
        self.Button_left.bind("<Leave>",lambda event : self.__leave(event,'left'))
        self.Button_right.bind("<Leave>",lambda event : self.__leave(event,'right'))
        self.Button_left.bind("<Button-1>",lambda event:self.__show_products(event))
        self.Button_right.bind("<Button-1>",lambda event:self.__add_products(event))

        self.main_form.mainloop()



    def __enter(self,event,enter):
        if enter=='left':
            self.Button_left.config(bg="#f9a602")
        else:
            self.Button_right.config(bg="#f9a602")
    def __leave(self,event,enter):
        if enter=='left':
            self.Button_left.config(bg="#f0f0f0")
        else:
            self.Button_right.config(bg="#f0f0f0")
    def __show_products(self,event):
        #-------create new window-------
        product_window=Toplevel(self.main_form)
        product_window.title("نمایش تمامی محصولات")
        self.__set_size(product_window,900,300)
        #-------create table for showing products--------
        tree=ttk.Treeview(product_window,column=('image','title','score','city','price before','discount','price after','id'),show='headings',height=10)
        tree.grid(row=1,columnspan=1,padx=10,pady=20)
        tree.column('# 1',anchor=CENTER,width=100)
        tree.heading('# 1',text='عکس محصول')
        tree.column('# 2',anchor=CENTER,width=200)
        tree.heading('# 2',text='عنوان محصول')
        tree.column('# 3',anchor=CENTER,width=100)
        tree.heading('# 3',text='امتیاز محصول')
        tree.column('# 4',anchor=CENTER,width=75)
        tree.heading('# 4',text='شهر')
        tree.column('# 5',anchor=CENTER,width=100)
        tree.heading('# 5',text='قیمت قبل تخفیف')
        tree.column('# 6',anchor=CENTER,width=100)
        tree.heading('# 6',text='تخفیف')
        tree.column('# 7',anchor=CENTER,width=100)
        tree.heading('# 7',text='قیمت بعد تخفیف')
        tree.column('# 8',anchor=CENTER,width=100)
        tree.heading('# 8',text='شناسه محصول')
        #------get all products---------
        i=1
        for item in self.list_of_products:
            tree.insert('','end',text=str(i),values=(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7]))
            # tree.insert('','end',text=str(i),values=(item.image,item.title,item.score,item.city,item.price_before,item.discount,item.price_after,item.id))
            i+=1
    def __add_products(self,event):
        #-------create new window-------
        add_window=Toplevel(self.main_form)
        add_window.title("ثبت محصول جدید در دیتابیس")
        self.__set_size(add_window,780,340)
        #-------create table for showing products--------
        image_label=Label(add_window,text='لینک عکس')
        image_entry=Entry(add_window,width=100)
        title_label=Label(add_window,text='عنوان')
        title_entry=Entry(add_window,width=100)
        score_label=Label(add_window,text='امتیاز')
        score_entry=Entry(add_window,width=100)
        city_label=Label(add_window,text='شهر')
        city_entry=Entry(add_window,width=100)
        pricebefore_label=Label(add_window,text='قیمت قبل از تخخفیف')
        pricebefore_entry=Entry(add_window,width=100)
        discount_label=Label(add_window,text='تخفیف')
        discount_entry=Entry(add_window,width=100)
        priceafter_label=Label(add_window,text='قیمت بعد از تخفیف')
        priceafter_entry=Entry(add_window,width=100)
        submit_button=Button(add_window,text="ثبت محصول در دیتابیس",font=('tahoma',14,BOLD))

        def adding(event):
            img=image_entry.get()
            title=title_entry.get()
            score=score_entry.get()
            city=city_entry.get()
            pricebefore=pricebefore_entry.get()
            discount=discount_entry.get()
            priceafter=priceafter_entry.get()
            p1=product(img,title,int(score),city,int(pricebefore),discount,int(priceafter))
            adding=Database_manager()
            adding.insert_into_type1(p1)
            image_entry.delete(0,END)
            title_entry.delete(0,END)
            score_entry.delete(0,END)
            city_entry.delete(0,END)
            pricebefore_entry.delete(0,END)
            discount_entry.delete(0,END)
            priceafter_entry.delete(0,END)
            messagebox.showinfo(add_window,message="محصول شما با موفقیت در دیتابیس ثبت گردید\nدر صورت عدم ثبت محصول یکبار برنامه بسته و سپس باز کنید")
            add_window.destroy()

        submit_button.bind("<Button-1>",lambda event :adding(event))
        #------------------------------------
        image_label.grid(row=0,column=0,padx=20,pady=10)
        image_entry.grid(row=0,column=1,columnspan=6)
        ############
        title_label.grid(row=1,column=0,padx=20,pady=10)
        title_entry.grid(row=1,column=1,columnspan=6)
        ############
        score_label.grid(row=2,column=0,padx=20,pady=10)
        score_entry.grid(row=2,column=1,columnspan=6)
        ############
        city_label.grid(row=3,column=0,padx=20,pady=10)
        city_entry.grid(row=3,column=1,columnspan=6)
        ############
        pricebefore_label.grid(row=4,column=0,padx=20,pady=10)
        pricebefore_entry.grid(row=4,column=1,columnspan=6)
        ############
        discount_label.grid(row=5,column=0,padx=20,pady=10)
        discount_entry.grid(row=5,column=1,columnspan=6)
        ############
        priceafter_label.grid(row=6,column=0,padx=20,pady=10)
        priceafter_entry.grid(row=6,column=1,columnspan=6)
        ############
        submit_button.grid(row=7,column=1,columnspan=6)

