'''VertexAnimationTexture

This tool is designed to take a SOP level animation and generate a vertex animation texture from it.

The resulting texture is in this format.
x-axis: point number
y-axis: frame number
RGB: relative point position
'''

def init(nodes):
    if len(nodes) > 1 or len(nodes) <= 0:
        return "Please select a single node to process."
