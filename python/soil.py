import gmsh
import sys
import os
from soils.homog_mesh import *
from soils.non_homog_mesh import *
from soils.freesoil_EE import *
from header import write_metadata
from aux_functions import finalize_gmsh


def main():
    # Materiais:
    Ge = 1.0
    v = 0.3
    dam = 0.01
    rho = 1.0
    material_table = [[Ge, v, dam, rho]]

    # Frequencias do problema
    nFrs = [150]
    frs = [0.01, 5]
    # nFrs = []
    # frs = []

    # Dados de integração
    nGP = 8

    # Dados dos elementos
    offset = 0.4
    tipo = 1 # 0 para constantes, 1 para linear e 2 para quadrático

    # Condições de contorno
    fx = 0.0
    fy = 0.0
    fz = 1.0
    mx = 0.0
    my = 0.0
    mz = 0.0

    f = [fx, fy, fz, mx, my, mz]
    # f = []

    # Dados para malha
    fe = 2
    a = 1.0
    fl = 2.0
    fs = 10.0
    nf = 10
    ns = 7
    nf1 = 6
    nf2 = 4
    z = 5.0*a
    z1 = 5.0*a
    z2 = 5.0*a
    nel = 30


    # Parâmetros para malha não homogenea
    f1 = 1.0
    f2 = 1.0

    # Parametros de EE
    nee = 2
    nes = 2
    nexy = nee
    nez = nee
    dxy = 2
    dz = 5

    elementOrder = 1

    popup = False
    if '-popup' in sys.argv:
        popup = True

    # Create mesh:
    # file_msh = make_mesh_soil_foundation(a=a, fl=fl, fs=fs, nf=nf,ns = ns, popup=False)
    # file_msh = make_mesh_soil_foundation_nonhomog(a=a, fl=fl, fs=fs, nf=nf, f1 = f1, f2 = f2, ns = ns, inverse = True, popup=popup)

    # file_msh = make_mesh_soil_free_EE_nonhomog_equal(a=a, fs=fs, nel = nel,nexy = nexy,nez = nez, nes = nes,dxy=dxy, dz = dz,elementOrder = elementOrder, inverse = True, popup=popup)
    # file_msh = make_mesh_soil_free_EE_nonhomog(a=a, fl=fl, fs=fs, nf=nf, ns = ns, f1 = f1, f2 = f2,nexy = nexy,nez = nez, nes = nes,dxy = dxy, dz = dz,elementOrder = elementOrder, inverse = True, popup=popup)
    # file_msh = make_mesh_soil_free_EE_homog(a=a, fl=fl, fs=fs, nf=nf,ns = ns,nexy = nexy,nez = nez, nes = nes,dxy=dxy, dz = dz,elementOrder = elementOrder, inverse = True, popup=popup)
    # file_msh = make_mesh_soil_free_EE_homog2(a=a, fl=fl, fs=fs,f1 = f1,f2=f2, nf=nf,ns = ns,nexy = nexy,nez = nez, nes = nes,dxy=dxy, dz = dz,elementOrder = elementOrder, inverse = True, popup=popup)


    # file_msh = make_mesh_soil_foundation_rock_nonhomog2(a=a, fl=fl, fs=fs, nf1=nf1, nf2 = nf2,f1 = f1, f2 = f2, ns = ns, z1 = z1, z2 = z2,inverse = True, popup=popup)

    file_msh = make_mesh_soil_foundation_rock(a=a, fl=fl, fs=fs, nf1=nf1, nf2 = nf2, z = z,inverse = True, popup=popup)


    folder = "data"
    # file_out = "soil_rb_" + str(nf) + "_" + str(ns) + "_fs_" + str(int(fs)) + "_homog"
    file_out = "soil_rb_" + str(nel) + "_" + str(4*nes*nexy + 4*nez*nexy + nexy*nexy) + "EE"

    file_vtk = "mesh.vtk"
    file_out_msh = os.path.join(folder, file_out + ".msh")
    file_out_vtk = os.path.join(folder, file_out + ".vtk")
    os.rename(file_vtk,file_out_vtk)
    write_metadata(file_msh, file_out_msh,material_table, f, nFrs, frs, nGP, offset, tipo)

    

if __name__ == "__main__":
    main()
    