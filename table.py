
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 table - pythonspot.com'
        self.left = 50
        self.top = 50
        self.width = 300
        self.height = 200
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 

        # Show widget
        self.show()

    def createTable(self):
       # Create table
        gtg_comb=['Eng comm','Thursday',930,1230]
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(16)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setItem(0,0,QTableWidgetItem("Day/time"))
        self.tableWidget.setItem(0,1,QTableWidgetItem("Mon"))
        self.tableWidget.setItem(0,2,QTableWidgetItem("Tues"))
        self.tableWidget.setItem(0,3,QTableWidgetItem("Wed"))
        self.tableWidget.setItem(0,4,QTableWidgetItem("Thurs"))
        self.tableWidget.setItem(0,5,QTableWidgetItem("Fri"))
        self.tableWidget.setItem(0,6,QTableWidgetItem("Sat"))
        self.tableWidget.setItem(1,0,QTableWidgetItem("830:930"))
        self.tableWidget.setItem(2,0,QTableWidgetItem("930:1030"))
        self.tableWidget.setItem(3,0,QTableWidgetItem("1030:1130"))
        self.tableWidget.setItem(4,0,QTableWidgetItem("1130:1230"))
        self.tableWidget.setItem(5,0,QTableWidgetItem("1230:1330"))
        self.tableWidget.setItem(6,0,QTableWidgetItem("1330:1430"))
        self.tableWidget.setItem(7,0,QTableWidgetItem("1430:1530"))
        self.tableWidget.setItem(8,0,QTableWidgetItem("1530:1630"))
        self.tableWidget.setItem(9,0,QTableWidgetItem("1630:1730"))
        self.tableWidget.setItem(10,0,QTableWidgetItem("1730:1830"))
        self.tableWidget.setItem(11,0,QTableWidgetItem("1830:1930"))
        self.tableWidget.setItem(12,0,QTableWidgetItem("1930:2030"))

        gtg_comb=["CZ1005","Monday",1030,1230]
        
        for i in range (0,7):
            if (i==0 and gtg_comb[1]=='Monday')or (i==1 and gtg_comb[1]=='Tuesday') or (i==2 and gtg_comb[1]=='Wednesday') or (i==3 and gtg_comb[1]=='Thursday') or (i==4 and gtg_comb[1]=='Friday') or (i==5 and gtg_comb[1]=='Saturday') or (i==6 and gtg_comb[1]=='Sunday'):
             day=i
             print (i)
        for j in range (int((gtg_comb[2]-830)/100),int((gtg_comb[3]-830)/100)):
                    self.tableWidget.setItem(j+1,day+1,QTableWidgetItem(gtg_comb[0]))
        self.tableWidget.move(0,0)
        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)
            
                    
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
   
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
