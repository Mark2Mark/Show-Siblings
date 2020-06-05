# -*- coding: utf-8 -*-

## TODO:
## + add .sc support




from __future__ import print_function
from __future__ import absolute_import
import sys
import objc
from Foundation import NSAttributedString, NSRect
from AppKit import NSApplication, NSColor, NSBezierPath, NSForegroundColorAttributeName, NSFontAttributeName, NSFont
from vanilla import *
import traceback

import GlyphsApp

from .customSiblings import availableScripts as customAvailableScripts

##########################################################################################
# class ShowSiblings2ReporterLib:
class ShowSiblings2ReporterLib(object):

	version = "2.0"

	def __init__(self):

		self.tool = None
		self.UI_selectedDrawMethod = "Fill"
		self.UI_selectedScript = "Latin"
		self.Glyphs = NSApplication.sharedApplication()

		self.drawMethods = ["Fill", "Fill (flat)", "Stroke", "Stroke (no Overlap)"]


		self.CAS = customAvailableScripts()
		# # call outsourced custom Scripts:
		self.listOfAvailableScripts = []
		for key, value in self.CAS.items():
			scr = str(key).replace("__Siblings__", "")
			if scr not in self.listOfAvailableScripts:
				self.listOfAvailableScripts.append(scr)
		if "Twins" not in self.listOfAvailableScripts:
			self.listOfAvailableScripts.append("Twins")


		# UI
		self.prefwindow = reporterPreferenceWindow(self)

		self.drawNodes = 0
		self.R, self.G, self.B = 0.15, 0.40, 0.25 # 0.18, 0.337, 0.859

		# print "This is not being printed. WHY? [in Version 2.3b (862) it is printed on Glyphs launch]"


	def Open(self):
		self.prefwindow.w.show()
		# self.RefreshView()
	
	def Close(self):
		self.prefwindow.w.hide()
		# self.RefreshView()



	###################################
	def niceGlyphName(self, glyphName):
		'''
		RETURN THE NICENAME (GlyphsApp Convention) FOR THE GIVEN GLYPHNAME
		VIA THE `SCHOULD-BE-GLYPHNAME` AS LONG AS IT HAS THE CORRECT UNICODE
		e.g. Your unicode 0411 is called "BeCyrillic", using its unicode to rename to "Be-cy"
		'''	
		try:
			uni = self.Glyphs.font.glyphs[glyphName].unicode
		except:
			uni = None
		try:
			thisNiceGlyphName = str(self.Glyphs.glyphInfoForUnicode(uni).name)
			return thisNiceGlyphName
		except:
			# print "could not get niceGlyphName from %s, using %s instead" % (glyphName, glyphName)
			return str(self.Font.glyphForName_(glyphName).name)

	#********************
	def customItalicConstruction(self):
		'''
		RETURN LIST OF GLYPHNAMES FROM CP 'Italic Construction' IF GIVEN
		'''
		try:
			parameterString = self.Font.customParameters['Italic Construction']
			if parameterString is not None:
				return parameterString.split(", ")
		except:
			return None
	#********************



	# def allScripts(self):
	# 	scripts = {}
	# 	for vars, value in dict(locals()).items():
	# 		if vars.endswith("__Siblings__"):
	# 			scripts[vars] = value
	# 	return scripts



	def availableTwins(self, Glyph):
		'''
		SIMILAR TO THE OUTSOURCED METHOD `availableScripts()`
		BUT INSTEAD OF HARDCODING THE SIBLINGS, IT COMPUTES THE SIBLINGS
		AND RETURNS THEM AS A DICTIONARY, WHICH LOOKS THE SAME AS THE ONE
		FROM `availableScripts()`
		'''
		scripts = {}
		Twins__Siblings__ = []
		for ggg in self.Font.glyphs:
			if "." in ggg.name:
				glyphNameWithoutSuffix = str(ggg.name.split(".")[0])
				#if glyphNameWithoutSuffix == Glyph.name:
				if glyphNameWithoutSuffix == str(Glyph.name.split(".")[0]):
					if glyphNameWithoutSuffix not in Twins__Siblings__:
						Twins__Siblings__.append(glyphNameWithoutSuffix)
					Twins__Siblings__.append(ggg.name)
		Twins__Siblings__ = [tuple(Twins__Siblings__)]
		
		for vars, value in dict(locals()).items():
			if vars.endswith("__Siblings__"):
				scripts[vars] = value
		return scripts





	def drawSiblings( self, layer, scale, isActiveLayer=False ):
		self.label = []
		self.labelActive = []
		self.scale = scale
		self.isActiveLayer = isActiveLayer


		# print self.CAS # custom scripts imported, dict()

		try:
			# Glyphs = NSApplication.sharedApplication()
			Glyph = layer.parent
			self.Font = Glyph.parent
			thisMaster = self.Font.selectedFontMaster
			masters = self.Font.masters

			#********************			

			activeMasterIndex = masters.index(thisMaster)
			currentGlyphUnicode = Glyph.unicode
			niceGlyphName = self.niceGlyphName(Glyph.name)
			if self.isActiveLayer:
				self.activeGlyphName = niceGlyphName ## quickly added for `labelGlyphNames() Method`
			

			## leave glyphs out, that are drawn exactly the same in different sripts.
			## it is better to use components in these cases, instead of having this plugin
			## overlapping the exact same shapes too often
			

			#************************************
			latin__Siblings__ = []
			#("D", "O"] ## this adds the D to the whole O-Group ... not nice.

			latin__Siblings__.append( ("c", "e", "o") )
			latin__Siblings__.append( ("b", "p") )	
			'''
			Working draft; ToDo: filter for a & g to add to this group, otherwise an s will be added as well if it is part of the custon parameter
			'''
			# 1)
			addItalic_a_Group = [] ## check for `a` and `g`
			if self.customItalicConstruction() != None:
				for x in self.customItalicConstruction():
					addItalic_a_Group.append( x )
				latin__Siblings__.append( ("d", "q", "u") + tuple(addItalic_a_Group) )
			else:
				latin__Siblings__.append( ("d", "q", "u") )
			# 2)
			## a into n group ???
			if self.customItalicConstruction() != None:
				if "a" not in self.customItalicConstruction():
					latin__Siblings__.append( ("h", "l", "n", "r", "a") )
				else:
					latin__Siblings__.append( ("h", "l", "n", "r") )
			else:
				latin__Siblings__.append( ("h", "l", "n", "r") )
			# latin__Siblings__.append( ("h", "l", "n", "r") )






			# ##################
			# GET SCRIPT FROM UI
			# ##################
			try:
				# UI_chosenSiblings = self.availableScripts()["%s%s" % (self.UI_selectedScript, "__Siblings__")]
				UI_chosenSiblings = self.CAS["%s%s" % (self.UI_selectedScript, "__Siblings__")]
			except:
				UI_chosenSiblings = self.availableTwins(Glyph)["%s%s" % (self.UI_selectedScript, "__Siblings__")]


			# ######################
			# GET DRAWMETHOD FROM UI
			# ######################
			fill = False
			fillStroke = False
			strokeOverlapped = False
			strokeOutlined = False

			if self.UI_selectedDrawMethod == self.drawMethods[0]:
				fill = True # Fill
				fillStroke = True

			if self.UI_selectedDrawMethod == self.drawMethods[1]:
				fill = True # Fill Flat

			if self.UI_selectedDrawMethod == self.drawMethods[2]:
				strokeOverlapped = True # Stroke

			if self.UI_selectedDrawMethod == self.drawMethods[3]:
				strokeOutlined = True # Stroke no Overlap
			# ##################





			for idx, group in enumerate(UI_chosenSiblings):
				try:
					alpha = .4/float(len(group))
				except:
					alpha = .4/float(1) # avoid division by 0
				
				thisSiblings = UI_chosenSiblings[idx]		

				# # reset list if current glyph has no siblings:
				# if niceGlyphName not in thisSiblings:
				# 	self.prefwindow.updateList()

				# otherwise:
				if niceGlyphName in thisSiblings:
					for thisGlyphName in thisSiblings:
						if niceGlyphName != thisGlyphName:

							sibling = self.Font.glyphForUnicode_(self.Glyphs.glyphInfoForName(thisGlyphName).unicode)
							if sibling == None:
								sibling = self.Font.glyphForName_(thisGlyphName)


							### NEW +++++++++
							if self.isActiveLayer:
								self.labelActive.append(sibling.name)
								# self.prefwindow.w.siblingsList.set( [ x for x in self.labelActive ]  )
								# self.prefwindow.updateList()
								self.sibListCopy = self.labelActive # make a copy of the current state, will be passed into labelGlyphNames()
							### NEW +++++++++


							if sibling:
								thisLayer = sibling.layers[activeMasterIndex]
								self.label.append(sibling.name)
								# if self.isActiveLayer == "activeLayer":
								# 	self.labelActive.append(sibling.name)
								# 	self.prefwindow.w.siblingsList.set( [ x for x in self.labelActive ]  )
								# 	print self.labelActive

								try:
									thisBezierPathWithComponent = thisLayer.copyDecomposedLayer().bezierPath
								except:
									thisBezierPathWithComponent = thisLayer.copyDecomposedLayer().bezierPath()

								if thisBezierPathWithComponent:
									if fill:
										NSColor.colorWithCalibratedRed_green_blue_alpha_( self.R, self.G, self.B, alpha ).set() # 0.0, 0.15, 0.2
										thisBezierPathWithComponent.fill()

									if fillStroke:
										NSColor.colorWithCalibratedRed_green_blue_alpha_( 1, 1, 1, 0.5 ).set()
										thisBezierPathWithComponent.setLineWidth_( 3 / self.scale)
										thisBezierPathWithComponent.stroke()

										NSColor.colorWithCalibratedRed_green_blue_alpha_( 0.5, 0.5, 0.7, 0.5 ).set()
										thisBezierPathWithComponent.setLineWidth_( 1 / self.scale)
										thisBezierPathWithComponent.stroke()


									if strokeOverlapped:
										NSColor.colorWithCalibratedRed_green_blue_alpha_( self.R, self.G, self.B, 0.3 ).set() # 1, 0.0, 0.0, 0.5
										if thisBezierPathWithComponent:
											thisBezierPathWithComponent.setLineWidth_( 1 / self.scale )
											thisBezierPathWithComponent.stroke()

									if strokeOutlined:
										thisLayerCopy = thisLayer.copyDecomposedLayer()
										thisLayerCopy.removeOverlap()
										thisBezierPathWithComponent = thisLayerCopy.copyDecomposedLayer().bezierPath
										NSColor.colorWithCalibratedRed_green_blue_alpha_( self.R, self.G, self.B, 0.3 ).set()
										if thisBezierPathWithComponent:
											thisBezierPathWithComponent.setLineWidth_( 1 / self.scale )
											thisBezierPathWithComponent.stroke()


									if self.drawNodes:
										handleSize = 5/self.scale
										if thisLayer.paths:
											for path in thisLayer.paths:
												for node in path.nodes:
													if node.type != "offcurve":
														self.drawBadge( (node.x, node.y), handleSize, "red" )
													else:
														self.drawBadge( (node.x, node.y), handleSize, "blue" )


					self.drawTextAtPoint( "\n".join(self.label), (5, -100), fontColor=NSColor.colorWithCalibratedRed_green_blue_alpha_( self.R, self.G, self.B, 0.4 ) )

		except:
		 	pass # print traceback.format_exc()

	
	def labelGlyphNames(self, mylist):
		output = []
		output.append(self.activeGlyphName)
		# for glyph in self.label:
		for glyph in mylist:
			output.append(glyph)
		return output


	def drawTextAtPoint( self, text, textPosition, fontSize=10.0, fontColor=NSColor.redColor() ):
		try:
			# glyphEditView = self.controller.graphicView()
			glyphEditView = self.Glyphs.font.currentTab.graphicView()
			fontAttributes = { 
				NSFontAttributeName: NSFont.labelFontOfSize_( fontSize/ self.scale ),
				NSForegroundColorAttributeName: fontColor }
			displayText = NSAttributedString.alloc().initWithString_attributes_( text, fontAttributes )
			textAlignment = 6 # top left: 6, top center: 7, top right: 8, center left: 3, center center: 4, center right: 5, bottom left: 0, bottom center: 1, bottom right: 2
			displayText.drawAtPoint_alignment_( textPosition, textAlignment )
		except:
			print(traceback.format_exc())


	def drawBadge(self, xxx_todo_changeme, size, color):
		(x, y) = xxx_todo_changeme
		thisAlpha = 0.75
		if color == "red":
			thisColor = 0.5, 0.7, 0.2, thisAlpha
		if color == "blue":
			thisColor = 0.2, 0.2, 0.7, thisAlpha
		myRect = NSRect( ( x - size/2, y- size/2 ), ( size, size ) )
		thisPath = NSBezierPath.bezierPathWithOvalInRect_( myRect )
		NSColor.colorWithCalibratedRed_green_blue_alpha_( *thisColor ).set()
		thisPath.fill()


	def RefreshView(self):
		try:
			# Glyphs = NSApplication.sharedApplication()
			currentTabView = self.Glyphs.font.currentTab
			if currentTabView:
				currentTabView.graphicView().setNeedsDisplay_(True)
		except:	pass



	# ####################################
	# FUNCTIONS CALLED BY PREFERENCE PANEL
	def getValue(self, value, senderID):
		try:
			if senderID == "DRAWMETHOD":
				self.UI_selectedDrawMethod = self.drawMethods[value]
		except: pass
		
		try:
			if senderID == "SCRIPT":
				# self.UI_selectedScript = self.scripts[value]
				self.UI_selectedScript = self.listOfAvailableScripts[value]
		except: pass

	def setDrawNodes(self, value):
		self.drawNodes = value



