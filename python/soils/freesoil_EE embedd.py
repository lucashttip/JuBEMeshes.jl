import gmsh

def make_mesh_soil_free_EE_nonhomog_equal(a = 1.0, fs = 10, nel = 10,nexy = 1,nez = 1, nes = 1, dxy = 0, dz = 1,elementOrder = 1, inverse = True, popup=False):
    
    fl = fs/5
    nf = nel//5
    ns = 2*nel//5

    file_msh = make_mesh_soil_free_EE_nonhomog(a=a, fl=fl, fs=fs, nf=nf, ns = ns,nexy = nexy,nez = nez, nes = nes,f1 = 1.0, f2 = 1.0,dxy=dxy, dz = dz,elementOrder = elementOrder, inverse = inverse, popup=popup)
    return file_msh


def make_mesh_soil_free_EE_nonhomog(a=1.0, fl=2.0, fs=10.0, nf=18, ns = 9, f1 = 8.0, f2 = 1.5, nexy = 1,nez = 1, nes = 1, dxy = 0, dz = 1,elementOrder = 1, inverse = True, popup=False):
    
    gmsh.initialize()

    gmsh.model.add("SoilFoundation")

    # Defining foundation geometry

    if dxy != 0:
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = make_soil_free_EE_nonhomog(a=a,fl=fl,fs=fs, z = 0.0,nf=nf, ns = ns,f1 = f1, f2 = f2, nexy = nexy,nez = nez,nes = nes, dxy = dxy, dz = dz, inverse = inverse)
    else:
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s14,s15,s16,s17,s18 = make_soil_free_EE_nonhomog(a=a,fl=fl,fs=fs, z = 0.0,nf=nf, ns = ns,f1 = f1, f2 = f2, nexy = nexy,nez = nez,nes = nes, dxy = dxy, dz = dz, inverse = inverse)

    pf = gmsh.model.addPhysicalGroup(2, [s1])
    gmsh.model.setPhysicalName(2, pf, "t 0.0 t 0.0 t 1.0 1")
    ps = gmsh.model.addPhysicalGroup(2, [s2, s3, s4, s5,s6,s7,s8,s9])
    gmsh.model.setPhysicalName(2, ps, "t 0.0 t 0.0 t 0.0 1")
    if dxy !=0:
        ee = gmsh.model.addPhysicalGroup(2, [s10, s11, s12, s13,s14,s15,s16,s17,s18])
    else:
        ee = gmsh.model.addPhysicalGroup(2, [s14,s15,s16,s17,s18])

    gmsh.model.setPhysicalName(2, ee, "ee 0.0 ee 0.0 ee 0.0 1")

    gmsh.model.geo.synchronize()
    gmsh.model.mesh.generate(2)
    gmsh.model.mesh.setOrder(elementOrder)

    # gmsh.option.setNumber("Mesh.SaveAll", 1)

    filename_msh = "mesh.msh"
    gmsh.write(filename_msh)

    filename_vtk = "mesh.vtk"
    gmsh.write(filename_vtk)


    if popup:
        gmsh.fltk.run()

    gmsh.finalize()

    return filename_msh

