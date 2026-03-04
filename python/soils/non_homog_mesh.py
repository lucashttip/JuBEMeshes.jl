import gmsh
from soils.homog_mesh import make_square

def make_soil_foundation_layer_nonhomog(a=1.0,fl=2.0,fs=10.0, z = 0.0,nf=18, f1 = 8.0, f2 = 1.5, ns = 9, inverse = False):
    p1 = gmsh.model.geo.addPoint(-fl*a/2.0, -fl*a/2.0, z)
    p2 = gmsh.model.geo.addPoint(fl*a/2.0, -fl*a/2.0, z)
    p3 = gmsh.model.geo.addPoint(fl*a/2.0, fl*a/2.0, z)
    p4 = gmsh.model.geo.addPoint(-fl*a/2.0, fl*a/2.0, z)
    l1 = gmsh.model.geo.addLine(p1, p2)
    l2 = gmsh.model.geo.addLine(p2, p3)
    l3 = gmsh.model.geo.addLine(p3, p4)
    l4 = gmsh.model.geo.addLine(p4, p1)
    if inverse == False:
        c1 = gmsh.model.geo.addCurveLoop([l1, l2, l3, l4])
    else:
        c1 = gmsh.model.geo.addCurveLoop([-l4,-l3,-l2,-l1])
    s1 = gmsh.model.geo.addPlaneSurface([c1])

    # Defining soil geometry
    p5 = gmsh.model.geo.addPoint(-fs*a/2.0, -fs*a/2.0, z)
    p6 = gmsh.model.geo.addPoint(fs*a/2.0, -fs*a/2.0, z)
    p7 = gmsh.model.geo.addPoint(fs*a/2.0, fs*a/2.0, z)
    p8 = gmsh.model.geo.addPoint(-fs*a/2.0, fs*a/2.0, z)

    # Baixo
    p9 = gmsh.model.geo.addPoint(-fl*a/2.0, -fs*a/2.0, z)
    p10 = gmsh.model.geo.addPoint(fl*a/2.0, -fs*a/2.0, z)

    # Direita
    p11 = gmsh.model.geo.addPoint(fs*a/2.0, -fl*a/2.0, z)
    p12 = gmsh.model.geo.addPoint(fs*a/2.0, fl*a/2.0, z)

    # Cima
    p13 = gmsh.model.geo.addPoint(fl*a/2.0, fs*a/2.0, z)
    p14 = gmsh.model.geo.addPoint(-fl*a/2.0, fs*a/2.0, z)

    # Esquerda
    p15 = gmsh.model.geo.addPoint(-fs*a/2.0, fl*a/2.0, z)
    p16 = gmsh.model.geo.addPoint(-fs*a/2.0, -fl*a/2.0, z)  


    # Esquerda-baixo
    l5 = gmsh.model.geo.addLine(p5,p9)
    l6 = gmsh.model.geo.addLine(p9,p1)
    l7 = gmsh.model.geo.addLine(p1,p16)
    l8 = gmsh.model.geo.addLine(p16,p5)

    # Meio-Baixo
    l9 = gmsh.model.geo.addLine(p9,p10)
    l10 = gmsh.model.geo.addLine(p10,p2)

    # Direita-baixo
    l11 = gmsh.model.geo.addLine(p10,p6)
    l12 = gmsh.model.geo.addLine(p6,p11)
    l13 = gmsh.model.geo.addLine(p11,p2)

    # Direta-meio
    l14 = gmsh.model.geo.addLine(p11,p12)
    l15 = gmsh.model.geo.addLine(p12,p3)

    # Direita-Cima
    l16 = gmsh.model.geo.addLine(p12,p7)
    l17 = gmsh.model.geo.addLine(p7,p13)
    l18 = gmsh.model.geo.addLine(p13,p3)

    # Meio-cima
    l19 = gmsh.model.geo.addLine(p13,p14)
    l20 = gmsh.model.geo.addLine(p14,p4)

    # Esquerda-Cima
    l21 = gmsh.model.geo.addLine(p14,p8)
    l22 = gmsh.model.geo.addLine(p8,p15)
    l23 = gmsh.model.geo.addLine(p15,p4)

    # Esquerda-meio
    l24 = gmsh.model.geo.addLine(p15,p16)

    if inverse == False:
        # Esquerda-baixo
        c2 = gmsh.model.geo.addCurveLoop([l5,l6,l7,l8])
        # Meio-baixo
        c3 = gmsh.model.geo.addCurveLoop([l9,l10,-l1,-l6])
        # Direita-baixo
        c4 = gmsh.model.geo.addCurveLoop([l11,l12,l13,-l10])
        # Direita-meio
        c5 = gmsh.model.geo.addCurveLoop([l14,l15,-l2,-l13])
        # Direita-cima
        c6 = gmsh.model.geo.addCurveLoop([l16,l17,l18,-l15])
        # Meio-cima
        c7 = gmsh.model.geo.addCurveLoop([l19,l20,-l3,-l18])
        # Esquerda-cima
        c8 = gmsh.model.geo.addCurveLoop([l21,l22,l23,-l20])
        # Esquerda-cima
        c9 = gmsh.model.geo.addCurveLoop([l24,-l7,-l4,-l23])
    else:
        c2 = gmsh.model.geo.addCurveLoop([-l8,-l7,-l6,-l5])
        # Meio-baixo
        c3 = gmsh.model.geo.addCurveLoop([l6,l1,-l10,-l9])
        # Direita-baixo
        c4 = gmsh.model.geo.addCurveLoop([l10,-l13,-l12,-l11])
        # Direita-meio
        c5 = gmsh.model.geo.addCurveLoop([l13,l2,-l15,-l14])
        # Direita-cima
        c6 = gmsh.model.geo.addCurveLoop([l15,-l18,-l17,-l16])
        # Meio-cima
        c7 = gmsh.model.geo.addCurveLoop([l18,l3,-l20,-l19])
        # Esquerda-cima
        c8 = gmsh.model.geo.addCurveLoop([l20,-l23,-l22,-l21])
        # Esquerda-cima
        c9 = gmsh.model.geo.addCurveLoop([l23,l4,l7,-l24])
    
    

    s2 = gmsh.model.geo.addPlaneSurface([c2])
    s3 = gmsh.model.geo.addPlaneSurface([c3])
    s4 = gmsh.model.geo.addPlaneSurface([c4])
    s5 = gmsh.model.geo.addPlaneSurface([c5])
    s6 = gmsh.model.geo.addPlaneSurface([c6])
    s7 = gmsh.model.geo.addPlaneSurface([c7])
    s8 = gmsh.model.geo.addPlaneSurface([c8])
    s9 = gmsh.model.geo.addPlaneSurface([c9])



    # s = gmsh.model.geo.addPlaneSurface([c1,c2])

    gmsh.model.geo.mesh.setTransfiniteCurve(l1, nf+1,"Bump",1.0/f1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l2, nf+1,"Bump",1.0/f1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l3, nf+1,"Bump",1.0/f1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l4, nf+1,"Bump",1.0/f1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l9, nf+1,"Bump",1.0/f1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l14, nf+1,"Bump",1.0/f1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l19, nf+1,"Bump",1.0/f1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l24, nf+1,"Bump",1.0/f1)


    gmsh.model.geo.mesh.setTransfiniteCurve(l5, ns+1,"Progression",1.0/f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l6, ns+1,"Progression",1.0/f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l7, ns+1,"Progression",f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l8, ns+1,"Progression",f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l23, ns+1,"Progression",1.0/f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l10, ns+1,"Progression",1.0/f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l15, ns+1,"Progression",1.0/f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l13, ns+1,"Progression",1.0/f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l20, ns+1,"Progression",1.0/f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l18, ns+1,"Progression",1.0/f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l11, ns+1,"Progression",f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l12, ns+1,"Progression",1.0/f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l16, ns+1,"Progression",f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l17, ns+1,"Progression",1.0/f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l21, ns+1,"Progression",f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l22, ns+1,"Progression",1.0/f2)



    gmsh.model.geo.mesh.setTransfiniteSurface(s1)
    gmsh.model.geo.mesh.setTransfiniteSurface(s2)
    gmsh.model.geo.mesh.setTransfiniteSurface(s3)
    gmsh.model.geo.mesh.setTransfiniteSurface(s4)
    gmsh.model.geo.mesh.setTransfiniteSurface(s5)
    gmsh.model.geo.mesh.setTransfiniteSurface(s6)
    gmsh.model.geo.mesh.setTransfiniteSurface(s7)
    gmsh.model.geo.mesh.setTransfiniteSurface(s8)
    gmsh.model.geo.mesh.setTransfiniteSurface(s9)


    gmsh.model.geo.mesh.setRecombine(2, s1)
    gmsh.model.geo.mesh.setRecombine(2, s2)
    gmsh.model.geo.mesh.setRecombine(2, s3)
    gmsh.model.geo.mesh.setRecombine(2, s4)
    gmsh.model.geo.mesh.setRecombine(2, s5)
    gmsh.model.geo.mesh.setRecombine(2, s6)
    gmsh.model.geo.mesh.setRecombine(2, s7)
    gmsh.model.geo.mesh.setRecombine(2, s8)
    gmsh.model.geo.mesh.setRecombine(2, s9)
    

    return s1,s2,s3,s4,s5,s6,s7,s8,s9

