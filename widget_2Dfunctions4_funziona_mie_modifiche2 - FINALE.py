# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_2D_functions2.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

#https://forum.freecadweb.org/viewtopic.php?f=22&t=43341
#riga inserita da me
import sympy
#riga (from sympy import *) aggiunta da me
from sympy import *

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
#QUESTA RIGA O BLOCCO SOTTO LA/LO AGGIUNGO DOPO AVER DEFINITO LA FUNZIONE. LA FUNZIONE SI CHIAMA createSolidFunction
#se faccio run da python mi da errore perche' FreeCAD non e' un modulo Python

import FreeCAD, FreeCADGui, Part
import math
from FreeCAD import Base


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(396, 300)
        ###
        self.insert_function = QLabel(Dialog)
        self.insert_function.setObjectName(u"insert_function")
        self.insert_function.setGeometry(QRect(20, 0, 81, 20))
        ####
        self.insert_X = QLabel(Dialog)
        self.insert_X.setObjectName(u"insert_X")
        self.insert_X.setGeometry(QRect(20, 80, 47, 13))
        ####
        self.insert_A = QLabel(Dialog)
        self.insert_A.setObjectName(u"insert_A")
        self.insert_A.setGeometry(QRect(20, 120, 47, 13))
        #####
        self.insert_Nb = QLabel(Dialog)
        self.insert_Nb.setObjectName(u"insert_Nb")
        self.insert_Nb.setGeometry(QRect(10, 160, 61, 16))
        #####
        self.insert_OFFSET = QLabel(Dialog)
        self.insert_OFFSET.setObjectName(u"insert_OFFSET")
        self.insert_OFFSET.setGeometry(QRect(10, 240, 81, 16))
        #####
        self.insert_XT = QLabel(Dialog)
        self.insert_XT.setObjectName(u"insert_XT")
        self.insert_XT.setGeometry(QRect(170, 20, 47, 13))
        self.insert_YT = QLabel(Dialog)
        self.insert_YT.setObjectName(u"insert_YT")
        self.insert_YT.setGeometry(QRect(170, 60, 47, 13))
        self.insert_ZT = QLabel(Dialog)
        self.insert_ZT.setObjectName(u"insert_ZT")
        self.insert_ZT.setGeometry(QRect(170, 100, 47, 13))
        self.insert_RX = QLabel(Dialog)
        self.insert_RX.setObjectName(u"insert_RX")
        self.insert_RX.setGeometry(QRect(170, 140, 47, 13))
        self.insert_RY = QLabel(Dialog)
        self.insert_RY.setObjectName(u"insert_RY")
        self.insert_RY.setGeometry(QRect(170, 180, 47, 13))
        self.insert_RZ = QLabel(Dialog)
        self.insert_RZ.setObjectName(u"insert_RZ")
        self.insert_RZ.setGeometry(QRect(170, 220, 47, 13))
        #####
        self.insert_VX = QLabel(Dialog)
        self.insert_VX.setObjectName(u"insert_VX")
        self.insert_VX.setGeometry(QRect(290, 20, 47, 13))
        self.insert_VY = QLabel(Dialog)
        self.insert_VY.setObjectName(u"insert_VY")
        self.insert_VY.setGeometry(QRect(290, 60, 47, 13))
        self.insert_VZ = QLabel(Dialog)
        self.insert_VZ.setObjectName(u"insert_VZ")
        self.insert_VZ.setGeometry(QRect(290, 100, 47, 13))
        ####
        self.insert_EXT = QLabel(Dialog)
        self.insert_EXT.setObjectName(u"insert_EXT")
        self.insert_EXT.setGeometry(QRect(280, 140, 47, 13))
        ######
        ######
        self.insert_function_2 = QLineEdit(Dialog)
        self.insert_function_2.setObjectName(u"insert_function_2")
        self.insert_function_2.setGeometry(QRect(20, 20, 104, 41))
        #####
        self.insert_X_2 = QLineEdit(Dialog)
        self.insert_X_2.setObjectName(u"insert_X_2")
        self.insert_X_2.setGeometry(QRect(80, 70, 41, 31))
        self.insert_X_2.setText("-10")
        ####
        self.insert_A_2 = QLineEdit(Dialog)
        self.insert_A_2.setObjectName(u"insert_A_2")
        self.insert_A_2.setGeometry(QRect(80, 110, 41, 31))
        self.insert_A_2.setText("10")
        #####
        self.insert_Nb_2 = QLineEdit(Dialog)
        self.insert_Nb_2.setObjectName(u"insert_Nb_2")
        self.insert_Nb_2.setGeometry(QRect(80, 150, 41, 31))
        self.insert_Nb_2.setText("100")
        #####
        self.insert_OFFSET_2 = QLineEdit(Dialog)
        self.insert_OFFSET_2.setObjectName(u"insert_OFFSET_2")
        self.insert_OFFSET_2.setGeometry(QRect(80, 230, 41, 31))
        self.insert_OFFSET_2.setText("5")
        ######
        ########
        self.insert_XT_2 = QLineEdit(Dialog)
        self.insert_XT_2.setObjectName(u"insert_XT_2")
        self.insert_XT_2.setGeometry(QRect(220, 10, 41, 31))
        self.insert_XT_2.setText("10")
        self.insert_YT_2 = QLineEdit(Dialog)
        self.insert_YT_2.setObjectName(u"insert_YT_2")
        self.insert_YT_2.setGeometry(QRect(220, 50, 41, 31))
        self.insert_YT_2.setText("0")
        self.insert_ZT_2 = QLineEdit(Dialog)
        self.insert_ZT_2.setObjectName(u"insert_ZT_2")
        self.insert_ZT_2.setGeometry(QRect(220, 90, 41, 31))
        self.insert_ZT_2.setText("0")
        self.insert_RX_2 = QLineEdit(Dialog)
        self.insert_RX_2.setObjectName(u"insert_RX_2")
        self.insert_RX_2.setGeometry(QRect(220, 130, 41, 31))
        self.insert_RX_2.setText("0")
        self.insert_RY_2 = QLineEdit(Dialog)
        self.insert_RY_2.setObjectName(u"insert_RY_2")
        self.insert_RY_2.setGeometry(QRect(220, 170, 41, 31))
        self.insert_RY_2.setText("0")
        self.insert_RZ_2 = QLineEdit(Dialog)
        self.insert_RZ_2.setObjectName(u"insert_RZ_2")
        self.insert_RZ_2.setGeometry(QRect(220, 210, 41, 31))
        self.insert_RZ_2.setText("0")
        #####
        ######
        self.insert_VX_2 = QLineEdit(Dialog)
        self.insert_VX_2.setObjectName(u"insert_VX_2")
        self.insert_VX_2.setGeometry(QRect(340, 10, 41, 31))
        self.insert_VX_2.setText("0")
        self.insert_VY_2 = QLineEdit(Dialog)
        self.insert_VY_2.setObjectName(u"insert_VY_2")
        self.insert_VY_2.setGeometry(QRect(340, 50, 41, 31))
        self.insert_VY_2.setText("0")
        self.insert_VZ_2 = QLineEdit(Dialog)
        self.insert_VZ_2.setObjectName(u"insert_VZ_2")
        self.insert_VZ_2.setGeometry(QRect(340, 90, 41, 31))
        self.insert_VZ_2.setText("0")
        #####
        self.insert_EXT_2 = QLineEdit(Dialog)
        self.insert_EXT_2.setObjectName(u"insert_EXT_2")
        self.insert_EXT_2.setGeometry(QRect(340, 130, 41, 31))
        self.insert_EXT_2.setText("5")
        #####
        #####
        self.invio_OK = QPushButton(Dialog)
        self.invio_OK.setObjectName(u"invio_OK")
        self.invio_OK.setGeometry(QRect(290, 240, 75, 23))
    #UI Dialog
        self.retranslateUi(Dialog)
    #inserisco questa riga tra le due righe per dire a FreeCAd di collegare il bottone alla funzione
        QtCore.QObject.connect(self.invio_OK,QtCore.SIGNAL("pressed()"),self.createSolidFunction)
        QMetaObject.connectSlotsByName(Dialog)
    # setupUi
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
    #####
        self.insert_function.setText(QCoreApplication.translate("Dialog", u"insert function", None))
    #####
        self.insert_X.setText(QCoreApplication.translate("Dialog", u"insert X", None))
        self.insert_A.setText(QCoreApplication.translate("Dialog", u"insert A", None))
        self.insert_Nb.setText(QCoreApplication.translate("Dialog", u"insert Nb", None))
        self.insert_OFFSET.setText(QCoreApplication.translate("Dialog", u"insert OFFSET", None))
    #####
        self.insert_XT.setText(QCoreApplication.translate("Dialog", u"insert XT", None))
        self.insert_YT.setText(QCoreApplication.translate("Dialog", u"insert YT", None))
        self.insert_ZT.setText(QCoreApplication.translate("Dialog", u"insert ZT", None))
        self.insert_RX.setText(QCoreApplication.translate("Dialog", u"insert RX", None))
        self.insert_RY.setText(QCoreApplication.translate("Dialog", u"insert RY", None))
        self.insert_RZ.setText(QCoreApplication.translate("Dialog", u"insert RZ", None))
    #####
        self.insert_VX.setText(QCoreApplication.translate("Dialog", u"insert VX", None))
        self.insert_VY.setText(QCoreApplication.translate("Dialog", u"insert VY", None))
        self.insert_VZ.setText(QCoreApplication.translate("Dialog", u"insert VZ", None))
        self.insert_EXT.setText(QCoreApplication.translate("Dialog", u"insert EXT", None))
    #####
        self.invio_OK.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi
    #QUESTA SOTTO E' LA FUNZIONE PER FARGLI FARE QUALCOSA
    #XT,YT,ZT sono parametri di traslazione; RX,RY,RZ sono parametri di rotazione
    #attorno agli assi; VX,VY,VZ sono parametri che indicano un vettore rispetto al
    #quale si posizione il solido; i parametri X indicano il punto iniziale del
    #dominio di f; Nb e' un parametro da cui dipende il numero degli step; EXT mi
    #da la dimensione da estrudere
    def createSolidFunction(self):
    #riga inserita da me    
        x = symbols('x')
    ####    
        A = float(self.insert_A_2.text()) 
    ####
    ####
        X_INIZ = float (self.insert_X_2.text())
        Nb = int (self.insert_Nb_2.text())
        Step = A/Nb
        Y = 0
        EXT = float (self.insert_EXT_2.text())
        OFFSET = float (self.insert_OFFSET_2.text())
    ####devo scambiare x con z nelle rotazioni
        XT = float (self.insert_XT_2.text())
        YT = float (self.insert_YT_2.text())
        ZT = float (self.insert_ZT_2.text())
        RX = float (self.insert_RZ_2.text())
        RY = float (self.insert_RY_2.text())
        RZ = float (self.insert_RX_2.text())
        VX = float (self.insert_VX_2.text())
        VY = float (self.insert_VY_2.text())
        VZ = float (self.insert_VZ_2.text())
    ###
    #    F =  float(self.insert_function_2.text())
    ### riga modificata da me
        F_DI_X = sympify(self.insert_function_2.text()).subs(x,X_INIZ).evalf()
        F_DI_X_OFFSET = F_DI_X + OFFSET
    ####
    #definisco i vettori
        points = [Base.Vector(X_INIZ,Y,0)]
        for I in range(Nb):
            X_INCREMENTO=X_INIZ+I*Step 
    ####
            F_DI_X = sympify(self.insert_function_2.text()).subs(x,X_INCREMENTO).evalf()
            F_DI_X_OFFSET_INCREMENTO = F_DI_X + OFFSET
            points.append(Base.Vector(X_INCREMENTO,Y,F_DI_X_OFFSET_INCREMENTO))
        points.append(Base.Vector(X_INCREMENTO,Y,0))
        points.append(points[0])
        poly = Part.makePolygon(points)
        face = Part.Face(poly)
        E = face.extrude(Base.Vector(0,EXT,0))
        P = E.Placement=App.Placement(App.Vector(XT,YT,ZT), App.Rotation(RX,RY,RZ), App.Vector(VX,VY,VZ))
    #   Gui.activeDocument().activeView().viewIsometric()
    #   Gui.ActiveDocument.ActiveView.setAxisCross(True)
        Part.show(E)
    #QUI FINISCE LA FUNZIONE

    #aggiunta di Mario per visualizzare la finestra in freeCAD

from PySide2 import QtWidgets, QtCore 
if __name__ == "__main__":
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #MainWindow.hide() 


