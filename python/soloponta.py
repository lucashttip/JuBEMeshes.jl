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
    Ge = 10.0
    v = 0.3
    dam = 0.01
    rho = 1.0
    material_table = [[Ge, v, dam, rho]]

    # Frequencias do problema
    nFrs = [10]
    frs = [0.01, 10]
    # nFrs = []
    # frs = []

    # Dados de integração
    nGP = 8

    # Dados dos elementos
    offset = 0.0
    tipo = 0 # 0 para constantes, 1 para linear e 2 para quadrático

    # Condições de contorno
    fx = 1.0
    fy = 0.0
    fz = 1.0
    mx = 0.0
    my = 0.0
    mz = 0.0

    f = [fx, fy, fz, mx, my, mz]
    # f = []

    # Dados para malha
    a = 1.0
    fl = 2.0
    fs = 15.0
    nf = 10
    ns = 15


    # Parâmetros para malha não homogenea
    f1 = 3.0
    f2 = 1.7

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

    file_msh = make_mesh_soil_free_EE_homog2(a=a, fl=fl, fs=fs,f1 = f1,f2=f2, nf=nf,ns = ns,nexy = nexy,nez = nez, nes = nes,dxy=dxy, dz = dz,elementOrder = elementOrder, inverse = True, popup=popup)




    folder = "data"
    file_out = "soil_rb_" + str(int(fs)) + "_" + str(nf) + "nf_" + str(ns) + "ns_ponta"


    file_vtk = "mesh.vtk"
    file_out_msh = os.path.join(folder, file_out + ".msh")
    file_out_vtk = os.path.join(folder, file_out + ".vtk")
    os.rename(file_vtk,file_out_vtk)
    write_metadata(file_msh, file_out_msh,material_table, f, nFrs, frs, nGP, offset, tipo)

    

if __name__ == "__main__":
    main()
    