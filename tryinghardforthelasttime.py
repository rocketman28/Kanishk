from PyQt5 import QtCore, QtGui,QtWidgets
import pandas as pd
df = pd.read_csv("CS_year1.csv")
course_list = list(df["COURSE_ID"].unique())
df = df.set_index("COURSE_ID")

course_dict = dict()
for x in course_list:
    course_dict[x] = df.loc[x].values.tolist()
for course_code in course_dict.keys():
    index_dict=dict()
    
    for j in course_dict[course_code]:
        try:
            index_dict[j[0]].append(j[1:])
        except:
            index_dict[j[0]] = [j[1:]]
    course_dict[course_code] = index_dict

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 10, 521, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 521, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 491, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 230, 481, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 260, 581, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(410, 70, 231, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(410, 190, 231, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(410, 230, 231, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(410, 270, 231, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 330, 201, 51))
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 100, 581, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.pushButton.clicked.connect(self.signup)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "NTU STARS PLANNER"))
        self.label_2.setText(_translate("MainWindow", "Course Codes:-"))
        self.label_3.setText(_translate("MainWindow", "Set your preferences:-"))
        self.label_4.setText(_translate("MainWindow", "Earliest Time preferred:-"))
        self.label_5.setText(_translate("MainWindow", "Latest Time preferred:-"))
        self.label_6.setText(_translate("MainWindow", "Weekday you wish to keep free, if any:-"))
        self.pushButton.setText(_translate("MainWindow", "Continue"))
        self.label_7.setText(_translate("MainWindow", "Enter with a space in between courses:-"))



    def signup(self):
        earliest_time=self.lineEdit_2.text()
        latest_time=self.lineEdit_3.text()
        weekday_free=self.lineEdit_4.text()
        course_codes=self.lineEdit.text()
        print(weekday_free)
        list_of_courses=course_codes.split()
        num_of_courses=len(list_of_courses)
        user_course_options=[]
        for x in list_of_courses:
             class_set=course_dict[x]
             user_course_options.append(class_set)
        rec_find_TT(list_of_courses,user_course_options,0,[])

   


   
    
def check_clash(i1,i2):
        l1=list()
        for x in i1:
                timings=(x[2], int(x[3][0:4]), int(x[3][5:]))
                l1.append(timings)
        
        l2=list()
        for x in i2:
                timings=(x[2], int(x[3][0:4]), int(x[3][5:]))
                l2.append(timings)
        for x in l1:
            for y in l2:
                if(x[0]==y[0]):
                    if(x[1]<y[1]<x[2])or (y[1]<x[1]<y[2])or(x[1]==y[1]):
                        return True
        
        return False

def rec_find_TT(course_list,user_course_options,level,TT):
    flag = True

    if level == len(course_list):
        for x in range(1,len(TT)):
            for y in range(x):
                a = check_clash(user_course_options[x][TT[x]],user_course_options[y][TT[y]])
                if a:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            print(TT)
            pos=0
            for courses in course_list:
                print(course_dict[courses][TT[pos]])
                pos+=1
            print()
            print()
            return
        else: 
            return
    for key,value in user_course_options[level].items():
        flag = True
        if TT:
            for x in range(1,len(TT)):
                for y in range(x):
                    if check_clash(user_course_options[x][TT[x]],user_course_options[y][TT[y]]):
                        flag = False
                        break
                if not flag:
                    break
        else:
            TT = list()
            rec_find_TT(course_list,user_course_options,level+1,TT+[key])
            flag = False
        
        if flag:
                rec_find_TT(course_list,user_course_options,level+1,TT+[key])



if __name__ == "__main__":
     import sys
     app = QtWidgets.QApplication(sys.argv)
     MainWindow = QtWidgets.QMainWindow()
     ui = Ui_MainWindow()
     ui.setupUi(MainWindow)
     MainWindow.show()
     sys.exit(app.exec_())
    

    # print("!")
    
    #num_of_courses=len(list_of_courses)
    #user_course_options=[]
    #for x in list_of_courses:
    #    class_set=course_dict[x]
    #    user_course_options.append(class_set)
    #print(check_clash(user_course_options[0][10158],user_course_options[3][10166]))
    #print(user_course_options[0][10158],user_course_options[3][10166])
    #rec_find_TT(list_of_courses,user_course_options,0,[])
# combo_num=0
# go_back_to=[]
# gtg_comb={}
# go_back=0
# for key,value in user_course_options[0].items():
#     gtg_comb[key]=value
#     level=1
#     iterations=0
    
#     for key1,value1 in user_course_options[level].items():
#              iterations+=1
#              if(go_back==1):
#                  for x in range(0,go_back_to[0]+1):
#                      continue
#              go_back=0      
#              for key2,value2 in gtg_comb.items():
#                  if(clash_time(value1,value2):
#                     continue
#                  else:
#                      gtg_comb[key1]=value1
#                      level+=1
#                      go_back_to=[level,iteration]
#                      break
#               level=go_back_to[0]
#               go_back=1
#          if(len(gtg_comb))==num_of_courses:
#              #code for displaying table
#              combo_num++
#              if(combo_num==4):
#                  break

