import gmsh
import sys
from header import write_metadata
from aux_functions import finalize_gmsh
from bars.vigaengastada import viga
 
 
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
    
    ne1 = 4
    ne2 = 24
    elementOrder = 2
    Le = 5
    lx = 1

     
    popup = False
    if '-popup' in sys.argv:
        popup = True
    file_msh = viga(ne1=ne1,ne2=ne2,L=Le,l=lx,elementOrder=elementOrder,popup=popup)
    # Create mesh:
     
    # file_msh = finalize_gmsh(popup)
    file_out = "viga_"+str(ne1)+"_"+str(ne2)
    if elementOrder == 2:
        file_out = file_out+"_quad"
    file_out = file_out+".msh"
    write_metadata(file_msh = file_msh, file_out=file_out, material_table = material_table, nGP = nGP, offset = offset, tipo = tipo)
 
 
if __name__ == '__main__':
    main()