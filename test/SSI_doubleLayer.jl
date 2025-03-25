using JuBEMeshes

args = (
    a=1.0,              # size of parameter a in meters 
    fl=2.0,             # size of the side of the foundation * a
    fs=8.0,            # size of the side of the soil * a
    nf=4,               # Number of elements on foundation side
    h=8.0,              # Height of the soil layer * a
    popup=false,        # Should popup gmsh?
    nee = 4,            # Number of enclosing elements per side
    elementOrder = 1    # elementOrder
)

make_mesh_SSI_layer(;args...)
