Name:		texlive-ascii
Version:	2.0
Release:	1
Summary:	Support for IBM "standard ASCII" font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/ascii
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ascii.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ascii.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ascii.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package makes available the graphical representation of
the ASCII characters as defined in the IBM PC Code Page 437 C0
Graphics. A Type 1 font of the glyphs is included.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/ascii/ascii.map
%{_texmfdistdir}/fonts/tfm/public/ascii/ASCII.tfm
%{_texmfdistdir}/fonts/type1/public/ascii/ASCII.pfb
%{_texmfdistdir}/tex/latex/ascii/ascii.sty
%doc %{_texmfdistdir}/doc/fonts/ascii/ascii2006.pdf
%doc %{_texmfdistdir}/doc/fonts/ascii/asciisty1994.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ascii/ascii.dtx
%doc %{_texmfdistdir}/source/latex/ascii/ascii.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
