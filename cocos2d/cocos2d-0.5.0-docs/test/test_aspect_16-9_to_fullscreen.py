# This code is so you can run the samples without installing the package

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


from pyglet.gl import *
import cocos
from cocos.director import director

width = 768
height = 480
assert abs(width/float(height)-16/10.0)<0.0001

class ProbeRect(cocos.cocosnode.CocosNode):
    def __init__(self, width, height, color4):
        super(ProbeRect,self).__init__()
        self.color4 = color4
        w2 = int(width/2)
        h2 = int(height/2)
        #self.vertexes = [(-w2,h2,0),(w2,h2,0), (w2,-h2,0),(-w2,-h2,0)]
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
    starts a 16/10 aspect ratio window.
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
##    r863 : when fullscreen the screen misses areas at left and right
##    r863 + patch  arnaud : covers the dektop but missing areaas at top and bottom
##    r863 + patch arnaud with correction JF : no go
##    r863 + modified Director.set_projection: runs ok

##test runs: in win xp, display with 1680 x 1050,
##           r863 + modified Director.set_projection  -> 16:10 ratio: runs ok

