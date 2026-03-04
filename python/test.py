import gmsh

gmsh.initialize()

gmsh.model.add("SoilFoundationEmbedd")


fl = 2.0
fs = 10.0
dz = 1.0
a = 1.0

c = 0.5

# Making SOIL
p1b = gmsh.model.geo.addPoint(-fl*a/2.0, -fl*a/2.0, dz,c)
p2b = gmsh.model.geo.addPoint(fl*a/2.0, -fl*a/2.0, dz,c)
p3b = gmsh.model.geo.addPoint(fl*a/2.0, fl*a/2.0, dz,c)
p4b = gmsh.model.geo.addPoint(-fl*a/2.0, fl*a/2.0, dz,c)

p1c = gmsh.model.geo.addPoint(-fl*a/2.0, -fl*a/2.0, 0,c)
p2c = gmsh.model.geo.addPoint(fl*a/2.0, -fl*a/2.0, 0,c)
p3c = gmsh.model.geo.addPoint(fl*a/2.0, fl*a/2.0, 0,c)
p4c = gmsh.model.geo.addPoint(-fl*a/2.0, fl*a/2.0, 0,c)

p5 = gmsh.model.geo.addPoint(-fs*a/2.0, -fs*a/2.0, 0)
p6 = gmsh.model.geo.addPoint(fs*a/2.0, -fs*a/2.0, 0)
p7 = gmsh.model.geo.addPoint(fs*a/2.0, fs*a/2.0, 0)
p8 = gmsh.model.geo.addPoint(-fs*a/2.0, fs*a/2.0, 0)



l1b = gmsh.model.geo.addLine(p1b, p2b)
l2b = gmsh.model.geo.addLine(p2b, p3b)
l3b = gmsh.model.geo.addLine(p3b, p4b)
l4b = gmsh.model.geo.addLine(p4b, p1b)


l1c = gmsh.model.geo.addLine(p1c, p2c)
l2c = gmsh.model.geo.addLine(p2c, p3c)
l3c = gmsh.model.geo.addLine(p3c, p4c)
l4c = gmsh.model.geo.addLine(p4c, p1c)

l1cb = gmsh.model.geo.addLine(p1b, p1c)
l2cb = gmsh.model.geo.addLine(p2b, p2c)
l3cb = gmsh.model.geo.addLine(p3b, p3c)
l4cb = gmsh.model.geo.addLine(p4b, p4c)


l5 = gmsh.model.geo.addLine(p5,p6)
l6 = gmsh.model.geo.addLine(p6,p7)
l7 = gmsh.model.geo.addLine(p7,p8)
l8 = gmsh.model.geo.addLine(p8,p5)


c1 = gmsh.model.geo.addCurveLoop([-l4b,-l3b,-l2b,-l1b])
c1cb = gmsh.model.geo.addCurveLoop([l1b,l2cb,-l1c,-l1cb])
c2cb = gmsh.model.geo.addCurveLoop([l2b,l3cb,-l2c,-l2cb])
c3cb = gmsh.model.geo.addCurveLoop([l3b,l4cb,-l3c,-l3cb])
c4cb = gmsh.model.geo.addCurveLoop([l4b,l1cb,-l4c,-l4cb])
c1c = gmsh.model.geo.addCurveLoop([l1c,l2c,l3c,l4c])
c2 = gmsh.model.geo.addCurveLoop([-l8,-l7,-l6,-l5])

s1 = gmsh.model.geo.addPlaneSurface([c1])
s1cb = gmsh.model.geo.addPlaneSurface([c1cb])
s2cb = gmsh.model.geo.addPlaneSurface([c2cb])
s3cb = gmsh.model.geo.addPlaneSurface([c3cb])
s4cb = gmsh.model.geo.addPlaneSurface([c4cb])
s1c = gmsh.model.geo.addPlaneSurface([c2,-c1c])

gmsh.model.geo.mesh.setTransfiniteSurface(s1)
gmsh.model.geo.mesh.setTransfiniteSurface(s1cb)
gmsh.model.geo.mesh.setTransfiniteSurface(s2cb)
gmsh.model.geo.mesh.setTransfiniteSurface(s3cb)
gmsh.model.geo.mesh.setTransfiniteSurface(s4cb)
# gmsh.model.geo.mesh.setTransfiniteSurface(s1c)


