import numpy as np
import matplotlib.pyplot as plt

## unit 1px=1mm
## the total height is 90mm
## so Z range from 0 to 90

def parametric_circle(t,xc,yc,R):
    x = xc + R*np.cos(t)
    y = yc + R*np.sin(t)
    return x,y

def inv_parametric_circle(x,xc,R):
    t = np.arccos((x-xc)/R)
    return t

N = 30 # control point in the curve
R = 3 # radius
xc = 0.0 # center x
yc = 0.0 # center y
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
for z in np.arange(0,5,1):
    start_point = (xc + R*np.cos(0), yc + R*np.sin(0))
    end_point   = (xc + R*np.cos(np.pi/6), yc + R*np.sin(np.pi/6))


    start_t = inv_parametric_circle(start_point[0], xc, R)
    end_t   = inv_parametric_circle(end_point[0], xc, R)

    arc_T = np.linspace(start_t, end_t, N)


    X,Y = parametric_circle(arc_T, xc, yc, R)
    Z=[z]*N
    ax.scatter(X,Y,Z)
    ax.scatter([xc],[yc],[z],color='r')
plt.axis('equal') 
plt.show()