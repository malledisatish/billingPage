from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib

def searchBill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==customer_BillNumber_enrty.get():
            f=open(f'bills/{i}','r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error',"Enter Valid Bill Number")

def clear():
    bathSoap_entry.delete(0, END)
    HairGel_entry.delete(0, END)
    HairSpray_entry.delete(0, END)
    HairWash_entry.delete(0, END)
    faceCream_entry.delete(0, END)
    faceWash_entry.delete(0, END)

    bathSoap_entry.insert(0, 0)
    HairGel_entry.insert(0, 0)
    HairSpray_entry.insert(0, 0)
    HairWash_entry.insert(0, 0)
    faceCream_entry.insert(0, 0)
    faceWash_entry.insert(0, 0)

    peanuts_entry.delete(0, END)
    sugar_entry.delete(0, END)
    oil_entry.delete(0, END)
    dal_entry.delete(0, END)
    wheat_entry.delete(0, END)
    rice_entry.delete(0, END)

    peanuts_entry.insert(0, 0)
    sugar_entry.insert(0, 0)
    oil_entry.insert(0, 0)
    dal_entry.insert(0, 0)
    wheat_entry.insert(0, 0)
    rice_entry.insert(0, 0)

    cutter_entry.delete(0, END)
    sacles_entry.delete(0, END)
    papers_entry.delete(0, END)
    pencils_entry.delete(0, END)
    pens_entry.delete(0, END)
    notes_entry.delete(0, END)

    cutter_entry.insert(0, 0)
    sacles_entry.insert(0, 0)
    papers_entry.insert(0, 0)
    pencils_entry.insert(0, 0)
    pens_entry.insert(0, 0)
    notes_entry.insert(0, 0)

    cosmeticsprice_entry.delete(0,END)
    groceryprice_entry.delete(0,END)
    stationeryprice_entry.delete(0,END)

    cosmeticstax_entry.delete(0,END)
    grocerytax_entry.delete(0,END)
    stationerytax_entry.delete(0,END)

    customer_name_enrty.delete(0,END)
    customer_Pnumber_enrty.delete(0,END)
    textarea.delete(1.0,END)

def printBill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        file=tempfile.mktemp(".txt")
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')

def sendBillEmail():
    def sendmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(sendmailID_entry.get(),sendmailPW_entry.get())
            message=mail_message.get(1.0,END)
            recivermail=recivermailID_entry.get()
            ob.sendmail(sendmailID_entry.get(),recivermail,message)
            ob.quit()
            messagebox.showinfo('Success','Mail Sent',parent=window1)
            window1.destroy()
        except:
            messagebox.showerror('Error','Something went Worng,Please try again',parent=window1)


    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Fill the Bill')
    else:
        window1=Toplevel()
        window1.grab_set()
        window1.title('Send Mail')
        window1.config(bg="#03fc5a")
        window1.resizable(0,0)
        senderFrame=LabelFrame(window1,text='SENDER',font=('time of roman',15,'bold'),bd=6,bg="#03fc5a")
        senderFrame.grid(row=0,column=0)

        sendmailIDlabel=Label(senderFrame,text="SENDER EMAIL",font=('time of roman',13,'bold'),bd=6,bg="#03fc5a")
        sendmailIDlabel.grid(row=0,column=0)

        sendmailID_entry=Entry(senderFrame,font=('time of roman',13,'bold'),bd=2,width=23,relief=RIDGE)
        sendmailID_entry.grid(row=0,column=1,padx=10,pady=8)

        sendmailPWlabel = Label(senderFrame, text="PASSWORD", font=('time of roman', 13, 'bold'), bd=6,bg="#03fc5a")
        sendmailPWlabel.grid(row=1, column=0)

        sendmailPW_entry = Entry(senderFrame, font=('time of roman', 13, 'bold'), bd=2, width=23, relief=RIDGE,show='*')
        sendmailPW_entry.grid(row=1, column=1, padx=10, pady=8)

        reciverFrame = LabelFrame(window1, text='Reciver', font=('time of roman', 15, 'bold'), bd=6, bg="#03fc5a")
        reciverFrame.grid(row=1, column=0)

        recivermailIDlabel = Label(reciverFrame, text="RECIVER EMAIL", font=('time of roman', 13, 'bold'), bd=6,bg="#03fc5a")
        recivermailIDlabel.grid(row=0, column=0)

        recivermailID_entry = Entry(reciverFrame, font=('time of roman', 13, 'bold'), bd=2, width=23, relief=RIDGE)
        recivermailID_entry.grid(row=0, column=1, padx=10, pady=8)

        messagelabel = Label(reciverFrame, text="MESSAGE", font=('time of roman', 13, 'bold'), bd=6,bg="#03fc5a")
        messagelabel.grid(row=1, column=0,padx=10,pady=8)

        mail_message=Text(reciverFrame,font=('time of roman',13,'bold'),bd=2,relief=SUNKEN,width=43,height=12)
        mail_message.grid(row=2,column=0,columnspan=2)
        mail_message.delete(1.0,END)
        mail_message.insert(END,textarea.get(1.0,END).replace('.',''))

        sendButton=Button(window1,text="SEND",font=('time of roman',15,'bold'),width=15,command=sendmail)
        sendButton.grid(row=2,column=0,pady=20)

        window1.mainloop()


