from tkinter import *
from fpdf import FPDF

window=Tk()

medicines={
    "Medicine A":20,
    "Medicine B":10,
    "Medicine C":40,
    "Medicine D":25,
    
}
cart=[]
def getMed():
    selectedMed=medicineListbox.get(ANCHOR)
    quantity=int(quantityEntry.get())
    price=medicines[selectedMed]
    itemTotal=quantity*price
    cart.append((selectedMed,quantity,itemTotal))
    totalAmountEntry.delete(0,END)
    totalAmountEntry.insert(END,str(calculateTotal()))
    updateInvoiceText()
    

def updateInvoiceText():
    invoiceTxt.delete(1.0,END)
    for item in cart:
        invoiceTxt.insert(END,f"mdecine:{item[0]},quantity:{item[1]},price:{item[2]}\n") 
    
def calculateTotal():
    total=0.0
    for item in cart:
        total=total+item[2]
    return total
        
def genrateInvoice():
    customerName=customerEntry.get()
    
    pdf=FPDF()
    pdf.set_font("Helvetica",size=12)
    pdf.add_page()
    pdf.cell(0,15,txt="Invoice",new_x="LMARGIN",new_y="NEXT",align="C")
    pdf.cell(0,10,txt="Customer:"+customerName,new_x="LMARGIN",new_y="NEXT",align="L")
    pdf.cell(0,10,txt="",new_x="LMARGIN",new_y="NEXT")
    for item in cart:
        medname,qnt,total=item
        pdf.cell(0,10,txt=f"Medecine:{medname},Quantity:{qnt},Total:{total}",new_x="LMARGIN",new_y="NEXT",align="L")
    
    pdf.cell(0,10,txt="Total amount:"+str(calculateTotal()),new_x="LMARGIN",new_y="NEXT",align="L")
    pdf.output(f"{customerName}.pdf")
    
    
window.title("Invoice generator")
medicineLablel=Label(window,text="Medicines: ")
medicineLablel.pack()

medicineListbox=Listbox(window,selectmode=SINGLE)
for med in medicines:
    medicineListbox.insert(END,med)
medicineListbox.pack()

quantityLabel=Label(window,text="Quantity:")
quantityLabel.pack()
quantityEntry=Entry(window)
quantityEntry.pack()

addBtn=Button(window,text="Add medicine",command=getMed)
addBtn.pack()

totalAmount=Label(window,text="Total Amount:")
totalAmount.pack()

totalAmountEntry=Entry(window)
totalAmountEntry.pack()

customerLabel=Label(window,text="Customer Name:")
customerLabel.pack()
customerEntry=Entry(window)
customerEntry.pack()

generateBtn=Button(window,text="Generate invoice", command=genrateInvoice)
generateBtn.pack()

invoiceTxt=Text(window,height=10,width=50)
invoiceTxt.pack()

window.mainloop()