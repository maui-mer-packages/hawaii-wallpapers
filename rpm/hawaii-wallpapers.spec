Name:       hawaii-wallpapers
Summary:    Wallpapers for the Hawaii desktop environment
Version:    0.2.0
Release:    1
License:    CC-BY-SA, CC-BY, CC0
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  cmake


%description
Collection of wallpapers shipped with the Hawaii desktop environment.


%prep
%setup -q -n %{name}-%{version}/upstream


%build
%cmake . \
    -DCMAKE_INSTALL_PREFIX=/usr
make %{?jobs:-j%jobs}


%install
rm -rf %{buildroot}
%make_install


%files
%defattr(-,root,root,-)
%{_datadir}/backgrounds/hawaii/16.jpg
%{_datadir}/backgrounds/hawaii/3.jpg
%{_datadir}/backgrounds/hawaii/Also_Calm.png
%{_datadir}/backgrounds/hawaii/Arancio.jpg
%{_datadir}/backgrounds/hawaii/Crane_Beach.jpg
%{_datadir}/backgrounds/hawaii/Grass.jpg
%{_datadir}/backgrounds/hawaii/Halfway_Gone.jpg
%{_datadir}/backgrounds/hawaii/Hawaii-blue.jpg
%{_datadir}/backgrounds/hawaii/Lighthouse_Cork.jpg
%{_datadir}/backgrounds/hawaii/Springlight.jpg