def make_soil_free_EE_nonhomog(a=1.0, fl=2.0, fs=10.0, z = 0.0, nf=18, ns = 9, f1 = 8.0, f2 = 1.5, nexy = 1,nez = 1, nes = 1, dxy = 0, dz = 1, inverse = False):
    
    # Making SOIL
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
    
    # Making EE
    if dxy != 0:
        ## Pontos quadrado externo:
        p17 = gmsh.model.geo.addPoint(-fs*a/2.0 - dxy, -fs*a/2.0 - dxy, z)
        p18 = gmsh.model.geo.addPoint(fs*a/2.0 + dxy, -fs*a/2.0 - dxy, z)
        p19 = gmsh.model.geo.addPoint(fs*a/2.0 + dxy, fs*a/2.0 + dxy, z)
        p20 = gmsh.model.geo.addPoint(-fs*a/2.0 - dxy, fs*a/2.0 + dxy, z)
    else:
        p17 = p5
        p18 = p6
        p19 = p7
        p20 = p8

    # Pontos inferiores
    p21 = gmsh.model.geo.addPoint(-fs*a/2.0 - dxy, -fs*a/2.0 - dxy, z + dz)
    p22 = gmsh.model.geo.addPoint(fs*a/2.0 + dxy, -fs*a/2.0 - dxy, z + dz)
    p23 = gmsh.model.geo.addPoint(fs*a/2.0 + dxy, fs*a/2.0 + dxy, z + dz)
    p24 = gmsh.model.geo.addPoint(-fs*a/2.0 - dxy, fs*a/2.0 + dxy, z + dz)

    # Linhas quadrado externo superior:
    l25 = gmsh.model.geo.addLine(p17, p18)
    l26 = gmsh.model.geo.addLine(p18, p19)
    l27 = gmsh.model.geo.addLine(p19, p20)
    l28 = gmsh.model.geo.addLine(p20, p17)

    # Linhas quadrado externo inferior:
    l29 = gmsh.model.geo.addLine(p21, p22)
    l30 = gmsh.model.geo.addLine(p22, p23)
    l31 = gmsh.model.geo.addLine(p23, p24)
    l32 = gmsh.model.geo.addLine(p24, p21)

    if dxy != 0:
        # Linhas dos quadrado externo superior com quadrado interno
        l33 = gmsh.model.geo.addLine(p17, p5)
        l34 = gmsh.model.geo.addLine(p18, p6)
        l35 = gmsh.model.geo.addLine(p19, p7)
        l36 = gmsh.model.geo.addLine(p20, p8)
        # Linhas do quadrado interno superior
        l41 = gmsh.model.geo.addLine(p5, p6)
        l42 = gmsh.model.geo.addLine(p6, p7)
        l43 = gmsh.model.geo.addLine(p7, p8)
        l44 = gmsh.model.geo.addLine(p8, p5)

    
    # Linhas que ligam quadrado superior com inferior:
    l37 = gmsh.model.geo.addLine(p17, p21)
    l38 = gmsh.model.geo.addLine(p18, p22)
    l39 = gmsh.model.geo.addLine(p19, p23)
    l40 = gmsh.model.geo.addLine(p20, p24)
    
    
    if dxy != 0:
    # Curvas superiores:
        ## Baixo-cima
        c10 = gmsh.model.geo.addCurveLoop([l41,-l34,-l25,l33])
        ## Direita-cima
        c11 = gmsh.model.geo.addCurveLoop([l42,-l35,-l26,l34])
        ## Cima-cima
        c12 = gmsh.model.geo.addCurveLoop([l43,-l36,-l27,l35])
        ## Esquerda-cima
        c13 = gmsh.model.geo.addCurveLoop([l44,-l33,-l28,l36])
    
    # Curvas laterais
    ## Baixo-meio
    c14 = gmsh.model.geo.addCurveLoop([-l32,-l40,l28,l37])
    ## Direita-meio
    c15 = gmsh.model.geo.addCurveLoop([-l31,-l39,l27,l40])
    ## Cima-meio
    c16 = gmsh.model.geo.addCurveLoop([-l30,-l38,l26,l39])
    ## Esquerda-meio
    c17 = gmsh.model.geo.addCurveLoop([-l29,-l37,l25,l38])

    # Curva inferior
    ## Tudo-baixo
    c18 = gmsh.model.geo.addCurveLoop([l29,l30,l31,l32])

    if dxy !=0:
        # Superfícies superiores
        s10 = gmsh.model.geo.addPlaneSurface([c10])
        s11 = gmsh.model.geo.addPlaneSurface([c11])
        s12 = gmsh.model.geo.addPlaneSurface([c12])
        s13 = gmsh.model.geo.addPlaneSurface([c13])
    
    # Superfícies laterais e inferiores
    s14 = gmsh.model.geo.addPlaneSurface([c14])
    s15 = gmsh.model.geo.addPlaneSurface([c15])
    s16 = gmsh.model.geo.addPlaneSurface([c16])
    s17 = gmsh.model.geo.addPlaneSurface([c17])
    s18 = gmsh.model.geo.addPlaneSurface([c18])

    # Linhas quadrado externo superior:
    gmsh.model.geo.mesh.setTransfiniteCurve(l25, nexy+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l26, nexy+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l27, nexy+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l28, nexy+1)

    # Linhas quadrado externo inferior: 
    gmsh.model.geo.mesh.setTransfiniteCurve(l29, nexy+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l30, nexy+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l31, nexy+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l32, nexy+1)

    # Linhas que ligam quadrado superior com inferior:
    gmsh.model.geo.mesh.setTransfiniteCurve(l37, nez+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l38, nez+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l39, nez+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l40, nez+1)
    

    if dxy !=0:
        # Linhas dos quadrado externo superior com quadrado interno
        gmsh.model.geo.mesh.setTransfiniteCurve(l33, nes+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l34, nes+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l35, nes+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l36, nes+1)

        # Linhas do quadrado interno superior
        gmsh.model.geo.mesh.setTransfiniteCurve(l41, nexy+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l42, nexy+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l43, nexy+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l44, nexy+1)



    if dxy !=0:
        gmsh.model.geo.mesh.setTransfiniteSurface(s10)
        gmsh.model.geo.mesh.setTransfiniteSurface(s11)
        gmsh.model.geo.mesh.setTransfiniteSurface(s12)
        gmsh.model.geo.mesh.setTransfiniteSurface(s13)
    gmsh.model.geo.mesh.setTransfiniteSurface(s14)
    gmsh.model.geo.mesh.setTransfiniteSurface(s15)
    gmsh.model.geo.mesh.setTransfiniteSurface(s16)
    gmsh.model.geo.mesh.setTransfiniteSurface(s17)
    gmsh.model.geo.mesh.setTransfiniteSurface(s18)

    if dxy !=0:
        gmsh.model.geo.mesh.setRecombine(2, s10)
        gmsh.model.geo.mesh.setRecombine(2, s11)
        gmsh.model.geo.mesh.setRecombine(2, s12)
        gmsh.model.geo.mesh.setRecombine(2, s13)
    gmsh.model.geo.mesh.setRecombine(2, s14)
    gmsh.model.geo.mesh.setRecombine(2, s15)
    gmsh.model.geo.mesh.setRecombine(2, s16)
    gmsh.model.geo.mesh.setRecombine(2, s17)
    gmsh.model.geo.mesh.setRecombine(2, s18)


    if dxy != 0:
        return s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18
    else:
        return s1,s2,s3,s4,s5,s6,s7,s8,s9,s14,s15,s16,s17,s18


