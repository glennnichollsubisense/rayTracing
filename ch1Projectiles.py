
import pointsVectors as pv
import projectiles as prjs


def tick (proj, env):
    position = pv.addAB (proj.getPosition(), proj.getVelocity())
    velocity = pv.addAB (proj.getVelocity(), pv.addAB(env.getGravity(), env.getWind()))

    return prjs.Projectile(position, velocity)

if __name__== "__main__":

    ##  Testing scripts

    aProjectile = prjs.Projectile (pv.newPoint(0, 0, 0), pv.newVector(200, 2000, 0))
    aEnvironment = prjs.Environment (pv.newVector(0, -10, 0), pv.newVector(0, 0, 0))

    counter = 0
    while not aProjectile.isBelowGround():

        print ('%i: pos = %s, velocity = %s' % (counter, aProjectile.getPosition(), aProjectile.getVelocity()))

        aProjectile = tick(aProjectile, aEnvironment)
        counter = counter+1
    
