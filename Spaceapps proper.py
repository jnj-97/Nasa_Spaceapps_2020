
from tkinter import *
from PIL import ImageTk,Image
Sleep_times=[]
Nutrition_times=[]
Exercise_times=[]
Integers=[]
Heights=[]
Ages=[]
def set_times():
        Sleep_times.append((sleep_input.get()))
        Exercise_times.append((Exercise_input.get()))
        if len(Sleep_times)==1:
           pass
        elif((int((Sleep_times[-2])[:2]))-(int((Sleep_times[-1])[:2]))>4 or (int((Sleep_times[-2])[:2]))-(int((Sleep_times[-1])[:2]))<-4):
            Sleep_times.pop(-1)
            Error=Label(window,text="Sleep shift is too high. Please try again").place(x=100,y=500)
        if(len(Sleep_times)==7):
            Integers.append((int(Integer.get())))
            Heights.append((int(Height_input.get())))
            Ages.append((int(Age_input.get())))
            window.destroy()
            Schedule()
        
def Schedule():
    count=0
    Schedule=Tk()
    Schedule.geometry("1000x600")   
    Schedule.title("Schedule")
    x_coordinate=53 
    im1 = Image.open("Untitled-1.jpg")
    im=im1.resize((1000,600))
    ph = ImageTk.PhotoImage(im)
    background_label=Label(Schedule, image=ph).place(x=0, y=0, relwidth=1, relheight=1)
    im2 = Image.open("blue.jpg")
    im3=im2.resize((133,193))
    im4 = ImageTk.PhotoImage(im3)
    im20=im2.resize((20,20))
    im21=ImageTk.PhotoImage(im20)
    blue_label=Label(Schedule,text="-SLEEP").place(x=70,y=550)   
    im22=Image.open('yellow.png')
    im23=im22.resize((20,20))
    im24=ImageTk.PhotoImage(im23)
    Key_yellow=Label(Schedule,image=im24).place(x=120,y=550)
    yellow_label=Label(Schedule,text='-EXERCISE').place(x=140,y=550)
    Key_blue=Label(Schedule,image=im21).place(x=50,y=550)
    im10=Image.open("yellow.png")
    im11=im10.resize((133,70))
    yellow=ImageTk.PhotoImage(im11)
    while(count<=6):
        if(int((Sleep_times[count])[:2])==00):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=31)  
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=21)
        elif((Sleep_times[count])[:2]=='01'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=54)  
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=44)
        elif((Sleep_times[count])[:2]=='02'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=78)  
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=68)
        elif((Sleep_times[count])[:2]=='03'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=102)  
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=92)
        elif((Sleep_times[count])[:2]=='04'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=126)  
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=116)
        elif((Sleep_times[count])[:2]=='03'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=150)  
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=140)
        elif((Sleep_times[count])[:2]=='04'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=174)  
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=164)
        elif((Sleep_times[count])[:2]=='05'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=198)  
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=188)
        elif((Sleep_times[count])[:2]=='06'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=212)  
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=202)
        elif((Sleep_times[count])[:2]=='07'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=236)  
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=226)
        elif((Sleep_times[count])[:2]=='08'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=260)  
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=250)
        elif((Sleep_times[count])[:2]=='09'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=284)  
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=274)
        elif((Sleep_times[count])[:2]=='10'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=308)  
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=298)
        elif((Sleep_times[count])[:2]=='11'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=332)  
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=322)
        elif((Sleep_times[count])[:2]=='12'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=356)  
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=346)  
        elif((Sleep_times[count])[:2]=='13'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=370)  
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=360)
        elif((Sleep_times[count])[:2]=='14'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=394)  
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=384)
        elif((Sleep_times[count])[:2]=='15'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=418)  
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=408)
        elif((Sleep_times[count])[:2]=='16'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=442)
                im5=im2.resize((133,10))
                im6=ImageTk.PhotoImage(im5)
                blue_image2=Label(Schedule,image=im6)
                blue_image2.place(x=x_coordinate+135,y=21)
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=432)
        elif((Sleep_times[count])[:2]=='17'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=442)
                im5=im2.resize((133,30))
                im6=ImageTk.PhotoImage(im5)
                blue_image2=Label(Schedule,image=im6)
                blue_image2.place(x=x_coordinate+135,y=21)
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=432)
                im5=im2.resize((133,20))
                im6=ImageTk.PhotoImage(im5)
                blue_image2=Label(Schedule,image=im6)
                blue_image2.place(x=x_coordinate+135,y=21)
        elif((Sleep_times[count])[:2]=='18'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=466)
                im5=im2.resize((133,50))
                im6=ImageTk.PhotoImage(im5)
                blue_image2=Label(Schedule,image=im6)
                blue_image2.place(x=x_coordinate+135,y=21)
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=456)
                im5=im2.resize((133,40))
                im6=ImageTk.PhotoImage(im5)
                blue_image2=Label(Schedule,image=im6)
                blue_image2.place(x=x_coordinate+135,y=21)
        elif((Sleep_times[count])[:2]=='19'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=490)
                im5=im2.resize((133,70))
                im6=ImageTk.PhotoImage(im5)
                blue_image2=Label(Schedule,image=im6)
                blue_image2.place(x=x_coordinate+135,y=21)
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=480)
                im5=im2.resize((133,60))
                im6=ImageTk.PhotoImage(im5)
                blue_image2=Label(Schedule,image=im6)
                blue_image2.place(x=x_coordinate+135,y=21)
        elif((Sleep_times[count])[:2]=='20'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=514)
                im5=im2.resize((133,90))
                im6=ImageTk.PhotoImage(im5)
                blue_image2=Label(Schedule,image=im6)
                blue_image2.place(x=x_coordinate+135,y=21)
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=504)
                im5=im2.resize((133,80))
                im6=ImageTk.PhotoImage(im5)
                blue_image2=Label(Schedule,image=im6)
                blue_image2.place(x=x_coordinate+135,y=21)
        elif((Sleep_times[count])[:2]=='21'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=538)
                im5=im2.resize((133,110))
                im6=ImageTk.PhotoImage(im5)
                blue_image2=Label(Schedule,image=im6)
                blue_image2.place(x=x_coordinate+135,y=21)
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=528)
                im5=im2.resize((133,100))
                im6=ImageTk.PhotoImage(im5)
                blue_image2=Label(Schedule,image=im6)
                blue_image2.place(x=x_coordinate+135,y=21)
        elif((Sleep_times[count])[:2]=='22'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=562)
                im5=im2.resize((133,130))
                im6=ImageTk.PhotoImage(im5)
                blue_image2=Label(Schedule,image=im6)
                blue_image2.place(x=x_coordinate+135,y=21)
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=552)
                im5=im2.resize((133,120))
                im6=ImageTk.PhotoImage(im5)
                blue_image2=Label(Schedule,image=im6)
                blue_image2.place(x=x_coordinate+135,y=21)
        elif((Sleep_times[count])[:2]=='23'):
            if((int((Sleep_times[count])[3:5]))==30):
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=576)
                im5=im2.resize((133,150))
                im6=ImageTk.PhotoImage(im5)
                blue_image2=Label(Schedule,image=im6)
                blue_image2.place(x=x_coordinate+135,y=21)
            else:
                blue_image=Label(Schedule,image=im4)
                blue_image.place(x=x_coordinate,y=566)
                im5=im2.resize((133,140))
                im6=ImageTk.PhotoImage(im5)
                blue_image2=Label(Schedule,image=im6)
                blue_image2.place(x=x_coordinate+135,y=21)
        if((Exercise_times[count])[:2]=='00'):
            if((Exercise_times[count])[3:5]=='30'):
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=31)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=21)
        elif((Exercise_times[count])[:2]=='01'):
            if((Exercise_times[count])[3:5]=='30'):
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=55)
            else:
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=45)
    
        elif((Exercise_times[count])[:2]=='02'):
            if((Exercise_times[count])[3:5]=='30'):
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=79)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=69)
        
        elif((Exercise_times[count])[:2]=='03'):
            if((Exercise_times[count])[3:5]=='30'):
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=103)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=93)
        
        elif((Exercise_times[count])[:2]=='04'):
            if((Exercise_times[count])[3:5]=='30'):
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=127)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=117)
        
        elif((Exercise_times[count])[:2]=='05'):
            if((Exercise_times[count])[3:5]=='30'):
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=151)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=141)
                
        elif((Exercise_times[count])[:2]=='06'):
            if((Exercise_times[count])[3:5]=='30'):
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=175)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=165)
                
        elif((Exercise_times[count])[:2]=='07'):
            if((Exercise_times[count])[3:5]=='30'):
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=199)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=189)        
                
        elif((Exercise_times[count])[:2]=='08'):
            if((Exercise_times[count])[3:5]=='30'):
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=223)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=213)        
                
        elif((Exercise_times[count])[:2]=='09'):
            if((Exercise_times[count])[3:5]=='30'):
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=247)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=237)        
                
        elif((Exercise_times[count])[:2]=='10'):
            if((Exercise_times[count])[3:5]=='30'):
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=271)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=261)        
                
        elif((Exercise_times[count])[:2]=='11'):
            if((Exercise_times[count])[3:5]=='30'):
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=295)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=285)        
                
        elif((Exercise_times[count])[:2]=='12'):
            if((Exercise_times[count])[3:5]=='30'):
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=319)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=309)        
                
        elif((Exercise_times[count])[:2]=='13'):
            if((Exercise_times[count])[3:5]=='30'):
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=343)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=333)        
                
        elif((Exercise_times[count])[:2]=='14'):
            if((Exercise_times[count])[3:5]=='30'):
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=367)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=357)        
                
        elif((Exercise_times[count])[:2]=='15'):
            if((Exercise_times[count])[3:5]=='30'):
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=391)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=381)        
                
        elif((Exercise_times[count])[:2]=='16'):
            if((Exercise_times[count])[3:5]=='30'):
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=415)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=405)
                
        elif((Exercise_times[count])[:2]=='17'):
            if((Exercise_times[count])[3:5]=='30'):
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=439)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=429)        
                
        elif((Exercise_times[count])[:2]=='18'):
            if((Exercise_times[count])[3:5]=='30'):
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=463)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=453)       
                        
        elif((Exercise_times[count])[:2]=='19'):
            if((Exercise_times[count])[3:5]=='30'):
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=487)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=477) 
                
        elif((Exercise_times[count])[:2]=='20'):
            if((Exercise_times[count])[3:5]=='30'):
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=511)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=501)
                
        elif((Exercise_times[count])[:2]=='21'):
            if((Exercise_times[count])[3:5]=='30'):
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=535)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=525)        
                
        elif((Exercise_times[count])[:2]=='22'):
            if((Exercise_times[count])[3:5]=='30'):
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=573)
                image=Image.open("yellow.png")
                im7=image.resize((133,10))
                im6=ImageTk.PhotoImage(im7)
                yellow_image2=Label(Schedule,image=im6)
                yellow_image2.place(x=x_coordinate+135,y=21)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=549)
        elif((Exercise_times[count])[:2]=='23'):
            if((Exercise_times[count])[3:5]=='30'):
                 yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=585)
                 image=Image.open("yellow.png")
                 im7=image.resize((133,34))
                 im6=ImageTk.PhotoImage(im7)
                 yellow_image2=Label(Schedule,image=im6)
                 yellow_image2.place(x=x_coordinate+135,y=21)
            else:
                yellow_image=Label(Schedule,image=yellow).place(x=x_coordinate,y=575)
                image=Image.open("yellow.png")
                im7=image.resize((133,24))
                im6=ImageTk.PhotoImage(im7)
                yellow_image2=Label(Schedule,image=im6)
                yellow_image2.place(x=x_coordinate+135,y=21)
        x_coordinate=x_coordinate+135
        count=count+1
    if(Gender_input.get()=='Male'):
        BEE= 66 + (13.7 * Integers[0]) + (5 * Heights[0]) - (6.8 * Ages[0])
        Nutrition=Label(Schedule,text="Daily Nutrition Consumption={} kcal/day".format(BEE)).place(x=200,y=650)
    elif(Gender_input.get()=='Female'):
        BEE= 655 + (9.6 * Integers[0]) + (1.7 * Heights[0]) - (4.7 * Ages[0])
        Nutrition=Label(Schedule,text="Daily Nutrition Consumption={} kcal/day".format(BEE)).place(x=200,y=650)            
    Schedule.mainloop()

    
