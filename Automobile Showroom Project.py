'''toyata,mahindra,mercedes
take the input from user for the car company name and in the input msg give the user the 3 options companies this company name goes as the input/argument to model name function,
which welcomes the user accordingly to the company name.ask the user to enter the specific model name for that company,gns,svegan.,cdi
the 2nd fun who name is variant . according to the company name and car model the user should be asked to enter the variant he would like to choose from petrol,disel
the  3rd fun display according to the car company ,car model name and car variant first its ex showroom price should be displayed and thenn its onroad price should be displayed ,
 which is calculated as ex showrrom price +cgst+sgst+insurance.#sgst cgst and insurance all the 3 have a common value throughout the showroom.'''
class model:
    def _init_(self):
        self.ip=input("enter your name:")
        print("hello!",self.ip,"please select the company")
        print("1.toyota 2.mahindra 3.mercedes")
    def check(self):
         while True:
            print("enter car company name or enter option:")
            self.a=input("")
            if(self.a=="toyota" or self.a=="mahe\indra" or self.a=="mercedes" or self.a=="1" or self.a=="2" or self.a=="3"):
                break
            else:
                print("invalid company name or invalid option name")
    def modelsel(self):
        if(self.a=="1" or self.a=="toyota"):
            print("welcome to toyota family")
        elif(self.a=="2" or self.a=="mahendra"):
            print("welcome to mahindra family")
        else:
            print("welcome to mercedes family")
        print("please select the model of",self.a,"company")
        if(self.a=="1" or self.a=="toyota"):
            print("1.innova 2.maruti 3.audi")
            print("enter car model:")
        elif(self.a=="2" or self.a=="mahindra"):
            print("1.Mahindra Scorpio 2.Mahindra Thar 3.Mahindra Bolero")
            print("enter car model:")
        else:
            print("1.gwagon 2.glc 3.benz")
            print("enter car model:")
            
    def checks(self):       
        while True:
            self.b=input("")
            if(self.b=="innova" or self.b=="maruti" or self.b=="audi" or self.b=="1" or self.b=="2" or self.b=="3" or self.b=="Mahendra Scorpio" or self.b=="Mahendra Thar" or self.b=="Manhendra Bolero" or self.b=="gvegan" or self.b=="benz" or self.b=="glc"):
                break
            else:
                print("invalid model name or invalid option")
    def varient(self):
        print("please choose your required varient")
        print("1.petrol 2.diesel")
    def  checkss(self):
        while True:
            self.c=input("enter varient/option:")
            if(self.c=="petrol" or self.c=="diesel" or self.c=="1" or self.c=="2"):
                break
            else:
                print("invalid varient or option")
    def shprice(self):
        if(self.a=="toyota" or self.a=="1"):
            if(self.b=="innova" or self.b=="1"):
                if(self.c=="petrol" or self.c=="1"):
                    self.sp=12000
                    self.cgst=(self.sp)*0.2
                    self.sgst=(self.sp)*0.2
                    self.ins=(self.sp)*0.2
                    print(self.sp+self.cgst+self.sgst+self.ins)
                else:
                    self.sp=15000
                    self.cgst=(self.sp)*0.2
                    self.sgst=(self.sp)*0.2
                    self.ins=(self.sp)*0.2
                    print(self.sp+self.cgst+self.ins+self.sgst)
            elif(self.b=="maruti" or self.b=="2"):
                if(self.c=="petrol" or self.c=="1"):
                    self.sp=50000
                    self.cgst=(self.sp)*0.3
                    self.sgst=(self.sp)*0.3
                    self.ins=(self.sp)*0.3
                    print(self.sp+self.cgst+self.sgst+self.ins)
                else:
                    self.sp=15000
                    self.cgst=(self.sp)*0.2
                    self.sgst=(self.sp)*0.2
                    self.ins=(self.sp)*0.2
                    print(self.sp+self.cgst+self.ins+self.sgst)
            else:
                if(self.c=="petrol" or self.c=="1"):
                    self.sp=60000
                    self.cgst=(self.sp)*0.25
                    self.sgst=(self.sp)*0.25
                    self.ins=(self.sp)*0.25
                    print(self.sp+self.cgst+self.sgst+self.ins)
                else:
                    self.sp=55000
                    self.cgst=(self.sp)*0.25
                    self.sgst=(self.sp)*0.25
                    self.ins=(self.sp)*0.25
                    print(self.sp+self.cgst+self.ins+self.sgst)
        elif(self.a=="mahindra" or self.a=="2"):
            if(self.b=="Mahindra Scorpio" or self.b=="1"):
                if(self.c=="petrol" or self.c=="1"):
                    self.sp=70000
                    self.cgst=(self.sp)*0.3
                    self.sgst=(self.sp)*0.3
                    self.ins=(self.sp)*0.3
                    print(self.sp+self.cgst+self.sgst+self.ins)
                else:
                    self.sp=75000
                    self.cgst=(self.sp)*0.4
                    self.sgst=(self.sp)*0.4
                    self.ins=(self.sp)*0.4
                    print(self.sp+self.cgst+self.ins+self.sgst)
            elif(self.b=="Mahindra Thar" or self.b=="2"):
                if(self.c=="petrol" or self.c=="1"):
                    self.sp=28000
                    self.cgst=(self.sp)*0.21
                    self.sgst=(self.sp)*0.21
                    self.ins=(self.sp)*0.21
                    print(self.sp+self.cgst+self.sgst+self.ins)
                else:
                    self.sp=22000
                    self.cgst=(self.sp)*0.19
                    self.sgst=(self.sp)*0.19
                    self.ins=(self.sp)*0.19
                    print(self.sp+self.cgst+self.ins+self.sgst)
            else:
                if(self.c=="petrol" or self.c=="1"):
                    self.sp=38000
                    self.cgst=(self.sp)*0.3
                    self.sgst=(self.sp)*0.3
                    self.ins=(self.sp)*0.3
                    print(self.sp+self.cgst+self.sgst+self.ins)
                else:
                    self.sp=32000
                    self.cgst=(self.sp)*0.2
                    self.sgst=(self.sp)*0.2
                    self.ins=(self.sp)*0.2
                    print(self.sp+self.cgst+self.ins+self.sgst)
        else:
            if(self.b=="benz" or self.b=="1"):
                if(self.c=="petrol" or self.c=="1"):
                    self.sp=68000
                    self.cgst=(self.sp)*0.35
                    self.sgst=(self.sp)*0.35
                    self.ins=(self.sp)*0.35
                    print(self.sp+self.cgst+self.sgst+self.ins)
                else:
                    self.sp=63000
                    self.cgst=(self.sp)*0.3
                    self.sgst=(self.sp)*0.3
                    self.ins=(self.sp)*0.3
                    print(self.sp+self.cgst+self.ins+self.sgst)
            elif(self.b=="glc" or self.b=="2"):
                if(self.c=="petrol" or self.c=="1"):
                    self.sp=46000
                    self.cgst=(self.sp)*0.15
                    self.sgst=(self.sp)*0.15
                    self.ins=(self.sp)*0.15
                    print(self.sp+self.cgst+self.sgst+self.ins)
                else:
                    self.sp=48299
                    self.cgst=(self.sp)*0.23
                    self.sgst=(self.sp)*0.23
                    self.ins=(self.sp)*0.23
                    print(self.sp+self.cgst+self.ins+self.sgst)
            else:
                if(self.c=="petrol" or self.c=="1"):
                    self.sp=50000
                    self.cgst=(self.sp)*0.32
                    self.sgst=(self.sp)*0.32
                    self.ins=(self.sp)*0.32
                    print(self.sp+self.cgst+self.sgst+self.ins)
                else:
                    self.sp=48000
                    self.cgst=(self.sp)*0.26
                    self.sgst=(self.sp)*0.26
                    self.ins=(self.sp)*0.26
                    print(self.sp+self.cgst+self.ins+self.sgst)
obj=model()
obj.check()
obj.modelsel()
obj.checks()
obj.varient()
obj.checkss()
obj.shprice()
