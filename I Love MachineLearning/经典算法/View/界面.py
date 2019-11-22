# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 11:41:54 2017

@author: Administrator
"""
import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets


'''初始化界面变量'''
Main_Window = u'界面.ui'
Ui_MainWindow, QtBaseClass1 = uic.loadUiType(Main_Window)



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    '''界面框架'''
    def __init__(self):
        '''初始化变量与控件'''
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.Start = self.Nothing       #初始化最初为KNN
        self.setupUi(self)
        self.tool_init()       #初始化工具栏
        self.button_init()      #初始化button
        self.Edit_init()
        self.file_name = ''      #初始化导入数据名
        #print(self.file_name)
    
    
    
    
    def tool_init(self): 
        '''存放工具栏触发点击函数'''
        self.addKNN = QtWidgets.QAction(QtGui.QIcon(""), 
                                        "KNN", self, triggered = self.To_KNN)
        self.addDecision_Tree = QtWidgets.QAction(QtGui.QIcon(""),
                                               "决策树", self, triggered = self.To_Decision_Tree)
        self.addSVM = QtWidgets.QAction(QtGui.QIcon(""),
                                               "SVM", self, triggered = self.To_SVM)
        self.addBP = QtWidgets.QAction(QtGui.QIcon(""),
                                               "BP神经网络", self, triggered = self.To_BP)
        self.addRegression = QtWidgets.QAction(QtGui.QIcon(""),
                                               "回归", self, triggered = self.To_Regression)
        self.addTree_Regression = QtWidgets.QAction(QtGui.QIcon(""),
                                               "树回归", self, triggered = self.To_Tree_Regression)
        self.addAssociation_Rules = QtWidgets.QAction(QtGui.QIcon(""),
                                               "关联规则", self, triggered = self.To_Association_Rules)

        '''存放工具栏'''
        self.addMenu = self.menuBar().addMenu("&分类")
        self.addMenu.addAction(self.addKNN)
        self.addMenu.addAction(self.addDecision_Tree)
        self.addMenu.addAction(self.addSVM)
        self.addMenu.addAction(self.addBP)
        
        self.modifyMenu = self.menuBar().addMenu("&预测")
        self.modifyMenu.addAction(self.addRegression)
        self.modifyMenu.addAction(self.addTree_Regression)
        
        self.settingMenu = self.menuBar().addMenu("&其他")
        self.settingMenu.addAction(self.addAssociation_Rules)
        


    def button_init(self):
        self.exit_.clicked.connect(quit)                       #退出button
        self.read_file.clicked.connect(self.choice_file)       #读取文件button
        self.start.clicked.connect(self.Start)                 #开始button
        
    
    def Edit_init(self):
        self.text_.setPlainText("启动成功！")

        
    
    def choice_file(self):
        self.file_name = QtWidgets.QFileDialog.getOpenFileName()
        print(self.file_name)
        
     
    '''切换到相应的算法''' 
    def To_KNN(self):
        self.Start = self.KNN
        self.text_.setPlainText("切换至KNN")
    
    
    def To_Decision_Tree(self):
        self.Start = self.Decision_Tree
        self.text_.setPlainText("切换至决策树")
    
        
    def To_SVM(self):
        self.Start = self.SVM
        self.text_.setPlainText("切换至支持向量机")
       
        
    def To_BP(self):
        self.Start = self.BP
        self.text_.setPlainText("切换至BP神经网络")
    
    
    def To_Regression(self):
        self.Start = self.Regression
        self.text_.setPlainText("切换至回归")

        
    def To_Tree_Regression(self):
        self.Start = self.Tree_Regression
        self.text_.setPlainText("切换至树回归")

                 
    def To_Association_Rules(self):
        self.Start = self.Association_Rules
        self.text_.setPlainText("切换至关联规则")




    '''切换执行的算法函数'''
    def Nothing(self):
        self.text_.setPlainText("初始化")
    
    def KNN(self):
        self.text_.setPlainText("KNN启动成功")
    
    
    def Decision_Tree(self):
        self.text_.setPlainText("决策树启动成功")
        
        
    def SVM(self):
        self.text_.setPlainText("支持向量机启动成功")
       
        
    def BP(self):
        self.text_.setPlainText("BP神经网络启动成功")
    
    
    def Regression(self):
        self.text_.setPlainText("回归启动成功")

        
    def Tree_Regression(self):
        self.text_.setPlainText("树回归启动成功")

             
    def Association_Rules(self):
        self.text_.setPlainText("关联规则启动成功")

        
    '''算法结束'''
        
if __name__ == '__main__':
    robo = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    #mainloop()
    sys.exit(robo.exec_())