if not os.path.exists('bills'):
    os.mkdir('bills')
def saveBill():
    global  billnumber
    result=messagebox.askyesno('Conform','Do you want to save the bill')
    if result:
        billpaper=textarea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(billpaper)
        file.close()
        messagebox.showinfo('Success',f'Bill Number{billnumber} is saved successfully')
        billnumber=random.randint(1,1000)

billnumber=random.randint(1,1000)
def clickbill():
    if customer_name_enrty.get()=="" or customer_Pnumber_enrty.get()=="":
        messagebox.showerror("Error","Enter Customer Details")
    elif cosmeticsprice_entry.get()=="" and groceryprice_entry.get()=="" and stationeryprice_entry.get()=="":
        messagebox.showerror("Error","No produts are selected")
    elif cosmeticsprice_entry.get()=="0 Rs" and groceryprice_entry.get()=="0 Rs" and stationeryprice_entry.get()=="0 Rs":
        messagebox.showerror('Eroor',"No products selected")
    else:
        textarea.delete(1.0,END)
        textarea.insert(END,"\t\tWelcome "+str(customer_name_enrty.get()))
        textarea.insert(END,f'\nBill Number:{billnumber}')
        textarea.insert(END,f'\nCustomer Name:{customer_name_enrty.get()}')
        textarea.insert(END,f'\nCustomer Phone Number:{customer_Pnumber_enrty.get()}')
        textarea.insert(END,"\n..................................................")
        textarea.insert(END,'Product \t\t Quantity \t\t Price')
        textarea.insert(END, "\n..................................................")
        if bathSoap_entry.get()!='0':
            textarea.insert(END,f'\nBath Soap \t\t {bathSoap_entry.get()} \t\t {soapCost}')
        if faceWash_entry.get()!='0':
            textarea.insert(END,f'\nFace Wash \t\t {faceWash_entry.get()} \t\t {facewashCost}')
        if faceCream_entry.get()!='0':
            textarea.insert(END,f'\nFace Cream \t\t {faceCream_entry.get()} \t\t {facecreamCost}')
        if HairWash_entry.get()!='0':
            textarea.insert(END,f'\nHair Wash \t\t {HairWash_entry.get()} \t\t {hairwashCost}')
        if HairGel_entry.get()!='0':
            textarea.insert(END,f'\nHair Gel \t\t {HairGel_entry.get()} \t\t {hairgelCost}')
        if HairSpray_entry.get()!='0':
            textarea.insert(END,f'\nHair Wash \t\t {HairSpray_entry.get()} \t\t {harisprayCost}')

        if rice_entry.get()!='0':
            textarea.insert(END,f'\nRice \t\t {rice_entry.get()} \t\t {riceCost}')
        if wheat_entry.get()!='0':
            textarea.insert(END,f'\nWheat \t\t {wheat_entry.get()} \t\t {wheatCost}')
        if dal_entry.get()!='0':
            textarea.insert(END,f'\nDal \t\t {dal_entry.get()} \t\t {dalCost}')
        if oil_entry.get()!='0':
            textarea.insert(END,f'\nOil \t\t {oil_entry.get()} \t\t {oilCost}')
        if sugar_entry.get()!='0':
            textarea.insert(END,f'\nSugar \t\t {sugar_entry.get()} \t\t {sugarCost}')
        if peanuts_entry.get()!='0':
            textarea.insert(END,f'\nPea nuts \t\t {peanuts_entry.get()} \t\t {peanutsCost}')

        if notes_entry.get()!='0':
            textarea.insert(END,f'\nNotes \t\t {notes_entry.get()} \t\t {notesCost}')
        if pens_entry.get()!='0':
            textarea.insert(END,f'\nPens \t\t {pens_entry.get()} \t\t {pensCost}')
        if pencils_entry.get()!='0':
            textarea.insert(END,f'\nNotes \t\t {pencils_entry.get()} \t\t {pencilsCost}')
        if papers_entry.get()!='0':
            textarea.insert(END,f'\nNotes \t\t {papers_entry.get()} \t\t {paperCost}')
        if sacles_entry.get()!='0':
            textarea.insert(END,f'\nNotes \t\t {sacles_entry.get()} \t\t {saclesCost}')
        if cutter_entry.get()!='0':
            textarea.insert(END,f'\nNotes \t\t {cutter_entry.get()} \t\t {cutterCost}')

        textarea.insert(END, "\n..................................................")
        if cosmeticstax_entry.get()!='0.0 Rs':
            textarea.insert(END,f'\n Cosmetic Tax \t\t {cosmeticstax_entry.get()}')
        if grocerytax_entry.get()!='0.0 Rs':
            textarea.insert(END,f'\n Grpcery Tax \t\t {grocerytax_entry.get()}')
        if stationerytax_entry.get()!='0.0 Rs':
            textarea.insert(END,f'\n Stationery Tax \t\t {stationerytax_entry.get()}')

        textarea.insert(END,f'\nTotal Bill \t\t {totalBill}')
        textarea.insert(END, "\n..................................................")
        saveBill()

