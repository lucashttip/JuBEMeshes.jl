import gmsh

def make_square(l = 2.0, z1 = 0.0, z2 = 0.0, nf = 18, inverse = False):
    p1 = gmsh.model.geo.addPoint(-l/2.0, -l/2.0, z1)
    p2 = gmsh.model.geo.addPoint(l/2.0, -l/2.0, z2)
    p3 = gmsh.model.geo.addPoint(l/2.0, l/2.0, z2)
    p4 = gmsh.model.geo.addPoint(-l/2.0, l/2.0, z1)
    l1 = gmsh.model.geo.addLine(p1, p2)
    l2 = gmsh.model.geo.addLine(p2, p3)
    l3 = gmsh.model.geo.addLine(p3, p4)
    l4 = gmsh.model.geo.addLine(p4, p1)
    if inverse == True:
        c1 = gmsh.model.geo.addCurveLoop([-l4, -l3, -l2, -l1])
    else:
        c1 = gmsh.model.geo.addCurveLoop([l1, l2, l3, l4])
    s = gmsh.model.geo.addPlaneSurface([c1])

    # s = gmsh.model.geo.addPlaneSurface([c1,c2])

    gmsh.model.geo.mesh.setTransfiniteCurve(l1, nf+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l2, nf+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l3, nf+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l4, nf+1)
    
    gmsh.model.geo.mesh.setTransfiniteSurface(s)
    
    gmsh.model.geo.mesh.setRecombine(2, s)
    
    return s

def make_soil_foundation_layer(a=1.0,fl=2.0,fs=10.0, z = 0.0,nf=18,ns = 9, transf = False, inverse = False):


    df = (fl*a)/nf
    ds = (fs*a)/ns

    p1 = gmsh.model.geo.addPoint(-fl*a/2.0, -fl*a/2.0, z,df)
    p2 = gmsh.model.geo.addPoint(fl*a/2.0, -fl*a/2.0, z,df)
    p3 = gmsh.model.geo.addPoint(fl*a/2.0, fl*a/2.0, z,df)
    p4 = gmsh.model.geo.addPoint(-fl*a/2.0, fl*a/2.0, z,df)
    l1 = gmsh.model.geo.addLine(p1, p2)
    l2 = gmsh.model.geo.addLine(p2, p3)
    l3 = gmsh.model.geo.addLine(p3, p4)
    l4 = gmsh.model.geo.addLine(p4, p1)
    if inverse == False:
        c1 = gmsh.model.geo.addCurveLoop([l1, l2, l3, l4])
    else:
        c1 = gmsh.model.geo.addCurveLoop([-l4, -l3, -l2, -l1])
    s1 = gmsh.model.geo.addPlaneSurface([c1])

    # Defining soil geometry
    p5 = gmsh.model.geo.addPoint(-fs*a/2.0, -fs*a/2.0, z, ds)
    p6 = gmsh.model.geo.addPoint(fs*a/2.0, -fs*a/2.0, z,ds)
    p7 = gmsh.model.geo.addPoint(fs*a/2.0, fs*a/2.0, z,ds)
    p8 = gmsh.model.geo.addPoint(-fs*a/2.0, fs*a/2.0, z,ds)

    l5 = gmsh.model.geo.addLine(p5, p6)
    l6 = gmsh.model.geo.addLine(p6, p7)
    l7 = gmsh.model.geo.addLine(p7, p8)
    l8 = gmsh.model.geo.addLine(p8, p5)

    l9 = gmsh.model.geo.addLine(p1,p5)
    l10 = gmsh.model.geo.addLine(p2,p6)
    l11 = gmsh.model.geo.addLine(p3,p7)
    l12 = gmsh.model.geo.addLine(p4,p8)

    if inverse == False:
        c2 = gmsh.model.geo.addCurveLoop([l5, -l10, -l1, l9])
        c3 = gmsh.model.geo.addCurveLoop([l6, -l11, -l2, l10])
        c4 = gmsh.model.geo.addCurveLoop([l7, -l12, -l3, l11])
        c5 = gmsh.model.geo.addCurveLoop([l8, -l9, -l4, l12])
    else:
        c2 = gmsh.model.geo.addCurveLoop([-l9, l1, l10, -l5])
        c3 = gmsh.model.geo.addCurveLoop([-l10, l2, l11, -l6])
        c4 = gmsh.model.geo.addCurveLoop([-l11, l3, l12, -l7])
        c5 = gmsh.model.geo.addCurveLoop([-l12, l4, l9, -l8])
    

    s2 = gmsh.model.geo.addPlaneSurface([c2])
    s3 = gmsh.model.geo.addPlaneSurface([c3])
    s4 = gmsh.model.geo.addPlaneSurface([c4])
    s5 = gmsh.model.geo.addPlaneSurface([c5])


    # s = gmsh.model.geo.addPlaneSurface([c1,c2])

    if transf:

        gmsh.model.geo.mesh.setTransfiniteCurve(l1, nf+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l2, nf+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l3, nf+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l4, nf+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l5, nf+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l6, nf+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l7, nf+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l8, nf+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l9, ns+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l10, ns+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l11, ns+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l12, ns+1)



        gmsh.model.geo.mesh.setTransfiniteSurface(s1)
        gmsh.model.geo.mesh.setTransfiniteSurface(s2)
        gmsh.model.geo.mesh.setTransfiniteSurface(s3)
        gmsh.model.geo.mesh.setTransfiniteSurface(s4)
        gmsh.model.geo.mesh.setTransfiniteSurface(s5)


    gmsh.model.geo.mesh.setRecombine(2, s1)
    gmsh.model.geo.mesh.setRecombine(2, s2)
    gmsh.model.geo.mesh.setRecombine(2, s3)
    gmsh.model.geo.mesh.setRecombine(2, s4)
    gmsh.model.geo.mesh.setRecombine(2, s5)

    return s1,s2,s3,s4,s5

def make_mesh_soil_foundation(a=1.0, fl=2.0, fs=10.0, nf=18, ns = 9, popup=False,transf = False, inverse = True):
    gmsh.initialize()

    gmsh.model.add("SoilFoundation")

    # Defining foundation geometry

    s1,s2,s3,s4,s5 = make_soil_foundation_layer(a=a,fl=fl,fs=fs,nf=nf,ns = ns, z = 0.0, transf = transf, inverse = inverse)
    

    pf = gmsh.model.addPhysicalGroup(2, [s1])
    gmsh.model.setPhysicalName(2, pf, "rb 0.0 rb 0.0 rb 0.0 1")
    ps = gmsh.model.addPhysicalGroup(2, [s2, s3, s4, s5])
    gmsh.model.setPhysicalName(2, ps, "t 0.0  t 0.0 t 0.0 1")

    gmsh.model.geo.synchronize()
    gmsh.model.mesh.generate(2)

    # gmsh.option.setNumber("Mesh.SaveAll", 1)

    filename_msh = "mesh.msh"
    gmsh.write(filename_msh)

    filename_vtk = "mesh.vtk"
    gmsh.write(filename_vtk)


    if popup:
        gmsh.fltk.run()

    gmsh.finalize()

    return filename_msh
 