gmsh.model.geo.mesh.setRecombine(2, s1)
gmsh.model.geo.mesh.setRecombine(2, s1cb)
gmsh.model.geo.mesh.setRecombine(2, s2cb)
gmsh.model.geo.mesh.setRecombine(2, s3cb)
gmsh.model.geo.mesh.setRecombine(2, s4cb)
gmsh.model.geo.mesh.setRecombine(2, s1c)


dxy = 2
dz = 5


## Pontos quadrado externo:
p17 = gmsh.model.geo.addPoint(-fs*a/2.0 - dxy, -fs*a/2.0 - dxy, 0,2.0)
p18 = gmsh.model.geo.addPoint(fs*a/2.0 + dxy, -fs*a/2.0 - dxy, 0,2.0)
p19 = gmsh.model.geo.addPoint(fs*a/2.0 + dxy, fs*a/2.0 + dxy, 0,2.0)
p20 = gmsh.model.geo.addPoint(-fs*a/2.0 - dxy, fs*a/2.0 + dxy, 0,2.0)


# Pontos inferiores
p21 = gmsh.model.geo.addPoint(-fs*a/2.0 - dxy, -fs*a/2.0 - dxy, 0 + dz,2.0)
p22 = gmsh.model.geo.addPoint(fs*a/2.0 + dxy, -fs*a/2.0 - dxy, 0 + dz,2.0)
p23 = gmsh.model.geo.addPoint(fs*a/2.0 + dxy, fs*a/2.0 + dxy, 0 + dz,2.0)
p24 = gmsh.model.geo.addPoint(-fs*a/2.0 - dxy, fs*a/2.0 + dxy, 0 + dz,2.0)

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


# # Linhas que ligam quadrado superior com inferior:
l33 = gmsh.model.geo.addLine(p17, p21)
l34 = gmsh.model.geo.addLine(p18, p22)
l35 = gmsh.model.geo.addLine(p19, p23)
l36 = gmsh.model.geo.addLine(p20, p24)


cee_cima = gmsh.model.geo.addCurveLoop([-l28,-l27,-l26,-l25])
c1ee = gmsh.model.geo.addCurveLoop([l25,l34,-l29,-l33])
c2ee = gmsh.model.geo.addCurveLoop([l26,l35,-l30,-l34])
c3ee = gmsh.model.geo.addCurveLoop([l27,l36,-l31,-l35])
c4ee = gmsh.model.geo.addCurveLoop([l28,l33,-l32,-l36])
cee_baixo = gmsh.model.geo.addCurveLoop([l29,l30,l31,l32])


see_cima = gmsh.model.geo.addPlaneSurface([cee_cima,-c2])
see1 = gmsh.model.geo.addPlaneSurface([c1ee])
see2 = gmsh.model.geo.addPlaneSurface([c2ee])
see3 = gmsh.model.geo.addPlaneSurface([c3ee])
see4 = gmsh.model.geo.addPlaneSurface([c4ee])
see_baixo = gmsh.model.geo.addPlaneSurface([cee_baixo])

gmsh.model.geo.mesh.setRecombine(2, see_cima)
gmsh.model.geo.mesh.setRecombine(2, see1)
gmsh.model.geo.mesh.setRecombine(2, see2)
gmsh.model.geo.mesh.setRecombine(2, see3)
gmsh.model.geo.mesh.setRecombine(2, see4)
gmsh.model.geo.mesh.setRecombine(2, see_baixo)



pf = gmsh.model.addPhysicalGroup(2, [s1, s1cb, s2cb, s3cb, s4cb])
gmsh.model.setPhysicalName(2, pf, "rb 0.0 rb 0.0 rb 0.0 1")
ps = gmsh.model.addPhysicalGroup(2, [s1c])
gmsh.model.setPhysicalName(2, ps, "t 0.0 t 0.0 t 0.0 1")
ee = gmsh.model.addPhysicalGroup(2, [see_cima, see1, see2,see3,see4,see_baixo])
gmsh.model.setPhysicalName(2, ee, "ee 0.0 ee 0.0 ee 0.0 1")

gmsh.model.geo.synchronize()
gmsh.model.mesh.generate(2)
# gmsh.model.mesh.setOrder(elementOrder)

# gmsh.option.setNumber("Mesh.SaveAll", 1)

filename_msh = "mesh.msh"
gmsh.write(filename_msh)

filename_vtk = "mesh.vtk"
gmsh.write(filename_vtk)



gmsh.model.geo.synchronize()
gmsh.fltk.run()

gmsh.finalize()