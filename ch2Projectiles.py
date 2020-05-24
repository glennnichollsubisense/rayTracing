
import pointsVectors as pv
import projectiles as prjs
import canvas as cv
import colours as cl


def tick (proj, env):
    position = pv.addAB (proj.getPosition(), proj.getVelocity())
    velocity = pv.addAB (proj.getVelocity(), pv.addAB(env.getGravity(), env.getWind()))

    return prjs.Projectile(position, velocity)

if __name__== "__main__":

    ##  Testing scripts

    aProjectile = prjs.Projectile (pv.newPoint(0, 0, 0), pv.newVector(5, 5, 0))
    aEnvironment = prjs.Environment (pv.newVector(0, -1, 0), pv.newVector(0, 0, 0))

    aCanvas = cv.Canvas(640, 400)
    aCanvas.showMe(True)
    aCanvas.makeBlackCanvas()


    counter = 0
    while not aProjectile.isBelowGround():

        print ('%i: pos = %s, velocity = %s' % (counter, aProjectile.getPosition(), aProjectile.getVelocity()))

        pos = aProjectile.getPosition()

        try:
            aCanvas.setPixel (pos[0], aCanvas.height() - pos[1], cl.newYellow())
        except cv.outOfCanvasBounds:
            print ('%s out of bounds' % str(pos))
            

        aProjectile = tick(aProjectile, aEnvironment)
        counter = counter+1
    
    aCanvas.saveAs ('/home/pi/Projects/rayTracing/outputs/testCanvas.ppm')
