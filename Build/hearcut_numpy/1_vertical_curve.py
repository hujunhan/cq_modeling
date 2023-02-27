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

N = 300 # control point in the curve
R = (3.5*np.sqrt(3)+1.5)/3.5*90 # radius
xc = -3.5*np.sqrt(3)/3.5*90 # center x
yc = 0.0 # center y
fig = plt.figure()
ax=fig.add_subplot(111)
start_point = (xc + R*np.cos(0), yc + R*np.sin(0))
end_point   = (xc + R*np.cos(np.pi/6), yc + R*np.sin(np.pi/6))

Y=np.arange

start_t = inv_parametric_circle(start_point[0], xc, R)
end_t   = inv_parametric_circle(end_point[0], xc, R)

arc_T = np.linspace(start_t, end_t, N)


X,Y = parametric_circle(arc_T, xc, yc, R)
ax.scatter(X,Y)
ax.scatter([xc],[yc],color='r')
plt.axis('equal') 
plt.show()