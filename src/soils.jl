
function make_square(l=2.0, z1=0.0, z2=0.0, nf=10)

    points = [
        1   -l/2.0  -l/2.0  z1
        2   l/2.0   -l/2.0  z2
        3   l/2.0   l/2.0   z2
        4   -l/2.0  l/2.0   z1
    ]

    lines = [
        1 1 2
        2 2 3
        3 3 4
        4 4 1
    ]

    curves = [
        1 -4 -3 -2 -1
    ]
        
    surfaces = [1]
    
    ps, ls, cs,ss = create_points_curves_surfs(points,lines,curves,surfaces)

    make_lines_transfinite(ls, nf+1)

    set_squares(ss)

    return ss[1]
end

function make_soil_foundation_layer_traps(a=1.0, fl=2.0, fs=10.0, z=0.0, nf=18, ns=9, inverse=false)
    
    p1 = gmsh.model.geo.addPoint(-fl*a/2.0, -fl*a/2.0, z)
    p2 = gmsh.model.geo.addPoint(fl*a/2.0, -fl*a/2.0, z)
    p3 = gmsh.model.geo.addPoint(fl*a/2.0, fl*a/2.0, z)
    p4 = gmsh.model.geo.addPoint(-fl*a/2.0, fl*a/2.0, z)

    
    l1 = gmsh.model.geo.addLine(p1, p2)
    l2 = gmsh.model.geo.addLine(p2, p3)
    l3 = gmsh.model.geo.addLine(p3, p4)
    l4 = gmsh.model.geo.addLine(p4, p1)
    
    if !inverse
        c1 = gmsh.model.geo.addCurveLoop([l1, l2, l3, l4])
    else
        c1 = gmsh.model.geo.addCurveLoop([-l4, -l3, -l2, -l1])
    end
    
    s1 = gmsh.model.geo.addPlaneSurface([c1])
    
    p5 = gmsh.model.geo.addPoint(-fs*a/2.0, -fs*a/2.0, z)
    p6 = gmsh.model.geo.addPoint(fs*a/2.0, -fs*a/2.0, z)
    p7 = gmsh.model.geo.addPoint(fs*a/2.0, fs*a/2.0, z)
    p8 = gmsh.model.geo.addPoint(-fs*a/2.0, fs*a/2.0, z)
    
    l5 = gmsh.model.geo.addLine(p5, p6)
    l6 = gmsh.model.geo.addLine(p6, p7)
    l7 = gmsh.model.geo.addLine(p7, p8)
    l8 = gmsh.model.geo.addLine(p8, p5)
    
    l9 = gmsh.model.geo.addLine(p1, p5)
    l10 = gmsh.model.geo.addLine(p2, p6)
    l11 = gmsh.model.geo.addLine(p3, p7)
    l12 = gmsh.model.geo.addLine(p4, p8)
    
    if !inverse
        c2 = gmsh.model.geo.addCurveLoop([l5, -l10, -l1, l9])
        c3 = gmsh.model.geo.addCurveLoop([l6, -l11, -l2, l10])
        c4 = gmsh.model.geo.addCurveLoop([l7, -l12, -l3, l11])
        c5 = gmsh.model.geo.addCurveLoop([l8, -l9, -l4, l12])
    else
        c2 = gmsh.model.geo.addCurveLoop([-l9, l1, l10, -l5])
        c3 = gmsh.model.geo.addCurveLoop([-l10, l2, l11, -l6])
        c4 = gmsh.model.geo.addCurveLoop([-l11, l3, l12, -l7])
        c5 = gmsh.model.geo.addCurveLoop([-l12, l4, l9, -l8])
    end
    
    s2 = gmsh.model.geo.addPlaneSurface([c2])
    s3 = gmsh.model.geo.addPlaneSurface([c3])
    s4 = gmsh.model.geo.addPlaneSurface([c4])
    s5 = gmsh.model.geo.addPlaneSurface([c5])
    
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
    
    return s1, s2, s3, s4, s5
end

function make_mesh_soil_foundation(a=1.0, fl=2.0, fs=10.0, nf=18, ns=9, popup=false)
    gmsh.initialize()
    gmsh.model.add("SoilFoundation")
    
    s1, s2, s3, s4, s5 = make_soil_foundation_layer(a=a, fl=fl, fs=fs, nf=nf, ns=ns, z=0.0)
    
    pf = gmsh.model.addPhysicalGroup(2, [s1])
    gmsh.model.setPhysicalName(2, pf, "rb 0.0 rb 0.0 rb 0.0")
    ps = gmsh.model.addPhysicalGroup(2, [s2, s3, s4, s5])
    gmsh.model.setPhysicalName(2, ps, "t 0.0 t 0.0 t 0.0")
    
    gmsh.model.geo.synchronize()
    gmsh.model.mesh.generate(2)
    
    filename_msh = "mesh.msh"
    gmsh.write(filename_msh)
    
    filename_vtk = "mesh.vtk"
    gmsh.write(filename_vtk)
    
    if popup
        gmsh.fltk.run()
    end
    
    gmsh.finalize()
    
    return filename_msh
end
