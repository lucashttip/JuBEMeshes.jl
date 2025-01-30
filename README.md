# JuBEMeshes

[![Stable](https://img.shields.io/badge/docs-stable-blue.svg)](https://lucashttip.github.io/JuBEMeshes.jl/stable/)
[![Dev](https://img.shields.io/badge/docs-dev-blue.svg)](https://lucashttip.github.io/JuBEMeshes.jl/dev/)
[![Build Status](https://github.com/lucashttip/JuBEMeshes.jl/actions/workflows/CI.yml/badge.svg?branch=main)](https://github.com/lucashttip/JuBEMeshes.jl/actions/workflows/CI.yml?query=branch%3Amain)
[![Coverage](https://codecov.io/gh/lucashttip/JuBEMeshes.jl/branch/main/graph/badge.svg)](https://codecov.io/gh/lucashttip/JuBEMeshes.jl)


JuBEMeshes.jl is an auxiliary module for JuBEM.jl that helps generate mesh files for specific problems currently being studies.

JuBEMeshes uses the [Gmsh.jl](https://github.com/JuliaFEM/Gmsh.jl) API to generate meshes using [Gmsh](https://gmsh.info/).

To install JuBEMeshes to run on your local julia run the following command:

```julia
] dev https://github.com/lucashttip/JuBEMeshes.jl
```

# Function reference

Functions currently available are described below.

## Simple bar

```julia
homog_bar(;ne1=4, ne2=8, lx=10, ly=1, lz=1, elementOrder=1, popup=true)
```

```julia
multi_bar(ne1 = 1, ne2 = 10,lx1 = 5, lx2 = 5,popup=true)
```

```julia
make_mesh_SSI_layer(a=1.0,fl=2.0,fs=8.0,nf=4,h=6;popup=true,nee = 4)
```

```julia
make_mesh_SSI_singleLayer(a=1.0,fl=2.0,fs=8.0,nf=4,ns2 = 16,h=4;popup=true,nee = 4)
```