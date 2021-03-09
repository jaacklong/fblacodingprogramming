import tkinter as tk
import random, webbrowser, os
from datetime import datetime
from fpdf import FPDF
from time import sleep
class Question:
     def __init__(self, type, prompt, choices, correct):
          self.prompt = prompt.strip("\n")
          self.type = type.strip("\n")
          self.choices = choices
          self.correct = correct.strip("\n")
          self.selected = -1

     def set_type(self, new):
          self.type = new
     def set_prompt(self, new):
          self.prompt = new
     def set_choices(self, new):
          self.choices = new
     def set_correct(self, new):
          self.correct = new
     def set_selected(self, new):
          self.selected = new
          print("selected button is now " + str(self.selected))
     def get_selected(self):
          return self.selected
     def get_type(self):
          return self.type
     def get_prompt(self):
          return self.prompt
     def get_choices(self):
          return self.choices
     def get_correct(self):
          return self.correct
     def check(self):
          print("submitted answer is " + str(self.selected))
          return str(self.selected).lower().strip(" ") in self.correct.lower().strip(" ")

     def str(self):
          return self.prompt+'\n'+str(self.choices)+'\n'+self.correct



def main_frames():
     # main frames
     frames['a'] = tk.Frame(master=window)
     frames['b'] = tk.Frame(master=window)



     # a subframes
     frames['a1'] = tk.Frame(master=frames['a'], bg='#00529b')
     frames['a2'] = tk.Frame(master=frames['a'])
     frames['a2a'] = tk.Frame(master=frames['a2'])
     frames['a2q'] = tk.Frame(master=frames['a2'])


     # b subframes
     frames['b1'] = tk.Frame(master=frames['b'], bg="#be2c37")
     frames['b2'] = tk.Frame(master=frames['b'])

     # a subframes pack
     frames['a1'].pack(side='top', fill='x')
     frames['a2'].pack(expand='true', fill='both')
     frames['a2a'].pack(side='right', expand='true', fill='both')
     frames['a2q'].pack(side='left', expand='true', fill='both')



     # b subframes pack
     frames['b1'].pack(side='top', fill='x')
     frames['b2'].pack(side='bottom', fill='both')

     # main frames pack
     frames['a'].pack(side='left', expand='true', fill='both')
     frames['b'].pack(side='right', expand='true', fill='both')

     # helpframes pack



     '''
     for key, value in frames.items():
          if key not in ['a', 'b', 'a2']:
               test_labels(value, key)
     '''
     topbar()
def test_labels(frame, letter):
     testlabel = tk.Label(master=frame, text = letter)
     testlabel.pack()
def topbar():
     helpbutton=tk.Button(frames['b1'], text='help', command = lambda:helpmenu(), height=2)
     title = tk.Label(master=frames['a1'], text="FBLA Quiz", font='Helvetica 24 bold', bg='#00529b', fg='white')
     title.pack()
     helpbutton.pack()
def helpmenu():
     for widget in frames['b1'].winfo_children():
          widget.destroy();
     exit = tk.Button(frames['b1'], text='x', command = lambda:exithelpmenu())
     printresults = tk.Button(frames['b1'], text="print results", command=lambda:printmenu())
     moreinfo = tk.Button(frames['b1'], text="more info", command=lambda:infomenu())

     exit.pack(side='right')
     printresults.pack(side='top')
     moreinfo.pack(side='top')
def printmenu():
     dir_path = os.path.dirname(os.path.realpath(__file__))
     print(dir_path)
     for widget in window.winfo_children():
          widget.destroy();
     frames['print'] = tk.Frame(master=window)
     frames['print'].pack(expand='true', fill='both')

     exit=tk.Button(master=frames['print'], text='x', command=lambda:exitbigmenu(), fg='red')

     printlabel = tk.Label(master=frames['print'], text='GENERATE PRINTABLE REPORT', font='Helvetica 18 bold')
     pdf = tk.Button(master=frames['print'],text='.pdf',
                     command = lambda: webbrowser.open('file://'+dir_path+'/results.pdf'))
     txt = tk.Button(master=frames['print'], text='.txt',
                     command = lambda: webbrowser.open('file://'+dir_path+'/results.txt'))

     exit.pack(side='top', anchor='nw')
     tk.Label(master=frames['print'], text='PRINT RESULTS').pack()
     printlabel.pack()
     txt2pdf()
     pdf.pack()
     txt.pack()
def txt2pdf():
     pdf = FPDF()
     pdf.add_page()
     pdf.set_font("Arial", size=15)
     results = open("results.txt", "r")
     for i in results:
          pdf.cell(50, 5, txt=i, ln=1.5, align='C')
     pdf.output("results.pdf")
