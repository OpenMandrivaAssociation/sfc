%define name	sfc
%define version	0.016
%define release 2mdk

Name: 	 	%{name}
Summary: 	SoundFontCombi - ALSA MIDI event mixer
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://personal.telefonica.terra.es/web/soudfontcombi
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	fltk-devel libalsa-devel

%description
SoudFontCombi uses the ALSA sequencer to route MIDI events. You have 8 parts
and 2 MIDI ports, and you can produce combinations of sounds like some fancy
synthetizers.

%prep
%setup -q

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="sound_section.png" needs="x11" title="SoundFontCombi" longtitle="MIDI event mixer" section="Multimedia/Sound"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files
%defattr(-,root,root)
%doc  AUTHORS ChangeLog README COPYING
%{_bindir}/%name
%{_datadir}/%name
%{_menudir}/%name

