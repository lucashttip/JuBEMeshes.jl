
function make_lines_transfinite(lines, ne)
    for line in lines
        gmsh.model.geo.mesh.setTransfiniteCurve(line, ne+1)
    end
end

function set_squares(surfaces)
    for surface in surfaces
        gmsh.model.geo.mesh.setTransfiniteSurface(surface)
    end
    for surface in surfaces
        gmsh.model.geo.mesh.setRecombine(2, surface)
    end
end

function finalize_gmsh(popup)
    gmsh.model.geo.synchronize()
    gmsh.model.mesh.generate(2)

    # gmsh.option.setNumber("Mesh.SaveAll", 1)

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

function create_points_curves_surfs(points,lines,curves,surfaces)
    ps = []
    ls = []
    cs = []
    ss = []
    for i in axes(points,1)
        push!(ps,gmsh.model.geo.addPoint(points[i,2],points[i,3],points[i,4]))
    end

    for i in axes(lines,1)
        push!(ls,gmsh.model.geo.addLine(ps[lines[i,2]],ps[lines[i,3]]))
    end

    for i in axes(curves,1)
        orientation = sign.(curves[i,:])
        idxs = Int.(abs.(curves[i,:]))
        push!(cs,gmsh.model.geo.addCurveLoop([orientation[2]*ls[idxs[2]], orientation[3]*ls[idxs[3]], orientation[4]*ls[idxs[4]], orientation[5]*ls[idxs[5]]]))
    end

    for i in axes(surfaces,1)
        push!(ss,gmsh.model.geo.addPlaneSurface([cs[surfaces[i]]]))
    end

    return ps, ls, cs,ss

end

function create_lines(points,lines)
    ps = []
    ls = []
    np = size(points,1)
    nl = size(lines,1)
    for i in 1:np
        push!(ps,gmsh.model.geo.addPoint(points[i,1],points[i,2],points[i,3]))
    end

    for i in 1:nl
        push!(ls,gmsh.model.geo.addLine(lines[i,1],lines[i,2]))
    end

    return ps, ls

end


function create_points(points,lines)
    ps = []
    ls = []
    np = size(points,1)
    nl = size(lines,1)
    for i in 1:np
        push!(ps,gmsh.model.geo.addPoint(points[i,1],points[i,2],points[i,3]))
    end

    for i in 1:nl
        push!(ls,gmsh.model.geo.addLine(lines[i,1],lines[i,2]))
    end

    return ps, ls

end