def make_soil_foundation_layer_nonhomog_inclined(a=1.0,fl=2.0,fs=10.0, z1 = 5.0, z2 = 6.0,nf=18, f1 = 8.0, f2 = 1.5, ns = 9, inverse = False):
    p1 = gmsh.model.geo.addPoint(-fl*a/2.0, -fl*a/2.0, z1)
    p2 = gmsh.model.geo.addPoint(fl*a/2.0, -fl*a/2.0, z2)
    p3 = gmsh.model.geo.addPoint(fl*a/2.0, fl*a/2.0, z2)
    p4 = gmsh.model.geo.addPoint(-fl*a/2.0, fl*a/2.0, z1)
    l1 = gmsh.model.geo.addLine(p1, p2)
    l2 = gmsh.model.geo.addLine(p2, p3)
    l3 = gmsh.model.geo.addLine(p3, p4)
    l4 = gmsh.model.geo.addLine(p4, p1)
    if inverse == False:
        c1 = gmsh.model.geo.addCurveLoop([l1, l2, l3, l4])
    else:
        c1 = gmsh.model.geo.addCurveLoop([-l4,-l3,-l2,-l1])
    s1 = gmsh.model.geo.addPlaneSurface([c1])

    # Defining soil geometry
    p5 = gmsh.model.geo.addPoint(-fs*a/2.0, -fs*a/2.0, z1)
    p6 = gmsh.model.geo.addPoint(fs*a/2.0, -fs*a/2.0, z2)
    p7 = gmsh.model.geo.addPoint(fs*a/2.0, fs*a/2.0, z2)
    p8 = gmsh.model.geo.addPoint(-fs*a/2.0, fs*a/2.0, z1)

    # Baixo
    p9 = gmsh.model.geo.addPoint(-fl*a/2.0, -fs*a/2.0, z1)
    p10 = gmsh.model.geo.addPoint(fl*a/2.0, -fs*a/2.0, z2)

    # Direita
    p11 = gmsh.model.geo.addPoint(fs*a/2.0, -fl*a/2.0, z2)
    p12 = gmsh.model.geo.addPoint(fs*a/2.0, fl*a/2.0, z2)

    # Cima
    p13 = gmsh.model.geo.addPoint(fl*a/2.0, fs*a/2.0, z2)
    p14 = gmsh.model.geo.addPoint(-fl*a/2.0, fs*a/2.0, z1)

    # Esquerda
    p15 = gmsh.model.geo.addPoint(-fs*a/2.0, fl*a/2.0, z1)
    p16 = gmsh.model.geo.addPoint(-fs*a/2.0, -fl*a/2.0, z1)  


    # Esquerda-baixo
    l5 = gmsh.model.geo.addLine(p5,p9)
    l6 = gmsh.model.geo.addLine(p9,p1)
    l7 = gmsh.model.geo.addLine(p1,p16)
    l8 = gmsh.model.geo.addLine(p16,p5)

    # Meio-Baixo
    l9 = gmsh.model.geo.addLine(p9,p10)
    l10 = gmsh.model.geo.addLine(p10,p2)

    # Direita-baixo
    l11 = gmsh.model.geo.addLine(p10,p6)
    l12 = gmsh.model.geo.addLine(p6,p11)
    l13 = gmsh.model.geo.addLine(p11,p2)

    # Direta-meio
    l14 = gmsh.model.geo.addLine(p11,p12)
    l15 = gmsh.model.geo.addLine(p12,p3)

    # Direita-Cima
    l16 = gmsh.model.geo.addLine(p12,p7)
    l17 = gmsh.model.geo.addLine(p7,p13)
    l18 = gmsh.model.geo.addLine(p13,p3)

    # Meio-cima
    l19 = gmsh.model.geo.addLine(p13,p14)
    l20 = gmsh.model.geo.addLine(p14,p4)

    # Esquerda-Cima
    l21 = gmsh.model.geo.addLine(p14,p8)
    l22 = gmsh.model.geo.addLine(p8,p15)
    l23 = gmsh.model.geo.addLine(p15,p4)

    # Esquerda-meio
    l24 = gmsh.model.geo.addLine(p15,p16)

    if inverse == False:
        # Esquerda-baixo
        c2 = gmsh.model.geo.addCurveLoop([l5,l6,l7,l8])
        # Meio-baixo
        c3 = gmsh.model.geo.addCurveLoop([l9,l10,-l1,-l6])
        # Direita-baixo
        c4 = gmsh.model.geo.addCurveLoop([l11,l12,l13,-l10])
        # Direita-meio
        c5 = gmsh.model.geo.addCurveLoop([l14,l15,-l2,-l13])
        # Direita-cima
        c6 = gmsh.model.geo.addCurveLoop([l16,l17,l18,-l15])
        # Meio-cima
        c7 = gmsh.model.geo.addCurveLoop([l19,l20,-l3,-l18])
        # Esquerda-cima
        c8 = gmsh.model.geo.addCurveLoop([l21,l22,l23,-l20])
        # Esquerda-cima
        c9 = gmsh.model.geo.addCurveLoop([l24,-l7,-l4,-l23])
    else:
        c2 = gmsh.model.geo.addCurveLoop([-l8,-l7,-l6,-l5])
        # Meio-baixo
        c3 = gmsh.model.geo.addCurveLoop([l6,l1,-l10,-l9])
        # Direita-baixo
        c4 = gmsh.model.geo.addCurveLoop([l10,-l13,-l12,-l11])
        # Direita-meio
        c5 = gmsh.model.geo.addCurveLoop([l13,l2,-l15,-l14])
        # Direita-cima
        c6 = gmsh.model.geo.addCurveLoop([l15,-l18,-l17,-l16])
        # Meio-cima
        c7 = gmsh.model.geo.addCurveLoop([l18,l3,-l20,-l19])
        # Esquerda-cima
        c8 = gmsh.model.geo.addCurveLoop([l20,-l23,-l22,-l21])
        # Esquerda-cima
        c9 = gmsh.model.geo.addCurveLoop([l23,l4,l7,-l24])
    
    

    s2 = gmsh.model.geo.addPlaneSurface([c2])
    s3 = gmsh.model.geo.addPlaneSurface([c3])
    s4 = gmsh.model.geo.addPlaneSurface([c4])
    s5 = gmsh.model.geo.addPlaneSurface([c5])
    s6 = gmsh.model.geo.addPlaneSurface([c6])
    s7 = gmsh.model.geo.addPlaneSurface([c7])
    s8 = gmsh.model.geo.addPlaneSurface([c8])
    s9 = gmsh.model.geo.addPlaneSurface([c9])



    # s = gmsh.model.geo.addPlaneSurface([c1,c2])

    gmsh.model.geo.mesh.setTransfiniteCurve(l1, nf+1,"Bump",1.0/f1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l2, nf+1,"Bump",1.0/f1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l3, nf+1,"Bump",1.0/f1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l4, nf+1,"Bump",1.0/f1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l9, nf+1,"Bump",1.0/f1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l14, nf+1,"Bump",1.0/f1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l19, nf+1,"Bump",1.0/f1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l24, nf+1,"Bump",1.0/f1)


    gmsh.model.geo.mesh.setTransfiniteCurve(l5, ns,"Progression",1.0/f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l6, ns,"Progression",1.0/f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l7, ns,"Progression",f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l8, ns,"Progression",f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l23, ns,"Progression",1.0/f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l10, ns,"Progression",1.0/f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l15, ns,"Progression",1.0/f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l13, ns,"Progression",1.0/f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l20, ns,"Progression",1.0/f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l18, ns,"Progression",1.0/f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l11, ns,"Progression",f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l12, ns,"Progression",1.0/f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l16, ns,"Progression",f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l17, ns,"Progression",1.0/f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l21, ns,"Progression",f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l22, ns,"Progression",1.0/f2)



    gmsh.model.geo.mesh.setTransfiniteSurface(s1)
    gmsh.model.geo.mesh.setTransfiniteSurface(s2)
    gmsh.model.geo.mesh.setTransfiniteSurface(s3)
    gmsh.model.geo.mesh.setTransfiniteSurface(s4)
    gmsh.model.geo.mesh.setTransfiniteSurface(s5)
    gmsh.model.geo.mesh.setTransfiniteSurface(s6)
    gmsh.model.geo.mesh.setTransfiniteSurface(s7)
    gmsh.model.geo.mesh.setTransfiniteSurface(s8)
    gmsh.model.geo.mesh.setTransfiniteSurface(s9)


    gmsh.model.geo.mesh.setRecombine(2, s1)
    gmsh.model.geo.mesh.setRecombine(2, s2)
    gmsh.model.geo.mesh.setRecombine(2, s3)
    gmsh.model.geo.mesh.setRecombine(2, s4)
    gmsh.model.geo.mesh.setRecombine(2, s5)
    gmsh.model.geo.mesh.setRecombine(2, s6)
    gmsh.model.geo.mesh.setRecombine(2, s7)
    gmsh.model.geo.mesh.setRecombine(2, s8)
    gmsh.model.geo.mesh.setRecombine(2, s9)
    

    return s1,s2,s3,s4,s5,s6,s7,s8,s9