def make_mesh_soil_free_EE_homog(a=1.0, fl=2.0, fs=10.0, nf=18,ns = 9,nexy = 1,nez = 1, nes = 1, dxy = 0, dz = 1,elementOrder = 1, inverse = True, popup=False):
    
    gmsh.initialize()

    gmsh.model.add("SoilFoundation")

    # Defining foundation geometry

    if dxy != 0:
        s1,s2,s3,s4,s5,s10,s11,s12,s13,s14,s15,s16,s17,s18 = make_soil_free_EE_homog(a=a,fl=fl,fs=fs, z = 0.0,nf=nf,ns = ns, nexy = nexy,nez = nez,nes = nes, dxy = dxy, dz = dz, inverse = inverse)
    else:
        s1,s2,s3,s4,s5,s14,s15,s16,s17,s18 = make_soil_free_EE_homog(a=a,fl=fl,fs=fs, z = 0.0,nf=nf,ns = ns, nexy = nexy,nez = nez,nes = nes, dxy = dxy, dz = dz, inverse = inverse)

    pf = gmsh.model.addPhysicalGroup(2, [s1])
    gmsh.model.setPhysicalName(2, pf, "t 0.0 t 0.0 t 1.0 1")
    ps = gmsh.model.addPhysicalGroup(2, [s2, s3, s4, s5])
    gmsh.model.setPhysicalName(2, ps, "t 0.0 t 0.0 t 0.0 1")
    if dxy !=0:
        ee = gmsh.model.addPhysicalGroup(2, [s10, s11, s12, s13,s14,s15,s16,s17,s18])
    else:
        ee = gmsh.model.addPhysicalGroup(2, [s14,s15,s16,s17,s18])

    gmsh.model.setPhysicalName(2, ee, "ee 0.0 ee 0.0 ee 0.0 1")

    gmsh.model.geo.synchronize()
    gmsh.model.mesh.generate(2)
    gmsh.model.mesh.setOrder(elementOrder)

    # gmsh.option.setNumber("Mesh.SaveAll", 1)

    filename_msh = "mesh.msh"
    gmsh.write(filename_msh)

    filename_vtk = "mesh.vtk"
    gmsh.write(filename_vtk)


    if popup:
        gmsh.fltk.run()

    gmsh.finalize()

    return filename_msh

