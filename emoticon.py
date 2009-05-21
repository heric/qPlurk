#!/usr/bin/env python

import os,sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Emoticon(QWidget):

	def __init__(self, parent = None):
    
		QWidget.__init__(self, parent)

		layout = QGridLayout()
		path=os.getcwd()+'/smilies/'

		for var in range(0,64):
			smiley=path+str(int(var)+1)+'.gif'
			exec 'self.btn%s=QPushButton(QIcon(smiley),QString(''))' % str(var)

			x=int(var)/10
			y=int(var)%10
			exec 'layout.addWidget(self.btn%s,x,y)' % str(var)
			exec 'self.btn%s.setFlat(True)' % str(var)
			exec 'self.connect(self.btn%s, SIGNAL("pressed()"), self.insertEmoticon)' % str(var)

		self.setLayout(layout)
		self.setWindowTitle(self.tr("Insert Smileys"))

	def insertEmoticon(self):
		global emoticonFlag
		emoticon=[':-))',':-)',':-D','(LOL)',':-P','(woot)',';-)',':-o','X-(',':-(',':-&;','(angry)','(annoyed)','(bye)','B-)','(cozy)','(sick)','(:','(goodluck)','(griltongue)','(mmm)','(hungry)','(music)','(tears)','(tongue)','(unsure)','(highfive)','(dance)','(doh)','(brokenheart)','(drinking)','(girlkiss)','(rofl)','(money)','(rock)','(nottalking)','(party)','(sleeping)','(thinking)','(bringit)','(worship)','(applause)','8-)','(gym)','(heart)','(devil)','(lmao)','(banana_cool)','(banana_rock)','(evil_grin)','(headspin)','(heart_beat)','(ninja)','(haha)','(evilsmirk)','(bigeyes)','(funkydance)','(idiot)','(lonely)','(scenic)','(hassle)','(panic)','(okok)','(yahoo)']

		for i in range(0,64):
			exec 'a=self.btn%s.isDown()' % str(i)
			if a:
				if emoticonFlag==1:
					qplurk.ui.txtMsg.setText(qplurk.ui.txtMsg.Text()+emoticon[i+1])
				if emoticonFlag==2:
					qplurk.ui.txtResponse.setText(qplurk.ui.txtResponse.Text()+emoticon[i+1])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Emoticon = Emoticon()
    Emoticon.show()
    sys.exit(app.exec_())
