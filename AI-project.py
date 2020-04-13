import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from tkinter import messagebox
from tkinter import *
from matplotlib import pyplot as plt
import numpy as np 
top=Tk()
top.geometry('800x350')
top.configure(bg='light blue')
top.title('Named Entity Recognition')
gpe=[]
person=[]
org=[]
loc=[]
mon=[]
nouns=""
postags=[]
def NER(entry):
    global nouns,person,gpe,org,loc,mon
    global postags
    word_tokens=nltk.word_tokenize(entry)
    postags=nltk.pos_tag(word_tokens)
    nouns=ne_chunk(postags)
    for t in str(nouns).split("\n"):
        if "NNP" in t:
            if "PERSON" in t:
                a=t.split("/")
                b=a[0].split(" ")
                person.append(b[3])
                person=set(person)
                person=list(person)
            elif "GPE" in t:
                a=t.split("/")
                b=a[0].split(" ")
                gpe.append(b[3])
                gpe=set(gpe)
                gpe=list(gpe)
            elif "ORGANIZATION" in t:
                a=t.split("/")
                b=a[0].split(" ")
                org.append(b[3])
                org=set(org)
                org=list(org)      
            elif "LOC" in t:
                a=t.split("/")
                b=a[0].split(" ")
                loc.append(b[3])
                loc=set(loc)
                loc=list(loc)
        elif "CD" in t:
            a=t.split(" ")
            b=a[2].split("/")
            mon.append(b[0])
            mon=set(mon)
            mon=list(mon)     
    show()
    return 0
def show():
    print("--person--")
    for i in person:
        print(i)
    print("--geo political entity--")    
    for i in gpe:
        print(i)
    print("--organization--")
    for i in org:
        print(i)    
    print("--monetary values--")
    for i in mon:
        print(i)    
    print("--locations--")
    for i in loc:
        print(i)  
    messagebox.showinfo(title="terminal", message="the entities are displayed in terminal.")      
    return 0             
def fun1():
    entry=t1.get("1.0",'end-1c')
    NER(entry)
    return 0
def fun2():
    entry=t1.get("1.0",'end-1c')
    parset(entry)
    return 0    
def parset(entry):
    global nouns
    if(entry==""):
        messagebox.showerror(title="no_text", message="Please enter text to view parse tree.")
    else:
        try:
            nouns.draw()
        except(AttributeError):
            messagebox.showerror(title="Extract_first", message="Please extract the enteties first.") 
    return 0
noun=['NNS','NN','NNP','NNPS']
verb=['VB','VBN','VBD','VBG','VBP','VBZ']
adjective=['JJ','JJR','JJS']
preposition=['IN']
adverb=['RB','RBR','RBS','WRB']
article=['DT','WDT']
inter=['UH']
pronoun=['PRP','PRPS','WP']
conjunction=['CC']
noun_=0
verb_=0
adj_=0
pre_=0
adv_=0
art_=0
inter_=0
pro_=0
con_=0    
def fun3():
    global postags,art_,noun_,inter_,verb_,adj_,pre_,adv_,pro_,con_
    for i in postags:
        if i[1] in noun:
            noun_+=1
        elif i[1] in verb:
            verb_+=1
        elif i[1] in adjective:
            adj_+=1
        elif i[1] in preposition:
            pre_+=1
        elif i[1] in adverb:
            adv_+=1
        elif i[1] in article:
            art_+=1
        elif i[1] in inter:
            inter_+=1
        elif i[1] in pronoun:
            pro_+=1
        elif i[1] in conjunction:
            con_+=1
    plt.title("usage of parts of speech")
    plt.xlabel("parts of speech")
    plt.ylabel("")
    x=['nouns','verbs','adj','prepos','adverb','article','inter','pronoun','conjun']
    y=[noun_,verb_,adj_,pre_,adv_,art_,inter_,pro_,con_]
    plt.yticks(np.arange(0,51,10))
    plt.xticks(np.arange(0,9,1))
    plt.bar(x,y,color='green',align='center')
    plt.show()       
def fun4():
    t1.insert(END,"""A multi-agency manhunt is under way across several states and Mexico after
police say the former Los Angeles police officer suspected in the murders of a
college basketball coach and her fiancÃ© last weekend is following through on
his vow to kill police officers after he opened fire Wednesday night on three
police officers, killing one."In this case, we're his target," Sgt. Rudy Lopez
 from the Corona PoliceDepartment said at a press conference.
The suspect has been identified as Christopher Jordan Dorner, 33, and he is
considered extremely dangerous and armed with multiple weapons, authorities
say. The killings appear to be retribution for his 2009 termination from the
 Los Angeles Police Department for making false statements, authorities say.
Dorner posted an online manifesto that warned, "I will bring unconventional
and asymmetrical warfare to those in LAPD uniform whether on or off duty.""")
def fun5():
    global nouns
    print(nouns)
    messagebox.showinfo(title="view terminal", message="the chunks are displayed in the terminal.")

l1=Label(top,bg='light blue',font=('Times',16,'bold'),width=20,text="Enter the text:").grid(row=2,column=0)
t1=Text(top,height=10,width=60)
t1.grid(row=3,column=0,padx=5,pady=5)

b1=Button(top,text='Extract\nEntities',bg='yellow',command=fun1,width=10).grid(row=0,column=0,padx=20,pady=5)
b2=Button(top,text='parse\ntree',bg='yellow',command=fun2,width=10).grid(row=0,column=1,padx=0,pady=5)
b3=Button(top,text='parts of\nspeech',bg='yellow',command=fun3,width=10).grid(row=0,column=2,padx=5,pady=5)
b5=Button(top,text='chunks',bg="yellow",command=fun5,width=10,height=2).grid(row=0,column=3,padx=0,pady=5)
b4=Button(top,text='default text',bg='red',command=fun4,width=10).grid(row=4,column=0)
top.mainloop()