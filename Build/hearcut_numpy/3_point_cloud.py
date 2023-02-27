import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d
## unit 1px=1mm
## the total height is 90mm
## so Z range from 0 to 90
## 
pcl = o3d.geometry.PointCloud()

def parametric_circle(t,xc,yc,R):
    x = xc + R*np.cos(t)
    y = yc + R*np.sin(t)
    return x,y

def inv_parametric_circle(x,xc,R):
    t = np.arccos((x-xc)/R)
    return t

x_all=[]
y_all=[]
z_all=[]
N = 30 # control point in the curve
R_z = (3.5*np.sqrt(3)+1.5)/3.5*90 # radius
R=1.5/3.5*90
xc_z = -3.5*np.sqrt(3)/3.5*90 # center x

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
for z in np.arange(0,89,1):
    theta=np.arctan2(z,-xc_z)
    R=R_z+10-R_z*np.cos(theta)
    xc = 0.0 # center x
    yc = 0.0 # center y
    start_point = (xc + R*np.cos(0), yc + R*np.sin(0))
    end_point   = (xc + R*np.cos(np.pi/6), yc + R*np.sin(np.pi/6))


    start_t = inv_parametric_circle(start_point[0], xc, R)
    end_t   = inv_parametric_circle(end_point[0], xc, R)

    arc_T = np.linspace(start_t, end_t, N)


    X,Y = parametric_circle(arc_T, xc, yc, R)
    Z=[z]*N
    x_all.extend(X)
    y_all.extend(Y)
    z_all.extend(Z)
    ax.scatter(X,Y,Z)
    ax.scatter([0],[yc],[z],color='r')

    ## 0 side
    ax.scatter(R+np.linspace(0,5,50),[0]*50,[z]*50)
    ax.scatter((R+np.linspace(0,5,50))*np.cos(np.pi/6),(R+np.linspace(0,5,50))*np.sin(np.pi/6),[z]*50)
    
    
    if z==0 or z==88:
        for offset in np.arange(0,5,0.1):
            R=R_z+10+offset-R_z*np.cos(theta)
            xc = 0.0 # center x
            yc = 0.0 # center y
            start_point = (xc + R*np.cos(0), yc + R*np.sin(0))
            end_point   = (xc + R*np.cos(np.pi/6), yc + R*np.sin(np.pi/6))


            start_t = inv_parametric_circle(start_point[0], xc, R)
            end_t   = inv_parametric_circle(end_point[0], xc, R)

            arc_T = np.linspace(start_t, end_t, N)


            X,Y = parametric_circle(arc_T, xc, yc, R)
            Z=[z]*N
            ax.scatter(X,Y,Z)

for z in np.arange(0,89,1):
    theta=np.arctan2(z,-xc_z)
    R=R_z+15-R_z*np.cos(theta)
    xc = 0.0 # center x
    yc = 0.0 # center y
    start_point = (xc + R*np.cos(0), yc + R*np.sin(0))
    end_point   = (xc + R*np.cos(np.pi/6), yc + R*np.sin(np.pi/6))


    start_t = inv_parametric_circle(start_point[0], xc, R)
    end_t   = inv_parametric_circle(end_point[0], xc, R)

    arc_T = np.linspace(start_t, end_t, N)


    X,Y = parametric_circle(arc_T, xc, yc, R)
    Z=[z]*N
    ax.scatter(X,Y,Z)
    ax.scatter([0],[yc],[z],color='r')
plt.axis('equal') 
plt.show()