def make_soil_free_EE_homog(a=1.0, fl=2.0, fs=10.0, z = 0.0, nf=18,ns = 9, nexy = 1,nez = 1, nes = 1, dxy = 0, dz = 1, inverse = False):
    
    # foundation
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
        c1 = gmsh.model.geo.addCurveLoop([-l4, -l3, -l2, -l1])
    s1 = gmsh.model.geo.addPlaneSurface([c1])

    # Defining soil geometry
    p5 = gmsh.model.geo.addPoint(-fs*a/2.0, -fs*a/2.0, z)
    p6 = gmsh.model.geo.addPoint(fs*a/2.0, -fs*a/2.0, z)
    p7 = gmsh.model.geo.addPoint(fs*a/2.0, fs*a/2.0, z)
    p8 = gmsh.model.geo.addPoint(-fs*a/2.0, fs*a/2.0, z)

    l5 = gmsh.model.geo.addLine(p5, p6)
    l6 = gmsh.model.geo.addLine(p6, p7)
    l7 = gmsh.model.geo.addLine(p7, p8)
    l8 = gmsh.model.geo.addLine(p8, p5)

    l9 = gmsh.model.geo.addLine(p1,p5)
    l10 = gmsh.model.geo.addLine(p2,p6)
    l11 = gmsh.model.geo.addLine(p3,p7)
    l12 = gmsh.model.geo.addLine(p4,p8)

    if inverse == False:
        c2 = gmsh.model.geo.addCurveLoop([l5, -l10, -l1, l9])
        c3 = gmsh.model.geo.addCurveLoop([l6, -l11, -l2, l10])
        c4 = gmsh.model.geo.addCurveLoop([l7, -l12, -l3, l11])
        c5 = gmsh.model.geo.addCurveLoop([l8, -l9, -l4, l12])
    else:
        c2 = gmsh.model.geo.addCurveLoop([-l9, l1, l10, -l5])
        c3 = gmsh.model.geo.addCurveLoop([-l10, l2, l11, -l6])
        c4 = gmsh.model.geo.addCurveLoop([-l11, l3, l12, -l7])
        c5 = gmsh.model.geo.addCurveLoop([-l12, l4, l9, -l8])
    

    s2 = gmsh.model.geo.addPlaneSurface([c2])
    s3 = gmsh.model.geo.addPlaneSurface([c3])
    s4 = gmsh.model.geo.addPlaneSurface([c4])
    s5 = gmsh.model.geo.addPlaneSurface([c5])


    # s = gmsh.model.geo.addPlaneSurface([c1,c2])

    gmsh.model.geo.mesh.setTransfiniteCurve(l1, nf+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l2, nf+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l3, nf+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l4, nf+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l5, nf+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l6, nf+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l7, nf+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l8, nf+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l9, ns+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l10, ns+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l11, ns+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l12, ns+1)



    gmsh.model.geo.mesh.setTransfiniteSurface(s1)
    gmsh.model.geo.mesh.setTransfiniteSurface(s2)
    gmsh.model.geo.mesh.setTransfiniteSurface(s3)
    gmsh.model.geo.mesh.setTransfiniteSurface(s4)
    gmsh.model.geo.mesh.setTransfiniteSurface(s5)


    gmsh.model.geo.mesh.setRecombine(2, s1)
    gmsh.model.geo.mesh.setRecombine(2, s2)
    gmsh.model.geo.mesh.setRecombine(2, s3)
    gmsh.model.geo.mesh.setRecombine(2, s4)
    gmsh.model.geo.mesh.setRecombine(2, s5)
    
    # Making EE
    if dxy != 0:
        ## Pontos quadrado externo:
        p17 = gmsh.model.geo.addPoint(-fs*a/2.0 - dxy, -fs*a/2.0 - dxy, z)
        p18 = gmsh.model.geo.addPoint(fs*a/2.0 + dxy, -fs*a/2.0 - dxy, z)
        p19 = gmsh.model.geo.addPoint(fs*a/2.0 + dxy, fs*a/2.0 + dxy, z)
        p20 = gmsh.model.geo.addPoint(-fs*a/2.0 - dxy, fs*a/2.0 + dxy, z)
    else:
        p17 = p5
        p18 = p6
        p19 = p7
        p20 = p8

    # Pontos inferiores
    p21 = gmsh.model.geo.addPoint(-fs*a/2.0 - dxy, -fs*a/2.0 - dxy, z + dz)
    p22 = gmsh.model.geo.addPoint(fs*a/2.0 + dxy, -fs*a/2.0 - dxy, z + dz)
    p23 = gmsh.model.geo.addPoint(fs*a/2.0 + dxy, fs*a/2.0 + dxy, z + dz)
    p24 = gmsh.model.geo.addPoint(-fs*a/2.0 - dxy, fs*a/2.0 + dxy, z + dz)

    # Linhas quadrado externo superior:
    l25 = gmsh.model.geo.addLine(p17, p18)
    l26 = gmsh.model.geo.addLine(p18, p19)
    l27 = gmsh.model.geo.addLine(p19, p20)
    l28 = gmsh.model.geo.addLine(p20, p17)

    # Linhas quadrado externo inferior:
    l29 = gmsh.model.geo.addLine(p21, p22)
    l30 = gmsh.model.geo.addLine(p22, p23)
    l31 = gmsh.model.geo.addLine(p23, p24)
    l32 = gmsh.model.geo.addLine(p24, p21)

    if dxy != 0:
        # Linhas dos quadrado externo superior com quadrado interno
        l33 = gmsh.model.geo.addLine(p17, p5)
        l34 = gmsh.model.geo.addLine(p18, p6)
        l35 = gmsh.model.geo.addLine(p19, p7)
        l36 = gmsh.model.geo.addLine(p20, p8)
        # Linhas do quadrado interno superior
        l41 = gmsh.model.geo.addLine(p5, p6)
        l42 = gmsh.model.geo.addLine(p6, p7)
        l43 = gmsh.model.geo.addLine(p7, p8)
        l44 = gmsh.model.geo.addLine(p8, p5)
        # l41 = l5
        # l42 = l6
        # l43 = l7
        # l44 = l8

    
    # Linhas que ligam quadrado superior com inferior:
    l37 = gmsh.model.geo.addLine(p17, p21)
    l38 = gmsh.model.geo.addLine(p18, p22)
    l39 = gmsh.model.geo.addLine(p19, p23)
    l40 = gmsh.model.geo.addLine(p20, p24)
    
    
    if dxy != 0:
    # Curvas superiores:
        ## Baixo-cima
        c10 = gmsh.model.geo.addCurveLoop([l41,-l34,-l25,l33])
        ## Direita-cima
        c11 = gmsh.model.geo.addCurveLoop([l42,-l35,-l26,l34])
        ## Cima-cima
        c12 = gmsh.model.geo.addCurveLoop([l43,-l36,-l27,l35])
        ## Esquerda-cima
        c13 = gmsh.model.geo.addCurveLoop([l44,-l33,-l28,l36])
    
    # Curvas laterais
    ## Baixo-meio
    c14 = gmsh.model.geo.addCurveLoop([-l32,-l40,l28,l37])
    ## Direita-meio
    c15 = gmsh.model.geo.addCurveLoop([-l31,-l39,l27,l40])
    ## Cima-meio
    c16 = gmsh.model.geo.addCurveLoop([-l30,-l38,l26,l39])
    ## Esquerda-meio
    c17 = gmsh.model.geo.addCurveLoop([-l29,-l37,l25,l38])

    # Curva inferior
    ## Tudo-baixo
    c18 = gmsh.model.geo.addCurveLoop([l29,l30,l31,l32])

    if dxy !=0:
        # Superfícies superiores
        s10 = gmsh.model.geo.addPlaneSurface([c10])
        s11 = gmsh.model.geo.addPlaneSurface([c11])
        s12 = gmsh.model.geo.addPlaneSurface([c12])
        s13 = gmsh.model.geo.addPlaneSurface([c13])
    
    # Superfícies laterais e inferiores
    s14 = gmsh.model.geo.addPlaneSurface([c14])
    s15 = gmsh.model.geo.addPlaneSurface([c15])
    s16 = gmsh.model.geo.addPlaneSurface([c16])
    s17 = gmsh.model.geo.addPlaneSurface([c17])
    s18 = gmsh.model.geo.addPlaneSurface([c18])

    # Linhas quadrado externo superior:
    gmsh.model.geo.mesh.setTransfiniteCurve(l25, nexy+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l26, nexy+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l27, nexy+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l28, nexy+1)

    # Linhas quadrado externo inferior: 
    gmsh.model.geo.mesh.setTransfiniteCurve(l29, nexy+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l30, nexy+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l31, nexy+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l32, nexy+1)

    # Linhas que ligam quadrado superior com inferior:
    gmsh.model.geo.mesh.setTransfiniteCurve(l37, nez+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l38, nez+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l39, nez+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l40, nez+1)
    

    if dxy !=0:
        # Linhas dos quadrado externo superior com quadrado interno
        gmsh.model.geo.mesh.setTransfiniteCurve(l33, nes+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l34, nes+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l35, nes+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l36, nes+1)

        # Linhas do quadrado interno superior
        gmsh.model.geo.mesh.setTransfiniteCurve(l41, nexy+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l42, nexy+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l43, nexy+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l44, nexy+1)



    if dxy !=0:
        gmsh.model.geo.mesh.setTransfiniteSurface(s10)
        gmsh.model.geo.mesh.setTransfiniteSurface(s11)
        gmsh.model.geo.mesh.setTransfiniteSurface(s12)
        gmsh.model.geo.mesh.setTransfiniteSurface(s13)
    gmsh.model.geo.mesh.setTransfiniteSurface(s14)
    gmsh.model.geo.mesh.setTransfiniteSurface(s15)
    gmsh.model.geo.mesh.setTransfiniteSurface(s16)
    gmsh.model.geo.mesh.setTransfiniteSurface(s17)
    gmsh.model.geo.mesh.setTransfiniteSurface(s18)

    if dxy !=0:
        gmsh.model.geo.mesh.setRecombine(2, s10)
        gmsh.model.geo.mesh.setRecombine(2, s11)
        gmsh.model.geo.mesh.setRecombine(2, s12)
        gmsh.model.geo.mesh.setRecombine(2, s13)
    gmsh.model.geo.mesh.setRecombine(2, s14)
    gmsh.model.geo.mesh.setRecombine(2, s15)
    gmsh.model.geo.mesh.setRecombine(2, s16)
    gmsh.model.geo.mesh.setRecombine(2, s17)
    gmsh.model.geo.mesh.setRecombine(2, s18)


    if dxy != 0:
        return s1,s2,s3,s4,s5,s10,s11,s12,s13,s14,s15,s16,s17,s18
    else:
        return s1,s2,s3,s4,s5,s14,s15,s16,s17,s18


