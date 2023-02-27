import cadquery as cq
from jupyter_cadquery.viewer.client import show, show_object

dock_height=60
thick=3
dock_width=48
side_with=16

lidar_mount_size=28.2
lidar_hole_diameter=2

# result = cq.Workplane("XY").box(height, width, thickness) 
pts=[
    (0,dock_height-thick),
    (dock_width/2.0-thick,dock_height-thick),
    (dock_width/2.0-thick,0),
    (dock_width/2.0+side_with,0),
    (dock_width/2.0+side_with,thick),
    (dock_width/2.0,thick),
    (dock_width/2.0,dock_height),
    (0,dock_height),
]



## Construct the basic mount base
result=cq.Workplane('front').polyline(pts).mirrorY().extrude(24,both=True)

## Drill the hole for lidar to mount on base
result=result.faces('>Y').workplane().rect(lidar_mount_size,lidar_mount_size,forConstruction=True)\
    .vertices().hole(lidar_hole_diameter)

## Drill the hole for base to mount on robot
result=result.faces('<Y').workplane().rect(dock_width+8*2,32,forConstruction=True)\
    .vertices().hole(4)
    
# Render the solid
show_object(result)
cq.exporters.export(result,'result.stl')