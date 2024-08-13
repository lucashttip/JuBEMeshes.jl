module JuBEMeshes

# Write your package code here.
import Gmsh: gmsh
using Infiltrator

include("auxfunctions.jl")
include("bars.jl")
include("soils.jl")


export homog_bar, multi_bar, make_mesh_SSI_layer

end
