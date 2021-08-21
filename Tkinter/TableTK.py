#!/usr/bin/python2
'''
    TableTK

    Copyright (C) 2021 Luciano A.

    TableTK is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    TableTK program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with TableTK.  If not, see <https://www.gnu.org/licenses/>.
'''

import sys
import random

try: 
    import Tkinter
    import Tkconstants
    import ttk
except ImportError:  #  Python 3.x
    import tkinter as Tkinter
    import tkinter.ttk  as ttk
    import tkinter.constants as Tkconstants
except: 
    print("Instate python 2.x o 3.x o algo ...")
    sys.exit(1)


class Application(Tkinter.Frame):

    def __init__(self,root,valores,*args,**kwargs):
        Tkinter.Frame.__init__(self,root)
        self.parent=root
        self.parent.configure(background='lavender')

        tree=ttk.Treeview(self.parent)
        tree['columns']=('A','B','C','D','E','F','G')
        tree['show']='headings'
        tree.heading('A',anchor=Tkconstants.CENTER,text='Valor')
        tree.heading('B',anchor=Tkconstants.CENTER,text='f.abs')
        tree.heading('C',anchor=Tkconstants.CENTER,text='f.rel')
        tree.heading('D',anchor=Tkconstants.CENTER,text='f.%')
        tree.heading('E',anchor=Tkconstants.CENTER,text='f.abs.ac')
        tree.heading('F',anchor=Tkconstants.CENTER,text='f.rel.ac')
        tree.heading('G',anchor=Tkconstants.CENTER,text='f.%.ac')

        tree.column('A',stretch=Tkinter.YES,width=60)
        tree.column('B',stretch=Tkinter.YES,width=60)
        tree.column('C',stretch=Tkinter.YES,width=60)
        tree.column('D',stretch=Tkinter.YES,width=60)
        tree.column('E',stretch=Tkinter.YES,width=60)
        tree.column('F',stretch=Tkinter.YES,width=60)
        tree.column('G',stretch=Tkinter.YES,width=60)
        #tree.grid(rows=4,columnspan=4,sticky='nsew')
        

        count=0
        f_abs_ac=0.0
        f_rel_ac=0.0
        f_per_ac=0.0
        fr=1.0/len(valores)


        tag=('white','yellow')
        for v in valores:
            f_abs=1.0
            f_rel=fr
            f_per=f_rel*100.0

            f_abs_ac+=f_abs
            f_rel_ac+=f_rel
            f_per_ac+=f_per

            tree.insert('','end',tags=tag[count%2],values=(v,f_abs,f_rel,f_per,f_abs_ac,f_rel_ac,f_per_ac))
            count+=1
        
        tree.tag_configure('yellow',background='yellow')

        tree.pack(fill='both',expand=True,side='left')

        vsb=ttk.Scrollbar(self.parent,orient='vertical',command=tree.yview)
        vsb.pack(fill='both',side='right')
        tree.configure(yscrollcommand=vsb.set)

        self.pack(fill='both',side='top' )




def main():
    tk=Tkinter.Tk()
    N=1000
    r=random.Random()
    valores=[ round(r.gauss(175,8),2)  for x in range(0,N) ]
    valores.sort()

    print( "amplitud del los intervalos =  ", (max(valores)- min(valores))/N )

    app=Application(root=tk,valores=valores)
    tk.update_idletasks()
    tk.geometry('+%d+%d'%((tk.winfo_screenwidth()-tk.winfo_width())//2,(tk.winfo_screenheight()-tk.winfo_height())//2))
    tk.mainloop()


if __name__ == '__main__':
    main()
        
