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