def total():
    global soapCost,facewashCost,facecreamCost,hairwashCost,harisprayCost,hairgelCost
    global riceCost,wheatCost,dalCost,oilCost,sugarCost,peanutsCost
    global notesCost,pensCost,pencilsCost,paperCost,saclesCost,cutterCost
    global totalBill
    soapCost=int(bathSoap_entry.get())*30
    facewashCost=int(faceWash_entry.get())*50
    facecreamCost=int(faceCream_entry.get())*100
    hairwashCost=int(HairWash_entry.get())*90
    harisprayCost=int(HairSpray_entry.get())*130
    hairgelCost=int(HairGel_entry.get())*150

    totalCosmeticsPrice=soapCost+facewashCost+facecreamCost+hairwashCost+harisprayCost+hairgelCost
    cosmeticsprice_entry.delete(0,END)
    cosmeticsprice_entry.insert(0,str(totalCosmeticsPrice)+" Rs")
    cosmeticstax=totalCosmeticsPrice*0.15
    cosmeticstax_entry.delete(0, END)
    cosmeticstax_entry.insert(0,str(cosmeticstax)+" Rs")

    riceCost=int(rice_entry.get())*500
    wheatCost=int(wheat_entry.get())*250
    dalCost=int(dal_entry.get())*100
    oilCost=int(oil_entry.get())*120
    sugarCost=int(sugar_entry.get())*50
    peanutsCost=int(peanuts_entry.get())*110

    totalGroceryPrice=riceCost+wheatCost+dalCost+oilCost+sugarCost+peanutsCost
    groceryprice_entry.delete(0,END)
    groceryprice_entry.insert(0,str(totalGroceryPrice)+" Rs")
    grocerytax=totalGroceryPrice*0.10
    grocerytax_entry.delete(0,END)
    grocerytax_entry.insert(0,str(grocerytax)+" Rs")

    notesCost=int(notes_entry.get())*25
    pensCost=int(pens_entry.get())*15
    pencilsCost=int(pencils_entry.get())*10
    paperCost=int(papers_entry.get())*3
    saclesCost=int(sacles_entry.get())*10
    cutterCost=int(cutter_entry.get())*20

    totalStationeryPrice=notesCost+pensCost+pencilsCost+paperCost+paperCost+saclesCost+cutterCost
    stationeryprice_entry.delete(0,END)
    stationeryprice_entry.insert(0,str(totalStationeryPrice)+" Rs")
    stationerytax=totalStationeryPrice*0.9
    stationerytax_entry.delete(0,END)
    stationerytax_entry.insert(0,str(stationerytax)+" Rs")

    totalBill=totalCosmeticsPrice+totalGroceryPrice+totalStationeryPrice+cosmeticstax+grocerytax+stationerytax