def make_mesh_soil_foundation_nonhomog(a=1.0, fl=2.0, fs=10.0, nf=18, f1 = 8.0, f2 = 1.5, ns = 9, inverse = True, popup=False):


    gmsh.initialize()

    gmsh.model.add("SoilFoundation")

    # Defining foundation geometry

    s1,s2,s3,s4,s5,s6,s7,s8,s9 = make_soil_foundation_layer_nonhomog(a=a,fl=fl,fs=fs, z = 0.0,nf=nf, f1 = f1, f2 = f2, ns = ns, inverse = inverse)
    

    pf = gmsh.model.addPhysicalGroup(2, [s1])
    gmsh.model.setPhysicalName(2, pf, "rb 0.0 rb 0.0 rb 0 0 1")
    ps = gmsh.model.addPhysicalGroup(2, [s2, s3, s4, s5,s6,s7,s8,s9])
    gmsh.model.setPhysicalName(2, ps, "t 0.0 t 0.0 t 0.0 1")

    gmsh.model.geo.synchronize()
    gmsh.model.mesh.generate(2)

    # gmsh.option.setNumber("Mesh.SaveAll", 1)

    filename_msh = "mesh.msh"
    gmsh.write(filename_msh)

    filename_vtk = "mesh.vtk"
    gmsh.write(filename_vtk)


    if popup:
        gmsh.fltk.run()

    gmsh.finalize()

    return filename_msh

