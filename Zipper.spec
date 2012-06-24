Summary:	File archive viewer application for GNUstep
Summary(pl.UTF-8):   Przeglądarka plików archiwów dla GNUstepa
Name:		Zipper
Version:	1.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://xanthippe.dyndns.org/Zipper/%{name}-%{version}.tar.gz
# Source0-md5:	db9d9e88bd71fce128890adfd01b70c6
Patch0:		%{name}-initwitharguments.patch
URL:		http://xanthippe.dyndns.org/Zipper/
BuildRequires:	Renaissance-devel
BuildRequires:	gnustep-gui-devel >= 0.9.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/%{_lib}/GNUstep

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%(echo %{_target_cpu} | sed -e 's/amd64/x86_64/;s/ppc/powerpc/')
%endif

%description
Zipper is a tool for inspecting the contents of a compressed archive
and for extracting.

I know that there's a GNUstep port of the famous OpenUp application
but I must admit that for a living I have to use Windoze at work.
After a while I got quite used to Winzip's UI. Although I don't like
some of its features, what I really like is the content listing of an
archive without actually having to unpack it. This is what Zipper
currently tries to mimic. This has also the advantage that you don't
have to unpack archives from networked volumes to your local disk just
to view what's in it.

%description -l pl.UTF-8
Zipper to narzędzie do oglądania zawartości i rozpakowywania
skompresowanych archiwów.

Autor jest świadom istnienia GNUstepowego portu słynnej aplikacji
OpenUp, ale jako że w pracy musi używać Windows, przyzwyczaił się do
interfejsu Winzipa. Mimo że nie lubi niektórych jego cech, podoba mu
się sposób wyświetlania zawartości archiwów bez potrzeby
rozpakowywania ich. Właśnie to próbuje naśladować Zipper. Ma także tę
zaletę, że nie trzeba rozpakowywać archiwów z woluminów sieciowych na
dysk lokalny tylko w celu sprawdzenia co jest w środku.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
. %{_prefix}/System/Library/Makefiles/GNUstep.sh
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_prefix}/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_prefix}/System

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%dir %{_prefix}/System/Applications/Zipper.app
%attr(755,root,root) %{_prefix}/System/Applications/Zipper.app/Zipper
%dir %{_prefix}/System/Applications/Zipper.app/Resources
%{_prefix}/System/Applications/Zipper.app/Resources/*.desktop
%{_prefix}/System/Applications/Zipper.app/Resources/*.plist
%{_prefix}/System/Applications/Zipper.app/Resources/*.tiff
%{_prefix}/System/Applications/Zipper.app/Resources/*.gsmarkup
%dir %{_prefix}/System/Applications/Zipper.app/%{gscpu}
%dir %{_prefix}/System/Applications/Zipper.app/%{gscpu}/%{gsos}
%dir %{_prefix}/System/Applications/Zipper.app/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{_prefix}/System/Applications/Zipper.app/%{gscpu}/%{gsos}/%{libcombo}/Zipper
%{_prefix}/System/Applications/Zipper.app/%{gscpu}/%{gsos}/%{libcombo}/*.openapp