def infomenu():
     for widget in window.winfo_children():
          widget.destroy();
     frames['info'] = tk.Frame(master=window)
     frames['info'].pack(expand='true', fill='both')

     exit = tk.Button(master=frames['info'], text='x', command=lambda: exitbigmenu(), fg='red')
     infolabel = tk.Label(master=frames['info'], text='MORE INFO')
     exit.pack(side='top', anchor='nw')
     infolabel.pack()
     tk.Label(master=frames['info'], text="Created by Jack Long, 2021", font="Helvetica 18 bold").pack()
     tk.Label(master=frames['info'], text="Built with the Tkinter GUI tooklit for Python.").pack()
     tk.Label(master=frames['info'], text="Documentation of non-standard modules used:").pack()
     label1 = tk.Label(master=frames['info'], text="fpdf", fg='blue')
     label2 = tk.Label(master=frames['info'], text="datetime", fg='blue')
     label3 = tk.Label(master=frames['info'], text="webbrowser", fg='blue')
     label4 = tk.Label(master=frames['info'], text="tkinter", fg='blue')
     modulelabels = [label1, label2, label3, label4]
     links = [
              'http://www.fpdf.org/en/doc/index.php',
              'https://docs.python.org/3/library/datetime.html',
              'https://docs.python.org/3/library/webbrowser.html',
              'https://docs.python.org/3/library/tk.html']
     for i in range(4):
          modulelabels[i].pack()
          modulelabels[i].bind("<Button-1>", lambda e: webbrowser.open(links[i]))


def exitbigmenu():
     for widget in window.winfo_children():
          widget.destroy();
     main_frames()
     if qcounter<5:
          ask_question(questions[qlist[qcounter-1]])
     else:
          writeresults()
          final_screen()


def exithelpmenu():
     for widget in frames['b1'].winfo_children():
          widget.destroy();
     for widget in frames['a1'].winfo_children():
          widget.destroy();
     topbar()
def ask_question(q):
     selected_choice = 1
     global choicebuttons, submitbutton
     choicebuttons = ['']*len(q.get_choices())

     submitbutton = tk.Button(master=frames['b2'], text='submit', command = lambda:submit(q))
     submitbutton.pack(side='right', expand='true')

     question = tk.Label(master=frames['a2q'], text=q.get_prompt(), wraplength=400)
     question.pack(side='left')
     if 'mc' in q.get_type():
          choicebuttons[0] = tk.Button(master=frames['a2a'], text=q.get_choices()[0],
                                       command=lambda: select(q,0))
          choicebuttons[1] = tk.Button(master=frames['a2a'], text=q.get_choices()[1],
                                        command=lambda: select(q,1))
          choicebuttons[2] = tk.Button(master=frames['a2a'], text=q.get_choices()[2],
                                        command=lambda: select(q,2))
          choicebuttons[3] = tk.Button(master=frames['a2a'], text=q.get_choices()[3],
                                        command=lambda: select(q,3))

          for i in choicebuttons:
               if i == choicebuttons[0]:
                    i.pack(pady=(100, 0))
               else:
                    i.pack()
     elif 'tf' in q.get_type():
          choicebuttons[0] = tk.Button(master=frames['a2a'], text=q.get_choices()[0],
                                       command=lambda: select(q,0))
          choicebuttons[1] = tk.Button(master=frames['a2a'], text=q.get_choices()[1],
                                        command=lambda: select(q,1))

          for i in choicebuttons:
               if i==choicebuttons[0]:
                    i.pack(pady=(100,0))
               else:
                    i.pack()
     elif 'fr' in q.get_type():
          qvar = tk.StringVar()
          answerbox = tk.Entry(master=frames['a2a'], textvariable=  qvar, borderwidth=2)
          answerbox.pack(pady=120)
          submitbutton.configure(command=lambda: submitfr(q, qvar.get))
     elif 'dd' in q.get_type():
          qvar = tk.StringVar(frames['a2a'])
          qprompts = { q.get_choices()[0], q.get_choices()[1], q.get_choices()[2],q.get_choices()[3]}
          answermenu = tk.OptionMenu(frames['a2a'], qvar, *qprompts)
          answermenu.pack(pady=120)
          submitbutton.configure(command=lambda: submitfr(q, qvar.get))
     else:
          print('input read wrong')
def submitfr(q, a):
     answer = a()
     try:
          answer=int(answer)
          badinputlabel = tk.Label(master=frames['a2a'], text="Please enter a set of words without digits.")
          badinputlabel.pack()
     except:
          if len(answer)<1:
               badinputlabel = tk.Label(master=frames['a2a'], text="Please input an answer.")
               badinputlabel.pack()
          else:
               q.set_selected(answer)
               submit(q)
