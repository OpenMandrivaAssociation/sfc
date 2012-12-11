Name:		sfc
Summary:	SoundFontCombi - ALSA MIDI event mixer
Version:	0.018
Release:	1
License:	GPLv2
Group:		Sound
URL:		http://personal.telefonica.terra.es/web/soudfontcombi
Source:		%{name}-%{version}.tar.gz
BuildRequires:	fltk-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(x11)

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
%makeinstall_std

#menu
mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=Audio;
Icon=sound_section
Name=SoundFontCombi
Comment=MIDI event mixer
Categories=AudioVideo;Player;Audio;
EOF

%files
%doc AUTHORS ChangeLog README COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop

