def button_val(switch):#func  for getting the value of the switch ,called in the command of a switch
    value=switch.cget("text")
    current_val=entry.cget("text")
    entry.insert(tk.END,current_val+value)
    entry.icursor(tk.END)
def clr(entry):
    current_val=entry.cget("text")
    ind=int(len(entr))#index of last number to be delted using clear button 
    entry.delete(len(int(entry.cget("text"))-1),tk.END)
    
    

    
    
    
def display():
    global entry
    entry=tk .Entry(window,width=15,font=("Arial", 24),borderwidth=2,relief="solid")
    entry.grid(row=0,column=0,sticky="nsew")
def buttons(val,row,column):
    switch=tk.Button(frame_window,text=str(val),bg="#CCFF00",font="22",command=lambda:button_val(switch))
    equal_switch=tk.Button(frame_window,text="=",bg="#87CEEB",font="22",command=lambda:execute())
    equal_switch.grid(row=4,column=2,sticky ="nsew")
    clr_switch=tk.Button(frame_window,text="clear",bg="#CCFF00",font="22",command=lambda:clr())
    clr_switch.grid(row=5,columnspan="3",sticky="nsew")
    clr_switch.rowconfigure(1,weight=1)
    
    
    switch.grid(row=row,column=column,sticky="nsew")
buttons_pos=[[9,0,0],[8,0,1],[7,0,2],
             [6,1,0],[5,1,1],[4,1,2],
             [3,2,0],[2,2,1],[1,2,2],
             ["+",3,0],[0,3,1],["-",3,2],
             ["x",4,0],["÷",4,1]]#["=",4,2]], have to decalre = seperately to do its function 

def clr():
    entry.delete(0,tk.END)   
def execute():#func for showing ans by updating the entry window 
    try:
        ans=entry.get()
        ans=ans.replace("x","*").replace("÷","/")
        ans=eval(ans)
        entry.delete(0,tk.END)
        entry.insert(tk.END,str(ans))
    except Exception as e:
            entry.delete(0,tk.END)
            entry.insert(tk.END,f"error:{e}")
        
          
    
import tkinter as tk
window=tk.Tk()
window.title("CALCULATOR")
window.geometry("230x260")
entry=tk.Entry(window,width=20,font=("ARIAL",20),borderwidth=2)
entry.grid(row=0,column=0,sticky="nsew")
frame_window=tk.Frame(window,bg="lightblue",bd=2)
frame_window.grid(row=1,column=0,columnspan=4,sticky="nsew")
for k in range(5):
    frame_window.rowconfigure(k,weight=1)
    frame_window.columnconfigure(k,weight=1)

display()
for i in(buttons_pos):
    buttons(i[0],i[1],i[2])
    
tk.mainloop()


    

    