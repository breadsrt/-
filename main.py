from math import *
from direct.showbase.ShowBase import  ShowBase, CollisionRay, CollisionNode, CollisionHandlerQueue, CollisionTraverser

from map import Map

def degToRad(degrees):
    return degrees * (3.14 / 180.0)
class Game(ShowBase):
    def __init__(self):
        super().__init__()
        map = Map()
        map.create_block((0,0,0))
        map.model = 'blocks/stone-block.glb'
        map.create_block((0, 0,2))
        map.create_block((0, 0, 4))
        map.create_block((0, 0, 6))
        map.create_block((0, 0, 8))
        map.create_block((0, 0, 10))
        map.create_block((0, 0, 12))
        map.create_block((0, 0, 14))
        map.create_block((0, 0, 16))
        map.create_block((2, 0, 16))
        map.create_block((4, 0, 16))
        map.create_block((6, 0, 16))
        map.create_block((8, 0, 16))
        map.create_block((10, 0, 16))
        map.create_block((12, 0, 16))
        map.create_block((14, 0, 16))
        map.create_block((16, 0, 16))
        map.create_block((16, 0, 14))
        map.create_block((16, 0, 12))
        map.create_block((16, 0, 10))
        map.create_block((16, 0, 8))
        map.create_block((16, 0, 6))
        map.create_block((16, 0, 4))
        map.create_block((16, 0, 2))
        map.create_block((16, 0, 0))
        map.create_block((14, 0, 0))
        map.create_block((12, 0, 0))
        map.create_block((10, 0, 0))
        map.create_block((8, 0, 0))
        map.create_block((6, 0, 0))
        map.create_block((4, 0, 0))
        map.create_block((2, 0, 0))
        self.setupCamera()
        self.setupControls()
        self.taskMgr.add(self.update, 'update')

    def update_move(self, key, value):
        self.key_map[key] = value
    def setupControls(self):
        self.key_map = {
            "forward": False,
            "backward": False,
            "left": False,
            "right": False,
            "up": False,
            "down": False,
        }

        self.accept("w", self.update_move, ["forward", True])
        self.accept("w-up", self.update_move, ["forward", False])
        self.accept("s", self.update_move, ["backward", True])
        self.accept("s-up", self.update_move, ["backward", False])
        self.accept("a", self.update_move, ["left", True])
        self.accept("a-up", self.update_move, ["left", False])
        self.accept("d", self.update_move, ["right", True])
        self.accept("d-up", self.update_move, ["right", False])
        self.accept("space", self.update_move, ["up", True])
        self.accept("space-up", self.update_move, ["up", False])
        self.accept("shift", self.update_move, ["down", True])
        self.accept("shift-up", self.update_move, ["down", False])





    def update(self, task):
        dt = globalClock.getDt()

        speed = 10

        x = y = z = 0
        if self.key_map["forward"]:
            x -=dt * speed * sin(degToRad(self.camera.getH()))
            y += dt * speed * cos(degToRad(self.camera.getH()))
        if self.key_map['backward']:
            x += dt * speed * sin(degToRad(self.camera.getH()))
            y -= dt * speed * cos(degToRad(self.camera.getH()))
        if self.key_map['left']:
            x -= dt * speed * cos(degToRad(self.camera.getH()))
            y -= dt * speed * sin(degToRad(self.camera.getH()))
        if self.key_map['right']:
            x += dt * speed * cos(degToRad(self.camera.getH()))
            y += dt * speed * sin(degToRad(self.camera.getH()))
        if self.key_map['up']:
            z += dt * speed
        if self.key_map['down']:
            z -= dt * speed

        self.camera.setPos(
            self.camera.getX() +x,
            self.camera.getY() + y,
            self.camera.getZ() + z,
        )
        return task.cont
    def setupCamera(self):
        self.disableMouse()
        self.camera.setPos(0, -10, 0)
        self.camLens.setFov(80)

        ray = CollisionRay()
        ray.setFromLens(self.cam.node(), 0, 0)
        rayNode = CollisionNode('ray ')
        rayNode.addSolid(ray)

        rayNodePath = self.camera.attachNewNode(rayNode)

        self.ray_queue = CollisionHandlerQueue()
        self.cTrav = CollisionTraverser()
        self.cTrav.addCollider(rayNodePath,self.ray_queue)


game = Game()
game.run()