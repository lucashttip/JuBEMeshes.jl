using Revise
using JuBEMeshes

homog_bar(ne1 = 1, ne2 = 10,lx=10,popup=true)

multi_bar(ne1 = 1, ne2 = 10,lx1 = 5, lx2 = 5,popup=true)

multi_bar(ne1 = 1, ne2 = 2,lx1 = 5, lx2 = 5,popup=true)

make_mesh_SSI_layer(a=1.0,fl=2.0,fs=8.0,nf=4,h=6;popup=true,nee = 4)

make_mesh_SSI_singleLayer(a=1.0,fl=2.0,fs=8.0,nf=4,ns2 = 16,h=4;popup=true,nee = 4)
