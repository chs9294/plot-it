from numpy import arange, sin, pi, exp, log, tan , floor, ceil 
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.widgets import Slider, Button, RadioButtons
import matplotlib.pyplot as plt
import wx
class MyFrame(wx.Frame):
        def __init__(self, parent, title):
            wx.Frame.__init__(self, parent, title=title, size=(100,100))
            self.CreateStatusBar() #A statusbar at the bottom of the window
            self.figure = plt.figure()
            self.canvas = FigureCanvas(self, -1, self.figure)#Setting up the canvas
            
            # setting up the menu.
            filemenu= wx.Menu()
            
            # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets
            # give names to the following things
            menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
            filemenu.AppendSeparator()
            menuExit = filemenu.Append(wx.ID_EDIT, "&Exit"," Terminate the program")
            
            # Creating the menubar
            menuBar = wx.MenuBar()
            menuBar.Append(filemenu, "&File") # adding the "filename" to the...
            self.SetMenuBar(menuBar) # Adding the MenuBar for the Frame content
            
            #New code beings here:
            #set events:
            self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
            self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
            self.Show(True)
        
            # SETTING UP THE BUTTONS:
            
            self.sizer2 = wx.BoxSizer(wx.VERTICAL) # stack the buttons in a vetical way
            self.sizer = wx.BoxSizer(wx.HORIZONTAL)
            self.buttons = []
            self.xlims = np.array([0.1,3])
            
            #Creating an array
            names = ["SELECT RANGE","sin(x)", "logx", "exp(x)","tan(x)", "floor", "ceil"]
            
            for i in range(0,7):  # this command adds the buttons
                    self.buttons.append(wx.Button(self, -1, names[i]))
                    self.sizer2.Add(self.buttons[i], 0, wx.EXPAND|wx.ALIGN_CENTER)
                    
            #Bind the buttons to the event
            self.Bind(wx.EVT_BUTTON, self.functionname, self.buttons[1])
            self.Bind(wx.EVT_BUTTON, self.functionname1, self.buttons[3])
            self.Bind(wx.EVT_BUTTON, self.functionname2, self.buttons[2])
            self.Bind(wx.EVT_BUTTON, self.funcxlims, self.buttons[0])
            self.Bind(wx.EVT_BUTTON, self.functionname3, self.buttons[4])
            self.Bind(wx.EVT_BUTTON, self.functionname4, self.buttons[5])
            self.Bind(wx.EVT_BUTTON, self.functionname5, self.buttons[6])
            
            #use some sizers to see layout options
            self.sizer.Add(self.sizer2, 0, wx.EXPAND) # the box where the buttons go
            #self.sizer.Add(self.sizer2, 0, wx.ALIGN_TOP)
            self.sizer.Add(self.canvas, 1, wx.EXPAND)# adjust the canvas
        
            #Layout sizers
            self.SetSizer(self.sizer)
            self.sizer.Fit(self)
            self.Show(True)
            
        #add our new functions:
        def functionname(self,event):
            ax = self.figure.add_subplot(111)
            t = arange(self.xlims[0],self.xlims[1],0.01)
            s = sin(t)
            ax.plot(t,s)
            self.canvas.draw()
            ax.clear()
            
            #Exponential function
        def functionname1(self,event):
            ax = self.figure.add_subplot(111)
            t1 = arange(self.xlims[0],self.xlims[1],0.01)
            s1 = exp(t1)
            ax.plot(t1,s1)
            self.canvas.draw()
            ax.clear()
            
            #DIALOG BOX FOR ERROR MESSAGE
        def functionname2(self,event):
            ax = self.figure.add_subplot(111)
            if self.xlims[0]<1e-6:
                dlg = wx.MessageDialog( self, "log can't be less than or equal to zero", "Error message:", wx.OK)
                dlg.ShowModal() # Show it
                dlg.Destroy() # finally destroy it when finished.
            else:
                t2 = arange(self.xlims[0],self.xlims[1],0.01)
                s2 = log(t2)
                ax.plot(t2,s2)
                self.canvas.draw()
                ax.clear()

        def OnAbout(self,e):
            # A message dialog box with an OK button, wx.OK is a standard ID
            dlg = wx.MessageDialog(self,"Plot functions","PLOT IT", wx.OK)
            dlg.ShowModal() #show it
            dlg.Destroy() # destroy it when finished
        
        def OnExit(self,e):
            self.Close(True) # close the frame
            
            #CREATE A DIALOG BOX
        def funcxlims(self,e):
            xlimbox = wx.TextEntryDialog(None, 'xlimits', 'Please select Xrange as xmin,xmax eg 1,2')
            if xlimbox.ShowModal() == wx.ID_OK:
                x_lims = str(xlimbox.GetValue())
                x_lims = x_lims.split(',')
                xmin = float(x_lims[0])
                xmax = float(x_lims[1])
                self.xlims = np.array([xmin,xmax])
                
                #ARCSIN
        def functionname3(self,event):
            ax = self.figure.add_subplot(111)
            t3 = arange(self.xlims[0],self.xlims[1],0.01)
            s3 = tan(t3)
            ax.plot(t3,s3)
            self.canvas.draw()
            ax.clear()
            
            #FLOOR FUNCTION
        def functionname4(self,event):
            ax = self.figure.add_subplot(111)
            t4 = arange(self.xlims[0],self.xlims[1],0.01)
            s4 = floor(t4)
            ax.plot(t4,s4)
            self.canvas.draw()
            ax.clear()
            
            #CEILING FUNCTION
        def functionname5(self,event):
            ax = self.figure.add_subplot(111)
            t5 = arange(self.xlims[0],self.xlims[1],0.01)
            s5 = ceil(t5)
            ax.plot(t5,s5)
            self.canvas.draw()
            ax.clear()
        
            
app = wx.App(False)
frame = MyFrame(None, 'PLOT IT')
app.MainLoop()