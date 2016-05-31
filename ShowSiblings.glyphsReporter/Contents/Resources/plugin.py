# encoding: utf-8

###########################################################################################################
#
#
#	Reporter Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################

from GlyphsApp.plugins import *
from vanilla import *
import traceback
import inspect


import ShowSiblings2ReporterUI.ShowSiblings2ReporterLIB
ShowSiblings2ReporterLIB = ShowSiblings2ReporterUI.ShowSiblings2ReporterLIB.ShowSiblings2ReporterLib()


class ShowSiblings(ReporterPlugin):

	def settings(self):

		self.menuName = Glyphs.localize({'en': u'* Show Siblings',}) #  👫

		try:
			self.ShowSiblings2ReporterLIB = ShowSiblings2ReporterLIB
			# self.ShowSiblings2ReporterLIB.__init__()
			# self.ShowSiblings2ReporterLIB.tool = self

			### read plugin view status from the defaults just for the case it is active on Glyphs launch:
			### Otherwise it will be (de)activated via the View menu toggle
			activeReporterPlugins = NSUserDefaults.standardUserDefaults().objectForKey_("visibleReporters")
			# if "com.markfromberg.ShowSiblings2" in activeReporterPlugins:
			if "com.markfromberg.%s" % self.__class__.__name__ in activeReporterPlugins:
				self.ShowSiblings2ReporterLIB.Open()
			else:
				pass

			return self
		except Exception as e:
			# self.logToConsole( "init: %s" % str(e) )
			print "init: %s" % str(e)

		

	def willActivate(self):
		try:
			self.ShowSiblings2ReporterLIB.Open()
		except:
			print "[%s]:\n%s" % (self.nameOfFunction(), traceback.format_exc())
		# super(ShowSiblings2, self).willActivate()

	def willDeactivate(self):
		try:
			self.ShowSiblings2ReporterLIB.Close()
		except:
			print "[%s]:\n%s" % (self.nameOfFunction(), traceback.format_exc())
		# super(ShowSiblings2, self).willDeactivate()

	def toggleWhoeUI(self):
		try:
			if self.Glyphs.font.currentTab:
				print "TABD"
				self.ShowSiblings2ReporterLIB.Open()
		except:
			print "[%s]:\n%s" % (self.nameOfFunction(), traceback.format_exc())
		# super(ShowSiblings2, self).willActivate()		


	def nameOfFunction(self):
		# use [0][3] if this function is not used nested like here
		return "[%s]" % inspect.stack()[1][3]
		

	def background(self, layer):  # def foreground(self, layer):
		try:
			self.ShowSiblings2ReporterLIB.drawSiblings(layer, self.getScale(), isActiveLayer=True )
		except:
			print "[%s]:\n%s" % (self.nameOfFunction(), traceback.format_exc())

	def inactiveLayers(self, layer):  # def foreground(self, layer):
		try:
			self.ShowSiblings2ReporterLIB.drawSiblings(layer, self.getScale() )

			path = layer.copyDecomposedLayer().bezierPath
			NSColor.blackColor().set()
			if path:
				path.fill()


		except:
			print "[%s]:\n%s" % (self.nameOfFunction(), traceback.format_exc())


