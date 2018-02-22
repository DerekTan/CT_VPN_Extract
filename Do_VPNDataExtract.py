# -*- coding: utf-8 -*-
# This program is developed with python 3.x

from PyQt5 import QtCore, QtGui, QtWidgets

import datetime
import re
import os

class extractVPNCfg(QtCore.QThread):
    """ class extractVPNCfg """

    ptnInterface = re.compile(r'interface\s*(\S*)')
    ptnDescription = re.compile(r'description\s*(\S*)')
    ptnTermination = re.compile(r'q termination\s*(\S.*)')
    ptnVPNInstance = re.compile(r'vpn-instance\s*(\S*)')
    ptnIPAddress = re.compile(r'ip address\s*(\S.*)')

    paramPtnDict = { 'description' : ptnDescription, \
                     'termination' : ptnTermination, \
                     'vpn-instance' : ptnInterface, \
                     'ip address' : ptnIPAddress }

    # signal
    #sigProcessFiles = QtCore.pyqtSignal(str)
    sigRecord = QtCore.pyqtSignal(str)
#    sigRecordClear = QtCore.pyqtSignal()
#    sigLineProcessed = QtCore.pyqtSignal(int)
#    sigTotalLineNum = QtCore.pyqtSignal(int)
#    sigStartTimer = QtCore.pyqtSignal()
#    sigStopTimer = QtCore.pyqtSignal()

    def __init__(self):
        super(extractVPNCfg, self).__init__()
        self.path = None

    def loadPara(self, path, outFile = None):
        self.path = path
        if outFile is None:
            self.outFile = self.genOutFilename()
        else:
            self.outFile = outFile
        print(self.outFile)

    def genOutFilename(self):
        t = datetime.datetime.now()
        s = datetime.datetime.strftime(t, '%Y%m%d_%H%M%S')
        filename = 'out_' + s + '.xls'
        if type(self.path) is str: # input is a directory string
            path = self.path
        elif type(self.path) is list: # input is a file list
            path = os.path.split(self.path[0])[0]
        return os.path.join(path, filename)


    def run(self):
        if self.path is None:
            return
        if type(self.path) is str: # input is a directory string
            self.directoryExact(self.path)
        elif type(self.path) is list: # input is a file list
            for fn in self.path:
                self.fileExact(fn)
            #if os.path.exists(self.path):


    def directoryExact(self, dn):
        if os.path.isdir(dn):
            for parent, dirnames, filenames in os.walk(dn):
                for filename in filenames:
                    fn = os.path.join(parent, filename)
                    self.fileExact(fn)


    def fileExact(self, fn):
        # check if file is *.cfg
        if os.path.splitext(fn)[-1] != '.cfg':
            return

        # start analyse
        isInterfaceStart = False
        item = {}
        with open(fn, 'r') as fp:
            for line in fp:
                line = line.strip()
                if isInterfaceStart:
                        # reach the end of the instance
                        # save the item #TODO
                    if line == '#': #reach the end
                        self.saveItem(item)
                        #reset item
                        isInterfaceStart = False
                        item = {}
                        keyItemNum = 0
                    else:
                        #match interface internal parameters
                        for title, ptn in self.paramPtnDict.items():
                            result = ptn.search(line)
                            if result:
                                if title == 'ip address':
                                    if item.get(title) is None:
                                        item[title] = [result.group(1)]
                                    else:
                                        item[title].append(result.group(1))
                                else:
                                    item[title] = result.group(1)
                else: # interface not started, find the start
                    result = self.ptnInterface.match(line) 
                    if result:
                        item['interface'] = result.group(1)
                        isInterfaceStart = True

    def saveItem(self, item):
        if self.isValidItem(item):
            self.writeItemToExcel(item)
        else:
            print(item)

    def isValidItem(self, item):
        # interface name must contains '.'
        if '.' not in item[interface]:
            return false
        return True

    def writeItemToExcel(self, item):
        pass

#    def fAnalyseCANLog(self):
#        self.syncStart = False
#        self.cntRecv = [0, 0]
#        self.recvNodes = [set(), set()]
#        self.recvRedundant = [ [], [] ]
#        self.syncNum = 0
#        self.syncFailNum = 0
#        self.nodesUpdated = False
#
#        self.sigRecordClear.emit()
#        lastLineUpdateTime = datetime.datetime.now()
#        tPastTime = datetime.timedelta(0, 0, 0)
#        self.tSyncTime = datetime.timedelta(0, 0, 0)
#
#        with open(self.fn, 'r') as fp:
#            self.lineProcess = 0
#            self.logHeader = LogHeader()
#            for line in fp:
#                self.lineProcess += 1
#        # save the time of last line
#        self.logTime = tPastTime

    def fRecord(self, s):
        self.sigRecord.emit(s)

    def fNowPastTimeStr(self):
        delta = datetime.datetime.now() - self.tAnalyseStartTime
        return '%d.%d seconds' % (delta.seconds, delta.microseconds)


    def fGetFileLines(self, fn):
        i = -1
        with open(fn) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    def fSummary(self):
        s = []
        s.append( 'Summary:' )
        self.fRecord('\r\n'.join(s))

    def fStartTimer(self):
        self.sigStartTimer.emit()

    def fTimerEvent(self):
        self.sigLineProcessed.emit(self.lineProcess)

    def fStopTimer(self):
        self.sigStopTimer.emit()
        self.sigLineProcessed.emit(self.lineProcess)


if __name__ == "__main__":
    fn = input('Input file:')
    app = extractVPNCfg()
    app.sigRecord.connect(print)
    if os.path.isdir(fn):
        inParam = fn
    else:
        inParam = [fn]
    app.loadPara(inParam)
    app.start()
    input('')