class reporterPreferenceWindow(object):

	def __init__(self, parent):
		#------------------------------------------------------
		### MONKEY PATCH
		def __setID(self, customTitle):
			self._nsObject.setIdentifier_(customTitle)

		def __getID(self):
			return self._nsObject.identifier()

		PopUpButton.setID = __setID
		PopUpButton.getID = __getID

		self.windowWidth = 150

		self.parent = parent
		self.y = 10
		self.mutableY = 0
		self.w = FloatingWindow((0, 0), "Show Siblings %s" % self.parent.version, closable = False, )
		self.w.PopUpButtonFillOrStroke = PopUpButton((10, self.y, -10, 20), self.parent.drawMethods, sizeStyle="small", callback=self.PopUpButtonCallback)
		self.w.PopUpButtonFillOrStroke.setID("DRAWMETHOD")

		self.y += 25
		self.w.PopUpButtonScript = PopUpButton((10, self.y, -10, 20), self.parent.listOfAvailableScripts, sizeStyle="small", callback=self.PopUpButtonCallback)
		self.w.PopUpButtonScript.setID("SCRIPT")

		self.y += 25
		self.w.CheckDrawNodes = CheckBox((10, self.y, -10, 20), "Display Nodes", sizeStyle="small", callback=self.CheckBoxCallback)

		self.y += 25
		self.w.ButtonSiblingsToTab = Button((10, self.y, -10, 20), "Open Siblings in Tab", sizeStyle="small", callback=self.siblingsToTab)
		# self.w.ButtonSiblingsToTab = Button((10, y, -10, 20), "Expand Siblings", sizeStyle="small", callback=self.expandSiblingsInTab)
		self.y += 25

		##### NEW + + + + + + + + +
		# listRows = 3
		# listHeight = listRows*22
		# self.w.siblingsList = List(( 10, self.y, -10, listHeight), [],
		# 			# selectionCallback=self.selectionCallback,
		# 			allowsMultipleSelection=False,
		# 			drawFocusRing=False,
		# 			rowHeight=20,
		# 			autohidesScrollers=True,
		# 			)
		# self.mutableY += listHeight + 10
		##### NEW + + + + + + + + +
		# self.w.resize(self.windowWidth, self.y + self.mutableY + 20)
		self.w.resize(self.windowWidth, self.y)

	# def updateList(self):
	# 	thisSiblingList = [ x for x in self.parent.labelActive ]
	# 	self.mutableY = len(thisSiblingList) * 22
	# 	self.w.siblingsList.set( thisSiblingList )
	# 	self.w.siblingsList.resize(self.windowWidth-20, self.mutableY )
	# 	# self.w.resize(self.windowWidth, self.y + self.mutableY +10) # this slows glyphs down as hell (!) only call on change of active layer


	def PopUpButtonCallback(self, sender):
		try:
			self.parent.getValue( sender.get(), sender.getID() )
		except:
			self.parent.getValue( 0, sender.getID() )
		self.parent.RefreshView()


	def CheckBoxCallback(self, sender):
		self.parent.setDrawNodes( sender.get() )
		self.parent.RefreshView()


	def siblingsToTab(self, sender):
		try:
			tabOutput = "/" + "/".join( [ x for x in self.parent.labelGlyphNames(self.parent.sibListCopy) ] )
			self.parent.Font.newTab(tabOutput)
		except:
			print(traceback.format_exc()) # this does not work sometimes?!?!?!*
			# *) always after changing active layer via keys: fn+left/right
			#    Once you clicked in the view, the tab opening works



	# def expandSiblingsInTab(self, sender):
	# 	'''
	# 	*UC* because it inserts e.g. "/be-cy" and not the glyph, like newTab() does
	# 	'''
	# 	try:
	# 		view = self.parent.Glyphs.font.currentTab.graphicView()
	# 		tabOutput = "/" + "/".join( [ x for x in self.parent.labelGlyphNames() ] )
	# 		# self.parent.Font.newTab(tabOutput)
	# 		view.insertText_replacementRange_(tabOutput, (0, 0))
	# 	except:
	# 		print traceback.format_exc()			