def make_mesh_soil_foundation_rock_nonhomog(a=1.0, fl=2.0, fs=10.0, nf1=18, nf2 = 9,f1 = 8.0, f2 = 1.5, ns = 9, z = 1.0,inverse = True, popup=False):
    gmsh.initialize()

    gmsh.model.add("SoilFoundation")

    # Defining foundation geometry

    s1,s2,s3,s4,s5,s6,s7,s8,s9 = make_soil_foundation_layer_nonhomog(a=a,fl=fl,fs=fs,nf=nf1,f1=f1,f2=f2,ns=ns, z = 0.0,inverse = True)
    s10,s11,s12,s13,s14,s15,s16,s17,s18 = make_soil_foundation_layer_nonhomog(a=a,fl=fl,fs=fs,nf=nf2,f1=f1,f2=f2,ns=ns, z = z)
    

    pf = gmsh.model.addPhysicalGroup(2, [s1])
    gmsh.model.setPhysicalName(2, pf, "rb")
    ps = gmsh.model.addPhysicalGroup(2, [s2,s3,s4,s5,s6,s7,s8,s9])
    gmsh.model.setPhysicalName(2, ps, "t 0.0 0.0 0.0")

    pr = gmsh.model.addPhysicalGroup(2, [s10,s11,s12,s13,s14,s15,s16,s17,s18])
    gmsh.model.setPhysicalName(2, pr, "u 0.0 0.0 0.0")


    gmsh.model.geo.synchronize()
    gmsh.model.mesh.generate(2)

    # gmsh.option.setNumber("Mesh.SaveAll", 1)

    filename_msh = "mesh.msh"
    gmsh.write(filename_msh)

    filename_vtk = "mesh.vtk"
    gmsh.write(filename_vtk)

    if popup:
        gmsh.fltk.run()

    gmsh.finalize()

    return filename_msh

