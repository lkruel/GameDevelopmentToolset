'''
Just a template to get a user off the ground!
'''

def init(nodes):
    '''
    Functions: We're passing the current node selection, but really you can pass any arguements you'd like. To test this out, highlight a SOP level node that has some geometry and click the Template shelf tool!
    '''

    '''
    We're just printing out a bunch of data from the classes you'll likely use the most. Remember to look these up in the hou documentation!
    http://www.sidefx.com/docs/houdini15.0/hom/hou/_index
    '''
    for node in nodes:
        #Accessing geometry at the SOP level
        #http://www.sidefx.com/docs/houdini15.0/hom/hou/SopNode
        print node.geometry()

        #Accessing points in the geometry
        #http://www.sidefx.com/docs/houdini15.0/hom/hou/Point
        print node.geometry().points()

        #Reporting the position of point 0
        print node.geometry().points[0].position()

        #Accessing point 0's position attribute
        print node.geometry().points[0].attribValue('P')

        #Creating nodes
        subnet = node.createOutputNode('subnet', 'TemplateSubnetTest')
        node1 = subnet.createNode('xform', 'TemplateXFormTest')
        node2 = subnet.createNode('null', 'TemplateNullTest')

        #Connecting two nodes
        node2.setFirstInput(node1)
        #Alternatively, you can directly set a specific input: node2.setInput(0, node1)

        #Laying out nodes
        #This command will set ALL children...previously made nodes WILL be moved :)
        subnet.layoutChildren()

        #Setting a bunch of parameters (setParms takes a dictionary input!)
        node1.setParms({'tx':1,
                        'ty':1,
                        'tz':1})

        #Setting keyframes
        hou.keyed_parm = node1.parm('rx')
        hou_keyframe = hou.Keyframe()
        hou_keyframe(setFrame(1))
        hou_keyframe.setValue(15)
        hou_keyed_parm.setKeyframe(hou_keyframe)

        hou.keyed_parm = node1.parm('ry')
        hou_keyframe = hou.Keyframe()
        hou_keyframe(setFrame(1))
        hou_keyframe.setValue(30)
        hou_keyed_parm.setKeyframe(hou_keyframe)

        hou.keyed_parm = node1.parm('rz')
        hou_keyframe = hou.Keyframe()
        hou_keyframe(setFrame(1))
        hou_keyframe.setValue(45)
        hou_keyed_parm.setKeyframe(hou_keyframe)

        #Evaluating Houdini variables
        print "Timeline start frame: {}".format(hou.expandString('$RFSTART'))
        print "Timeline end frame: {}".format(hou.expandString('$RFEND'))

        #Locking nodes to store their geometry
        #Useful for storing cooked geometry, if it needs to be refreshed, just unlock and lock again.
        #Also useful in case you need to send your hip file to someone without having to include external files.
        subnet.setHardLocked(True)
