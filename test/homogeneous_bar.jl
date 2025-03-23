using JuBEMeshes

args = (
    neyz = 1,           # numberOfElementsInYZ
    nex = 10,           # numberOfElementsInX
    lx = 10,            # lengthInX
    ly = 1,             # lengthInY
    lz = 1,             # lengthInZ
    elementOrder = 1,   # elementOrder
    popup = false,      # shouldPopup
)

homog_bar(;args...)