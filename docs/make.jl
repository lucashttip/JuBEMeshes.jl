using JuBEMeshes
using Documenter

DocMeta.setdocmeta!(JuBEMeshes, :DocTestSetup, :(using JuBEMeshes); recursive=true)

makedocs(;
    modules=[JuBEMeshes],
    authors="Lucas Pacheco",
    sitename="JuBEMeshes.jl",
    format=Documenter.HTML(;
        canonical="https://lucashttip.github.io/JuBEMeshes.jl",
        edit_link="main",
        assets=String[],
    ),
    pages=[
        "Home" => "index.md",
    ],
)

deploydocs(;
    repo="github.com/lucashttip/JuBEMeshes.jl",
    devbranch="main",
)