window=Tk()
window.title("Sleep Shift Scheduling Tool")
window.geometry("1000x600")
im1=Image.open('Background.jpg')
im=im1.resize((1000,600))
ph = ImageTk.PhotoImage(im)
background_label=Label(window, image=ph).place(x=0, y=0, relwidth=1, relheight=1)

Heading=Label(window, text='SLEEP SHIFT SCHEDULING TOOL',font='Helvetica 18 bold',bg='black',fg='white').grid(row=0,column=0)
window.columnconfigure(0, weight=1)
times=['00:00','00:30','01:00','01:30','02:00','02:30','03:00','03:30','04:00','04:30','05:00','05:30','06:00','06:30','07:00','07:30','08:00','08:30','09:00','09:30','10:00','10:30','11:00','11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00','17:30','18:00','18:30','19:00','19:30','20:00','20:30','21:00','21:30','22:00','22:30','23:00','23:30']
age=[]
for integer in range(20,101):
    age.append(integer)
height=[]
for integer in range(149,194):
    height.append(integer)
weight=[]
for  integer in range(30, 151):
    weight.append(integer)  
Gender_list=['Male','Female']
Sleep=Label(window,text="When do you want to sleep(please enter in HH:MM format)",font='Arial 11',fg='white',bg='black').place(x=10,y=100)
sleep_input=StringVar()
option=OptionMenu(window,sleep_input,*times)
sleep_input.set(times[0])
option['highlightthickness']=0
option['borderwidth']=0
option.config(bg="grey")
option.place(x=10,y=130)
# sleep_select=Button(window,bg='black',text='SELECT',fg='white').place(x=60,y=130)
Gender=Label(window,text="Select your gender",font='Arial 11',fg='white',bg='black').place(x=10,y=180)
Gender_input=StringVar()
gender=OptionMenu(window,Gender_input,*Gender_list)
gender['highlightthickness']=0
gender['borderwidth']=0
gender.config(bg="grey")
gender.place(x=10,y=210)
Weight=Label(window,text="Select your Weight",font='Arial 11',fg='white',bg='black').place(x=10,y=250)
Integer=StringVar()
Weight=OptionMenu(window,Integer,*times)
Integer.set(weight[0])
# select1=Button(window,text='SELECT',bg='black',fg='white').place(x=60,y=210)
Weight['highlightthickness']=0
Weight['borderwidth']=0
Weight.config(bg="grey")
Weight.place(x=10,y=280)
# Select2=Button(window,text='SELECT',bg='black',fg='white').place(x=60,y=280)
Height=Label(window,text="Select your Height",font='Arial 11',fg='white',bg='black').place(x=10,y=330)
Height_input=StringVar()
Height=OptionMenu(window,Height_input,*height)
Height_input.set(height[0])
Height['highlightthickness']=0
Height['borderwidth']=0
Height.config(bg="grey")
Height.place(x=10,y=360)
# Select3=Button(window,text='SELECT',bg='black',fg='white').place(x=60,y=360)
Age=Label(window,text="Select your Age",font='Arial 11',fg='white',bg='black').place(x=10,y=400)
Age_input=StringVar()
Age_menu=OptionMenu(window,Age_input,*age)
Age_input.set(age[0])
Age_menu['highlightthickness']=0
Age_menu['borderwidth']=0
Age_menu.config(bg="grey")
Age_menu.place(x=10,y=430)
# Seclect4=Button(window,text='SELECT',bg='black',fg='white').place(x=60,y=430)
# sleep_select=Button(window,bg='black',text='SELECT',fg='white').place(x=60,y=130)
Exercise=Label(window,bg='black',fg='white',text="What time do you want to Exercise").place(x=10,y=470)
Exercise_input=StringVar()
Exercise_menu=OptionMenu(window,Exercise_input,*times)
Exercise_input.set(times[0])
Exercise_menu['highlightthickness']=0
Exercise_menu['borderwidth']=0
Exercise_menu.config(bg="grey")
Exercise_menu.place(x=10,y=500)
Select5=Button(window,text='SELECT TIME',bg='black',fg='white',command=set_times).place(x=100,y=550)
window.mainloop()    

  