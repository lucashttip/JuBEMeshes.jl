import gmsh


def make_lines_transfinite(lines, ne):
    for line in lines:
        gmsh.model.geo.mesh.setTransfiniteCurve(line, ne+1)

def set_squares(surfaces):
    for surface in surfaces:
        gmsh.model.geo.mesh.setTransfiniteSurface(surface)
    for surface in surfaces:
        gmsh.model.geo.mesh.setRecombine(2, surface)
        


def finalize_gmsh(popup):



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