def make_mesh_soil_foundation_rock_nonhomog2(a=1.0, fl=2.0, fs=10.0, nf1=18, nf2 = 9,f1 = 8.0, f2 = 1.5, ns = 9, z1 = 1.0, z2 = 1.0,inverse = True, popup=False):
    gmsh.initialize()

    gmsh.model.add("SoilFoundation")

    # Defining foundation geometry

    s1,s2,s3,s4,s5,s6,s7,s8,s9 = make_soil_foundation_layer_nonhomog(a=a,fl=fl,fs=fs,nf=nf1,f1=f1,f2=f2,ns=ns, z = 0.0,inverse = True)
    s10 = make_square(l=a*fs, z1 = z1, z2 = z2, nf = nf2)

    pf = gmsh.model.addPhysicalGroup(2, [s1])
    gmsh.model.setPhysicalName(2, pf, "rb")
    ps = gmsh.model.addPhysicalGroup(2, [s2,s3,s4,s5,s6,s7,s8,s9])
    gmsh.model.setPhysicalName(2, ps, "t 0.0 0.0 0.0")

    pr = gmsh.model.addPhysicalGroup(2, [s10])
    gmsh.model.setPhysicalName(2, pr, "u 0.0 0.0 0.0")


    gmsh.model.geo.synchronize()
    gmsh.model.mesh.generate(2)

    # gmsh.option.setNumber("Mesh.SaveAll", 1)

    filename_msh = "mesh.msh"
    gmsh.write(filename_msh)

    filename_vtk = "mesh.vtk"
    gmsh.write(filename_vtk)

    if popup:
        gmsh.fltk.run()

    gmsh.finalize()

    return filename_msh


