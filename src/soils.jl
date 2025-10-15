
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

function make_mesh_SSI_layer(filename="";a=1.0,fl=2.0,fs=10.0,nf=4,h=5.0,popup=false,nee = 2,elementOrder = 1)

    gmsh.initialize()
    gmsh.model.add("soil")

    lf = fl*a
    ls = fs*a

    ne1 = nf
    ne2 = Int(((ls-lf)/2)/(lf/nf))
    ne3 = Int(ls/(lf/nf))


    points = [
        1   -lf/2   -lf/2   0   # Fundação
        2   lf/2    -lf/2   0   # Fundação 
        3   lf/2    lf/2    0   # Fundação
        4   -lf/2   lf/2    0   # Fundação
        5   -ls/2   -ls/2   0   # Camada 1
        6   -lf/2   -ls/2   0   # Camada 1
        7   lf/2    -ls/2   0   # Camada 1
        8   ls/2    -ls/2   0   # Camada 1
        9   ls/2    -lf/2   0   # Camada 1
        10  ls/2    lf/2    0   # Camada 1
        11  ls/2    ls/2    0   # Camada 1
        12  lf/2    ls/2    0   # Camada 1
        13  -lf/2   ls/2    0   # Camada 1
        14  -ls/2   ls/2    0   # Camada 1
        15  -ls/2   lf/2    0   # Camada 1
        16  -ls/2   -lf/2   0   # Camada 1
        17  -ls/2   -ls/2   h   # Camada 2
        18  ls/2    -ls/2   h   # Camada 2
        19  ls/2    ls/2    h   # Camada 2
        20  -ls/2   ls/2    h   # Camada 2
        21  -ls/2   -ls/2   2h   # Camada 2
        22  ls/2    -ls/2   2h   # Camada 2
        23  ls/2    ls/2    2h   # Camada 2
        24  -ls/2   ls/2    2h   # Camada 2
    ]

    lines = [
        1   1   2   # Foundation (nf)
        2   2   3   # Foundation (nf)
        3   3   4   # Foundation (nf)
        4   4   1   # Foundation (nf)
        5   5   6   # Soil-big (ne2)
        6   6   7   # Soil-small (nf)
        7   7   8   # Soil-big (ne2)
        8   8   9   # Soil-big (ne2)
        9   9   10  # Soil-small (nf)
        10  10  11  # Soil-big (ne2)
        11  11  12  # Soil-big (ne2)
        12  12  13  # Soil-small (nf)
        13  13  14  # Soil-big (ne2)
        14  14  15  # Soil-big (ne2)
        15  15  16  # Soil-small (nf)
        16  16  5   # Soil-big (ne2)
        17  6   1   # Soil-big (ne2)
        18  7   2   # Soil-big (ne2)
        19  9   2   # Soil-big (ne2)
        20  10  3   # Soil-big (ne2)
        21  12  3   # Soil-big (ne2)
        22  13  4   # Soil-big (ne2)
        23  15  4   # Soil-big (ne2)
        24  16  1   # Soil-big (ne2)
        25  5   17  # Soil-EE (nee) camada 1
        26  8   18  # Soil-EE (nee) camada 1
        27  11  19  # Soil-EE (nee) camada 1
        28  14  20  # Soil-EE (nee) camada 1
        29  17  18  # Soil-Layer2 (ne3)
        30  18  19  # Soil-Layer2 (ne3)
        31  19  20  # Soil-Layer2 (ne3)
        32  20  17  # Soil-Layer2 (ne3)
        33  5   8   # Soil-EE (nee) camada 1
        34  8   11  # Soil-EE (nee) camada 1
        35  11  14  # Soil-EE (nee) camada 1
        36  14  5   # Soil-EE (nee) camada 1
        37  17  18  # Soil-EE (nee) camada 1
        38  18  19  # Soil-EE (nee) camada 1
        39  19  20  # Soil-EE (nee) camada 1
        40  20  17  # Soil-EE (nee) camada 1
        41  17  21 # Soil-EE (nee) camada 2
        42  18  22 # Soil-EE (nee) camada 2
        43  19  23 # Soil-EE (nee) camada 2
        44  20  24 # Soil-EE (nee) camada 2
        45  21  22 # Soil-EE (nee) camada 2
        46  22  23 # Soil-EE (nee) camada 2
        47  23  24 # Soil-EE (nee) camada 2
        48  24  21 # Soil-EE (nee) camada 2
    ]

    curves = [
        1   1   2   3   4       # Foundation
        2   5   17  -24 16      # Soil Layer 1
        3   6   18  -1  -17     # Soil Layer 1
        4   7   8   19  -18     # Soil Layer 1
        5   9   20  -2  -19     # Soil Layer 1
        6   10  11  21  -20     # Soil Layer 1
        7   12  22  -3  -21     # Soil Layer 1
        8   13  14  23  -22     # Soil Layer 1
        9   15  24  -4  -23     # Soil Layer 1
        10  33  26  -37 -25     # Side EE (camada 1)
        11  34  27  -38 -26     # Side EE (camada 1)
        12  35  28  -39 -27     # Side EE (camada 1)
        13  36  25  -40 -28     # Side EE (camada 1)
        14  29  30  31  32      # Soil Layer 2
        15  37  42  -45 -41     # Side EE (camada 2)
        16  38  43  -46 -42     # Side EE (camada 2)
        17  39  44  -47 -43     # Side EE (camada 2)
        18  40  41  -48 -44     # Side EE (camada 2)
        19  45  46  47  48      # Side EE (camada 2)
    ]

    surfaces = [-1 .* collect(1:9);collect(10:19)]

    ps, ls, cs, ss = create_points_curves_surfs(points,lines,curves,surfaces)

    make_lines_transfinite(ls[[1:4...,6,9,12,15]], nf)
    make_lines_transfinite(ls[[5,7,8,10,11,13,14,16:24...]], ne2)
    make_lines_transfinite(ls[[25:28...,33:48...]], nee)
    make_lines_transfinite(ls[29:32], ne3)

    set_squares(ss)

    foundation = gmsh.model.addPhysicalGroup(2, [ss[1]])
    gmsh.model.setPhysicalName(2, foundation, "Foundation")
    freea = gmsh.model.addPhysicalGroup(2, ss[2:9])
    gmsh.model.setPhysicalName(2, freea, "Free Soil Layer 1")
    EE = gmsh.model.addPhysicalGroup(2, ss[10:13])
    gmsh.model.setPhysicalName(2, EE, "Enclosing Elements - Layer 1")
    interface1 = gmsh.model.addPhysicalGroup(2, [ss[14]])
    gmsh.model.setPhysicalName(2, interface1, "Interface - Layer 1 (normal ok)")
    interface2 = gmsh.model.addPhysicalGroup(2, [ss[14]])
    gmsh.model.setPhysicalName(2, interface2, "Interface - Layer 2 (invert normal)")
    EE2 = gmsh.model.addPhysicalGroup(2, ss[15:19])
    gmsh.model.setPhysicalName(2, EE2, "Enclosing Elements - Layer 2")

    gmsh.model.geo.synchronize()

    # Generate and save the mesh
    gmsh.model.mesh.generate(2)
    gmsh.model.mesh.setOrder(elementOrder)


    
    if filename != ""
        name = filename
    else
        name = "SoilLayers_a=$(a)_fl=$(fl)_fs=$(fs)_h=$(h),nf=$(nf)_eo=$(elementOrder)"
    end

    file_msh = string(name,".msh")
    gmsh.write(file_msh)

    file_vtk = string(name,".vtk")
    gmsh.write(file_vtk)


    # Launch the GUI to see the results
    if popup
        gmsh.fltk.run()
    end

    gmsh.finalize()
    return file_msh

