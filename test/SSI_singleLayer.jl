using JuBEMeshes

args = (
    a=1.0,              # size of parameter a in meters 
    fl=2.0,             # size of the side of the foundation * a
    fs=8.0,            # size of the side of the soil * a
    nf=4,               # Number of elements on foundation side
    h=8.0,              # Height of the soil layer * a
    popup=true,        # Should popup gmsh?
    nee = 4,            # Number of enclosing elements per side
    ns2 = 16,            # Number of enclosing elements on the bottom?
    elementOrder = 1,    # elementOrder
    growth = 2.0
)

make_mesh_SSI_singleLayer(;args...)
