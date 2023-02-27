
import cadquery as cq
from jupyter_cadquery.viewer.client import show, show_object
import numpy as np

height=100
depth=32
alpha=np.arctan(height/depth)
theta=np.pi-2*alpha
theta_degree=np.degrees(theta)
r=32+100*np.tan(np.pi/2-theta)
print(theta_degree,r)
r_inner=r-3

## Attempt 1, failed, the curve is NOT what I want 
# result=cq.Workplane('front').sphere(r,(1,0,0),0-theta_degree,0,30)-\
#     cq.Workplane('front').sphere(r-4,(1,0,0),-60,0,30)


## Attempt 2, using sweep, this is what I want
hoz_theta=np.pi/8
path = cq.Workplane("XZ").moveTo(r,0).\
    radiusArc((r*np.cos(theta),r*np.sin(theta)),r)
# result=cq.Workplane('XY').center(r,0).polygon(12,10).sweep(path,normal=[0,0,1])
# result=cq.Workplane('XY').moveTo(r_inner,0)\
#     .lineTo(r,0).radiusArc((r*np.cos(hoz_theta),r*np.sin(hoz_theta)),-r)\
#         .lineTo(r_inner*np.cos(hoz_theta),r_inner*np.sin(hoz_theta))\
#             .radiusArc((r_inner,0),r_inner).close()
result=cq.Workplane('XY').moveTo(r_inner*np.cos(-hoz_theta/2),r_inner*np.sin(-hoz_theta/2))\
    .lineTo(r*np.cos(hoz_theta/2),r*np.sin(-hoz_theta/2)).radiusArc((r*np.cos(hoz_theta/2),r*np.sin(hoz_theta/2)),-r)\
        .lineTo(r_inner*np.cos(hoz_theta/2),r_inner*np.sin(hoz_theta/2))\
            .radiusArc((r_inner*np.cos(-hoz_theta/2),r_inner*np.sin(-hoz_theta/2)),r_inner).close()
           
result=result.sweep(path,normal=(0,0,1))


## Get net
Ylim=r_inner*np.sin(hoz_theta)
Zlim=height
pad=4
grid_y_num=3
grid_z_num=5
string_width=1.2
print(Ylim,Zlim)
grid_y_size=(Ylim-pad*2-(grid_y_num-1)*string_width)/grid_y_num
pad_y_size=(Ylim-pad*2)/grid_y_num
grid_z_size=(Zlim-pad*2-(grid_z_num-1)*string_width)/grid_z_num
pad_z_size=(Zlim-pad*2)/grid_z_num

print(grid_y_size,grid_z_size)
for i in range(grid_y_num):
    for j in range(grid_z_num):
        # print(i,j)
        # print([pad+grid_y_size/2+i*pad_y_size,pad+grid_z_size/2+pad_z_size*j])
        net=cq.Workplane('YZ',origin=[0,-Ylim/2+pad+grid_y_size/2+i*pad_y_size,pad+grid_z_size/2+pad_z_size*j]).rect(grid_y_size,grid_z_size).extrude(300)
        # show_object(net)
        result=result.cut(net)

for i in [-Ylim/4,Ylim/4]:
    for j in [pad/2,Zlim-pad/2]:
        m3_hole=cq.Workplane('YZ',origin=[0,i,j]).circle(1.5).extrude(300)
        result=result.cut(m3_hole)
# net=cq.Workplane('YZ').circle(10).extrude(200)

# result=result.cut(net)

# # Render the solid
show_object(result)
# show_object(net)
cq.exporters.export(result,'center.stl')