window=Tk()
window.title("SUPER MARKER BILLING PAGE")
window.geometry("1270x685")
window.iconbitmap("icon.ico")

NameLabel=Label(window,text="Super Market Bill",font=("times new roman",30,"bold"),bg="#03fc5a",fg="#8883e6",bd=12,relief=GROOVE)
NameLabel.pack(fill=X,pady=2)

customer_info_frame=LabelFrame(window,text="Customer Detils",font=("time new roman",15,"bold"),bg="#03fc5a",fg="#8883e6",bd=8,relief=GROOVE)
customer_info_frame.pack(fill=X)

customer_name=Label(customer_info_frame,text="Name",font=("time new roman",15,"bold"),bg="#03fc5a")
customer_name.grid(row=0,column=0,padx=20)
customer_name_enrty=Entry(customer_info_frame,font=("aril",15),bd=7,width=18)
customer_name_enrty.grid(row=0,column=1,padx=8)

customer_Pnumber=Label(customer_info_frame,text="Phone Number",font=("time new roman",15,"bold"),bg="#03fc5a")
customer_Pnumber.grid(row=0,column=2,padx=20,pady=2)
customer_Pnumber_enrty=Entry(customer_info_frame,font=("aril",15),bd=7,width=18)
customer_Pnumber_enrty.grid(row=0,column=3,padx=8)

customer_BillNumber=Label(customer_info_frame,text="Bill Number",font=("time new roman",15,"bold"),bg="#03fc5a")
customer_BillNumber.grid(row=0,column=4,padx=20,pady=2)
customer_BillNumber_enrty=Entry(customer_info_frame,font=("aril",15),bd=7,width=18)
customer_BillNumber_enrty.grid(row=0,column=5,padx=8)

search_button=Button(customer_info_frame,text="Search",font=("arial",12,"bold"),bd=7,width=8,command=searchBill)
search_button.grid(row=0,column=6,padx=20,pady=8)

items_frame=Frame(window)
items_frame.pack(pady=2)

cosmetics_frame=LabelFrame(items_frame,text="Cosmetics",font=("time new roman",15,"bold"),bg="#03fc5a",fg="#8883e6",bd=8,relief=GROOVE)
cosmetics_frame.grid(row=0,column=0)

bathSoapLable=Label(cosmetics_frame,text="Bath Soap",font=("time new roman",15,"bold"),bg="#03fc5a")
bathSoapLable.grid(row=0,column=0,pady=9,padx=10)
bathSoap_entry=Entry(cosmetics_frame,font=("times new roman",15,"bold"),width=10,bd=5)
bathSoap_entry.grid(row=0,column=1,pady=9,padx=10,sticky="W")
bathSoap_entry.insert(0,0)

