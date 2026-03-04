import gmsh
import sys
import math

def viga(ne1=4,ne2=8,L=10,l=1,elementOrder=1,popup=True):

    gmsh.initialize()
    gmsh.model.add("barra")

    p1 = gmsh.model.geo.addPoint(0,0,0)
    p2 = gmsh.model.geo.addPoint(0,l,0)
    p3 = gmsh.model.geo.addPoint(0,l,l)
    p4 = gmsh.model.geo.addPoint(0,0,l)
    p5 = gmsh.model.geo.addPoint(L,0,0)
    p6 = gmsh.model.geo.addPoint(L,l,0)
    p7 = gmsh.model.geo.addPoint(L,l,l)
    p8 = gmsh.model.geo.addPoint(L,0,l)
    

    l1 = gmsh.model.geo.addLine(p1,p2)
    l2 = gmsh.model.geo.addLine(p2,p3)
    l3 = gmsh.model.geo.addLine(p3,p4)
    l4 = gmsh.model.geo.addLine(p4,p1)
    l5 = gmsh.model.geo.addLine(p1,p5)
    l6 = gmsh.model.geo.addLine(p2,p6)
    l7 = gmsh.model.geo.addLine(p3,p7)
    l8 = gmsh.model.geo.addLine(p4,p8)
    l9 = gmsh.model.geo.addLine(p5,p6)
    l10 = gmsh.model.geo.addLine(p6,p7)
    l11 = gmsh.model.geo.addLine(p7,p8)
    l12 = gmsh.model.geo.addLine(p8,p5)



    c1 = gmsh.model.geo.addCurveLoop([-l4,-l3,-l2,-l1])
    c2 = gmsh.model.geo.addCurveLoop([l9,l10,l11,l12])
    c3 = gmsh.model.geo.addCurveLoop([l1,l6,-l9,-l5])
    c4 = gmsh.model.geo.addCurveLoop([l2,l7,-l10,-l6])
    c5 = gmsh.model.geo.addCurveLoop([l3,l8,-l11,-l7])
    c6 = gmsh.model.geo.addCurveLoop([l4,l5,-l12,-l8])
    # c1 = gmsh.model.geo.addCurveLoop([-l4,-l3,-l2,-l1])
    # c1 = gmsh.model.geo.addCurveLoop([-l4,-l3,-l2,-l1])

    s1 = gmsh.model.geo.addPlaneSurface([c1])   # Face esquerda
    s2 = gmsh.model.geo.addPlaneSurface([c2])   # Face direita
    s3 = gmsh.model.geo.addPlaneSurface([c3])   # Face traseira
    s4 = gmsh.model.geo.addPlaneSurface([c4])   # Face superior
    s5 = gmsh.model.geo.addPlaneSurface([c5])   # Face frontal
    s6 = gmsh.model.geo.addPlaneSurface([c6])   # Face inferior



    gmsh.model.geo.mesh.setTransfiniteCurve(l1, ne1+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l2, ne1+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l3, ne1+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l4, ne1+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l5, ne2+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l6, ne2+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l7, ne2+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l8, ne2+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l9, ne1+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l10, ne1+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l11, ne1+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l12, ne1+1)

    
    gmsh.model.geo.mesh.setTransfiniteSurface(s1)
    gmsh.model.geo.mesh.setTransfiniteSurface(s2)
    gmsh.model.geo.mesh.setTransfiniteSurface(s3)
    gmsh.model.geo.mesh.setTransfiniteSurface(s4)
    gmsh.model.geo.mesh.setTransfiniteSurface(s5)
    gmsh.model.geo.mesh.setTransfiniteSurface(s6)

    gmsh.model.geo.mesh.setRecombine(2, s1)
    gmsh.model.geo.mesh.setRecombine(2, s2)
    gmsh.model.geo.mesh.setRecombine(2, s3)
    gmsh.model.geo.mesh.setRecombine(2, s4)
    gmsh.model.geo.mesh.setRecombine(2, s5)
    gmsh.model.geo.mesh.setRecombine(2, s6)

    fixed = gmsh.model.addPhysicalGroup(2, [s1])
    gmsh.model.setPhysicalName(2, fixed, "u 0.0 u 0.0 u 0.0 1")
    free = gmsh.model.addPhysicalGroup(2, [s2, s3, s5, s6])
    gmsh.model.setPhysicalName(2, free, "t 0.0 t 0.0 t 0.0 1")
    forced = gmsh.model.addPhysicalGroup(2, [s4])
    gmsh.model.setPhysicalName(2, forced, "t 0.0 t -1.0 t 0.0 1")
   
    gmsh.model.geo.synchronize()

    # We finally generate and save the mesh:
    gmsh.model.mesh.generate(2)
    gmsh.model.mesh.setOrder(elementOrder)
    file_msh = "mesh.msh"
    gmsh.write(file_msh)

    file_vtk = "mesh.vtk"
    gmsh.write(file_vtk)

    # Launch the GUI to see the results:
    if popup is True:
        gmsh.fltk.run()

    gmsh.finalize()
    return file_msh