def make_mesh_soil_free_EE_homog2(a=1.0, fl=2.0, fs=10.0,f1 = 1.0,f2 = 1.0, nf=18,ns = 9,nexy = 1,nez = 1, nes = 1, dxy = 0, dz = 1,elementOrder = 1, inverse = True, popup=False):
    
    gmsh.initialize()

    gmsh.model.add("SoilFoundation")

    # Defining foundation geometry

    if dxy != 0:
        s1,s2,s3,s4,s5,s10,s11,s12,s13,s14,s15,s16,s17,s18 = make_soil_free_EE_homog2(a=a,fl=fl,fs=fs,f1 = f1,f2=f2, z = 0.0,nf=nf,ns = ns, nexy = nexy,nez = nez,nes = nes, dxy = dxy, dz = dz, inverse = inverse)
    else:
        s1,s2,s3,s4,s5,s14,s15,s16,s17,s18 = make_soil_free_EE_homog2(a=a,fl=fl,fs=fs,f1 = f1,f2=f2, z = 0.0,nf=nf,ns = ns, nexy = nexy,nez = nez,nes = nes, dxy = dxy, dz = dz, inverse = inverse)

    pf = gmsh.model.addPhysicalGroup(2, [s1])
    gmsh.model.setPhysicalName(2, pf, "t 0.0 t 0.0 t 1.0 1")
    ps = gmsh.model.addPhysicalGroup(2, [s2, s3, s4, s5])
    gmsh.model.setPhysicalName(2, ps, "t 0.0 t 0.0 t 0.0 1")
    if dxy !=0:
        ee = gmsh.model.addPhysicalGroup(2, [s10, s11, s12, s13,s14,s15,s16,s17,s18])
    else:
        ee = gmsh.model.addPhysicalGroup(2, [s14,s15,s16,s17,s18])

    gmsh.model.setPhysicalName(2, ee, "ee 0.0 ee 0.0 ee 0.0 1")

    gmsh.model.geo.synchronize()
    gmsh.model.mesh.generate(2)
    gmsh.model.mesh.setOrder(elementOrder)

    # gmsh.option.setNumber("Mesh.SaveAll", 1)

    filename_msh = "mesh.msh"
    gmsh.write(filename_msh)

    filename_vtk = "mesh.vtk"
    gmsh.write(filename_vtk)


    if popup:
        gmsh.fltk.run()

    gmsh.finalize()

    return filename_msh