def response(check):
     global rightcounter
     for widget in window.winfo_children():
          widget.destroy();
     frames['response'] = tk.Frame(master=window, bg='green')
     frames['response'].pack(expand='true', fill='both')
     if check:
          rightcounter+=1
          correctlabel = tk.Label(master=frames['response'], text='Correct!', bg='green', fg='white', font="Helvetica 24 bold")
          correctlabel.pack(pady=100)
     else:
          frames['response'].configure(bg='red')
          correctlabel = tk.Label(master=frames['response'], text='Incorrect!', bg='red', fg='white', font="Helvetica 24 bold")
          correctlabel.pack(pady=100)
     nextb = tk.Button(master=frames['response'], text='next',command=exitresponse)
     nextb.pack()
def exitresponse():
     global qcounter
     for widget in window.winfo_children():
          widget.destroy();
     main_frames()
     print('qcounter:%i'%qcounter)
     if qcounter<5:
          ask_question(questions[qlist[qcounter]])
          qcounter+=1
     else:
          writeresults()
          final_screen()


def submit(q):
     global qcounter, rightcounter, submitbutton
     if q.get_selected()==-1:
          errorlabel = tk.Label(master=frames['a2a'], text="Please select an answer.")
          errorlabel.pack()
     else:
          response(q.check())

def unpack():
     for widget in frames['a2a'].winfo_children():
          widget.destroy()
     for widget in frames['a2q'].winfo_children():
          widget.destroy()

     for widget in frames['b2'].winfo_children():
          widget.destroy()
     '''
     for widget in frames['a1'].winfo_children():
          widget.destroy()
     for widget in frames['b1'].winfo_children():
          widget.destroy()
     '''
def writeresults():
     global rightcounter
     resultsdata["Score"] = rightcounter
     resultsfile = open('results.txt', 'a')
     resultsfile.write("Date:%s\n" % resultsdata["Datetime"].strftime("%m/%d/%Y, %H:%M:%S"))
     resultsfile.write("Score:%s\n" % str(resultsdata['Score']))
     resultsfile.close()
def final_screen():
     frames['a'].pack_forget()
     frames['b'].pack_forget()
     tk.Label(window, text="score: %i/%i"%(rightcounter, 5)).pack()
     printb = tk.Button(master=window, text="print results", command=printmenu)
     printb.pack()
     infob = tk.Button(master=window, text="get more info", command=infomenu)
     infob.pack()

def select(q, ans):

     global choicebuttons

     if 'mc' in q.get_type() or 'tf' in q.get_type() or 'dd' in q.get_type():
          if 'mc' in q.get_type() or 'dd' in q.get_type():
               s=4
          else:
               s=2
          if choicebuttons[ans].cget("text") == 'selected':
               choicebuttons[ans].configure(text=q.get_choices()[ans])
               q.set_selected(-1)
          else:
               for answer in [(ans-1)%s, (ans-2)%s, (ans-3)%s]:
                    choicebuttons[answer].configure(text=q.get_choices()[answer])
               choicebuttons[ans].configure(text='selected')
               q.set_selected(ans)




def populate_questions():
     file = open("questions.txt", "r")
     c=0
     qtype =''
     while '~' not in qtype:
          qtype = file.readline().strip('\n')
          print('current qtype is '+qtype)
          print(type(qtype))
          qprompt = file.readline()
          qchoices = []
          if "mc" in qtype:
               print('reading mc')
               for i in range(4):
                    qchoices.append(file.readline().strip('\n'))
               qcorrect = file.readline()
               print("qcorrect is now "+qcorrect)
          elif "dd" in qtype:
               print('reading dd')
               for i in range(4):
                    qchoices.append(file.readline().strip('\n'))
               qcorrect = file.readline()
               print("qcorrect is now "+qcorrect)
          elif "tf" in qtype:
               print('reading tf')
               qchoices.append(file.readline().strip('\n'))
               qchoices.append(file.readline().strip('\n'))
               qcorrect = file.readline()
               print("qcorrect is now " + qcorrect)
          elif 'fr' in qtype:
               print('reading fr')

               qcorrect = file.readline()
               print("qcorrect is now " + qcorrect)
          else:
               print('qtype not recognized')
               qcorrect = ''
               print("qcorrect is now nothing")
          file.readline()
          questions.append(Question(qtype, qprompt, qchoices, qcorrect))
          print(questions[c].str()+'\n')
          c+=1

     file.close()
def main():
     global qcounter, resultsdata
     #start er up

     resultsdata['Datetime']= datetime.now()
     window.geometry('600x300')
     populate_questions()
     main_frames()
     ask_question(questions[qlist[qcounter]])
     qcounter+=1
     window.mainloop()

if __name__ == "__main__":
     resultsdata={}
     rightcounter=0
     qcounter=0
     qlist=random.sample(range(0,25),5)
     frames = {}
     window = tk.Tk()
     questions = []
     submitbutton = tk.Button()
     choicebuttons = []
     main()

