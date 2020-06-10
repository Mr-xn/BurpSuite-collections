# -*- coding: utf-8 -*-
# Thursday, 4 April 2019
# Author:nianhua
# Blog:http://nianhua.in

# Python Import
import re

# Burp Import
from burp import IBurpExtender
from burp import IProxyListener
from burp import IMessageEditorTab
from burp import IMessageEditorTabFactory



class BurpExtender(IBurpExtender, IProxyListener, IMessageEditorTabFactory):

    #
    # implement IBurpExtender
    #
    # register extender callbacks
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Sensitive Information")
        callbacks.registerProxyListener(self)
        callbacks.registerMessageEditorTabFactory(self)
        print 'sstvINFO by [nianhua]\nBlog: nianhua.in\nTeam: TIDE'
        return

    def createNewInstance(self, controller, editable):
        # implement createNewInstance
        self.SstvInfo = SstvInfoTab(self, controller, editable)
        return self.SstvInfo

    #
    # implement IHttpListener
    #

    def processProxyMessage(self, messageIsRequest, messageInfo):
        # only process response
        if messageIsRequest:
            return
        # messageInfo is a IHttpRequestResponse object
        messageInfo = messageInfo.getMessageInfo()

        content = messageInfo.getResponse()

        r = self._helpers.analyzeResponse(content)

        headers = content[:r.getBodyOffset()].tostring()

        msg = content[r.getBodyOffset():].tostring()

        Xhacker = True if "X-Hacker" in headers else False

        if stringIsGps(Xhacker, msg):
            messageInfo.setHighlight('green')

        if stringIsPhone(msg):
            messageInfo.setHighlight('blue')

        if stringIsIdCard(msg):
            messageInfo.setHighlight('red')

        if stringIsAssets(msg):
            messageInfo.setHighlight('yellow')



class SstvInfoTab(IMessageEditorTab):

    def __init__(self, extender, controller, editable):

        self._extender = extender
        self._helpers = extender._helpers
        self._editable = editable
        self._txtInput = extender._callbacks.createTextEditor()
        self._txtInput.setEditable(editable)
        return

    def getTabCaption(self):
        return "SSTVINFO"

    def getUiComponent(self):
        return self._txtInput.getComponent()

    def isEnabled(self, content, isRequest):  # only show tab in response

        if isRequest:
            return False
        else:
            return True

    def setMessage(self, content, isRequest):
        if content:
            pretty_msg = ''
            phone = stringIsPhone(content)
            idcard = stringIsIdCard(content)
            gpslocal = stringIsGps(False,content)
            assets = stringIsAssets(content)
            if phone != False:
                pretty_msg += "Find phone:" + phone + '\n'
            if idcard != False:
                pretty_msg += "Find idcard:" + idcard + '\n'
            if gpslocal != False:
                pretty_msg += "Find GpsLocal:" + gpslocal + '\n'
            if assets != False:
                pretty_msg += "Find IP Address:" + assets + '\n'
            self._txtInput.setText(pretty_msg)
        return


def stringIsGps(Xhacker, string):  # check GPS information
    if Xhacker:
        return False
    if ("\"longitude\"" in string and "\"latitude\"" in string) or ("\"lat\"" in string and "\"lon\"" in string):
        locations = re.findall(r'\d{2,3}\.\d{3,6}', string)
        for location in locations:
            if 3 < float(location) < 135:
                return location
    return False


def stringIsPhone(string):
    iphones = re.findall(r'[%"\'< ](?:13[012]\d{8}[%"\'< ]|15[56]\d{8}[%"\'< ]|18[56]\d{8}[%"\'< ]|176\d{8}[%"\'< ]|145\d{8}[%"\'< ]|13[456789]\d{8}[%"\'< ]|147\d{8}[%"\'< ]|178\d{8}[%"\'< ]|15[012789]\d{8}[%"\'< ]|18[23478]\d{8}[%"\'< ]|133\d{8}[%"\'< ]|153\d{8}[%"\'< ]|189\d{8}[%"\'< ])', string)
    if iphones != []:
        iphones = set(iphones)
        iphoneSet = set()
        for i in iphones:
            iphoneSet.add(filter(str.isdigit, i))
        iphones = ','.join(iphoneSet)
        return iphones
    return False

def stringIsAssets(string):
    assets = re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b', string)
    if assets != []:
        assetss = set(assets)
        assetsSet = set()
        for i in assets:
            assetsSet.add(i)
        assetss = ','.join(assetsSet)
        return assetss
    return False

def stringIsIdCard(string):
    coefficient = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    parityBit = '10X98765432'
    idcards = re.findall(r'([1-8][1-7]\d{4}[1|2]\d{3}[0|1]\d{1}[1-3]\d{4}[0-9|X|x])', string)
    idcardSet = set()
    if idcards != []:
        for idcard in idcards:
            sumnumber = 0
            for i in range(17):
                sumnumber += int(idcard[i]) * coefficient[i]
            if parityBit[sumnumber % 11] == idcard[-1]:
                idcardSet.add(idcard)
        idcards = ','.join(idcardSet)
        return idcards
    return False
