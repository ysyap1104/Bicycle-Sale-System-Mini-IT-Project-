import Tkinter as tk   # python3
#import Tkinter as tk   # python
import tkMessageBox
import smtplib
import ttk
from Tkinter import *
import MySQLdb








TITLE_FONT = ("Helvetica", 18, "bold")

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Login, checkrequirement,Insertdata,purchase,purchaseWithoutStatisfy,menu):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Login")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        def check_password():
            while username.get() != "Jeffnyap" or password.get() != "Iambicycleseller123":
                tkMessageBox.showinfo("Failed","Please enter the correct username and password!")
                return
                
                
            tkMessageBox.showinfo("Success", "Login Successful!")
            self.destroy()
            return
        #photo
        
        photo=PhotoImage(file="login.gif")
        background_label =Label(self, image=photo)
        background_label.img=photo
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
  
        #photo
        title = Label(self, text="Bicycle Sale System",font=TITLE_FONT)
        title.grid(row=2,column=1,sticky="w",padx=600,pady=100)
        user=Label(self,text="Username:",font=20)
        user.grid(row=6,column=1,padx=450,sticky="w")
        username=Entry(self,width=60,bd=8)
        username.grid(row=6,column=1,padx=550,sticky="w")
        passwordLabel=Label(self,text="Password:",font=20)
        passwordLabel.grid(row=7,column=1,padx=450,sticky="w",pady=20)
        password=Entry(self,width=60,bd=8,show="*")
        password.grid(row=7,column=1,padx=550,sticky="w")
        btnLogin=Button(self,bd=5,text="Login",width=10,height=2,command=check_password)
        btnLogin.grid(row=8,column=1,sticky="w",padx=670)
        


 
        
        
class menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #photo
        photo2=PhotoImage(file="menu.gif")
        background_label =Label(self, image=photo2)
        background_label.img=photo2
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        def checkcustomerdata():
            global a
            controller.show_frame("Insertdata")
            buttonNew.configure(state="disabled")
            buttonExist.configure(state="disabled")
            searchName.configure(state="normal")
            validbutton.configure(state="disabled")
            invalidbutton.configure(state="disabled")
            global searchButton
            searchButton.configure(state="normal")
            a=1
            
        def checkrequirementframe():
            global a
            controller.show_frame("checkrequirement")
            buttonNew.configure(state="normal")
            buttonExist.configure(state="normal")
            searchName.delete(0,'end')
            searchName.configure(state="disabled")
            a=2
        
            
            
      
            
            
            













            
        titlemenu = Label(self, text="Choose your option",font=TITLE_FONT)
        titlemenu.grid(row=2,column=1,sticky="w",padx=900,pady=100)

       
        optionButton1 = tk.Button(self,width=20, height= 5,text = "View Customer Details",command=checkcustomerdata,bd=8)
        optionButton1.grid(row=3,column=1,sticky="w",padx=750)

        optionButton2 = tk.Button(self,width=20, height= 5,text = "Check Requirement",command=checkrequirementframe,bd=8)
        optionButton2.grid(row=3,column=1,sticky="w",padx=925)

        optionButton3=tk.Button(self, width=20, height=5, text="Purchase", command=lambda : controller.show_frame("purchaseWithoutStatisfy"),bd=8)
        optionButton3.grid(row=3,column=1,sticky="w",padx=1100)

        
        

       
        

