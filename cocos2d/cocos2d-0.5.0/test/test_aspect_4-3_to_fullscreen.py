# This code is so you can run the samples without installing the package

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pyglet.gl import *
import cocos
from cocos.director import director

width = 640
height = 480
assert abs(width/float(height)-4/3.0)<0.0001

class ProbeRect(cocos.cocosnode.CocosNode):
    def __init__(self, width, height, color4):
        super(ProbeRect,self).__init__()
        self.color4 = color4
        w2 = int(width/2)
        h2 = int(height/2)
        self.vertexes = [(0,0,0),(0,height,0), (width,height,0),(width,0,0)]

    def draw(self):
        glPushMatrix()
        self.transform()
        glBegin(GL_QUADS)
        glColor4ub( *self.color4 )
        for v in self.vertexes:
            glVertex3i(*v)
        glEnd()
        glPopMatrix()

class TestLayer(cocos.layer.Layer):
    def __init__(self):
        super(TestLayer, self).__init__()
        self.add( ProbeRect(width, height, (0,0,255,255)), z=1)
        border_size = 10
        inner = ProbeRect(width-2*border_size, height-2*border_size, (255,0,0,255))
        inner.position = (border_size, border_size)
        self.add(inner, z=2 )
        outer = ProbeRect(width+2*border_size, height+2*border_size, (255,255,0,255))
        outer.position = (-border_size, -border_size)
        self.add(outer, z=0 )
                
def usage():
    print """
    starts a 4/3 aspect ratio window.
    CTRL-F toggles fullscreen

    The scene draw three boxes, centered at the window center.
      blue box: the exact same size as the window
      yellow box: a little bigger than blue box
      red box: a little smaller than blue box
    Draw order is yellow, blue, red
    You must see no yellow, and a red rectangle with equal sized blue borders
    """


usage()

director.init( width=width, height=height, resizable=False )
director.window.set_caption('aspect ratio and fullscreen - see console for usage')
director.show_FPS = True
scene = cocos.scene.Scene()
scene.add(TestLayer())
director.run( scene )


##test runs: (in win xp, display with 4:3 ratio)
##    r809 : ok (except losing focus (by alt-tab by example) dont let the other
##           window go on top
##    r863 : ok (same)
##    r863 + modified Director.set_projection: runs ok

##    r880 : broken: 
##            1) I see yellow on the right and left, so it shows more x than desired
##            2) The window is misplaced, ie the desktop shows
##            3) The window's client height is less than desired.
##            (should be same as screen height)
##            4) Previuos CTRL-F behavoir was toggle, now is allways 'go_fullscreem'

##test runs: in win xp, display with 1680 x 1050,
##           r863 + modified Director.set_projection  -> 16:10 ratio: runs ok
