%global tl_name firamath-otf
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.03b
Release:	%{tl_revision}.1
Summary:	Use OpenType math font Fira Math
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/firamath-otf
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/firamath-otf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/firamath-otf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(firamath)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers XeTeX/LuaTeX support for the Sans Serif OpenType Fira
Math Font.