class checkrequirement(tk.LabelFrame):
    def __init__(self, parent, controller):
        tk.LabelFrame.__init__(self,parent)
        self.controller=controller
        labelframe1=LabelFrame(self,text="Check Requirement")
        labelframe1.grid(row=0, columnspan=7, sticky='W',padx=5, pady=5, ipadx=5, ipady=5)
        labelframe2=LabelFrame(self,text="Result")
        labelframe2.grid(row=0, column=9, columnspan=2, rowspan=8, sticky='NS', padx=5, pady=5)
        
        def calculateBMI(mass,height):
            Mass=float(mass)
            Height=float(height)
            Height=Height*(0.01)
            BMI=Mass/(Height **2.0)
            return BMI
        
        
        def checkAge(Age,Agelessthan19,Age19,Agemorethan60):
            Age=int(Age)
            if Age < 19:
               suitable_Bike_Age= Agelessthan19
            else:
                if Age < 60:
                    suitable_Bike_Age= Age19
                else:
                    suitable_Bike_Age= Agemorethan60
            
            return suitable_Bike_Age


        def checksuitableBMI(suitable_Bike_Age,BMI,BMIlessthan19,BMIbetween19and25,BMImorethan25):
            countBIKE=0
            timeBIKE=0
            suitable_BIKE_BMI=[]
            if BMI <= 18:
                while countBIKE < len(suitable_Bike_Age):
                    if BMIlessthan19[countBIKE]==suitable_Bike_Age[timeBIKE]:
                        suitable_BIKE_BMI=suitable_BIKE_BMI+[BMIlessthan19[countBIKE]]
                        timeBIKE=timeBIKE+1
                    else:
                        timeBIKE=timeBIKE+1
                    if timeBIKE==len(suitable_Bike_Age):
                        countBIKE=countBIKE+1
                        if countBIKE == len(BMIlessthan19):
                            countBIKE=len(suitable_Bike_Age)
                        timeBIKE=0
            else:
                if BMI <=25:
                    while countBIKE < len(suitable_Bike_Age):
                        if BMIbetween19and25[countBIKE]==suitable_Bike_Age[timeBIKE]:
                            suitable_BIKE_BMI=suitable_BIKE_BMI+[BMIbetween19and25[countBIKE]]
                            timeBIKE=timeBIKE+1
                        else:
                            timeBIKE=timeBIKE+1
                        if timeBIKE==len(suitable_Bike_Age):
                            countBIKE=countBIKE+1
                            if countBIKE == len(BMIbetween19and25):
                                countBIKE=len(suitable_Bike_Age)
                            timeBIKE=0
                else:
                    while countBIKE < len(suitable_Bike_Age):
                        if BMImorethan25[countBIKE]==suitable_Bike_Age[timeBIKE]:
                            suitable_BIKE_BMI=suitable_BIKE_BMI+[BMImorethan25[countBIKE]]
                            timeBIKE=timeBIKE+1
                        else:
                            timeBIKE=timeBIKE+1
                        if timeBIKE==len(suitable_Bike_Age):
                            countBIKE=countBIKE+1
                            if countBIKE == len(BMImorethan25):
                                countBIKE=len(suitable_Bike_Age)
                            timeBIKE=0
            return suitable_BIKE_BMI
        

        def checksuitableGenderafterBMI(suitableBIKEBMI,Gender,MALEtypeofbike,FEMALEtypeofbike):
            countBMIBIKE=0
            countGENDERBIKE=0
            suitableBMInGENDER=[]
            if Gender == "Male":
                while countBMIBIKE < len(MALEtypeofbike):
                    if suitableBIKEBMI[countBMIBIKE] == MALEtypeofbike[countGENDERBIKE]:
                        suitableBMInGENDER=suitableBMInGENDER + [suitableBIKEBMI[countBMIBIKE]]
                        countGENDERBIKE=countGENDERBIKE + 1
                    else:
                        countGENDERBIKE=countGENDERBIKE+1
                    if countGENDERBIKE == len(MALEtypeofbike):
                        countBMIBIKE=countBMIBIKE + 1
                        if countBMIBIKE == len(suitableBIKEBMI):
                            countBMIBIKE=len(MALEtypeofbike)
                        countGENDERBIKE=0
            else:
                while countBMIBIKE < len(FEMALEtypeofbike):
                    if suitableBIKEBMI[countBMIBIKE]==FEMALEtypeofbike[countGENDERBIKE]:
                        suitableBMInGENDER=suitableBMInGENDER + [suitableBIKEBMI[countBMIBIKE]]
                        countGENDERBIKE=countGENDERBIKE + 1
                    else:
                        countGENDERBIKE=countGENDERBIKE + 1
                    if countGENDERBIKE == len(FEMALEtypeofbike):
                        countBMIBIKE= countBMIBIKE+1
                        if countBMIBIKE == len(suitableBIKEBMI):
                            countBMIBIKE= len(FEMALEtypeofbike)
                        countGENDERBIKE=0
                
            return suitableBMInGENDER

        def checkPRICE(suitableBMInGENDER,PriceTypeofbike,typeofbike):
            count=0
            countBIKE=0
            Price=[]
            invalidresult="Invalid suitable bike for you"
            if len(suitableBMInGENDER) == 0:
                count= len(typeofbike)#make it out loop
                return invalidresult
            while count < len(typeofbike):
                if suitableBMInGENDER[count] == typeofbike[countBIKE]:
                    sameElement= countBIKE
                    Price=Price + [PriceTypeofbike[sameElement]]
                    countBIKE=countBIKE + 1
                else:
                    countBIKE=countBIKE + 1
                if countBIKE == len(typeofbike):
                    count=count + 1
                    if count == len(suitableBMInGENDER):
                        count=len(typeofbike)
                    countBIKE=0
            
            return Price

        def checkSuitablePRICE(Price, budget,suitableBMInGENDER):
            Budget=int(budget)
            countBIKE=0
            element=0
            suitablePRICE=[]
            invalidresult = "Invalid bike1"
            if len(suitableBMInGENDER) == 0:
                countBIKE= len(Price)#make it our loop
                return invalidresult

            while countBIKE < len(Price):
                if Budget >= int(Price[element]):
                    suitablePRICE= suitablePRICE + [Price[element]]
                    element=element+1
                else:
                    element=element+1
                if element == len(Price):
                    countBIKE = len(Price)
        

            return suitablePRICE

        def checkMostSuitable(suitablePRICE,typeofbike,PriceTypeofbike,suitableBMInGENDER):
            countBIKE=0
            timeBIKE=0
            mostsuitable=[]
            invalidresult="invalid bike2"
            if len(suitableBMInGENDER) == 0 or len(suitablePRICE)==0:
                countBIKE= len(PriceTypeofbike)#make it our loop
                return invalidresult
            while countBIKE < len(PriceTypeofbike):
                if suitablePRICE[countBIKE]== PriceTypeofbike[timeBIKE]:
                    sameElement=timeBIKE
                    mostsuitable=mostsuitable+ [typeofbike[sameElement]]
                    timeBIKE=timeBIKE + 1
                else:
                    timeBIKE=timeBIKE + 1
                if timeBIKE == len(PriceTypeofbike):
                    countBIKE=countBIKE + 1
                    if countBIKE == len(suitablePRICE):
                        countBIKE= len(PriceTypeofbike)   #make it our loop
                    timeBIKE=0

            return mostsuitable

        
        def enableEntry():
            global haveBudget
            budgetentry.configure(state="normal")
            budgetentry.update()
            haveBudget="Yes"
            ageentry.configure(state="normal")
            heightentry.configure(state="normal")
            massentry.configure(state="normal")
            
            

        def disableEntry():
            global haveBudget
            budgetentry.configure(state="disabled")
            budgetentry.update()
            haveBudget="No"
            ageentry.configure(state="normal")
            heightentry.configure(state="normal")
            massentry.configure(state="normal")
            
            


        def checkbutton():
            global suitableBMInGENDER
            global mostsuitable
            global Price
            global suitablePRICE
            global BMI
            a=typebike.get()
            b=Gender.get()
            c=ansBudget.get()
            d=ansMass.get()
            e=ansHeight.get()
            f=ansAge.get()
            if haveBudget == "Yes":
                while len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0 or len(e)==0 or len(f)==0:
                    tkMessageBox.showinfo("Failed", "Please enter your data!")
                    return

                Place=0
                while Place< len(ansBudget.get()):
                    digit=0
                    while ansBudget.get()[Place] != str(digit):
                        if str(digit)=="10":
                            tkMessageBox.showinfo("Try again","Please enter the budget in digit")
                            return
                            digit=0
                        else:
                            digit=digit+1
                    if str(digit) =="10":
                        Place=0
                    else:
                        Place=Place+1
                float(ansBudget.get())
                
                Place=0
                while Place< len(ansMass.get()):
                    digit=0
                    while ansMass.get()[Place] != str(digit):
                        if str(digit)=="10":
                            tkMessageBox.showinfo("Try again","Please enter the mass in digit")
                            return
                            digit=0
                        else:
                            digit=digit+1
                    if str(digit) =="10":
                        Place=0
                    else:
                        Place=Place+1
                float(ansMass.get())
                
                Place=0
                while Place< len(ansHeight.get()):
                    digit=0
                    while ansHeight.get()[Place] != str(digit):
                        if str(digit)=="10":
                            tkMessageBox.showinfo("Try again","Please enter the height in digit")
                            return
                            digit=0
                        else:
                            digit=digit+1
                    if str(digit) =="10":
                        Place=0
                    else:
                        Place=Place+1
                float(ansHeight.get())
                
                Place=0
                while Place< len(ansAge.get()):
                    digit=0
                    while ansAge.get()[Place] != str(digit):
                        if str(digit)=="10":
                            tkMessageBox.showinfo("Try again","Please enter the age in digit")
                            return
                            digit=0
                        else:
                            digit=digit+1
                    if str(digit) =="10":
                        Place=0
                    else:
                        Place=Place+1
                float(ansAge.get())
                                   
            else:
                while len(a)==0 or len(b)==0 or len(d)==0 or len(e)==0 or len(f)==0:
                    tkMessageBox.showinfo("Failed", "Please enter your data!")
                    return

                Place=0
                while Place< len(ansMass.get()):
                    digit=0
                    while ansMass.get()[Place] != str(digit):
                        if str(digit)=="10":
                            tkMessageBox.showinfo("Try again","Please enter the height in digit")
                            return
                            digit=0
                        else:
                            digit=digit+1
                    if str(digit) =="10":
                        Place=0
                    else:
                        Place=Place+1
                float(ansMass.get())
                Place=0
                while Place< len(ansHeight.get()):
                    digit=0
                    while ansHeight.get()[Place] != str(digit):
                        if str(digit)=="10":
                            tkMessageBox.showinfo("Try again","Please enter the mass in digit")
                            return
                            digit=0
                        else:
                            digit=digit+1
                    if str(digit) =="10":
                        Place=0
                    else:
                        Place=Place+1
                float(ansHeight.get())
                Place=0
                while Place< len(ansAge.get()):
                    digit=0
                    while ansAge.get()[Place] != str(digit):
                        if str(digit)=="10":
                            tkMessageBox.showinfo("Try again","Please enter the age in digit")
                            return
                            digit=0
                        else:
                            digit=digit+1
                    if str(digit) =="=10":
                        Place=0
                    else:
                        Place=Place+1
                float(ansAge.get())


            BMI=calculateBMI(ansMass.get(), ansHeight.get())

            Mountain=["GT Laguna Bike","Schwinn Scour Bike","Scott Spark 740","Diamondback Lux Sport ","Cannondale Rush  29er Bike","Diamondback Atroz Comp ","Schwinn Rosemary Bike","Diamondback Grind Pro BMX Bike","Novara Hickory 29er Bike","Ghost Kato FS","Diamondback El Oso Grande", 
               "Scott Genius 740","Diamondback Jr Viper BMX Bike","Diamondback Della Cruz Beach Cruiser","Diamondback Mason","Cannondale Habit Carbon","Ghost Lector LC ","Diamondback Sync'r"]
            
            Agelessthan19M=["GT Laguna Bike","Schwinn Scour Bike","Schwinn Rosemary Bike","Diamondback Grind Pro BMX Bike","Diamondback Jr Viper BMX Bike","Diamondback Della Cruz Beach Cruiser"]
            Age19M=["Scott Spark 740","Cannondale Foray X1 ","Novara Hickory 29er Bike","Ghost Kato FS","Diamondback Mason","Cannondale Habit Carbon"]
            Agemorethan60M=["Cannondale Rush  29er Bike","Diamondback Atroz Comp ","Diamondback El Oso Grande","Scott Genius 740","Ghost Lector LC ","Diamondback Sync'r"]

            BMIlessthan19M=["GT Laguna Bike","Schwinn Scour Bike","Novara Hickory 29er Bike","Ghost Kato FS","Ghost Lector LC ","Diamondback Sync'r"]
            BMIbetween19and25M=["Schwinn Rosemary Bike","Diamondback Grind Pro BMX Bike","Scott Spark 740","Diamondback Lux Sport ","Cannondale Rush  29er Bike","Diamondback Atroz Comp "]
            BMImorethan25M=["Diamondback Jr Viper BMX Bike","Diamondback Della Cruz Beach Cruiser","Diamondback Mason","Cannondale Habit Carbon","Diamondback El Oso Grande","Scott Genius 740"]

            MaleM=["GT Laguna Bike","Schwinn Scour Bike","Cannondale Rush  29er Bike","Diamondback Atroz Comp ","Diamondback Mason","Cannondale Habit Carbon","Ghost Lector LC ","Diamondback Sync'r","Novara Hickory 29er Bike"]
            FemaleM=["Diamondback Jr Viper BMX Bike","Diamondback Della Cruz Beach Cruiser","Schwinn Rosemary Bike","Diamondback Grind Pro BMX Bike","Scott Spark 740","Diamondback Lux Sport ","Ghost Kato FS","Diamondback El Oso Grande","Scott Genius 740"]

            PriceM=["350","740","1500","1900","400","550","900","2200","400","500","725","1400","1500","1650","950","900","1000","800"]

            Hybrid=["Cannondale Quick CX 4 Bike","Novara Buzz Bike","Pinnacle Lithium One Hybrid Bike","Glory Hybrid Bike","MiiR Wave 3-Speed Bike","Cannondale Contro 3 Bike","Diamondback Haanjo Metro Plus Bike","Cannondale Quick CX Bike","HOY Shizuoka Hybrid Bike","Pinnacle Cobalt Hybrid", "Boardman Hybrid Sport Bike","Boardman MX Comp Bike","GHOST Panamao X  Bike","FastRoad CoMax","Dawes Strawberry Cruiser Bike","Scott Sportster 30 Bike","Apollo Envoy Hybrid Bike","Indi Gemini Hybrid Bike"]
            Agelessthan19H=["Cannondale Quick CX 4 Bike","Novara Buzz Bike","Diamondback Haanjo Metro Plus Bike","Cannondale Quick CX Bike","GHOST Panamao X  Bike","FastRoad CoMax"]
            Age19H=["Pinnacle Lithium One Hybrid Bike","HOY Shizuoka Hybrid Bike","Power Glory Bike","Pinnacle Cobalt Hybrid Bike","Dawes Strawberry Cruiser Bike","Scott Sportster 30 Bike"]
            Agemorethan60H=["MiiR Wave 3-Speed Bike","Cannondale Contro 3 Bike","Boardman Hybrid Sport Bike","Boardman MX Comp Bike","Apollo Envoy Hybrid Bike","Indi Gemini Hybrid Bike"]
            
            BMIlessthan19H=["Cannondale Quick CX 4 Bike","Novara Buzz Bike","Power Glory Bike","Pinnacle Cobalt Hybrid Bike","Apollo Envoy Hybrid Bike","Indi Gemini Hybrid Bike"]
            BMIbetween19and25H=["Diamondback Haanjo Metro Plus Bike","Cannondale Quick CX Bike","Pinnacle Lithium One Hybrid Bike","HOY Shizuoka Hybrid Bike","MiiR Wave 3-Speed Bike","Cannondale Contro 3 Bike"]
            BMImorethan25H=["GHOST Panamao X  Bike","FastRoad CoMax","Dawes Strawberry Cruiser Bike","Scott Sportster 30 Bike","Boardman Hybrid Sport Bike","Boardman MX Comp Bike"]

            MaleH=["Cannondale Quick CX 4 Bike","Novara Buzz Bike","MiiR Wave 3-Speed Bike","Cannondale Contro 3 Bike","Dawes Strawberry Cruiser Bike","Scott Sportster 30 Bike","Apollo Envoy Hybrid Bike","Indi Gemini Hybrid Bike","HOY Shizuoka Hybrid Bike"]
            FemaleH=["GHOST Panamao X  Bike","FastRoad CoMax","Diamondback Haanjo Metro Plus Bike","Cannondale Quick CX Bike","Pinnacle Lithium One Hybrid Bike","Power Glory Bike","Pinnacle Cobalt Hybrid Bike","Boardman Hybrid Sport Bike","Boardman MX Comp Bike"]

            PriceH=["799","159","999","200","300","666","788","449","888","1299","1899","299","500","950","1499","349","450","3999"]
            
            Road=["Diamondback Clarity","Fuji Absolute Road Bike","NovaraRandonee Bike","Diamondback Century Disc Bike","DiamondbackInterval Carbon","MiiR McCall Bike","Fuji Ace Road Bike","Diamondback Insight Flat Bar Road Bike","Diamondback Insight STI-8 Disc Bike","Cannondale CAADX Disc 105 Bike","MiiR Payette Flip Flop Bike", \
                       "MiiR High 8-Speed Bike","MongooseFat Tire Mounten Bike","Pinarello FP0 Kids Road Bike","GHOST Nivolet 8 LC Di2 Bike","Scott Addict 20 Compact Ultegra Bike","Novara Carema 2A 650 Bike","Novara Strada 3D Bike"]
            Agelessthan19R=["Diamondback Clarity","Fuji Absolute Road Bike","Fuji Ace Road Bike","Diamondback Insight Flat Bar Road Bike","MongooseFat Tire Mounten Bike","Pinarello FP0 Kids Road Bike"]
            Age19R=["NovaraRandonee Bike","Diamondback Century Disc Bike","Diamondback Insight STI-8 Disc Bike","Cannondale CAADX Disc 105 Bike","GHOST Nivolet 8 LC Di2 Bike","Scott Addict 20 Compact Ultegra Bike"]
            Agemorethan60R=["DiamondbackInterval Carbon","MiiR McCall Bike","MiiR Payette Flip Flop Bike","MiiR High 8-Speed Bike","Novara Carema 2A 650 Bike","Novara Strada 3D Bike"]

            BMIlessthan19R=["Diamondback Clarity","Fuji Absolute Road Bike","Diamondback Insight STI-8 Disc Bike","Cannondale CAADX Disc 105 Bike","Novara Carema 2A 650 Bike","Novara Strada 3D Bike"]
            BMIbetween19and25R=["Fuji Ace Road Bike","Diamondback Insight Flat Bar Road Bike","NovaraRandonee Bike","Diamondback Century Disc Bike","DiamondbackInterval Carbon","MiiR McCall Bike"]
            BMImorethan25R=["MongooseFat Tire Mounten Bike","Pinarello FP0 Kids Road Bike","GHOST Nivolet 8 LC Di2 Bike","Scott Addict 20 Compact Ultegra Bike","MiiR Payette Flip Flop Bike","MiiR High 8-Speed Bike"]

            MaleR=["Diamondback Clarity","Fuji Absolute Road Bike","DiamondbackInterval Carbon","MiiR McCall Bike","GHOST Nivolet 8 LC Di2 Bike","Scott Addict 20 Compact Ultegra Bike","Novara Carema 2A 650 Bike","Novara Strada 3D Bike","Diamondback Insight STI-8 Disc Bike"]
            FemaleR=["MongooseFat Tire Mounten Bike","Pinarello FP0 Kids Road Bike","Fuji Ace Road Bike","Diamondback Insight Flat Bar Road Bike","NovaraRandonee Bike","Diamondback Century Disc Bike","Cannondale CAADX Disc 105 Bike","MiiR Payette Flip Flop Bike","MiiR High 8-Speed Bike"]

            PriceR=["450","499","359","729","799","299","199","559","669","1199","1899","500","600","1999","2299","399","999","800"]

            
            
            
                
            if typebike.get() == "Mountain":
                if haveBudget=="Yes":
                    suitable_Bike_Age=checkAge(ansAge.get(),Agelessthan19M,Age19M,Agemorethan60M)
                    suitable_BIKE_BMI=checksuitableBMI(suitable_Bike_Age,BMI,BMIlessthan19M,BMIbetween19and25M,BMImorethan25M)
                    suitableBMInGENDER=checksuitableGenderafterBMI(suitable_BIKE_BMI,Gender.get(),MaleM,FemaleM)
                    Price=checkPRICE(suitableBMInGENDER,PriceM,Mountain)
                    suitablePRICE=checkSuitablePRICE(Price, ansBudget.get(),suitableBMInGENDER)
                    mostsuitable=checkMostSuitable(suitablePRICE,Mountain,PriceM,suitableBMInGENDER)
                    print suitable_Bike_Age
                    print suitable_BIKE_BMI
                    print suitableBMInGENDER
                    print Price
                    print suitablePRICE
                    print mostsuitable
                else:
                    suitable_Bike_Age=checkAge(ansAge.get(),Agelessthan19M,Age19M,Agemorethan60M)
                    suitable_BIKE_BMI=checksuitableBMI(suitable_Bike_Age,BMI,BMIlessthan19M,BMIbetween19and25M,BMImorethan25M)
                    suitableBMInGENDER=checksuitableGenderafterBMI(suitable_BIKE_BMI,Gender.get(),MaleM,FemaleM)
                    suitablePRICE=checkPRICE(suitableBMInGENDER,PriceM,Mountain)
                    print suitable_Bike_Age
                    print suitable_BIKE_BMI
                    print suitableBMInGENDER
                    print suitablePRICE
                    
            else:
                if typebike.get()=="Road":
                    if haveBudget=="Yes":
                        suitable_Bike_Age=checkAge(ansAge.get(),Agelessthan19R,Age19R,Agemorethan60R)
                        suitable_BIKE_BMI=checksuitableBMI(suitable_Bike_Age,BMI,BMIlessthan19R,BMIbetween19and25R,BMImorethan25R)
                        suitableBMInGENDER=checksuitableGenderafterBMI(suitable_BIKE_BMI,Gender.get(),MaleR,FemaleR)
                        Price=checkPRICE(suitableBMInGENDER,PriceR,Road)
                        suitablePRICE=checkSuitablePRICE(Price, ansBudget.get(),suitableBMInGENDER)
                        mostsuitable=checkMostSuitable(suitablePRICE,Road,PriceR,suitableBMInGENDER)
                        print suitable_Bike_Age
                        print suitable_BIKE_BMI
                        print suitableBMInGENDER
                        print Price
                        print suitablePRICE
                        print mostsuitable
                    else:
                        suitable_Bike_Age=checkAge(ansAge.get(),Agelessthan19R,Age19R,Agemorethan60R)
                        suitable_BIKE_BMI=checksuitableBMI(suitable_Bike_Age,BMI,BMIlessthan19R,BMIbetween19and25R,BMImorethan25R)
                        suitableBMInGENDER=checksuitableGenderafterBMI(suitable_BIKE_BMI,Gender.get(),MaleR,FemaleR)
                        suitablePRICE=checkPRICE(suitableBMInGENDER,PriceR,Road)
                        print suitable_Bike_Age
                        print suitable_BIKE_BMI
                        print suitableBMInGENDER
                        print suitablePRICE
                else:
                    if haveBudget=="Yes":
                        suitable_Bike_Age=checkAge(ansAge.get(),Agelessthan19H,Age19H,Agemorethan60H)
                        suitable_BIKE_BMI=checksuitableBMI(suitable_Bike_Age,BMI,BMIlessthan19H,BMIbetween19and25H,BMImorethan25H)
                        suitableBMInGENDER=checksuitableGenderafterBMI(suitable_BIKE_BMI,Gender.get(),MaleH,FemaleH)
                        Price=checkPRICE(suitableBMInGENDER,PriceH,Hybrid)
                        suitablePRICE=checkSuitablePRICE(Price, ansBudget.get(),suitableBMInGENDER)
                        mostsuitable=checkMostSuitable(suitablePRICE,Hybrid,PriceH,suitableBMInGENDER)
                        print suitable_Bike_Age
                        print suitable_BIKE_BMI
                        print suitableBMInGENDER
                        print Price
                        print suitablePRICE
                        print mostsuitable
                    else:
                        suitable_Bike_Age=checkAge(ansAge.get(),Agelessthan19H,Age19H,Agemorethan60H)
                        suitable_BIKE_BMI=checksuitableBMI(suitable_Bike_Age,BMI,BMIlessthan19H,BMIbetween19and25H,BMImorethan25H)
                        suitableBMInGENDER=checksuitableGenderafterBMI(suitable_BIKE_BMI,Gender.get(),MaleH,FemaleH)
                        suitablePRICE=checkPRICE(suitableBMInGENDER,PriceH,Hybrid)
                        print suitable_Bike_Age
                        print suitable_BIKE_BMI
                        print suitableBMInGENDER
                        print suitablePRICE
                        
                        
            
            btnWant.configure(state="normal")
            btnNo.configure(state="normal")
            btnCheck.configure(state="disabled")
            btnClear.configure(state="disabled")
            btnBack.configure(state="disabled")
            tkMessageBox.showinfo("Success", "Check Successful!")
            budgetentry.configure(state="disabled")
            massentry.configure(state="disabled")
            heightentry.configure(state="disabled")
            ageentry.configure(state="disabled")
            btnBudgetYes.configure(state="disabled")
            btnBudgetNo.configure(state="disabled")

            showResult.configure(state="normal")
           
            
            
            showResult.insert(END, "Body Mass Index                  : %.2f  \n\n\n" % BMI ,)
            showResult.insert(END, "Your Gender                         : %s  \n\n\n" % Gender.get() )
            showResult.insert(END, "Your Age                               : %s  \n\n\n" % ansAge.get() )
            if haveBudget=="Yes":
                showResult.insert(END, "Your Budget                          :RM %s \n\n\n" % ansBudget.get() )
            else:
                showResult.insert(END, "Your Budget                          :No budget \n\n\n"  )
            showResult.insert(END, "Your Catogories Bike          : %s  \n\n\n" % typebike.get() )
        


            if suitableBMInGENDER ==[] or suitablePRICE==[]:
                showResult.insert(END, "Your Suitable Model             : %s  \n\n\n" % "Invalid Bike")
                showResult.insert(END, "Price of Model                      : %s  \n\n\n" % "Invalid ")
                btnBack.configure(state="normal")
                btnWant.configure(state="disabled")
                btnNo.configure(state="disabled")
               
            else:
                if haveBudget=="Yes":
                    showResult.insert(END, "Your Suitable Model             : %s  \n\n\n" % mostsuitable)
                else:
                    showResult.insert(END, "Your Suitable Model             : %s  \n\n\n" % suitableBMInGENDER)
                showResult.insert(END, "Price of Model                      : %s  \n\n\n" % suitablePRICE)

            
            
            showResult.configure(state="disabled")
            
            
            

            

            
            

        
       


                    
        def clear():
            
            budgetentry.configure(state="normal")
            budgetentry.delete(0, 'end')
            massentry.delete(0,'end')
            heightentry.delete(0,'end')
            ageentry.delete(0,'end')
            budgetentry.configure(state="disabled")

        def Yes():
            controller.show_frame("Insertdata")
            backmenubutton.configure(state="disabled")
            

        def No():
            controller.show_frame("menu")
            budgetentry.configure(state="normal")
            massentry.configure(state="normal")
            heightentry.configure(state="normal")
            ageentry.configure(state="normal")
            btnBudgetYes.configure(state="normal")
            btnBudgetNo.configure(state="normal")
            showResult.configure(state="normal")
            showResult.delete('1.0', END)
            budgetentry.delete(0, 'end')
            massentry.delete(0,'end')
            heightentry.delete(0,'end')
            ageentry.delete(0,'end')
            showResult.configure(state="disabled")
            budgetentry.configure(state="disabled")
            massentry.configure(state="disabled")
            heightentry.configure(state="disabled")
            ageentry.configure(state="disabled")
            btnCheck.configure(state="normal")
            btnClear.configure(state="normal")
            btnWant.configure(state="disabled")
            btnNo.configure(state="disabled")
            

        def backmenu():
            controller.show_frame("menu")
            budgetentry.configure(state="normal")
            massentry.configure(state="normal")
            heightentry.configure(state="normal")
            ageentry.configure(state="normal")
            btnBudgetYes.configure(state="normal")
            btnBudgetNo.configure(state="normal")
            showResult.configure(state="normal")
            showResult.delete('1.0', END)
            budgetentry.delete(0, 'end')
            massentry.delete(0,'end')
            heightentry.delete(0,'end')
            ageentry.delete(0,'end')
            showResult.configure(state="disabled")
            budgetentry.configure(state="disabled")
            massentry.configure(state="disabled")
            heightentry.configure(state="disabled")
            ageentry.configure(state="disabled")
            btnCheck.configure(state="normal")
            btnClear.configure(state="normal")
            

            
        
        
        ansBudget=StringVar()
        ansMass=StringVar()
        ansHeight=StringVar()
        ansAge=StringVar()
        

        

        
          
        #catogories
        catogories =tk.Label(  labelframe1,text="Please select your bike catogories :")
        catogories.grid(row=0,column=0)
        choices=('Mountain','Road','Hybrid')
        typebike=tk.StringVar( self)
        option=tk.OptionMenu( labelframe1,typebike,*choices)
        option.grid (row=0,column=1,sticky="wens")
        #gender
        catogories =tk.Label(  labelframe1,text="Please select your gender               :")
        catogories.grid(row=1,column=0)
        choicesg=('Male','Female')
        Gender=tk.StringVar( self)
        option=tk.OptionMenu( labelframe1,Gender,*choicesg)
        option.grid(row=1,column=1,sticky="wens",pady=30)
        #yes or no budget
        v = IntVar()
        budget = tk.Label(labelframe1, text="Do you have any budget                 :")
        budget.grid(row=2,column=0)
        global btnBudgetYes
        global btnBudgetNo
        btnBudgetYes=Button(labelframe1, borderwidth=4, text="Yes", width=20,height=2,padx=20,command=enableEntry)
        btnBudgetNo=Button(labelframe1, borderwidth=4, text="No", width=20,height=2,padx=20,command=disableEntry)
        btnBudgetYes.grid(row=2,column=1,sticky="w")
        btnBudgetNo.grid(row=2,column=2,sticky="w")
        #answerbudget
        global budgetentry
        Budget = tk.Label( labelframe1, text="Enter your budget(RM)                    :")
        Budget.grid(row=3,column=0)
        budgetentry=tk.Entry( labelframe1, textvariable=ansBudget,state="disabled")
        budgetentry.grid(row=3,column=1,sticky="wens",pady=30)
        #mass
        global massentry
        mass = tk.Label( labelframe1, text="Enter your mass(KG)                          :")
        mass.grid(row=4,column=0)
        massentry=tk.Entry( labelframe1,textvariable=ansMass,state="disabled")
        massentry.grid(row=4,column=1,sticky="wens",pady=30)
        #height
        global heightentry
        height = tk.Label( labelframe1, text="Enter your height(CM)                     :")
        height.grid(row=5,column=0)
        heightentry=tk.Entry( labelframe1,textvariable=ansHeight,state="disabled")
        heightentry.grid(row=5,column=1,sticky="wens",pady=30)
        #age
        global ageentry
        age = tk.Label( labelframe1, text="Enter your age                                   :")
        age.grid(row=6,column=0)
        ageentry=tk.Entry( labelframe1,textvariable=ansAge,state="disabled")
        ageentry.grid(row=6,column=1,sticky="wens",pady=30)
        #button
        global btnCheck
        global btnClear
        global btnBack
        btnCheck=tk.Button( labelframe1, width=20,height=2,borderwidth=4,text="Check",command=checkbutton)
        btnCheck.grid(row=7,column=0,sticky="w",padx=20)
        btnClear = tk.Button(labelframe1, width=20, height= 2, borderwidth=4, text="Clear",command=clear)
        btnClear.grid(row=7,column=1,sticky="w",padx=20)
        
        btnBack= tk.Button( labelframe1,width=20, height= 2,borderwidth=4,text = "Back",command=backmenu)
        btnBack.grid(row=7,column=2,sticky="w",padx=20)
     

        
        
        
        #Result
        #textbox
        global showResult
        showResult=Text(labelframe2, width=80,height=25,state="disabled",font="Helvetica")
        showResult.grid(pady=15,sticky="w")
        #Label
        labelSatisfy=Label(labelframe2, text="Do you want to buy          :")
        labelSatisfy.grid(row=6,column=0,sticky="w")
        #btn
        btnWant=Button(labelframe2,width=20, height=2,borderwidth=4,text="Yes",command=Yes,state=DISABLED)
        btnWant.grid(row=6,sticky="w",padx=200)
        btnNo=Button(labelframe2,width=20, height=2,borderwidth=4,text="No",command=No,state=DISABLED)
        btnNo.grid(row=6,sticky="w",padx=360)

     
        

        
            

        
            

       
 
        
                
        
    




        




