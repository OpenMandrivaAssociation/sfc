%define name	sfc
%define version	0.016
%define release %mkrel 6

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
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%name.desktop
[Desktop Entry]
Type=Application
Exec=Audio;
Icon=sound_section
Name=SoundFontCombi
Comment=MIDI event mixer
Categories=AudioVideo;Player;Audio;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc  AUTHORS ChangeLog README COPYING
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/mandriva-%name.desktop