faceWashLable=Label(cosmetics_frame,text="Face Wash",font=("time new roman",15,"bold"),bg="#03fc5a")
faceWashLable.grid(row=1,column=0,pady=9,padx=10)
faceWash_entry=Entry(cosmetics_frame,font=("times new roman",15,"bold"),width=10,bd=5)
faceWash_entry.grid(row=1,column=1,pady=9,padx=10,sticky="W")
faceWash_entry.insert(0,0)

faceCreamLable=Label(cosmetics_frame,text="Face Cream",font=("time new roman",15,"bold"),bg="#03fc5a")
faceCreamLable.grid(row=2,column=0,pady=9,padx=10)
faceCream_entry=Entry(cosmetics_frame,font=("times new roman",15,"bold"),width=10,bd=5)
faceCream_entry.grid(row=2,column=1,pady=9,padx=10,sticky="W")
faceCream_entry.insert(0,0)

HairWashLable=Label(cosmetics_frame,text="Hair Wash",font=("time new roman",15,"bold"),bg="#03fc5a")
HairWashLable.grid(row=3,column=0,pady=9,padx=10)
HairWash_entry=Entry(cosmetics_frame,font=("times new roman",15,"bold"),width=10,bd=5)
HairWash_entry.grid(row=3,column=1,pady=9,padx=10,sticky="W")
HairWash_entry.insert(0,0)

HairSprayLable=Label(cosmetics_frame,text="Hair Spray",font=("time new roman",15,"bold"),bg="#03fc5a")
HairSprayLable.grid(row=4,column=0,pady=9,padx=10)
HairSpray_entry=Entry(cosmetics_frame,font=("times new roman",15,"bold"),width=10,bd=5)
HairSpray_entry.grid(row=4,column=1,pady=9,padx=10,sticky="W")
HairSpray_entry.insert(0,0)

HairGelLable=Label(cosmetics_frame,text="Hair Gel",font=("time new roman",15,"bold"),bg="#03fc5a")
HairGelLable.grid(row=5,column=0,pady=9,padx=10)
HairGel_entry=Entry(cosmetics_frame,font=("times new roman",15,"bold"),width=10,bd=5)
HairGel_entry.grid(row=5,column=1,pady=9,padx=10,sticky="W")
HairGel_entry.insert(0,0)

grocery_frame=LabelFrame(items_frame,text="Grocery",font=("time new roman",15,"bold"),bg="#03fc5a",fg="#8883e6",bd=8,relief=GROOVE)
grocery_frame.grid(row=0,column=1)

riceLable=Label(grocery_frame,text="Rice",font=("time new roman",15,"bold"),bg="#03fc5a")
riceLable.grid(row=0,column=0,pady=9,padx=10)
rice_entry=Entry(grocery_frame,font=("times new roman",15,"bold"),width=10,bd=5)
rice_entry.grid(row=0,column=1,pady=9,padx=10,sticky="w")
rice_entry.insert(0,0)

wheatLable=Label(grocery_frame,text="Wheat",font=("time new roman",15,"bold"),bg="#03fc5a")
wheatLable.grid(row=1,column=0,pady=9,padx=10)
wheat_entry=Entry(grocery_frame,font=("times new roman",15,"bold"),width=10,bd=5)
wheat_entry.grid(row=1,column=1,pady=9,padx=10,sticky="w")
wheat_entry.insert(0,0)

dalLable=Label(grocery_frame,text="Dal",font=("time new roman",15,"bold"),bg="#03fc5a")
dalLable.grid(row=2,column=0,pady=9,padx=10)
dal_entry=Entry(grocery_frame,font=("times new roman",15,"bold"),width=10,bd=5)
dal_entry.grid(row=2,column=1,pady=9,padx=10,sticky="w")
dal_entry.insert(0,0)