class Insertdata(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        EorN=LabelFrame(self,text="Customer")
        EorN.grid(row=0, columnspan=7, sticky='W',padx=5, pady=5, ipadx=5, ipady=5)
        newcustomerframe=LabelFrame(self,text="New Customer")
        newcustomerframe.grid(row=1, columnspan=7, sticky='W',padx=5, pady=5, ipadx=15, ipady=5)
        oldcustomer=LabelFrame(self,text="Existing Customer")
        oldcustomer.grid(row=1, column=9, columnspan=2, rowspan=8, sticky='NS',padx=5, pady=5)
        
        
     
        def enableEntry():
            buttonExist.configure(state="disabled")
            ansName.configure(state="normal")
            ansIc.configure(state="normal")
            ansAddress.configure(state="normal")
            ansPhone.configure(state="normal")
            savebutton.configure(state="normal")
            searchName.configure(state="disabled")
            searchButton.configure(state="disabled")
            validbutton.configure(state="disabled")
            invalidbutton.configure(state="disabled")
            ansName.update()
            ansIc.update()
            ansAddress.update()
            ansPhone.update()
            savebutton.update()
            

        def disableEntry():
            buttonNew.configure(state="disabled")
            ansName.configure(state="disabled")
            ansIc.configure(state="disabled")
            ansAddress.configure(state="disabled")
            ansPhone.configure(state="disabled")
            savebutton.configure(state="disabled")
            searchName.configure(state="normal")
            searchButton.configure(state="normal")
            validbutton.configure(state="disabled")
            invalidbutton.configure(state="disabled")
            ansName.update()
            ansIc.update()
            ansAddress.update()
            ansPhone.update()
            savebutton.update()
            validbutton.update()
            invalidbutton.update()
            
        
              
        #Label Frame Exiting or New
        NeworExisting=Label(EorN, text="New Customer or Existing Customer   : ")
        NeworExisting.grid(row=0,column=0)
        
        global buttonNew
        buttonNew=Button(EorN, text="New",width=20,height=2,padx=20,borderwidth=4,command=enableEntry)
        buttonNew.grid(row=0,column=1,sticky="w")
        
        global buttonExist
        buttonExist=Button(EorN,text="Existing",width=20,height=2,padx=20,borderwidth=4,command=disableEntry)
        buttonExist.grid(row=0,column=2,sticky="w")

        #Label Frame Insert Data
        #Name
        global ansName
        namelabel = tk.Label( newcustomerframe, text="Enter your name                                    :")
        namelabel.grid(row=1,column=0)
        
        ansName=tk.Entry( newcustomerframe)
        ansName.configure(state="disabled")
        ansName.grid(row=1,column=1,sticky="wens",pady=30)
        
        #IC
        global ansIc
        iclabel = tk.Label( newcustomerframe, text="Enter your IC                                        :")
        iclabel.grid(row=2,column=0)
        
        ansIc=tk.Entry( newcustomerframe)
        ansIc.configure(state="disabled")
        ansIc.grid(row=2,column=1,sticky="wens",pady=30)
        
        #Address
        global ansAddress
        addresslabel = tk.Label( newcustomerframe, text="Enter your address                              :")
        addresslabel.grid(row=3,column=0)
        
        ansAddress=tk.Entry( newcustomerframe)
        ansAddress.configure(state="disabled")
        ansAddress.grid(row=3,column=1,sticky="wens",pady=30)
        
        #Phone
        global ansPhone
        phonelabel = tk.Label( newcustomerframe, text="Enter your phone number                  :")
        phonelabel.grid(row=4,column=0)
        
        ansPhone=tk.Entry( newcustomerframe)
        ansPhone.configure(state="disabled")
        ansPhone.grid(row=4,column=1,sticky="wens",pady=30)


        
        
        
        def savedata():
            a=ansName.get()
            b=ansIc.get()
            c=ansAddress.get()
            d=ansPhone.get()
            useduser="False"
            while len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0:
                tkMessageBox.showinfo("Save Failed", "Please enter your data completely!")
                return
            
            #Test if IC is alphabet
            Place=0
            while Place< len(ansIc.get()):
                digit=0
                while ansIc.get()[Place] != str(digit):
                    if str(digit)=="10":
                        tkMessageBox.showinfo("Save Failed", "Please enter your data completely!")
                        return
                        digit=0
                    else:
                        digit=digit+1
                if str(digit) =="10":
                    Place=0
                else:
                    Place=Place+1
                        
            #Test if Phone is alphabet
            Place=0
            while Place< len(ansPhone.get()):
                digit=0
                while ansPhone.get()[Place] != str(digit):
                    if str(digit)=="10":
                        tkMessageBox.showinfo("Save Failed", "Please enter your data completely!")
                        return
                        digit=0
                    else:
                        digit=digit+1
                if str(digit) =="10":
                    Place=0
                else:
                    Place=Place+1
                    
            #After enter a correct data          
            db = MySQLdb.connect(host='localhost',user='root',passwd='',db='yys' )
            try:
                cursor = db.cursor()
                cursor.execute("SELECT name from cd")
                data= cursor.fetchall()
                for row in data:
                    while a==row[0] or b==row[0] or c==row[0] or d==row[0]:
                        useduser="True"
                        break
            except MySQLdb.Error as error:
                    print (error)
            if useduser=="False":
                    
                sql = "INSERT INTO cd (name,ic,address,phone) \
                VALUES ('%s','%s','%s','%s')" %\
                (a,b,c,d)
                try:
                    cursor.execute(sql)
                    db.commit()
                except:
                    db.rollback()
                tkMessageBox.showinfo("Success", "Data Saved!")
                controller.show_frame("purchase")
            else:
                tkMessageBox.showinfo("Invalid", "The information you entered has already existed,please try again!")
   
                    
    
                       

        
            
        
        #Label Frame Exiting Data
        global savebutton
        savebutton = Button(newcustomerframe,text=" Save Data ",command=savedata,width=20, height= 2, borderwidth=4,state=DISABLED)
        savebutton.grid(row=5,column=1,sticky="w",padx=20)
        #---------------------------------------------------------
        #search name! !!!!!!!!!!
        def checkvalidorinvalid():
            global a
            db = MySQLdb.connect(host="localhost",user="root",passwd="",db="yys")
            cursor=db.cursor()
            cursor = db.cursor()
            cursor.execute("SELECT name,ic,address,phone FROM cd WHERE name LIKE '%s' " % (searchName.get()))
            for row in iter(cursor.fetchone, None): 
                select.insert(END,row) # append list
            
            cursor.close()
            if len(searchName.get())>0:
                validbutton.configure(state="normal")
                invalidbutton.configure(state="normal")
            else:
                validbutton.configure(state="disabled")
                invalidbutton.configure(state="disabled")


            if a == 1:
                validbutton.configure(state="disabled")
                invalidbutton.configure(state="disabled")
            else:
                validbutton.configure(state="normal")
                invalidbutton.configure(state="normal")
      
                
        #Search Name

        Searchname=StringVar
        searchlabel =Label( oldcustomer, text="Enter the name that you want to search")
        searchlabel.grid(row=0,column=2,sticky="s",pady=5)
        
        global searchName
        searchName=Entry(oldcustomer,textvariable=Searchname,state=DISABLED)
        searchName.grid (row=1,column=2,sticky="ns",pady=10)
        
        global searchButton
        searchButton= Button(oldcustomer,text="Search",width=5,height=1, borderwidth=4,command=checkvalidorinvalid,state=DISABLED)
        searchButton.grid(row=1,column=2,sticky="ne",padx=300)
        
        
    
        #Text box 
        scroll = Scrollbar(oldcustomer, orient=VERTICAL)
        select = Listbox(oldcustomer, yscrollcommand=scroll.set, width=90,height=15)
        scroll.config (command=select.yview)
        scroll.grid(row=2, column=2,sticky="wens")
        
        
        #PRINT SEARCH NAME !
        def clickme(x):
            #listbox to print search result
            select.delete(0, END) # delete all on list
            select.grid(row=2, column=2,sticky="w",padx=50) # show list # show list
            

        def invalidname():
             tkMessageBox.showinfo("Search Failed","Invalid Name,Please insert the customer data.")
             select.delete(0, END)
             savebutton.configure(state="disabled")
             buttonExist.configure(state="normal")
             buttonNew.configure(state="normal")
             searchButton.configure(state="disabled")
             searchName.delete(0,END)
             searchName.configure(state="disabled")
             validbutton.configure(state="disabled")
             invalidbutton.configure(state="disabled")
            
             


               
    
        controller.bind("<Key>", clickme)
        global validbutton
        validbutton = Button(oldcustomer,text="Valid ",width=20, height= 2, borderwidth=4,state=DISABLED,
                             command=lambda: controller.show_frame("purchase"))
        validbutton.grid(row=6,column=2,sticky="w")
        
        global invalidbutton
        invalidbutton = Button(oldcustomer,text="Invalid ",width=20, height= 2, borderwidth=4,state=DISABLED,command=invalidname)
        invalidbutton.grid(row=6,column=2,sticky="w",padx=155)

        global backmenubutton
        backmenubutton = Button(oldcustomer,text="Back ",width=20, height= 2, borderwidth=4,
                                 command=lambda: controller.show_frame("menu"))
        backmenubutton.grid(row=6,column=2,sticky="w",padx=310)
        

class purchase(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        labelframe=LabelFrame(self,text="Receipt")
        labelframe.grid(row=1, columnspan=7, sticky='wens',pady=5)

        labelframe2=LabelFrame(self, text="Quantity & Discount")
        labelframe2.grid(row=0, columnspan=7, sticky='wens',pady=5)

        labelframe3=LabelFrame(self, text="Asking Email")
        labelframe3.grid(row=2,columnspan=7, sticky="wens",pady=5)




        def CalcnewPrice(suitablePRICE,discount, QuantityOfModel):
            newPrice=(suitablePRICE -(suitablePRICE*discount))* QuantityOfModel
            return newPrice
        
        #Frame Q&Discount
        def clickDisplay():
            global mostsuitable
            global suitablePRICE
            Quantity.configure(state="normal")
            btnStudent.configure(state="normal")
            btnOld.configure(state="normal")
            btnNoDis.configure(state="normal")
            entryModel.configure(state="normal")
            if haveBudget == "Yes":
                labelresult=Label(labelframe2,text="%s"% mostsuitable)
            else:
                labelresult=Label(labelframe2,text="%s"% suitableBMInGENDER)
            labelresult.grid(row=0,column=1,sticky="w")
            labelresult=Label(labelframe2,text="%s"% suitablePRICE)
            labelresult.grid(row=1,column=1,sticky="w")
            btndisplay.configure(state="disabled")
            
            
        def studentDis():
            global discount
            discount=20/100.0
            btnOld.configure(state="disable")
            btnNoDis.configure(state="disable")
            btnSubmit.configure(state="normal")
        def oldcitizenDis():
            global discount
            discount=25/100.0
            btnStudent.configure(state="disable")
            btnNoDis.configure(state="disable")
            btnSubmit.configure(state="normal")
        def noDis():
            global discount
            discount=0
            btnStudent.configure(state="disable")
            btnOld.configure(state="disable")
            btnSubmit.configure(state="normal")
        def clickSubmit():
            global newPrice
            global discount
            global mostsuitable
            global suitablePRICE
            global finalModel

            #Check error
            QuantityOfModel=str(Quantity.get())
            
            while len(QuantityOfModel)==0:
                tkMessageBox.showinfo("Failed", "Please enter the quantity!")
                return
            while len(entryModel.get())==0:
                tkMessageBox.showinfo("Failed", "Please enter the models!")
                return
            
            Place=0
            while Place< len(QuantityOfModel):
                digit=0
                while QuantityOfModel[Place] != str(digit):
                    if str(digit)=="10":
                        tkMessageBox.showinfo("Failed","Enter the quantity.")
                        return
                        digit=0
                    else:
                        digit=digit+1
                if str(digit) =="10":
                    Place=0
                else:
                    Place=Place+1
            if int(QuantityOfModel)>200:
                tkMessageBox.showinfo("Failed","Enter the quantity below 200.")
                return
            if int(QuantityOfModel)==0:
                tkMessageBox.showinfo("Failed","Enter the quantity.")
                return
            else:
                btnPrint.configure(state="normal")
                btnStudent.configure(state="disabled")
                btnOld.configure(state="disabled")
                #Find the bike
                element=0
                if haveBudget == "Yes":
                    while element < len(mostsuitable):
                        if selectedModel.get()!= mostsuitable[element]:
                            invalidelement=element+1
                            if invalidelement==len(mostsuitable):
                                tkMessageBox.showinfo("Faled", "Enter the correct models.")
                                btnStudent.configure(state="normal")
                                btnOld.configure(state="normal")
                                btnNoDis.configure(state="normal")
                                return
                                
                        if selectedModel.get() == mostsuitable[element]:
                            finalModel = selectedModel.get()
                            suitablePRICE=suitablePRICE[element]
                            element=2
                        else:
                            element=element+1
                else:
                    while element < len(suitableBMInGENDER):
                        if selectedModel.get()!= suitableBMInGENDER[element]:
                            invalidelement=element+1
                            if invalidelement==len(suitableBMInGENDER):
                                tkMessageBox.showinfo("Faled", "Enter the correct models.")
                                btnStudent.configure(state="normal")
                                btnOld.configure(state="normal")
                                btnNoDis.configure(state="normal")
                                return
                                    
                        if selectedModel.get() == suitableBMInGENDER[element]:
                            finalModel = selectedModel.get()
                            suitablePRICE=suitablePRICE[element]
                            element=2
                        else:
                            element=element+1
                print finalModel
                suitablePRICE=int(suitablePRICE)

                QuantityOfModel=int(QuantityOfModel)
                
                newPrice=CalcnewPrice(suitablePRICE,discount, QuantityOfModel)
                print newPrice

                
                
                btnSubmit.configure(state="disabled")
                entryModel.configure(state="disabled")
                Quantity.configure(state="disabled")
                    
                   

             
                    
            

        labeldisplayModel=Label(labelframe2, text="Model                                   :",pady=10)
        labeldisplayModel.grid(row=0,column=0,sticky="w")

        labeldisplayPrice=Label(labelframe2, text="Price of Model                     :", pady=10)
        labeldisplayPrice.grid(row=1,column=0,sticky="w")

        labelSelectModel=Label(labelframe2, text="Select the model            :", pady=10)
        labelSelectModel.grid(row=1,column=1,padx=200,sticky="w")

        selectedModel=StringVar()
        entryModel=Entry(labelframe2, textvariable=selectedModel,state="disabled")
        entryModel.grid(row=1,column=1,padx=350,sticky="w")

        labelQuantity=Label(labelframe2, text="Your Quantity                      :",pady=10)
        labelQuantity.grid(row=2,column=0, sticky="w")

        Quantity= Spinbox(labelframe2, from_=0, to=500,width=10,state=DISABLED)
        Quantity.grid(row=2,column=1,sticky="w")

        btnSubmit=Button(labelframe2, text="Submit",width=20,state=DISABLED,borderwidth=4,command=clickSubmit,pady=10)
        btnSubmit.grid(row=3,column=1,sticky="w")
            
        btndisplay=Button(labelframe2, text="Display Models and Prices",width=20,borderwidth=4,command=clickDisplay,pady=10)
        btndisplay.grid(row=3,column=0,sticky="w")

        ansDiscount=StringVar()
        labelDiscount=Label(labelframe2, text="Select Your Discount     :",pady=10)
        labelDiscount.grid(row=2,column=1,padx=200,sticky='w')

        btnStudent=Button(labelframe2, text="Student Discount",state=DISABLED,borderwidth=4,pady=10,width=20,command=studentDis)
        btnStudent.grid(row=2,column=1, padx=350,sticky="w")

        btnOld=Button(labelframe2, text="Old Citizen Discount",state=DISABLED,borderwidth=4,pady=10,width=20,command=oldcitizenDis)
        btnOld.grid(row=2,column=1, padx=520,sticky="w")

        btnNoDis=Button(labelframe2, text="No Discount", state=DISABLED,borderwidth=4, pady=10,width=20,command=noDis)
        btnNoDis.grid(row=2,column=1,padx=690,sticky="w")


        #Frame receipt
        def clickPrint():
            btnYES.configure(state="normal")
            btnNO.configure(state="normal")

            labelreceiptModel=Label(labelframe,text="%s"% finalModel)
            labelreceiptModel.grid(row=0,column=1,sticky="w")
            
            labelreceiptPrice=Label(labelframe, text="RM %s"%suitablePRICE)
            labelreceiptPrice.grid(row=1,column=1,sticky="w")

            labelreceiptDiscount=Label(labelframe, text="%s percentage"%(discount*100))
            labelreceiptDiscount.grid(row=2,column=1,sticky="w")
            
            labelreceiptPayment=Label(labelframe, text="RM %s"% newPrice)
            labelreceiptPayment.grid(row=3,column=1,sticky="w")
            btnPrint.configure(state="disabled")
            
                
        labelModel=Label(labelframe, text= "Your Model is                                : ")
        labelModel.grid(row=0, column=0, sticky="w",pady=10)

        labelModelPrice=Label(labelframe, text= "Model's Price is                             : ")
        labelModelPrice.grid(row=1,column=0, sticky="w",pady=10)

        labeldiscount=Label(labelframe, text="Your discount percentage is       :")
        labeldiscount.grid(row=2,column=0,sticky="w",pady=10)

        labeltotalPrice=Label(labelframe, text="Your total payment is                  : ")
        labeltotalPrice.grid(row=3,column=0, sticky="w",pady=10)

        btnPrint=Button(labelframe, text="Display Receipt",borderwidth=4,width=20,state="disable",command=clickPrint)
        btnPrint.grid(row=4,column=0, sticky="w", pady=10)


        #Frame Asking receipt

        def clickYes():
            btnSend.configure(state="normal")
            entryEmail.configure(state="normal")
            btnBACK.configure(state="disabled")
            btnEXIT.configure(state="disabled")

        def clickNo():
            btnSend.configure(state="normal")
            entryEmail.configure(state="disabled")
            btnBACK.configure(state="normal")
            btnEXIT.configure(state="normal")
            btnSend.configure(state="disabled")

        def sendmail():
            x=entryEmail.get()
            gmail_sender='songsengyap@gmail.com'
            gmail_passwd='yap71104'
            SUBJECT = "Receipt From Bicycle Sale Store"
            TEXT = "Thank You For Coming \n\n The bicycle you bought :%s \n\n" %finalModel
            TEXT2="Price of the Bicycle :%s \n\n"%suitablePRICE
            TEXT3="Total Payment :%s \n\n"%newPrice
            
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(gmail_sender,gmail_passwd)

            BODY = '\r\n'.join(['To: %s' % x,
                                 'From: %s' % gmail_sender,
                                 'Subject: %s' % SUBJECT,
                                 '', TEXT,TEXT2,TEXT3])

            try:
                server.sendmail(gmail_sender,x,BODY)
                print 'email sent'
                tkMessageBox.showinfo("Success","Message Sent,Please come again!")
                btnBACK.configure(state="normal")
                btnEXIT.configure(state="normal")
            except:
                print'error'
                tkMessageBox.showinfo("Send Failed","Failed,Please enter a valid email!")
                btnBACK.configure(state="disabled")
                btnEXIT.configure(state="disabled")   
            server.quit()
            
        def purchaseback():
            controller.show_frame("menu")
            #Clear 
            budgetentry.configure(state="normal")
            massentry.configure(state="normal")
            heightentry.configure(state="normal")
            ageentry.configure(state="normal")
            btnBudgetYes.configure(state="normal")
            btnBudgetNo.configure(state="normal")
            showResult.configure(state="normal")
            showResult.delete('1.0', END)
            budgetentry.delete(0, 'end')
            massentry.delete(0,'end')
            heightentry.delete(0,'end')
            ageentry.delete(0,'end')
            showResult.configure(state="disabled")
            budgetentry.configure(state="disabled")
            massentry.configure(state="disabled")
            heightentry.configure(state="disabled")
            ageentry.configure(state="disabled")
            btnCheck.configure(state="normal")
            btnClear.configure(state="normal")
            ansName.delete(0,'end')
            ansIc.delete(0,'end')
            ansAddress.delete(0,'end')
            ansPhone.delete(0,'end')
            ansName.configure(state="disabled")
            ansIc.configure(state="disabled")
            ansAddress.configure(state="disabled")
            ansPhone.configure(state="disabled")
            savebutton.configure(state="disabled")
            btnBACK.configure(state="disabled")
            btnEXIT.configure(state="disabled")
            labelresult=Label(labelframe2,text="                                                                                                                                                       ")
            labelresult.grid(row=0,column=1,sticky="w")
            labelresult=Label(labelframe2,text="                                                                ")
            labelresult.grid(row=1,column=1,sticky="w")
            Quantity.configure(state="normal")
            Quantity.delete(0,'end')
            Quantity.insert(0,0)
            Quantity.configure(state="disabled")
            entryModel.configure(state="normal")
            entryModel.delete(0,'end')
            entryModel.configure(state="disabled")
            btndisplay.configure(state="normal")
            btnStudent.configure(state="disabled")
            btnOld.configure(state="disabled")
            btnNoDis.configure(state="disabled")
            labelreceiptModel=Label(labelframe,text="                                                                              ")
            labelreceiptModel.grid(row=0,column=1,sticky="w")
            labelreceiptPrice=Label(labelframe, text="                                                                             ")
            labelreceiptPrice.grid(row=1,column=1,sticky="w")
            labelreceiptDiscount=Label(labelframe, text="                                                                          ")
            labelreceiptDiscount.grid(row=2,column=1,sticky="w")
            labelreceiptPayment=Label(labelframe, text="                                                                        ")
            labelreceiptPayment.grid(row=3,column=1,sticky="w")
            btnYES.configure(state="disabled")
            btnNO.configure(state="disabled")
            entryEmail.delete(0,'end')
            entryEmail.configure(state="disabled")
            btnSend.configure(state="disabled")
            
            
            
            

          

        labelAsking=Label(labelframe3, text="Do you want receipt in email     :")
        labelAsking.grid(row=0,column=0,sticky="w")

        btnYES=Button(labelframe3, text="Yes",borderwidth=4,width=20,state="disabled",command=clickYes)
        btnYES.grid(row=0,column=1, sticky="w",padx=15)

        btnNO=Button(labelframe3, text="No",borderwidth=4,width=20,state="disabled",command=clickNo)
        btnNO.grid(row=0,column=2, sticky="w",padx=15)

        labelEmail=Label(labelframe3, text="Email Address                               :")
        labelEmail.grid(row=1,column=0, sticky="w",pady=10)

        email=StringVar()
        entryEmail=Entry(labelframe3, textvariable=email,width=25,state="disabled")
        entryEmail.grid(row=1,column=1, sticky="w",padx=15)

        btnSend=Button(labelframe3, text="Send", width=20, borderwidth=4,state="disabled",command=sendmail)
        btnSend.grid(row=1,column=2,sticky="w",padx=15)


        #outside frame
        btnBACK=Button(self, text="Back",width=20, borderwidth=4,state="disabled",command=purchaseback)
        btnBACK.grid(row=3,columnspan=7,sticky="w",padx=25)
        def clickExit():
            app.destroy()
        btnEXIT=Button(self, text="Exit", width=20, borderwidth=4,command=clickExit,state="disabled")
        btnEXIT.grid(row=3,columnspan=7,sticky="w",padx=200)

finalmodels=[]
allPrice=[]
total=[]

class purchaseWithoutStatisfy(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        

        
        
        labelframe1=LabelFrame(self, text="Select Bike")
        labelframe1.grid(row=1, column=0, sticky="w",pady=5,padx=100)

        labelframe2=LabelFrame(self, text="Purchase")
        labelframe2.grid(row=2,column=0,sticky="w",padx=640)

        labelframe3=LabelFrame(self, text="Receipt")
        labelframe3.grid(row=3,column=0,sticky="wens",padx=640)

        labelframe4=LabelFrame(self, text="Asking Email")
        labelframe4.grid(row=4,column=0,sticky="wens",padx=640)

        labelframe5=LabelFrame(self, text="Cart")
        labelframe5.grid(row=3,column=0,sticky="w",padx=100)


        #Mountain Bike
        labelModelM=Label(labelframe1, text="Model of Mountain Bike        :")
        labelModelM.grid(row=1, column=0, sticky="w")

        Mountainlist=["GT Laguna Bike","Schwinn Scour Bike","Scott Spark 740","Diamondback Lux Sport ","Cannondale Rush  29er Bike","Diamondback Atroz Comp ","Schwinn Rosemary Bike","Diamondback Grind Pro BMX Bike","Novara Hickory 29er Bike","Ghost Kato FS","Diamondback El Oso Grande", 
               "Scott Genius 740","Diamondback Jr Viper BMX Bike","Diamondback Della Cruz Beach Cruiser","Diamondback Mason","Cannondale Habit Carbon","Ghost Lector LC ","Diamondback Sync'r"]

        PriceM=["350","740","1500","1900","400","550","900","2200","400","500","725","1400","1500","1650","950","900","1000","800"]
        ModelM=StringVar()
        optionM=OptionMenu(labelframe1, ModelM , *Mountainlist)
        optionM.grid(row=1, column=1, sticky="w",padx=30)
        optionM.configure(width=20)


        labelQuantity=Label(labelframe1, text="Your Quantity                          :",pady=10)
        labelQuantity.grid(row=2,column=0, sticky="w")
        QuantityM=Spinbox(labelframe1, from_=0, to=500,width=25)
        QuantityM.grid(row=2,column=1,sticky="w",padx=30)





        #Road Bike
        labelModelR=Label(labelframe1, text="Model of Road Bike                :")
        labelModelR.grid(row=1, column=3, sticky="w")

        Roadlist=["Diamondback Clarity","Fuji Absolute Road Bike","NovaraRandonee Bike","Diamondback Century Disc Bike","DiamondbackInterval Carbon","MiiR McCall Bike","Fuji Ace Road Bike","Diamondback Insight Flat Bar Road Bike","Diamondback Insight STI-8 Disc Bike","Cannondale CAADX Disc 105 Bike","MiiR Payette Flip Flop Bike", "MiiR High 8-Speed Bike","MongooseFat Tire Mounten Bike","Pinarello FP0 Kids Road Bike","GHOST Nivolet 8 LC Di2 Bike","Scott Addict 20 Compact Ultegra Bike","Novara Carema 2A 650 Bike","Novara Strada 3D Bike"]
        PriceR=["450","499","359","729","799","299","199","559","669","1199","499","500","600","1999","2299","399","999","800"]
        ModelR=StringVar()
        optionR=OptionMenu(labelframe1, ModelR , *Roadlist)
        optionR.grid(row=1, column=4, sticky="w", padx=30)
        optionR.configure(width=20)

        labelQuantity=Label(labelframe1, text="Your Quantity                          :",pady=10)
        labelQuantity.grid(row=2,column=3, sticky="w")
        QuantityR=Spinbox(labelframe1, from_=0, to=500,width=25)
        QuantityR.grid(row=2,column=4,sticky="w",padx=30)







        #Hybrid Bike
        labelModelH=Label(labelframe1, text="Model of Hybrid Bike            :")
        labelModelH.grid(row=1, column=5, sticky="w")

        Hybridlist=["Cannondale Quick CX 4 Bike","Novara Buzz Bike","Pinnacle Lithium One Hybrid Bike","Glory Hybrid Bike","MiiR Wave 3-Speed Bike","Cannondale Contro 3 Bike","Diamondback Haanjo Metro Plus Bike","Cannondale Quick CX Bike","HOY Shizuoka Hybrid Bike","Pinnacle Cobalt Hybrid","Boardman Hybrid Sport Bike", "Boardman MX Comp Bike","GHOST Panamao X  Bike","FastRoad CoMax","Dawes Strawberry Cruiser Bike","Scott Sportster 30 Bike","Apollo Envoy Hybrid Bike","Indi Gemini Hybrid Bike"]
        PriceH=["799","159","999","200","300","666","788","449","888","1299","1899","299","500","950","1499","349","450","3999"]
        ModelH=StringVar()
        optionH=OptionMenu(labelframe1, ModelH , *Hybridlist)
        optionH.grid(row=1, column=6, sticky="w", padx=30)
        optionH.configure(width=20)

        labelQuantity=Label(labelframe1, text="Your Quantity                          :",pady=10)
        labelQuantity.grid(row=2,column=5, sticky="w")
        QuantityH=Spinbox(labelframe1, from_=0, to=500,width=25)
        QuantityH.grid(row=2,column=6,sticky="w",padx=30)


        def clickAdd():
            
            global selectedModel
            global selectedPrice
            global selectedQuantity
            global totalPrice
            global hello
            selectedModel=[]
            selectedQuantity=[]
            selectedPrice=[]
            totalPrice=[]

            QuantityOfM=str(QuantityM.get())
            QuantityOfR=str(QuantityR.get())
            QuantityOfH=str(QuantityH.get())

            while len(QuantityOfM)==0 or len(QuantityOfR)==0 or len(QuantityOfH)==0:
                tkMessageBox.showinfo("Failed", "Please enter your data!")
                return
        
            #Test the quantity is a number
            Place=0
            while Place< len(QuantityOfM):
                digit=0
                while QuantityOfM[Place] != str(digit):
                    if str(digit)=="10":
                        tkMessageBox.showinfo("Failed","Enter the quantity.")
                        return
                        digit=0
                    else:
                        digit=digit+1
                if str(digit) =="10":
                    Place=0
                else:
                    Place=Place+1
            #Must enter less than or equal 200
            if int(QuantityOfM)>200:
                tkMessageBox.showinfo("Failed","Enter the quantity below 200.")
                return
            
            #Test the quantity is a number
            Place=0
            while Place< len(QuantityOfR):
                digit=0
                while QuantityOfR[Place] != str(digit):
                    if str(digit)=="10":
                        tkMessageBox.showinfo("Failed","Enter the quantity.")
                        return
                        digit=0
                    else:
                        digit=digit+1
                if str(digit) =="10":
                    Place=0
                else:
                    Place=Place+1
            #Must enter less than or equal 200
            if int(QuantityOfR)>200:
                tkMessageBox.showinfo("Failed","Enter the quantity below 200.")
                return
            
            #Test the quantity is a number
            Place=0
            while Place< len(QuantityOfH):
                digit=0
                while QuantityOfH[Place] != str(digit):
                    if str(digit)=="10":
                        tkMessageBox.showinfo("Failed","Enter the quantity.")
                        return
                        digit=0
                    else:
                        digit=digit+1
                if str(digit) =="10":
                    Place=0
                else:
                    Place=Place+1

            

            #Must enter less than or equal 200
            if int(QuantityOfH)>200:
                tkMessageBox.showinfo("Failed","Enter the quantity below 200.")
                return

            if int(QuantityOfM) != 0 :
                if len(ModelM.get())==0:
                    tkMessageBox.showinfo("Failed", "Please select your model !")
                    return

            if int(QuantityOfR) != 0:
                if len(ModelR.get())==0:
                    tkMessageBox.showinfo("Failed", "Please select your model !")
                    return

            if int(QuantityOfH) != 0:
                if len(ModelH.get())==0:
                    tkMessageBox.showinfo("Failed", "Please select your model !")
                    return
         

            
            
            #Straight logic
            if str(QuantityM.get())!="0":
                selectedModel=selectedModel + [ModelM.get()]
                selectedQuantity=selectedQuantity + [QuantityM.get()]
                count=0
                countBIKE=0
                while count < len(Mountainlist):
                    if selectedModel[count] == Mountainlist[countBIKE]:
                        sameElement = countBIKE
                        selectedPrice=selectedPrice + [PriceM[sameElement]]
                        countBIKE=countBIKE + 1
                    else:
                        countBIKE=countBIKE + 1
                    if countBIKE == len(Mountainlist):
                        count=count + 1
                        if count == len(selectedModel):
                            count=len(Mountainlist)
                        countBIKE=0


             
                
                        
            if str(QuantityR.get())!="0":
                selectedModel=selectedModel + [ModelR.get()]
                selectedQuantity=selectedQuantity + [QuantityR.get()]
                count=0
                countBIKE=0
                while count < len(Roadlist):
                    if selectedModel[count] == Roadlist[countBIKE]:
                        sameElement= countBIKE
                        selectedPrice=selectedPrice + [PriceR[sameElement]]
                        countBIKE=countBIKE + 1
                    else:
                        countBIKE=countBIKE + 1
                    if countBIKE == len(Roadlist):
                        count=count + 1
                        if count == len(selectedModel):
                            count=len(Roadlist)
                        countBIKE=0
             
            
          
            
            if str(QuantityH.get())!="0":
                selectedModel=selectedModel + [ModelH.get()]
                selectedQuantity=selectedQuantity + [QuantityH.get()]
                count=0
                countBIKE=0
                while count < len(Roadlist):
                    if selectedModel[count] == Hybridlist[countBIKE]:
                        sameElement= countBIKE
                        selectedPrice=selectedPrice + [PriceR[sameElement]]
                        countBIKE=countBIKE + 1
                    else:
                        countBIKE=countBIKE + 1
                    if countBIKE == len(Hybridlist):
                        count=count + 1
                        if count == len(selectedModel):
                            count=len(Hybridlist)
                        countBIKE=0
                
            print selectedModel
            print selectedPrice
            
            hello=0
            while hello < len(selectedPrice):
                calcPrice= int(selectedPrice[hello]) * int(selectedQuantity[hello])
                calcPrice=str(calcPrice)
                totalPrice=totalPrice + [calcPrice]
                hello=hello+1

            print totalPrice    

            
                
         
            
            
            
            
            counter=0
            while counter < len(selectedModel):
                tv.insert('', counter, text=(selectedModel[counter]),value=(int(selectedQuantity[counter]), int(selectedPrice[counter]), int(totalPrice[counter])))
                counter=counter+1



            btnAdd.configure(state="disabled")
            btnContinueAdd.configure(state="normal")
            btnConfirm.configure(state="normal")
            tkMessageBox.showinfo("Success", "Add Success!")
            
                


            


            




                
                
                
                
            





        #Out side Frame
        btnAdd=Button(self, text="Add to purchase",borderwidth=4, width=20,command=clickAdd)
        btnAdd.grid(row=2,column=0, sticky="w",padx=100)


        #Frame Discount
        def studentDis():
            global discount
            discount=20/100.0
            btnOld.configure(state="disable")
            btnNoDis.configure(state="disable")
            btnPrint.configure(state="normal")
        def oldcitizenDis():
            global discount
            discount=25/100.0
            btnStudent.configure(state="disable")
            btnNoDis.configure(state="disable")
            btnPrint.configure(state="normal")
        def noDis():
            global discount
            discount=0
            btnStudent.configure(state="disable")
            btnOld.configure(state="disable")
            btnPrint.configure(state="normal")
            
        labelDiscount=Label(labelframe2, text="Select Your Discount     :",pady=10)
        labelDiscount.grid(row=2,column=1,sticky='w')

        btnStudent=Button(labelframe2, text="Student Discount",borderwidth=4,pady=10,width=20,command=studentDis,state="disabled")
        btnStudent.grid(row=2,column=2,sticky="w",padx=4)

        btnOld=Button(labelframe2, text="Old Citizen Discount",borderwidth=4,pady=10,width=20,command=oldcitizenDis,state="disabled")
        btnOld.grid(row=2,column=3,sticky="w",padx=4)

        btnNoDis=Button(labelframe2, text="No Discount",borderwidth=4, pady=10,width=20,command=noDis,state="disabled")
        btnNoDis.grid(row=2,column=4,sticky="w",padx=4)

        #Frame receipt
        def clickPrint():
            global totalPayment
            btnYES.configure(state="normal")
            btnNO.configure(state="normal")


            convert=0
            totalPayment=0
            while convert < len(total):
                totalPayment= totalPayment + int(total[convert])
                convert=convert+1

            totalPayment= totalPayment -(totalPayment * discount)
            
                
                


            

            labelModel=Label(labelframe3,text="%s"% finalmodels)
            labelModel.grid(row=0,column=1,sticky="w")
                          
            labeltotalPayment=Label(labelframe3, text="RM %s"% totalPayment)
            labeltotalPayment.grid(row=2,column=1,sticky="w")
            btnPrint.configure(state="disabled")
            btnOld.configure(state="disabled")
            btnStudent.configure(state="disabled")
            btnNoDis.configure(state="disabled")

        labelModel=Label(labelframe3, text= "Your Model is                      : ")
        labelModel.grid(row=0, column=0, sticky="w",pady=10)

        labeltotalPrice=Label(labelframe3, text="Your total payment is         : ")
        labeltotalPrice.grid(row=2,column=0, sticky="w",pady=10)

        btnPrint=Button(labelframe3, text="Display Receipt",borderwidth=4,width=20,state="disable",command=clickPrint)
        btnPrint.grid(row=3,column=0, sticky="w", pady=10)

        #Frame email

        def clickYes():
            btnSend.configure(state="normal")
            entryEmail.configure(state="normal")
            btnBACK.configure(state="disabled")
            btnEXIT.configure(state="disabled")

        def clickNo():
            btnSend.configure(state="normal")
            entryEmail.configure(state="disabled")
            btnBACK.configure(state="normal")
            btnEXIT.configure(state="normal")
            btnSend.configure(state="disabled")

        def sendmail():
            x=entryEmail.get()
            gmail_sender='songsengyap@gmail.com'
            gmail_passwd='yap71104'
            SUBJECT = "Receipt From Bicycle Sale Store"
            TEXT = "Please come again"
            TEXT1 = "Thank You For Coming \n\n The bicycle you bought :%s \n\n" % finalmodels
            TEXT2="Total Payment :%s \n\n"%totalPayment
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(gmail_sender,gmail_passwd)

            BODY = '\r\n'.join(['To: %s' % x,
                                 'From: %s' % gmail_sender,
                                 'Subject: %s' % SUBJECT,
                                 '', TEXT,TEXT1,TEXT2])

            try:
                server.sendmail(gmail_sender,x,BODY)
                print 'email sent'
                tkMessageBox.showinfo("Success","Message Sent,Please come again!")
                btnBACK.configure(state="normal")
                btnEXIT.configure(state="normal")
            except:
                print'error'
                tkMessageBox.showinfo("Send Failed","Failed,Please enter a valid email!")
                btnBACK.configure(state="disabled")
                btnEXIT.configure(state="disabled")   
            server.quit()
            btnSend.configure(state="disabled")
            btnBACK.configure(state="normal")
            btnEXIT.configure(state="normal")

            
        def btnYESemail():
            btnBACK.configure(state="disabled")
            btnEXIT.configure(state="disabled")
            entryEmail.configure(state="normal")
            btnSend.configure(state="normal")
        def btnNOemail():
            entryEmail.configure(state="disabled")
            btnSend.configure(state="disabled")
            btnBACK.configure(state="normal")
            btnEXIT.configure(state="normal")
        

          

        labelAsking=Label(labelframe4, text="Do you want receipt in email     :")
        labelAsking.grid(row=0,column=0,sticky="w")

        btnYES=Button(labelframe4, text="Yes",borderwidth=4,width=20,state=DISABLED,command=btnYESemail)
        btnYES.grid(row=0,column=1, sticky="w",padx=15)

        btnNO=Button(labelframe4, text="No",borderwidth=4,width=20,state=DISABLED,command=btnNOemail)
        btnNO.grid(row=0,column=2, sticky="w",padx=15)

        labelEmail=Label(labelframe4, text="Email Address                               :")
        labelEmail.grid(row=1,column=0, sticky="w",pady=10)

        email=StringVar()
        entryEmail=Entry(labelframe4, textvariable=email,width=25,state=DISABLED)
        entryEmail.grid(row=1,column=1, sticky="w",padx=15)

        btnSend=Button(labelframe4, text="Send", width=20, borderwidth=4,command=sendmail, state=DISABLED)
        btnSend.grid(row=1,column=2,sticky="w",padx=15)

        #outside frame
        def clickExit():
            app.destroy()
        def back():
            controller.show_frame("menu")
            QuantityM.delete(0, 'end')
            QuantityR.delete(0, 'end')
            QuantityH.delete(0, 'end')
            btnAdd.configure(state="normal")
            map(tv.delete, tv.get_children())
            entryEmail.configure(state="disabled")
            entryEmail.delete(0, 'end')
            btnBACK.configure(state="disabled")
            btnEXIT.configure(state="disabled")
            btnYES.configure(state="disabled")
            btnNO.configure(state="disabled")
            labelModel=Label(labelframe3,text="                                                                                                                                ")
            labelModel.grid(row=0,column=1,sticky="w")
            labeltotalPayment=Label(labelframe3, text="                                                                                                                     ")
            labeltotalPayment.grid(row=2,column=1,sticky="w")
            QuantityM.insert(0,0)
            QuantityR.insert(0,0)
            QuantityH.insert(0,0)
            global finalmodels
            global allPrice
            global total
            finalmodels=[]
            allPrice=[]
            total=[]
            
            



        btnBACK=Button(self, text="Back",width=20, borderwidth=4,command=back,state=DISABLED)
        btnBACK.grid(row=6,column=0,sticky="w",padx=637,pady=10)

        btnEXIT=Button(self, text="Exit", width=20, borderwidth=4,command=clickExit,state=DISABLED)
        btnEXIT.grid(row=6,column=0,sticky="w",padx=837,pady=10)

        #Treeview frame
        tv = ttk.Treeview(labelframe5)
        tv['columns']= ('Quantity',"Original Price","Total Price")
        tv.heading("#0", text='Model', anchor='w')
        tv.heading('Quantity', text='Quantity')
        tv.heading('Original Price', text='Original Price')
        tv.heading('Total Price', text='Total Price')

        tv.column("#0", anchor="w",stretch = 0, width = 200)
        tv.column('Quantity', anchor='center',stretch = 0, width = 100)
        tv.column('Original Price', anchor='center', stretch = 0, width = 100)
        tv.column('Total Price', anchor='center', stretch = 0, width = 100)
        tv.grid(row=1,column=0,sticky="w",pady=10)

        
        def clickContinue():
            global total
            global finalmodels
            global allPrice
            btnAdd.configure(state="normal")
            btnContinueAdd.configure(state="disabled")
            btnConfirm.configure(state="disabled")
            element=0
            while element < len(selectedModel):
                finalmodels=finalmodels+ [selectedModel[element]]
                total= total +[totalPrice[element]]
                element = element +1

            
      
                
               
            
        
        def clickConfirm():
            global finalmodels
            global totalPrice
            global total
            btnAdd.configure(state="disabled")
            btnContinueAdd.configure(state="disabled")

            counter=0
            while counter < len(totalPrice):
                total= total +[totalPrice[counter]]
                counter=counter+1
            testing=0
            while testing < len(selectedModel):
                finalmodels=finalmodels+ [selectedModel[testing]]
                testing = testing +1
            btnOld.configure(state="normal")
            btnStudent.configure(state="normal")
            btnNoDis.configure(state="normal")
            btnConfirm.configure(state="disabled")
                
        


        btnContinueAdd=Button(labelframe5, text="Cotinue Add",borderwidth=4,width=20,command=clickContinue,state="disabled")
        btnContinueAdd.grid(row=2,column=0,sticky="w")

        btnConfirm=Button(labelframe5, text="Confirm",borderwidth=4,width=20,command=clickConfirm,state="disabled")
        btnConfirm.grid(row=2, column=0,padx=170 ,sticky="w")
                                                    

 





if __name__ == "__main__":
    app = SampleApp()
    
    app.title('Bicycle Sale System')
    app.geometry("1280x600")
    app.mainloop()

   
