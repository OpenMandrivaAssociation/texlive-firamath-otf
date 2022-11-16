Name:		texlive-firamath-otf
Version:	50732
Release:	1
Summary:	Use OpenType math font Fira Math
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/firamath-otf
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/firamath-otf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/firamath-otf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers XeTeX/LuaTeX support for the Sans Serif
OpenType Fira Math Font.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/firamath-otf
%doc %{_texmfdistdir}/doc/fonts/firamath-otf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