oilLable=Label(grocery_frame,text="Oil",font=("time new roman",15,"bold"),bg="#03fc5a")
oilLable.grid(row=3,column=0,pady=9,padx=10)
oil_entry=Entry(grocery_frame,font=("times new roman",15,"bold"),width=10,bd=5)
oil_entry.grid(row=3,column=1,pady=9,padx=10,sticky="w")
oil_entry.insert(0,0)

sugarLable=Label(grocery_frame,text="Sugar",font=("time new roman",15,"bold"),bg="#03fc5a")
sugarLable.grid(row=4,column=0,pady=9,padx=10)
sugar_entry=Entry(grocery_frame,font=("times new roman",15,"bold"),width=10,bd=5)
sugar_entry.grid(row=4,column=1,pady=9,padx=10,sticky="w")
sugar_entry.insert(0,0)

peanutsLable=Label(grocery_frame,text="Peanuts",font=("time new roman",15,"bold"),bg="#03fc5a")
peanutsLable.grid(row=5,column=0,pady=9,padx=10)
peanuts_entry=Entry(grocery_frame,font=("times new roman",15,"bold"),width=10,bd=5)
peanuts_entry.grid(row=5,column=1,pady=9,padx=10,sticky="w")
peanuts_entry.insert(0,0)

stationery_frame=LabelFrame(items_frame,text="Stationery",font=("time new roman",15,"bold"),bg="#03fc5a",fg="#8883e6",bd=8,relief=GROOVE)
stationery_frame.grid(row=0,column=2)

notesLable=Label(stationery_frame,text="Note Books",font=("time new roman",15,"bold"),bg="#03fc5a")
notesLable.grid(row=0,column=0,pady=9,padx=10)
notes_entry=Entry(stationery_frame,font=("times new roman",15,"bold"),width=10,bd=5)
notes_entry.grid(row=0,column=1,pady=9,padx=10,sticky="w")
notes_entry.insert(0,0)

pensLable=Label(stationery_frame,text="Pens",font=("time new roman",15,"bold"),bg="#03fc5a")
pensLable.grid(row=1,column=0,pady=9,padx=10)
pens_entry=Entry(stationery_frame,font=("times new roman",15,"bold"),width=10,bd=5)
pens_entry.grid(row=1,column=1,pady=9,padx=10,sticky="w")
pens_entry.insert(0,0)

pencilsLable=Label(stationery_frame,text="Pencils",font=("time new roman",15,"bold"),bg="#03fc5a")
pencilsLable.grid(row=2,column=0,pady=9,padx=10)
pencils_entry=Entry(stationery_frame,font=("times new roman",15,"bold"),width=10,bd=5)
pencils_entry.grid(row=2,column=1,pady=9,padx=10,sticky="w")
pencils_entry.insert(0,0)

papersLable=Label(stationery_frame,text="Papers",font=("time new roman",15,"bold"),bg="#03fc5a")
papersLable.grid(row=3,column=0,pady=9,padx=10)
papers_entry=Entry(stationery_frame,font=("times new roman",15,"bold"),width=10,bd=5)
papers_entry.grid(row=3,column=1,pady=9,padx=10,sticky="w" )
papers_entry.insert(0,0)

saclesLable=Label(stationery_frame,text="Sacles",font=("time new roman",15,"bold"),bg="#03fc5a")
saclesLable.grid(row=4,column=0,pady=9,padx=10)
sacles_entry=Entry(stationery_frame,font=("times new roman",15,"bold"),width=10,bd=5)
sacles_entry.grid(row=4,column=1,pady=9,padx=10,sticky="w")
sacles_entry.insert(0,0)

cutterLable=Label(stationery_frame,text="Cutter",font=("time new roman",15,"bold"),bg="#03fc5a")
cutterLable.grid(row=5,column=0,pady=9,padx=10)
cutter_entry=Entry(stationery_frame,font=("times new roman",15,"bold"),width=10,bd=5)
cutter_entry.grid(row=5,column=1,pady=9,padx=10,sticky="w")
cutter_entry.insert(0,0)

