module JuBEMeshes

# Write your package code here.
import Gmsh: gmsh


include("auxfunctions.jl")
include("bars.jl")
include("soils.jl")


export homog_bar, multi_bar

end