end

function make_mesh_SSI_singleLayer(filename="";a=1.0,fl=2.0,fs=10.0,nf=4,h=5.0,popup=false,nee = 2,ns2 = 2,elementOrder = 1)
    gmsh.initialize()
    gmsh.model.add("soil")

    lf = fl*a
    ls = fs*a

    ne2 = Int(((ls-lf)/2)/(lf/nf))
    # ne3 = Int(ls/(lf/nf))


    points = [
        1   -lf/2   -lf/2   0   # Fundação
        2   lf/2    -lf/2   0   # Fundação 
        3   lf/2    lf/2    0   # Fundação
        4   -lf/2   lf/2    0   # Fundação
        5   -ls/2   -ls/2   0   # Camada 1
        6   -lf/2   -ls/2   0   # Camada 1
        7   lf/2    -ls/2   0   # Camada 1
        8   ls/2    -ls/2   0   # Camada 1
        9   ls/2    -lf/2   0   # Camada 1
        10  ls/2    lf/2    0   # Camada 1
        11  ls/2    ls/2    0   # Camada 1
        12  lf/2    ls/2    0   # Camada 1
        13  -lf/2   ls/2    0   # Camada 1
        14  -ls/2   ls/2    0   # Camada 1
        15  -ls/2   lf/2    0   # Camada 1
        16  -ls/2   -lf/2   0   # Camada 1
        17  -ls/2   -ls/2   h   # Camada 2
        18  ls/2    -ls/2   h   # Camada 2
        19  ls/2    ls/2    h   # Camada 2
        20  -ls/2   ls/2    h   # Camada 2
    ]

    lines = [
        1   1   2   # Foundation (nf)
        2   2   3   # Foundation (nf)
        3   3   4   # Foundation (nf)
        4   4   1   # Foundation (nf)
        5   5   6   # Soil-big (ne2)
        6   6   7   # Soil-small (nf)
        7   7   8   # Soil-big (ne2)
        8   8   9   # Soil-big (ne2)
        9   9   10  # Soil-small (nf)
        10  10  11  # Soil-big (ne2)
        11  11  12  # Soil-big (ne2)
        12  12  13  # Soil-small (nf)
        13  13  14  # Soil-big (ne2)
        14  14  15  # Soil-big (ne2)
        15  15  16  # Soil-small (nf)
        16  16  5   # Soil-big (ne2)
        17  6   1   # Soil-big (ne2)
        18  7   2   # Soil-big (ne2)
        19  9   2   # Soil-big (ne2)
        20  10  3   # Soil-big (ne2)
        21  12  3   # Soil-big (ne2)
        22  13  4   # Soil-big (ne2)
        23  15  4   # Soil-big (ne2)
        24  16  1   # Soil-big (ne2)
        25  5   17  # Soil-EE (nee) camada 1
        26  8   18  # Soil-EE (nee) camada 1
        27  11  19  # Soil-EE (nee) camada 1
        28  14  20  # Soil-EE (nee) camada 1
        29  17  18  # Soil-Layer2 (ne3)
        30  18  19  # Soil-Layer2 (ne3)
        31  19  20  # Soil-Layer2 (ne3)
        32  20  17  # Soil-Layer2 (ne3)
        33  5   8   # Soil-EE (nee) camada 1
        34  8   11  # Soil-EE (nee) camada 1
        35  11  14  # Soil-EE (nee) camada 1
        36  14  5   # Soil-EE (nee) camada 1
        37  17  18  # Soil-EE (nee) camada 1
        38  18  19  # Soil-EE (nee) camada 1
        39  19  20  # Soil-EE (nee) camada 1
        40  20  17  # Soil-EE (nee) camada 1
    ]

    curves = [
        1   1   2   3   4       # Foundation
        2   5   17  -24 16      # Soil Layer 1
        3   6   18  -1  -17     # Soil Layer 1
        4   7   8   19  -18     # Soil Layer 1
        5   9   20  -2  -19     # Soil Layer 1
        6   10  11  21  -20     # Soil Layer 1
        7   12  22  -3  -21     # Soil Layer 1
        8   13  14  23  -22     # Soil Layer 1
        9   15  24  -4  -23     # Soil Layer 1
        10  33  26  -37 -25     # Side EE (camada 1)
        11  34  27  -38 -26     # Side EE (camada 1)
        12  35  28  -39 -27     # Side EE (camada 1)
        13  36  25  -40 -28     # Side EE (camada 1)
        14  29  30  31  32      # Soil Layer 2
    ]

    surfaces = [-1 .* collect(1:9);collect(10:14)]

    ps, ls, cs, ss = create_points_curves_surfs(points,lines,curves,surfaces)

    make_lines_transfinite(ls[[1:4...,6,9,12,15]], nf)
    make_lines_transfinite(ls[[5,7,8,10,11,13,14,16:24...]], ne2)
    make_lines_transfinite(ls[[25:28...,33:40...]], nee)
    make_lines_transfinite(ls[29:32], ns2)

    set_squares(ss)

    foundation = gmsh.model.addPhysicalGroup(2, [ss[1]])
    gmsh.model.setPhysicalName(2, foundation, "Foundation")
    freea = gmsh.model.addPhysicalGroup(2, ss[2:9])
    gmsh.model.setPhysicalName(2, freea, "Free Soil Layer 1")
    EE = gmsh.model.addPhysicalGroup(2, ss[10:13])
    gmsh.model.setPhysicalName(2, EE, "Enclosing Elements - Layer 1")
    Bottom = gmsh.model.addPhysicalGroup(2, [ss[14]])
    gmsh.model.setPhysicalName(2, Bottom, "Bottom")
    # interface2 = gmsh.model.addPhysicalGroup(2, [ss[14]])

    gmsh.model.geo.synchronize()

    # Generate and save the mesh
    gmsh.model.mesh.generate(2)
    gmsh.model.mesh.setOrder(elementOrder)


    
    if filename != ""
        name = filename
    else
        name = "SoilSingleLayer_a=$(a)_fl=$(fl)_fs=$(fs)_h=$(h),nf=$(nf),ne2=$(ne2)_eo=$(elementOrder)"
    end

    file_msh = string(name,".msh")
    gmsh.write(file_msh)

    file_vtk = string(name,".vtk")
    gmsh.write(file_vtk)


    # Launch the GUI to see the results
    if popup
        gmsh.fltk.run()
    end

    gmsh.finalize()
    return file_msh
end