Summary:	MYuppy TrueType font
Name:		fonts-ttf-myuppy
Version:	1.0.0
Release:	%mkrel 2
License:	Eclipse Public Licence 1.0
URL:		http://developer.symbian.org/
Group:		System/Fonts/True type
Source0:	http://developer.symbian.org/xref/epl/raw/Symbian3/sf/os/textandloc/fontservices/referencefonts/truetype/myuppygb-medium.ttf
Source1:	http://developer.symbian.org/xref/epl/raw/Symbian3/sf/os/textandloc/fontservices/referencefonts/truetype/myuppygb-medium_readme.txt
BuildArch:	noarch
BuildRequires: fontconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
MYuppyGB-Medium

Format - TTF TrueType
Character set - GB2312
Encoding - Unicode

This font was designed to appeal to young urban professionals, Monotype
Yuppy is a newly designed typeface with a unique, modern feel. The
design combines elements of handwriting with classic letterform
characteristics, such as open shapes and proper proportions that help
the typeface retain legibility.

%prep
%setup -Tc
cp %{SOURCE1} .

%install
rm -fr %buildroot
mkdir -p %buildroot/%{_datadir}/fonts/TTF/myuppy
install -m 644 %{SOURCE0} %buildroot/%{_datadir}/fonts/TTF/myuppy

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/myuppy \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-myuppy:pri=50

%clean
rm -fr %buildroot

%files
%defattr(-,root,root,0755)
%doc *.txt
%dir %_datadir/fonts/TTF/myuppy/
%_datadir/fonts/TTF/myuppy/*.ttf
%_sysconfdir/X11/fontpath.d/ttf-myuppy:pri=50