def make_mesh_soil_foundation_rock_nonhomog_inclined(a=1.0, fl=2.0, fs=10.0, nf1=18, nf2 = 9, ns = 9, z1 = 5.0, z2 = 6.0,inverse = True, popup=False):
    gmsh.initialize()

    gmsh.model.add("SoilFoundation")

    # Defining foundation geometry

    s1,s2,s3,s4,s5,s6,s7,s8,s9 = make_soil_foundation_layer_nonhomog(a=a,fl=fl,fs=fs,nf=nf1,f1=8.0,f2=1.5,ns=ns, z = 0.0,inverse = True)
    s10,s11,s12,s13,s14,s15,s16,s17,s18 = make_soil_foundation_layer_nonhomog_inclined(a=a,fl=fl,fs=fs,nf=nf2,f1=8.0,f2=1.5,ns=ns, z1 = z1, z2 = z2)
    

    pf = gmsh.model.addPhysicalGroup(2, [s1])
    gmsh.model.setPhysicalName(2, pf, "rb")
    ps = gmsh.model.addPhysicalGroup(2, [s2,s3,s4,s5,s6,s7,s8,s9])
    gmsh.model.setPhysicalName(2, ps, "t 0.0 0.0 0.0")

    pr = gmsh.model.addPhysicalGroup(2, [s10,s11,s12,s13,s14,s15,s16,s17,s18])
    gmsh.model.setPhysicalName(2, pr, "u 0.0 0.0 0.0")


    gmsh.model.geo.synchronize()
    gmsh.model.mesh.generate(2)

    # gmsh.option.setNumber("Mesh.SaveAll", 1)

    filename_msh = "mesh.msh"
    gmsh.write(filename_msh)

    filename_vtk = "mesh.vtk"
    gmsh.write(filename_vtk)

    if popup:
        gmsh.fltk.run()

    gmsh.finalize()

    return filename_msh
