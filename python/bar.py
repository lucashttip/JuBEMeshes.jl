import gmsh
import sys
from header import write_metadata
from aux_functions import finalize_gmsh
from bars.barraengastada import barra, barra2
 
 
def main():
    # Materiais:
    Ge = 5.0*10**3
    v = 0.0
    dam = 0.01
    rho = 1.0
    material_table = [[Ge, v, dam, rho]]
     
    # Frequencias do problema
    nFrs = [2]
    frs = [0.01, 5]
     
    # Dados de integração
    nGP = 8
     
    # Dados dos elementos
    offset = 0.5
    tipo = 1 # 0 para constantes, 1 para linear e 2 para quadrático
     
    # Geometria
    lx = 10
    ly = 1
    lz = 1
    ne1 = 4
    ne2 = 10*ne1
    file_out = "bar_4_40.msh"



    popup = False
    if '-popup' in sys.argv:
        popup = True
    file_msh = barra(ne1 = ne1,ne2 = ne2,lx =lx,ly =ly,lz = lz,elementOrder=1,popup=popup)
    # file_msh = barra2(ne1 = ne1,ne2 = ne1,lx1 =5, lx2 = 5, ly =1,lz = 1,elementOrder=1,popup=popup)
    # Create mesh:
     
    # file_msh = finalize_gmsh(popup)
    write_metadata(file_msh = file_msh,file_out=file_out, material_table = material_table, nGP = nGP, offset = offset, tipo = tipo)
 
 
if __name__ == '__main__':
    main()