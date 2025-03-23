using JuBEMeshes

args = (
    neyz = 1,           # numberOfElementsInYZ,
    nex = 10,           # numberOfElementsForEachSectionInX,
    lx1 = 5,            # Length of first part in x
    lx2 = 5             # Length of second part in x
    ly = 1,             # lengthInY,
    lz = 1,             # lengthInZ,
    elementOrder = 1,   # elementOrder,
    popup = false,      # shouldPopup
)


multi_bar(;args...)