def make_soil_free_EE_homog2(a=1.0, fl=2.0, fs=10.0,f1 = 1.0,f2 = 1.0, z = 0.0, nf=18,ns = 9, nexy = 1,nez = 1, nes = 1, dxy = 0, dz = 1, inverse = False):
    
    # foundation
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
        c1 = gmsh.model.geo.addCurveLoop([-l4, -l3, -l2, -l1])
    s1 = gmsh.model.geo.addPlaneSurface([c1])

    # Defining soil geometry
    p5 = gmsh.model.geo.addPoint(-fs*a/2.0, -fs*a/2.0, z)
    p6 = gmsh.model.geo.addPoint(fs*a/2.0, -fs*a/2.0, z)
    p7 = gmsh.model.geo.addPoint(fs*a/2.0, fs*a/2.0, z)
    p8 = gmsh.model.geo.addPoint(-fs*a/2.0, fs*a/2.0, z)

    l5 = gmsh.model.geo.addLine(p5, p6)
    l6 = gmsh.model.geo.addLine(p6, p7)
    l7 = gmsh.model.geo.addLine(p7, p8)
    l8 = gmsh.model.geo.addLine(p8, p5)

    l9 = gmsh.model.geo.addLine(p1,p5)
    l10 = gmsh.model.geo.addLine(p2,p6)
    l11 = gmsh.model.geo.addLine(p3,p7)
    l12 = gmsh.model.geo.addLine(p4,p8)

    if inverse == False:
        c2 = gmsh.model.geo.addCurveLoop([l5, -l10, -l1, l9])
        c3 = gmsh.model.geo.addCurveLoop([l6, -l11, -l2, l10])
        c4 = gmsh.model.geo.addCurveLoop([l7, -l12, -l3, l11])
        c5 = gmsh.model.geo.addCurveLoop([l8, -l9, -l4, l12])
    else:
        c2 = gmsh.model.geo.addCurveLoop([-l9, l1, l10, -l5])
        c3 = gmsh.model.geo.addCurveLoop([-l10, l2, l11, -l6])
        c4 = gmsh.model.geo.addCurveLoop([-l11, l3, l12, -l7])
        c5 = gmsh.model.geo.addCurveLoop([-l12, l4, l9, -l8])
    

    s2 = gmsh.model.geo.addPlaneSurface([c2])
    s3 = gmsh.model.geo.addPlaneSurface([c3])
    s4 = gmsh.model.geo.addPlaneSurface([c4])
    s5 = gmsh.model.geo.addPlaneSurface([c5])


    # s = gmsh.model.geo.addPlaneSurface([c1,c2])

    gmsh.model.geo.mesh.setTransfiniteCurve(l1, nf+1,"Bump",1.0/f1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l2, nf+1,"Bump",1.0/f1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l3, nf+1,"Bump",1.0/f1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l4, nf+1,"Bump",1.0/f1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l5, nf+1,"Bump",1.0/f1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l6, nf+1,"Bump",1.0/f1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l7, nf+1,"Bump",1.0/f1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l8, nf+1,"Bump",1.0/f1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l9, ns+1,"Progression",f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l10, ns+1,"Progression",f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l11, ns+1,"Progression",f2)
    gmsh.model.geo.mesh.setTransfiniteCurve(l12, ns+1,"Progression",f2)



    gmsh.model.geo.mesh.setTransfiniteSurface(s1)
    gmsh.model.geo.mesh.setTransfiniteSurface(s2)
    gmsh.model.geo.mesh.setTransfiniteSurface(s3)
    gmsh.model.geo.mesh.setTransfiniteSurface(s4)
    gmsh.model.geo.mesh.setTransfiniteSurface(s5)


    gmsh.model.geo.mesh.setRecombine(2, s1)
    gmsh.model.geo.mesh.setRecombine(2, s2)
    gmsh.model.geo.mesh.setRecombine(2, s3)
    gmsh.model.geo.mesh.setRecombine(2, s4)
    gmsh.model.geo.mesh.setRecombine(2, s5)
    
    # Making EE
    if dxy != 0:
        ## Pontos quadrado externo:
        p17 = gmsh.model.geo.addPoint(-fs*a/2.0 - dxy, -fs*a/2.0 - dxy, z)
        p18 = gmsh.model.geo.addPoint(fs*a/2.0 + dxy, -fs*a/2.0 - dxy, z)
        p19 = gmsh.model.geo.addPoint(fs*a/2.0 + dxy, fs*a/2.0 + dxy, z)
        p20 = gmsh.model.geo.addPoint(-fs*a/2.0 - dxy, fs*a/2.0 + dxy, z)
    else:
        p17 = p5
        p18 = p6
        p19 = p7
        p20 = p8

    # Pontos inferiores
    p21 = gmsh.model.geo.addPoint(-fs*a/2.0 - dxy, -fs*a/2.0 - dxy, z + dz)
    p22 = gmsh.model.geo.addPoint(fs*a/2.0 + dxy, -fs*a/2.0 - dxy, z + dz)
    p23 = gmsh.model.geo.addPoint(fs*a/2.0 + dxy, fs*a/2.0 + dxy, z + dz)
    p24 = gmsh.model.geo.addPoint(-fs*a/2.0 - dxy, fs*a/2.0 + dxy, z + dz)

    # Linhas quadrado externo superior:
    l25 = gmsh.model.geo.addLine(p17, p18)
    l26 = gmsh.model.geo.addLine(p18, p19)
    l27 = gmsh.model.geo.addLine(p19, p20)
    l28 = gmsh.model.geo.addLine(p20, p17)

    # Linhas quadrado externo inferior:
    l29 = gmsh.model.geo.addLine(p21, p22)
    l30 = gmsh.model.geo.addLine(p22, p23)
    l31 = gmsh.model.geo.addLine(p23, p24)
    l32 = gmsh.model.geo.addLine(p24, p21)

    if dxy != 0:
        # Linhas dos quadrado externo superior com quadrado interno
        l33 = gmsh.model.geo.addLine(p17, p5)
        l34 = gmsh.model.geo.addLine(p18, p6)
        l35 = gmsh.model.geo.addLine(p19, p7)
        l36 = gmsh.model.geo.addLine(p20, p8)
        # Linhas do quadrado interno superior
        l41 = gmsh.model.geo.addLine(p5, p6)
        l42 = gmsh.model.geo.addLine(p6, p7)
        l43 = gmsh.model.geo.addLine(p7, p8)
        l44 = gmsh.model.geo.addLine(p8, p5)
        # l41 = l5
        # l42 = l6
        # l43 = l7
        # l44 = l8

    
    # Linhas que ligam quadrado superior com inferior:
    l37 = gmsh.model.geo.addLine(p17, p21)
    l38 = gmsh.model.geo.addLine(p18, p22)
    l39 = gmsh.model.geo.addLine(p19, p23)
    l40 = gmsh.model.geo.addLine(p20, p24)
    
    
    if dxy != 0:
    # Curvas superiores:
        ## Baixo-cima
        c10 = gmsh.model.geo.addCurveLoop([l41,-l34,-l25,l33])
        ## Direita-cima
        c11 = gmsh.model.geo.addCurveLoop([l42,-l35,-l26,l34])
        ## Cima-cima
        c12 = gmsh.model.geo.addCurveLoop([l43,-l36,-l27,l35])
        ## Esquerda-cima
        c13 = gmsh.model.geo.addCurveLoop([l44,-l33,-l28,l36])
    
    # Curvas laterais
    ## Baixo-meio
    c14 = gmsh.model.geo.addCurveLoop([-l32,-l40,l28,l37])
    ## Direita-meio
    c15 = gmsh.model.geo.addCurveLoop([-l31,-l39,l27,l40])
    ## Cima-meio
    c16 = gmsh.model.geo.addCurveLoop([-l30,-l38,l26,l39])
    ## Esquerda-meio
    c17 = gmsh.model.geo.addCurveLoop([-l29,-l37,l25,l38])

    # Curva inferior
    ## Tudo-baixo
    c18 = gmsh.model.geo.addCurveLoop([l29,l30,l31,l32])

    if dxy !=0:
        # Superfícies superiores
        s10 = gmsh.model.geo.addPlaneSurface([c10])
        s11 = gmsh.model.geo.addPlaneSurface([c11])
        s12 = gmsh.model.geo.addPlaneSurface([c12])
        s13 = gmsh.model.geo.addPlaneSurface([c13])
    
    # Superfícies laterais e inferiores
    s14 = gmsh.model.geo.addPlaneSurface([c14])
    s15 = gmsh.model.geo.addPlaneSurface([c15])
    s16 = gmsh.model.geo.addPlaneSurface([c16])
    s17 = gmsh.model.geo.addPlaneSurface([c17])
    s18 = gmsh.model.geo.addPlaneSurface([c18])

    # Linhas quadrado externo superior:
    gmsh.model.geo.mesh.setTransfiniteCurve(l25, nexy+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l26, nexy+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l27, nexy+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l28, nexy+1)

    # Linhas quadrado externo inferior: 
    gmsh.model.geo.mesh.setTransfiniteCurve(l29, nexy+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l30, nexy+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l31, nexy+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l32, nexy+1)

    # Linhas que ligam quadrado superior com inferior:
    gmsh.model.geo.mesh.setTransfiniteCurve(l37, nez+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l38, nez+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l39, nez+1)
    gmsh.model.geo.mesh.setTransfiniteCurve(l40, nez+1)
    

    if dxy !=0:
        # Linhas dos quadrado externo superior com quadrado interno
        gmsh.model.geo.mesh.setTransfiniteCurve(l33, nes+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l34, nes+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l35, nes+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l36, nes+1)

        # Linhas do quadrado interno superior
        gmsh.model.geo.mesh.setTransfiniteCurve(l41, nexy+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l42, nexy+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l43, nexy+1)
        gmsh.model.geo.mesh.setTransfiniteCurve(l44, nexy+1)



    if dxy !=0:
        gmsh.model.geo.mesh.setTransfiniteSurface(s10)
        gmsh.model.geo.mesh.setTransfiniteSurface(s11)
        gmsh.model.geo.mesh.setTransfiniteSurface(s12)
        gmsh.model.geo.mesh.setTransfiniteSurface(s13)
    gmsh.model.geo.mesh.setTransfiniteSurface(s14)
    gmsh.model.geo.mesh.setTransfiniteSurface(s15)
    gmsh.model.geo.mesh.setTransfiniteSurface(s16)
    gmsh.model.geo.mesh.setTransfiniteSurface(s17)
    gmsh.model.geo.mesh.setTransfiniteSurface(s18)

    if dxy !=0:
        gmsh.model.geo.mesh.setRecombine(2, s10)
        gmsh.model.geo.mesh.setRecombine(2, s11)
        gmsh.model.geo.mesh.setRecombine(2, s12)
        gmsh.model.geo.mesh.setRecombine(2, s13)
    gmsh.model.geo.mesh.setRecombine(2, s14)
    gmsh.model.geo.mesh.setRecombine(2, s15)
    gmsh.model.geo.mesh.setRecombine(2, s16)
    gmsh.model.geo.mesh.setRecombine(2, s17)
    gmsh.model.geo.mesh.setRecombine(2, s18)


    if dxy != 0:
        return s1,s2,s3,s4,s5,s10,s11,s12,s13,s14,s15,s16,s17,s18
    else:
        return s1,s2,s3,s4,s5,s14,s15,s16,s17,s18

