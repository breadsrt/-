from panda3d.core import CollisionBox, CollisionNode


class Map:
    def __init__(self):
        self.model = 'blocks/dirt-block.glb'
        self.land = render.attachNewNode("Land")


    def create_block(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setPos(position)
        self.block.setPythonTag('type', self.model)
        self.block.reparentTo(self.land)

        hitbox = CollisionBox((-1,-1,-1), (1, 1, 1))
        blockNode =CollisionNode("block-collision-node")
        blockNode.addSolid(hitbox)
        collider = self.block.attachNewNode(blockNode)
        collider.setPythonTag('owner', self.block)
