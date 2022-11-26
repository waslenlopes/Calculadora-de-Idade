#importando tkinter e ttk

from tkinter import *
from tkinter import ttk

#importando tkcalendar

from tkcalendar import Calendar, DateEntry

#importando dateutil

from dateutil.relativedelta import relativedelta

#importando datetime Python

from datetime import date



# criando janela

janela = Tk()
janela.title('Calculadora de Idade')
janela.geometry('310x400')

#cores

cor1 = '#D3D3D3' # cinza escuro
cor2 = '#BEBEBE' #  cinza claro
cor3 =  '#000000' #  preto
cor4 = '#000000' # preto

# criando frames

frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0,relief=FLAT, bg=cor2)
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=400, pady=0, padx=0,relief=FLAT, bg=cor1)
frame_baixo.grid(row=1, column=0)

#criando label cima

l_calculadora = Label(frame_cima, text='CALCULADORA', width=25, height=1, padx=0, relief='flat', anchor='center', font=('Arial 15 bold'), bg=cor2, fg=cor3)
l_calculadora.place(x=0, y=30) 

l_idade = Label(frame_cima, text='DE IDADE', width=11, height=1, padx=3, relief='flat', anchor='center', font=('Arial 35 bold '), bg=cor2, fg=cor4)
l_idade.place(x=0, y=70)


#criando função para culcular idade

def calcular():
    inicio = cal_1.get()
    termino = cal_2.get()

#separando os valores

    dia_1, mes_1, ano_1 = [ int(f) for f in inicio.split('/')]
    
#convertendo os valores em formato date/datetime

    data_inicio = date(ano_1, mes_1, dia_1)

    dia_2, mes_2, ano_2 = [ int(f) for f in termino.split('/')]
   
#convertendo os valores em formato date/datetime

    data_nascimento = date(ano_2, mes_2, dia_2)


    anos =relativedelta(data_inicio, data_nascimento).years
    meses =relativedelta(data_inicio, data_nascimento).months
    dias =relativedelta(data_inicio, data_nascimento).days

    l_app_anos['text'] = anos
    l_app_meses['text'] = meses
    l_app_dias['text'] = dias




#criando label para frame baixo

l_data_inicial = Label(frame_baixo, text='Data Ataul', height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('Ivi 11 '), bg=cor1, fg=cor3)
l_data_inicial.place(x=30, y=30)


#criando calendario 01

cal_1 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern='dd/mm/y', y=2021)
cal_1.place(x=180, y=30)



l_data_de_nascimento = Label(frame_baixo, text='Data De Nascimento', height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('Ivi 11 '), bg=cor1, fg=cor3)
l_data_de_nascimento.place(x=30, y=70)

#criando calendario 02

cal_2 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern='dd/mm/y', y=2021)
cal_2.place(x=180, y=70)


#criando label para ANOS, MESES, DIAS


l_app_anos = Label(frame_baixo, text='27', height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivi 25 bold '), bg=cor1, fg=cor3)
l_app_anos.place(x=60, y=135)
l_app_anos_nome = Label(frame_baixo, text='Anos', height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivi 11 bold '), bg=cor1, fg=cor3)
l_app_anos_nome.place(x=60, y=175)


l_app_meses = Label(frame_baixo, text='12', height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivi 25 bold '), bg=cor1, fg=cor3)
l_app_meses.place(x=130, y=135)
l_app_meses_nome = Label(frame_baixo, text='Meses', height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivi 11 bold '), bg=cor1, fg=cor3)
l_app_meses_nome.place(x=130, y=175)


l_app_dias = Label(frame_baixo, text='27', height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivi 25 bold '), bg=cor1, fg=cor3)
l_app_dias.place(x=210, y=135)
l_app_dias_nome = Label(frame_baixo, text='Dias', height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivi 11 bold '), bg=cor1, fg=cor3)
l_app_dias_nome.place(x=210, y=175)


#criando botão calcular

b_calcular = Button(frame_baixo, command=calcular, text='Calcular', width=20, height=1, relief='raised', overrelief='ridge', font=('Ivi 10 bold '), bg=cor1, fg=cor3)
b_calcular.place(x=70, y=225)




janela.mainloop()