billframe=Frame(items_frame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billarealable=Label(billframe,text="Bill Area",font=("times new roman",15,"bold") ,bd=7, relief=GROOVE)
billarealable.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=19,width=50,yscrollcommand=Scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenu_frame=LabelFrame(window,text="Bill Menu",font=("time new roman",15,"bold"),bg="#03fc5a",fg="#8883e6",bd=8,relief=GROOVE)
billmenu_frame.pack(fill=X)

cosmetiscsPriceLable=Label(billmenu_frame,text="Cosmetiscs Price",font=("time new roman",15,"bold"),bg="#03fc5a")
cosmetiscsPriceLable.grid(row=0,column=0,pady=9,padx=10)
cosmeticsprice_entry=Entry(billmenu_frame,font=("times new roman",13,"bold"),width=10,bd=5)
cosmeticsprice_entry.grid(row=0,column=1,pady=9,padx=10,sticky="w")

groceryPriceLable=Label(billmenu_frame,text="Grocery Price",font=("time new roman",15,"bold"),bg="#03fc5a")
groceryPriceLable.grid(row=1,column=0,pady=9,padx=10)
groceryprice_entry=Entry(billmenu_frame,font=("times new roman",13,"bold"),width=10,bd=5)
groceryprice_entry.grid(row=1,column=1,pady=9,padx=10,sticky="w")

stationeryPriceLable=Label(billmenu_frame,text="Stationery Price",font=("time new roman",15,"bold"),bg="#03fc5a")
stationeryPriceLable.grid(row=2,column=0,pady=9,padx=10)
stationeryprice_entry=Entry(billmenu_frame,font=("times new roman",13,"bold"),width=10,bd=5)
stationeryprice_entry.grid(row=2,column=1,pady=9,padx=10,sticky="w")

cosmetiscstaxLable=Label(billmenu_frame,text="Cosmetiscs Tax",font=("time new roman",15,"bold"),bg="#03fc5a")
cosmetiscstaxLable.grid(row=0,column=2,pady=9,padx=10)
cosmeticstax_entry=Entry(billmenu_frame,font=("times new roman",13,"bold"),width=10,bd=5)
cosmeticstax_entry.grid(row=0,column=3,pady=9,padx=10,sticky="w")

grocerytaxLable=Label(billmenu_frame,text="Grocery Tax",font=("time new roman",15,"bold"),bg="#03fc5a")
grocerytaxLable.grid(row=1,column=2,pady=9,padx=10)
grocerytax_entry=Entry(billmenu_frame,font=("times new roman",13,"bold"),width=10,bd=5)
grocerytax_entry.grid(row=1,column=3,pady=9,padx=10,sticky="w")

stationerytaxLable=Label(billmenu_frame,text="Stationery Tax",font=("time new roman",15,"bold"),bg="#03fc5a")
stationerytaxLable.grid(row=2,column=2,pady=9,padx=10)
stationerytax_entry=Entry(billmenu_frame,font=("times new roman",13,"bold"),width=10,bd=5)
stationerytax_entry.grid(row=2,column=3,pady=9,padx=10,sticky="w")

buttonframe=Frame(billmenu_frame,bd=8,relief=GROOVE)
buttonframe.grid(row=0,column=4,rowspan=3)
totalButton=Button(buttonframe,text="Total",font=("time new roman",13,"bold"),bg="#03fc5a",bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonframe,text="Bill",font=("time new roman",13,"bold"),bg="#03fc5a",bd=5,width=8,pady=10,command=clickbill)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonframe,text="email",font=("time new roman",13,"bold"),bg="#03fc5a",bd=5,width=8,pady=10,command=sendBillEmail)
emailButton.grid(row=0,column=2,pady=20,padx=5)

printButton=Button(buttonframe,text="Print",font=("time new roman",13,"bold"),bg="#03fc5a",bd=5,width=8,pady=10,command=printBill)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonframe,text="clear",font=("time new roman",13,"bold"),bg="#03fc5a",bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=5)

window.mainloop()
