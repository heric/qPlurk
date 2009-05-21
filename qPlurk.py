#!/usr/bin/python

# qPlurk v.0.1
# May 19,2009
# Plurk Client using PyQt
# Author : Heri Cahyono ( heri.cahyono@gmail.com )
# http://heric.web.id


import plurkapi
import sys,os
from PyQt4 import QtGui
from PyQt4 import QtCore
from main_ui import *
from login_ui import *
from about_ui import *


### Create a global instance of plurk API
plurk=plurkapi.PlurkAPI()

### Login Flag
isLogin = 0
plurks=''
plurkContent=''
emoticonFlag=0


### User interface part

class qPlurk(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle('QPlurk - Plurk Client')
		self.setFixedWidth(329)
		self.setFixedHeight(750)
		### Toolbox Title
		self.ui.toolBox.setItemText(0,'My Plurk')
		self.ui.toolBox.setItemText(1,'Respond to a Plurk')
		self.ui.lblProgress.setText('')

		### Disable link handling in QWebView
		webPage=self.ui.webView.page()
		webPage.setLinkDelegationPolicy(2)

		# Create Thread for get plurks & plurks response
		self.responseThread=responseThread()
		self.getPlurksThread=getPlurksThread()

		### Signal & Slot Connection
		QtCore.QObject.connect(self.ui.btnPlurk,QtCore.SIGNAL("clicked()"),postPlurks)
		QtCore.QObject.connect(self.ui.btnShowResponses,QtCore.SIGNAL("clicked()"),getResponses)
		QtCore.QObject.connect(self.ui.btnResponse,QtCore.SIGNAL("clicked()"),respondToPlurk)
		QtCore.QObject.connect(self.ui.actionGetPlurks,QtCore.SIGNAL("triggered()"),getPlurks)
		QtCore.QObject.connect(self.ui.actionAbout,QtCore.SIGNAL("triggered()"),showAbout)
		QtCore.QObject.connect(self.ui.actionExit,QtCore.SIGNAL("triggered()"),exit)

		QtCore.QObject.connect(self.ui.btnEmo1,QtCore.SIGNAL("clicked()"),self.showEmoticonWindow1)
		QtCore.QObject.connect(self.ui.btnEmo2,QtCore.SIGNAL("clicked()"),self.showEmoticonWindow2)

		# Thread Update Signal
		QtCore.QObject.connect(self.responseThread,QtCore.SIGNAL("output(QString,QString,QString)"),self.updateResponseThread)
		QtCore.QObject.connect(self.getPlurksThread,QtCore.SIGNAL("output(QString)"),self.updateResponse)

		QtCore.QObject.connect(self.responseThread,QtCore.SIGNAL("finished()"),self.updateUi)
		QtCore.QObject.connect(self.responseThread,QtCore.SIGNAL("terminated()"),self.updateUi)


	def updateResponseThread(self,plurkContent,prog,tot):

		if prog == 'none':
			self.ui.webView.setHtml(plurkContent)
		else:
			self.ui.webView.setHtml(plurkContent)
			self.ui.lblProgress.setText('Retrieved %s from %s responses' % (prog,tot))

	def updateResponse(self,plurkContent):
		self.ui.webView.setHtml(plurkContent)

	def updateUi(self):
		self.ui.btnShowResponses.setEnabled(True)

	def showEmoticonWindow1(self):
		global emoticonFlag
		emoticonFlag=1
		emoticon.show()

	def showEmoticonWindow2(self):
		global emoticonFlag
		emoticonFlag=2
		emoticon.show()


class qPlurkLogin(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_LoginForm()
		self.ui.setupUi(self)
		self.ui.txtPassword.setEchoMode(2)
		self.setWindowTitle('QPlurk Login')
		self.setFixedWidth(239)
		self.setFixedHeight(150)
		self.setWindowModality(2)
		QtCore.QObject.connect(self.ui.btnLogin,QtCore.SIGNAL("clicked()"),login)
		QtCore.QObject.connect(self.ui.txtPassword,QtCore.SIGNAL("returnPressed()"), login)
		
class qAbout(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_About()
		self.ui.setupUi(self)
		self.setWindowModality(2)
		self.setFixedWidth(199)
		self.setFixedHeight(131)


class Emoticon(QtGui.QWidget):

	def __init__(self, parent = None):
    
		QtGui.QWidget.__init__(self, parent)

		layout = QtGui.QGridLayout()
		path=os.getcwd()+'/smilies/'

		for var in range(0,64):
			smiley=path+str(int(var)+1)+'.gif'
			exec 'self.btn%s=QtGui.QPushButton(QtGui.QIcon(smiley),QtCore.QString(''))' % str(var)

			x=int(var)/10
			y=int(var)%10
			exec 'layout.addWidget(self.btn%s,x,y)' % str(var)
			exec 'self.btn%s.setFlat(True)' % str(var)
			exec 'QtCore.QObject.connect(self.btn%s, QtCore.SIGNAL("pressed()"), self.insertEmoticon)' % str(var)

		self.setLayout(layout)
		self.setWindowTitle(self.tr("Insert Smileys"))

	def insertEmoticon(self):
		global emoticonFlag
		emoticon=[':-))',':-)',':-D','(LOL)',':-P','(woot)',';-)',':-o','X-(',':-(',':-&;','(angry)','(annoyed)','(bye)','B-)','(cozy)','(sick)','(:','(goodluck)','(griltongue)','(mmm)','(hungry)','(music)','(tears)','(tongue)','(unsure)','(highfive)','(dance)','(doh)','(brokenheart)','(drinking)','(girlkiss)','(rofl)','(money)','(rock)','(nottalking)','(party)','(sleeping)','(thinking)','(bringit)','(worship)','(applause)','8-)','(gym)','(heart)','(devil)','(lmao)','(banana_cool)','(banana_rock)','(evil_grin)','(headspin)','(heart_beat)','(ninja)','(haha)','(evilsmirk)','(bigeyes)','(funkydance)','(idiot)','(lonely)','(scenic)','(hassle)','(panic)','(okok)','(yahoo)']

		for i in range(0,64):
			exec 'a=self.btn%s.isDown()' % str(i)
			if a:
				print emoticon[i+1]
				if emoticonFlag==1:
					curText=qplurk.ui.txtMsg.displayText()
					qplurk.ui.txtMsg.setText(curText+' '+emoticon[i+1])
				if emoticonFlag==2:
					curText=qplurk.ui.txtResponse.displayText()
					qplurk.ui.txtResponse.setText(curText+' '+emoticon[i+1])

### Login to Plurk
def login():
	global isLogin

	if isLogin==0:
		addQualifier()
		username=login.ui.txtUser.text()
		password=login.ui.txtPassword.text()

		## Login to Plurk
		if plurk.login(username,password) == True:
			isLogin=1
			
			## Display User Information
			qplurk.ui.lblUser.setText(plurk.nickname)
			qplurk.ui.lblUser2.setText(plurk.nickname)
			user_info = plurk.uidToUserinfo(plurk.uid)
			pageTitle=str(user_info['page_title'])

			qplurk.ui.lblKarma.setText(str(user_info['karma']))
			qplurk.ui.lblName.setText(str(user_info['full_name']))
			qplurk.setWindowTitle(pageTitle)
			gender=user_info['gender']

			if gender == 0:
				gender='Female'
			else:
				gender='Male'

			user_location="%s from %s" % (gender,str(user_info['location']))
			qplurk.ui.lblInfo1.setText(user_location)
			qplurk.ui.lblInfo2.setText(str(user_info['relationship']))

			login.hide()
			qplurk.show()
			getPlurks()
		else:
			qplurk.ui.lblUser.setText('Login Failed')
			MsgBox('Login Failed for user %s' % username)

	else:
		MsgBox('You Already Login')


### Post a plurk
def postPlurks():
	global isLogin

	if isLogin==1:
		plurkText=qplurk.ui.txtMsg.text()
		if plurkText=='':
			MsgBox('Plurk cant be empty')
		else:
			if len(plurkText)>140:
				MsgBox('Plurk cant be more than 140 characters')
			else:
				qualifier=qplurk.ui.cbQualifier.currentText()
				plurk.addPlurk(qualifier=qualifier, content=plurkText)
				getPlurks()
	else:
		MsgBox('Please Login First')

### Show Login Window
def showLogin():
	global isLogin
	if isLogin==0:
		login.show()
	else:
		MsgBox('You Already Login')

def showAbout():
	about.show()

### Retrieve Plurks
def getPlurks():
	qplurk.getPlurksThread.start()


### Get Plurks responses
def getResponses():
	qplurk.ui.btnShowResponses.setEnabled(False)
	qplurk.responseThread.start()

def respondToPlurk():

	plurkId=qplurk.ui.cbPlurkId.currentText()
	qualifier=qplurk.ui.cbQualifier2.currentText()
	content=qplurk.ui.txtResponse.text()

	if content == '':
		MsgBox('Please fill a response')
	else:
		if len(content)>140:
			MsgBox('Plurk Cant be more than 140 Characters')
		else:
			plurk.respondToPlurk(plurkId,lang='en',qualifier=qualifier,content=content)
			MsgBox('Successfuly send plurk response')
			getResponses()	

def exit():
	sys.exit(1)

def MsgBox(Message):
	QtGui.QMessageBox.information(qplurk,'QPlurk',Message,QtGui.QMessageBox.Ok)

def addQualifier():
	qplurk.ui.cbQualifier.clear()
	qplurk.ui.cbQualifier2.clear()

	qualifier=[':', 'loves',  'likes', 'shares', 'gives', 'hates', 'wants', 'wishes','needs', 'will', 'hopes', 'asks', 'has', 'was', 'wonders', 'feels', 'thinks', 'says', 'is']
	for i in qualifier:
		qplurk.ui.cbQualifier.addItem(i)
		qplurk.ui.cbQualifier2.addItem(i)




# Thread class for long running process  
#------------------------------------------------------------------------------------------------------------------------------

class responseThread(QtCore.QThread):
	global plurk,plurks,isLogin,plurkContent
	def __init__(self, parent = None):
		QtCore.QThread.__init__(self, parent)

	def __del__(self):
		self.wait()

	def run(self):
		plurkId=qplurk.ui.cbPlurkId.currentText()
		responses=plurk.getPlurkResponses(plurkId)['responses']

		# CSS
		plurkContent=css()

		for p in range(0,len(plurks)):
			if str(plurks[p]['plurk_id']) == str(plurkId):
				plurkContent+="<plurks><small><b>Plurk id %s Posted at %s:</small> </b> <br /> <b> %s </b> %s %s <br /> <small><b>responses</b></small> %s </plurks> <br />" % (plurks[p]['plurk_id'],plurks[p]['posted'],plurk.uidToNickname(plurks[p]['owner_id']),plurks[p]['qualifier'],plurks[p]['content'],plurks[p]['response_count'])

		self.emit(QtCore.SIGNAL("output(QString,QString,QString)"),plurkContent,'none','none')

		for i in range(0,len(responses)):
			commentator=plurk.uidToUserinfo(responses[i]['user_id'])['nick_name']
			comment=responses[i]['qualifier']+' '+responses[i]['content']
			posted=responses[i]['posted']
			plurkContent+='<blockquote><plurks> <small> Posted at %s <br /> %s %s </small></plurks></blockquote>' % (posted,commentator,comment)
			self.emit(QtCore.SIGNAL("output(QString,QString,QString)"),plurkContent,str(i+1),str(len(responses)))


#------------------------------------------------------------------------------------------------------------------------------
class getPlurksThread(QtCore.QThread):
	global plurk,plurks,isLogin,plurkContent
	def __init__(self, parent = None):
		QtCore.QThread.__init__(self, parent)

	def __del__(self):
		self.wait()

	def run(self):
		global isLogin,plurks,plurk

		qplurk.ui.cbPlurkId.clear()

		if isLogin == 1:
			plurks = plurk.getPlurks()

			# CSS
			plurkContent=css()

			for i in range(0,len(plurks)):
				plurkContent+="<plurks><small><b>Plurk id %s Posted at %s:</small> </b> <br /> <b> %s </b> %s %s <br /> <small><b>responses %s </b></small></plurks><br />" % (plurks[i]['plurk_id'],plurks[i]['posted'],plurk.uidToNickname(plurks[i]['owner_id']),plurks[i]['qualifier'],plurks[i]['content'],plurks[i]['response_count'])
				## Add Plurk ID to PlurkID Combo Box
				qplurk.ui.cbPlurkId.addItem(str(plurks[i]['plurk_id']))
				self.emit(QtCore.SIGNAL("output(QString)"),plurkContent)
		else:
			MsgBox('Please Login First')

# CSS
#------------------------------------------------------------------------------------------------------------------------------
def css():
	header='<head>'
	header+='<style type="text/css">'
	header+='plurks {'
	header+='border : 1px solid #000;'
	header+='float: left;'
	header+='margin: 2px;'
	header+='padding: 10px;'
	header+='background-color: #ccc;'
	header+='}'
	header+='</style>'
	header+='</head>'
	
	return(header)
# Main Loop  
#------------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	qplurk = qPlurk()
	login=qPlurkLogin()
	login.show()
	emoticon=Emoticon()
	about=qAbout()
	sys.exit(app.exec_())
