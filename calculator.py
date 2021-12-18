import tkinter as tk

def equal():
 try:
    global expression
    global label1Text 
    result = str(eval(expression))
    expression = result
 except:
    result = 'ERROR'
    expression = ''
 label1Text.set(result)

def press(n):
 global expression
 global label1Text 
 expression = expression+n
 label1Text.set(expression)

def clear() :
  global expression
  global label1text 
  expression = ''
  label1Text.set(str(expression))

m=tk.Tk()
m.title('calculatood')

expression = ''
label1Text=tk.StringVar()
label1Text.set(expression)

#number

label1 = tk.Label(m, borderwidth=10, bg="white",fg='black', relief='ridge', textvariable=label1Text, width=40,height=1)
label1.grid(row=0, columnspan=5)

button1 = tk.Button(m,text=1,width=5,command=lambda:press('1'))
button1.grid(row=1,column=0)

button2 = tk.Button(m,text=2,width=5,command=lambda:press('2'))
button2.grid(row=1,column=1)

button3=tk.Button(m,text=3,width=5,command=lambda:press('3'))
button3.grid(row=1,column=2)

button4=tk.Button(m,text=4,width=5,command=lambda:press('4'))
button4.grid(row=2,column=0)

button5=tk.Button(m,text=5,width=5,command=lambda:press('5'))
button5.grid(row=2,column=1)

button6=tk.Button(m,text=6,width=5,command=lambda:press('6'))
button6.grid(row=2,column=2)

button7=tk.Button(m,text=7,width=5,command=lambda:press('7'))
button7.grid(row=3,column=0)

button8=tk.Button(m,text=8,width=5,command=lambda:press('8'))
button8.grid(row=3,column=1)

button9=tk.Button(m,text=9,width=5,command=lambda:press('9'))
button9.grid(row=3,column=2)

button10=tk.Button(m,text=0,width=5,command=lambda:press('0'))
button10.grid(row=4,column=1)

button10 = tk.Button(m,text='00',width=5,command=lambda:press("00"))
button10.grid(row=4,column=0)

#operator

button11 = tk.Button(m, text='.',width=5,command=lambda:press('.'))
button11.grid(row=4, column=2)

button12 = tk.Button(m,text='CE',width=5,command=lambda:clear())
button12.grid(row=5,column=2)

button13 = tk.Button(m,text='=',width=14,command=lambda:equal())
button13.grid(row=5,column=3,columnspan=2)

button14 = tk.Button(m,text='+',width=5,command=lambda:press("+"))
button14.grid(row=1,column=3)

button15 = tk.Button(m,text='-',width=5,command=lambda:press("-"))
button15.grid(row=2,column=3)

button16 = tk.Button(m,text='x',width=5,command=lambda:press("*"))
button16.grid(row=3,column=3)

button17 = tk.Button(m,text='÷',width=5,command=lambda:press("/"))
button17.grid(row=4,column=3)

button18 = tk.Button(m,text='xᵃ',width=5,command=lambda:press(""))
button18.grid(row=1,column=4)

button19 = tk.Button(m,text='√x',width=5,command=lambda:press("(1/2)"))
button19.grid(row=2, column=4)

button20 = tk.Button(m,text='(',width=5,command=lambda:press("("))
button20.grid(row=5,column=0)

button21 = tk.Button(m,text=')',width=5,command=lambda:press(")"))
button21.grid(row=5,column=1)

button22 = tk.Button(m,text='CLOSE',width=5,command=lambda:m.destroy())
button22.grid(row=4,column=4)

button23 = tk.Button(m,text='π',width=5,command=lambda:press("22/7"))
button23.grid(row=3,column=4)

m.mainloop()
