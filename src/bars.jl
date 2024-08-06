"""
    homog_bar(;ne1=4, ne2=8, lx=5, ly=1, lz=1, elementOrder=1, popup=true)

Generates the mesh of a bar that is divided in two.  

# Arguments
- `ne1::Integer`: number of elements on the y and z directions.
- `ne2::Integer`: number of elements on the x direction.
- `lx::Float`: length in the x direction.
- `ly::Float`: length in the y direction.
- `lz::Float`: length in the z direction.
- `elementOrder::Integer`: Order of the element (1 or 2).
- `popup::Boolean`: Whether gmsh should popup with the mesh plotted.
"""
function homog_bar(;ne1=4, ne2=8, lx=10, ly=1, lz=1, elementOrder=1, popup=true)
    gmsh.initialize()
    gmsh.model.add("barra")

    points = [
        1   0   0   0
        2   0   ly  0
        3   0   ly  lz
        4   0   0   lz
        5   lx  0   0
        6   lx  ly  0
        7   lx  ly  lz
        8   lx  0   lz]
    
    lines = [
        1   1   2
        2   2   3
        3   3   4
        4   4   1
        5   1   5
        6   2   6
        7   3   7
        8   4   8
        9   5   6
        10  6   7
        11  7   8
        12  8   5]


    curves = [
    1   -4  -3  -2  -1
    2   9   10  11  12
    3   1   6   -9  -5
    4   2   7   -10 -6
    5   3   8   -11 -7
    6   4   5   -12 -8]
    

    surfaces = [1,2,3,4,5,6]

    ps, ls, cs,ss = create_points_curves_surfs(points,lines,curves,surfaces)

    make_lines_transfinite(ls, ne1)
    make_lines_transfinite(ls[5:8], ne2)

    set_squares(ss)

    fixed = gmsh.model.addPhysicalGroup(2, [ss[1]])
    gmsh.model.setPhysicalName(2, fixed, "Face on x=0")
    free = gmsh.model.addPhysicalGroup(2, ss[3:6])
    gmsh.model.setPhysicalName(2, free, "Faces parallel to x")
    forced = gmsh.model.addPhysicalGroup(2, [ss[2]])
    gmsh.model.setPhysicalName(2, forced, "Face on x=1")

    gmsh.model.geo.synchronize()

    # Generate and save the mesh
    gmsh.model.mesh.generate(2)
    gmsh.model.mesh.setOrder(elementOrder)

    name = "homogbar_ne=$(ne1)x$(ne2)_l=$(lx)x$(ly)x$(lz)_eo=$(elementOrder)"

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




"""
    multi_bar(;ne1=4, ne2=8, lx1=5, lx2=5, ly=1, lz=1, elementOrder=1, popup=true)

Generates the mesh of a bar that is divided in two.  

# Arguments
- `ne1::Integer`: number of elements on the y and z directions.
- `ne2::Integer`: number of elements on the x direction.
- `lx1::Float`: length of the first part in the x direction.
- `lx2::Float`: length of the second part in the x direction.
- `ly::Float`: length in the y direction.
- `lz::Float`: length in the z direction.
- `elementOrder::Integer`: Order of the element (1 or 2).
- `popup::Boolean`: Whether gmsh should popup with the mesh plotted.
"""
function multi_bar(;ne1::Integer=4, ne2::Integer=8, lx1::Number=5, lx2::Number=5, ly::Number=1, lz::Number=1, elementOrder::Integer=1, popup::Bool=true)
    
    gmsh.initialize()
    gmsh.model.add("bar")

    lx = lx1 + lx2

    points = [
    1   0   0   0
    2   0   ly  0
    3   0   ly  lz
    4   0   0   lz
    5   lx1 0   0
    6   lx1 ly  0
    7   lx1 ly  lz
    8   lx1 0   lz
    9   lx  0   0
    10  lx  ly  0
    11  lx  ly  lz
    12  lx  0   lz]

    lines = [
        1   1   2
        2   2   3
        3   3   4
        4   4   1
        5   1   5
        6   2   6
        7   3   7
        8   4   8
        9   5   6
        10  6   7
        11  7   8
        12  8   5
        13  5   9
        14  6   10
        15  7   11
        16  8   12
        17  9   10
        18  10  11
        19  11  12
        20  12  9
        ]
        
        
    curves = [
    1   -4  -3  -2  -1
    2   9   10  11  12
    3   1   6   -9  -5
    4   2   7   -10 -6
    5   3   8   -11 -7
    6   4   5   -12 -8   
    7   17  18  19  20
    8   9   14  -17 -13
    9   10  15  -18 -14
    10  11  16  -19 -15
    11  12  13  -20 -16
    ]

    surfaces = 1:11

    ps, ls, cs,ss = create_points_curves_surfs(points,lines,curves,surfaces)

    make_lines_transfinite(ls, ne1)
    make_lines_transfinite(ls[[5:8;13:16]], ne2)

    set_squares(ss)

    fixed = gmsh.model.addPhysicalGroup(2, [ss[1]])
    gmsh.model.setPhysicalName(2, fixed, "Face on x=0")
    freea = gmsh.model.addPhysicalGroup(2, ss[3:6])
    gmsh.model.setPhysicalName(2, freea, "Faces parallel to x. Bar 1")
    freeb = gmsh.model.addPhysicalGroup(2, ss[8:11])
    gmsh.model.setPhysicalName(2, freeb, "Faces parallel to x. Bar 2")
    forced = gmsh.model.addPhysicalGroup(2, [ss[7]])
    gmsh.model.setPhysicalName(2, forced, "Face on x = dx")
    interfacea = gmsh.model.addPhysicalGroup(2, [ss[2]])
    gmsh.model.setPhysicalName(2, interfacea, "Interface - bar 1 (normal ok)")
    interfaceb = gmsh.model.addPhysicalGroup(2, [ss[2]])
    gmsh.model.setPhysicalName(2, interfaceb, "Interface - bar 2 (invert normal)")

    gmsh.model.geo.synchronize()

    # Generate and save the mesh
    gmsh.model.mesh.generate(2)
    gmsh.model.mesh.setOrder(elementOrder)
   
   
    name = "multibar_ne=$(ne1)x($(ne2)+$(ne2))_l=($(lx1)+$(lx2))x$(ly)x$(lz)_eo=$(elementOrder)"

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