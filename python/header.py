from numpy import empty


def write_materialblock(fid, material_table):
    fid.write("$Material\n")
    fid.write("{}\n".format(len(material_table)))
    for material in material_table:
        Ge = material[0]
        v = material[1]
        dam = material[2]
        rho = material[3]
        fid.write("{:E} {} {} {}\n".format(Ge, v, dam, rho))
    fid.write("$EndMaterial\n")



def write_frequenciesblock(fid,nFrs, frs):
    fid.write("$Frequencies\n")
    fid.write("{}\n".format(len(nFrs)))
    for i in range(len(nFrs)):
        fid.write("{} {} {}\n".format(frs[i], frs[i+1], nFrs[i]))
    fid.write("$EndFrequencies\n")
    
def write_meshtypeblock(fid, nGP, offset, tipo):
    fid.write("$MeshType\n")
    fid.write("{}\n".format(nGP))
    fid.write("{}\n".format(offset))
    fid.write("{}\n".format(tipo))
    fid.write("$EndMeshType\n")
    
def write_forcesblock(fid,f):
    fid.write("$Forces\n")
    fid.write("1\n")
    fid.write("{:E} {:E} {:E} {:E} {:E} {:E}\n".format(f[0],f[1],f[2],f[3],f[4],f[5]))
    fid.write("$EndForces\n")


def write_metadata(file_msh, file_out, material_table=[], f=[], nFrs=[], frs=[], nGP=4, offset=0, tipo=0):
    fid = open(file_msh, 'r')
    buffer = fid.read()
    fid.close()

    fid = open(file_out,'w')

    if material_table:
        write_materialblock(fid, material_table)

    if frs and nFrs:
        write_frequenciesblock(fid,nFrs, frs)

    write_meshtypeblock(fid, nGP, offset, tipo)

    if f:
        write_forcesblock(fid,f)
    
    fid.write(buffer)

    fid.close()

    