
import pointsVectors as pv

class Projectile():

    def __init__(self, position, velocity):

        self.position = position
        self.velocity = velocity

    def getPosition(self):
        return self.position

    def getVelocity(self):
        return self.velocity

    def isBelowGround(self):
        return self.getPosition()[1] < 0

class Environment():

    def __init__(self, gravity, wind):

        self.gravity = gravity
        self.wind = wind

    def getGravity(self):
        return self.gravity

    def getWind(self):
        return self.wind


def tick (proj, env):
    position = pv.addAB (proj.getPosition(), proj.getVelocity())
    velocity = pv.addAB (proj.getVelocity(), pv.addAB(env.getGravity(), env.getWind()))

    return Projectile(position, velocity)
    

if __name__== "__main__":

    ##  Testing scripts

    aProjectile = Projectile (pv.newPoint(0, 0, 0), pv.newVector(200, 2000, 0))
    aEnvironment = Environment (pv.newVector(0, -10, 0), pv.newVector(0, 0, 0))

    counter = 0
    while not aProjectile.isBelowGround():

        print ('%i: pos = %s, velocity = %s' % (counter, aProjectile.getPosition(), aProjectile.getVelocity()))

        aProjectile = tick(aProjectile, aEnvironment)
        counter = counter+1
    
