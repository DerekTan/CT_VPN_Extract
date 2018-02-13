# -*- coding: utf-8 -*-
#from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QSize, QBasicTimer, QCoreApplication, Qt, pyqtSignal, QRect
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLabel
# import GUI
from Ui_ACT350Demo import Ui_MainWindow

#menu = [ {pixA : [pixAA, pixAB, pixAC]}, {pixB : [{ pixBA: [ pixBAA ]}, pixBB, pixBC]}, pixC ]

# override QLabel
class MyLabel(QLabel):
    pressed = pyqtSignal()

    def __init__(self, parent = None):
        super(MyLabel, self).__init__(parent)

    def mousePressEvent(self, e):
        self.pressed.emit()

class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.setFixedSize(300,280)
        self.setupUi(self)
        self.hist = []
        self.lastList = []
        self.lastDict = dict()
        self.currItem = ''
        self.addButton()
        self.disp()

    def addButton(self):
        # up
        self.labelUp = MyLabel(self.centralWidget)
        self.labelUp.setGeometry(QRect(54, 120, 87, 87))
        self.labelUp.setObjectName("labelUp")
        #self.gridLayout.addWidget(self.labelUp, 0, 0, 1, 1)

        # down
        self.labelDown = MyLabel(self.centralWidget)
        self.labelDown.setGeometry(QRect(165, 120, 87, 87))
        self.labelDown.setObjectName("labelDown")
        #self.gridLayout.addWidget(self.labelDown, 0, 1, 1, 1)

        # left
        self.labelLeft = MyLabel(self.centralWidget)
        self.labelLeft.setGeometry(QRect(54, 210, 87, 87))
        self.labelLeft.setObjectName("labelLeft")
        #self.gridLayout.addWidget(self.labelLeft, 1, 0, 1, 1)

        # right
        self.labelRight = MyLabel(self.centralWidget)
        self.labelRight.setGeometry(QRect(165, 210, 87, 87))
        self.labelRight.setObjectName("labelRight")
        #self.gridLayout.addWidget(self.labelRight, 1, 1, 1, 1)

        # add pixmap
        self.labelUp.setPixmap(QPixmap.fromImage(QImage(":/image/image/button/Up.jpg").scaled(self.labelUp.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)))
        self.labelDown.setPixmap(QPixmap.fromImage(QImage(":/image/image/button/Down.jpg").scaled(self.labelDown.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)))
        self.labelLeft.setPixmap(QPixmap.fromImage(QImage(":/image/image/button/Left.jpg").scaled(self.labelLeft.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)))
        self.labelRight.setPixmap(QPixmap.fromImage(QImage(":/image/image/button/Right.jpg").scaled(self.labelRight.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)))

        # signal from MyLabel
        self.labelUp.pressed.connect(self.onUp)
        self.labelDown.pressed.connect(self.onDown)
        self.labelRight.pressed.connect(self.onRight)
        self.labelLeft.pressed.connect(self.onLeft)


    def onRight(self):
        # if currItem is the key of a dictionary,
        # sub-menu is accessible
        if self.lastDict.get(self.currItem) is not None:
            # push current list and dictionary to stack,
            # they will be useful when left key is pressed.
            self.hist.append(self.lastList)
            self.hist.append(self.lastDict)
            self.disp(self.lastDict.get(self.currItem))

    def onLeft(self):
        # pop the list and dictionary,
        # and display the key of the dictionary.
        if len(self.hist) > 0:
            self.lastDict = self.hist.pop(-1)
            self.lastList = self.hist.pop(-1)
            self.disp(self.lastDict)

    def onUp(self):
        idx = 0
        if self.currItem in self.lastList:
            idx = self.lastList.index(self.currItem)
        elif self.currItem in self.lastDict.keys():
            idx = self.lastList.index(self.lastDict)
        idx -= 1
        self.disp(self.lastList[idx])

    def onDown(self):
        idx = 0
        if self.currItem in self.lastList:
            idx = self.lastList.index(self.currItem)
        elif self.currItem in self.lastDict.keys():
            idx = self.lastList.index(self.lastDict)
        idx += 1
        if idx == len(self.lastList):
            idx = 0
        self.disp(self.lastList[idx])

    def disp(self, item = None):
        pixmain =  QPixmap.fromImage(QImage('image/Menu/MainWeight.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pixRecall = QPixmap.fromImage(QImage('image/Menu/Recall.png').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pixComp = QPixmap.fromImage(QImage('image/Menu/Comparator.png').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pixCali = QPixmap.fromImage(QImage('image/Menu/Calibration.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pixSystem = QPixmap.fromImage(QImage('image/Menu/System Monitor.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pixLang = QPixmap.fromImage(QImage('image/Menu/Language.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pixSetup = QPixmap.fromImage(QImage('image/Menu/Setup.png').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))

        pix14I = QPixmap.fromImage(QImage('image/ConvetImage/14Inner.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix16I = QPixmap.fromImage(QImage('image/ConvetImage/16Inner.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix20I = QPixmap.fromImage(QImage('image/ConvetImage/20Inner.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix26I = QPixmap.fromImage(QImage('image/ConvetImage/26Inner.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix30I = QPixmap.fromImage(QImage('image/ConvetImage/30Inner.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix34I = QPixmap.fromImage(QImage('image/ConvetImage/34Inner.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix45I = QPixmap.fromImage(QImage('image/ConvetImage/45Inner.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix46I = QPixmap.fromImage(QImage('image/ConvetImage/46Inner.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix55I = QPixmap.fromImage(QImage('image/ConvetImage/55Inner.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix64I = QPixmap.fromImage(QImage('image/ConvetImage/64Inner.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix77I = QPixmap.fromImage(QImage('image/ConvetImage/77Inner.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))

        pix8U = QPixmap.fromImage(QImage('image/ConvertUpper/8Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix9U = QPixmap.fromImage(QImage('image/ConvertUpper/9Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix10U = QPixmap.fromImage(QImage('image/ConvertUpper/10Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix11U = QPixmap.fromImage(QImage('image/ConvertUpper/11Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix12U = QPixmap.fromImage(QImage('image/ConvertUpper/12Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix13U = QPixmap.fromImage(QImage('image/ConvertUpper/13Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix15U = QPixmap.fromImage(QImage('image/ConvertUpper/15Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix17U = QPixmap.fromImage(QImage('image/ConvertUpper/17Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix19U = QPixmap.fromImage(QImage('image/ConvertUpper/19Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix21U = QPixmap.fromImage(QImage('image/ConvertUpper/21Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix23U = QPixmap.fromImage(QImage('image/ConvertUpper/23Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix25U = QPixmap.fromImage(QImage('image/ConvertUpper/25Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix27U = QPixmap.fromImage(QImage('image/ConvertUpper/27Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix29U = QPixmap.fromImage(QImage('image/ConvertUpper/29Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix32U = QPixmap.fromImage(QImage('image/ConvertUpper/32Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix35U = QPixmap.fromImage(QImage('image/ConvertUpper/35Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix38U = QPixmap.fromImage(QImage('image/ConvertUpper/38Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix39U = QPixmap.fromImage(QImage('image/ConvertUpper/39Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix47U = QPixmap.fromImage(QImage('image/ConvertUpper/47Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix49U = QPixmap.fromImage(QImage('image/ConvertUpper/49Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix51U = QPixmap.fromImage(QImage('image/ConvertUpper/51Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix52U = QPixmap.fromImage(QImage('image/ConvertUpper/52Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix54U = QPixmap.fromImage(QImage('image/ConvertUpper/54Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix56U = QPixmap.fromImage(QImage('image/ConvertUpper/56Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix57U = QPixmap.fromImage(QImage('image/ConvertUpper/57Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix59U = QPixmap.fromImage(QImage('image/ConvertUpper/59Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix65U = QPixmap.fromImage(QImage('image/ConvertUpper/65Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix66U = QPixmap.fromImage(QImage('image/ConvertUpper/66Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix68U = QPixmap.fromImage(QImage('image/ConvertUpper/68Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix78U = QPixmap.fromImage(QImage('image/ConvertUpper/78Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix79U = QPixmap.fromImage(QImage('image/ConvertUpper/79Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix81U = QPixmap.fromImage(QImage('image/ConvertUpper/81Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix82U = QPixmap.fromImage(QImage('image/ConvertUpper/82Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix83U = QPixmap.fromImage(QImage('image/ConvertUpper/83Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix84U = QPixmap.fromImage(QImage('image/ConvertUpper/84Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix86U = QPixmap.fromImage(QImage('image/ConvertUpper/86Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix96U = QPixmap.fromImage(QImage('image/ConvertUpper/96Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix98U = QPixmap.fromImage(QImage('image/ConvertUpper/98Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix101U = QPixmap.fromImage(QImage('image/ConvertUpper/101Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix105U = QPixmap.fromImage(QImage('image/ConvertUpper/105Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix106U = QPixmap.fromImage(QImage('image/ConvertUpper/106Upper.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))

        pix15L = QPixmap.fromImage(QImage('image/ConvertLower/15Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix17L = QPixmap.fromImage(QImage('image/ConvertLower/17Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix18L = QPixmap.fromImage(QImage('image/ConvertLower/18Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix19L = QPixmap.fromImage(QImage('image/ConvertLower/19Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix21L = QPixmap.fromImage(QImage('image/ConvertLower/21Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix22L = QPixmap.fromImage(QImage('image/ConvertLower/22Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix23L = QPixmap.fromImage(QImage('image/ConvertLower/23Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix24L = QPixmap.fromImage(QImage('image/ConvertLower/24Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix25L = QPixmap.fromImage(QImage('image/ConvertLower/25Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix27L = QPixmap.fromImage(QImage('image/ConvertLower/27Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix28L = QPixmap.fromImage(QImage('image/ConvertLower/28Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix29L = QPixmap.fromImage(QImage('image/ConvertLower/29Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix32L = QPixmap.fromImage(QImage('image/ConvertLower/32Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix33L = QPixmap.fromImage(QImage('image/ConvertLower/33Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix35L = QPixmap.fromImage(QImage('image/ConvertLower/35Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix36L = QPixmap.fromImage(QImage('image/ConvertLower/36Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix37L = QPixmap.fromImage(QImage('image/ConvertLower/37Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix38L = QPixmap.fromImage(QImage('image/ConvertLower/38Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix39L = QPixmap.fromImage(QImage('image/ConvertLower/39Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix40L = QPixmap.fromImage(QImage('image/ConvertLower/40Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix41L = QPixmap.fromImage(QImage('image/ConvertLower/41Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix42L = QPixmap.fromImage(QImage('image/ConvertLower/42Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix43L = QPixmap.fromImage(QImage('image/ConvertLower/43Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix44L = QPixmap.fromImage(QImage('image/ConvertLower/44Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix47L = QPixmap.fromImage(QImage('image/ConvertLower/47Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix48L = QPixmap.fromImage(QImage('image/ConvertLower/48Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix49L = QPixmap.fromImage(QImage('image/ConvertLower/49Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix50L = QPixmap.fromImage(QImage('image/ConvertLower/50Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix51L = QPixmap.fromImage(QImage('image/ConvertLower/51Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix52L = QPixmap.fromImage(QImage('image/ConvertLower/52Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix53L = QPixmap.fromImage(QImage('image/ConvertLower/53Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix54L = QPixmap.fromImage(QImage('image/ConvertLower/54Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix56L = QPixmap.fromImage(QImage('image/ConvertLower/56Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix57L = QPixmap.fromImage(QImage('image/ConvertLower/57Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix58L = QPixmap.fromImage(QImage('image/ConvertLower/58Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix59L = QPixmap.fromImage(QImage('image/ConvertLower/59Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix60L = QPixmap.fromImage(QImage('image/ConvertLower/60Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix61L = QPixmap.fromImage(QImage('image/ConvertLower/61Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix62L = QPixmap.fromImage(QImage('image/ConvertLower/62Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix63L = QPixmap.fromImage(QImage('image/ConvertLower/63Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix66L = QPixmap.fromImage(QImage('image/ConvertLower/66Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix67L = QPixmap.fromImage(QImage('image/ConvertLower/67Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix68L = QPixmap.fromImage(QImage('image/ConvertLower/68Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix69L = QPixmap.fromImage(QImage('image/ConvertLower/69Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix70L = QPixmap.fromImage(QImage('image/ConvertLower/70Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix79L = QPixmap.fromImage(QImage('image/ConvertLower/79Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix80L = QPixmap.fromImage(QImage('image/ConvertLower/80Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix84L = QPixmap.fromImage(QImage('image/ConvertLower/84Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix85L = QPixmap.fromImage(QImage('image/ConvertLower/85Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix86L = QPixmap.fromImage(QImage('image/ConvertLower/86Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix87L = QPixmap.fromImage(QImage('image/ConvertLower/87Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix88L = QPixmap.fromImage(QImage('image/ConvertLower/88Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix89L = QPixmap.fromImage(QImage('image/ConvertLower/89Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix90L = QPixmap.fromImage(QImage('image/ConvertLower/90Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix91L = QPixmap.fromImage(QImage('image/ConvertLower/91Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix92L = QPixmap.fromImage(QImage('image/ConvertLower/92Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix93L = QPixmap.fromImage(QImage('image/ConvertLower/93Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix94L = QPixmap.fromImage(QImage('image/ConvertLower/94Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix95L = QPixmap.fromImage(QImage('image/ConvertLower/95Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix96L = QPixmap.fromImage(QImage('image/ConvertLower/96Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix97L = QPixmap.fromImage(QImage('image/ConvertLower/97Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix98L = QPixmap.fromImage(QImage('image/ConvertLower/98Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix99L = QPixmap.fromImage(QImage('image/ConvertLower/99Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix100L = QPixmap.fromImage(QImage('image/ConvertLower/100Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix101L = QPixmap.fromImage(QImage('image/ConvertLower/101Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix102L = QPixmap.fromImage(QImage('image/ConvertLower/102Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix103L = QPixmap.fromImage(QImage('image/ConvertLower/103Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix104L = QPixmap.fromImage(QImage('image/ConvertLower/104Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))
        pix106L = QPixmap.fromImage(QImage('image/ConvertLower/106Lower.jpg').scaled(self.labelLCD.size(), Qt.IgnoreAspectRatio,  Qt.SmoothTransformation))

        listRecall = [pix8U, pix9U, pix10U, pix11U, pix12U, pix13U, pix14I]
        listComp = [{pix15U: [pix15L]}]
        listCali = [{pix16I:[{pix17U:[pix17L, pix18L]}, {pix19U:[pix19L]}]}, {pix20I: [{pix21U: [pix21L, pix22L]}, {pix23U: [pix23L, pix24L]}, {pix25U: [pix25L]}]}]
        listSystem = [pix30I]
        listLang = [{pix32U: [pix32L, pix33L]}]
        
        listSetupa = [{pix35U: [pix35L, pix36L, pix37L]}, {pix38U:[pix38L]}, {pix39U: [pix39L, pix40L, pix41L, pix42L, pix43L, pix44L]}]
        listSetupb = [{pix17U: [pix17L, pix18L]}, {pix19U:[pix19L]}]
        listSetupc = [{pix21U: [pix21L, pix22L]}, {pix23U: [pix23L, pix24L]}, {pix25U: [pix25L]}]
        listSetupd = [{pix56U: [pix56L]}, {pix57U:[pix57L, pix58L]}, {pix59U: [pix59L, pix60L, pix61L, pix62L, pix63L]}]
        listSetupe = [pix65U, {pix66U: [pix66L, pix67L]}, {pix68U: [pix68L, pix69L, pix70L]}, {pix77I: [pix78U, {pix79U:[pix79L, pix80L]}, pix81U, pix82U, pix83U]}]
        listSetupf = [{pix84L: [{pix86U:[pix86L, pix87L, pix88L, pix89L, pix90L, pix91L, pix92L, pix93L, pix94L, pix95L]}, {pix96U: [pix96L, pix97L]}, {pix98U: [pix98L, pix99L, pix100L]}, {pix101U: [pix101L, pix102L, pix103L]}]}, {pix85L: [{pix86U:[pix86L, pix87L, pix88L, pix89L, pix90L, pix91L, pix92L, pix93L, pix94L, pix95L]}, {pix96U: [pix96L, pix97L]}, {pix98U: [pix98L, pix99L, pix100L]}, {pix101U: [pix101L, pix102L, pix103L]}]}, {pix104L: [pix105U, {pix106U:[pix106L]}]}]
        listSetup = [{pix34I: listSetupa}, {pix16I: listSetupb}, {pix20I: listSetupc}, {pix55I: listSetupd}, {pix64I: listSetupe}, {pix84U: listSetupf}]

        menu = [{pixmain: [{pixRecall: listRecall}, {pixComp: listComp}, {pixCali: listCali}, {pixSystem: listSystem}, {pixLang: listLang}, {pixSetup: listSetup}]}]

        if item is None:
            item = menu
        t =  type(item)
        if t is list:
            self.lastList = item
            self.disp(item[0])
        elif t is dict:
            self.lastDict = item
            self.disp(list(item.keys())[0])
        else:
            self.currItem = item
            self.labelLCD.setPixmap(item)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MyApp()
    MainWindow.show()
    sys.exit(app.exec_())
