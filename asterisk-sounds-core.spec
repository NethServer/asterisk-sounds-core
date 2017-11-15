#Workaround for 64 bit CPUs
%define _lib lib

Summary: Core Sounds for Asterisk, The Open Source PBX
Name: asterisk-sounds-core
Version: 1.5
Release: 3%{dist}
License: GPL
Group: Utilities/System
Source10: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-core-sounds-en-ulaw-%{version}.tar.gz
Source11: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-core-sounds-en-alaw-%{version}.tar.gz
Source12: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-core-sounds-en-g722-%{version}.tar.gz
Source13: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-core-sounds-en-sln16-%{version}.tar.gz

# Note that en_AU stops 1.4.27
Source21: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-core-sounds-en_AU-ulaw-1.4.27.tar.gz
Source22: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-core-sounds-en_AU-alaw-1.4.27.tar.gz
# No g722 transcode, use sln16 instead
Source23: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-core-sounds-en_AU-sln16-1.4.27.tar.gz

# Español
# Note that es stops 1.4.27, too
Source31: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-core-sounds-es-ulaw-1.4.27.tar.gz
Source32: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-core-sounds-es-alaw-1.4.27.tar.gz
Source33: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-core-sounds-es-g722-1.4.27.tar.gz

# Français
Source41: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-core-sounds-fr-ulaw-%{version}.tar.gz
Source42: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-core-sounds-fr-alaw-%{version}.tar.gz
Source43: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-core-sounds-fr-sln16-%{version}.tar.gz

# Italian
Source51: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-core-sounds-it-ulaw-%{version}.tar.gz
Source52: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-core-sounds-it-alaw-%{version}.tar.gz
Source53: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-core-sounds-it-sln16-%{version}.tar.gz

# Japanese
Source61: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-core-sounds-ja-ulaw-%{version}.tar.gz
Source62: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-core-sounds-ja-alaw-%{version}.tar.gz
Source63: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-core-sounds-ja-sln16-%{version}.tar.gz

# English
Source71: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-core-sounds-en_GB-ulaw-%{version}.tar.gz
Source72: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-core-sounds-en_GB-alaw-%{version}.tar.gz
Source73: http://downloads.digium.com/pub/telephony/sounds/releases/asterisk-core-sounds-en_GB-sln16-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch
URL: http://www.asterisk.org
BuildRequires: wget

%description
Asterisk is an open source PBX and telephony development platform.  Asterisk
can both replace a conventional PBX and act as a platform for the
development of custom telephony applications for the delivery of dynamic
content over a telephone; similar to how one can deliver dynamic content
through a web browser using CGI and a web server.

Asterisk supports a variety of telephony hardware including BRI, PRI, POTS,
and IP telephony clients using the Inter-Asterisk eXchange (IAX) protocol (e.g.
gnophone or miniphone).  For more information and a current list of supported
hardware, see http://www.asterisk.org

%package en-ulaw
Summary: Asterisk core sounds - en - ulaw.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%package en-alaw
Summary: Asterisk core sounds - en - alaw.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%package en-wideband
Summary: Asterisk core sounds - en - High Definition Audio.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%package en_AU-ulaw
Summary: Asterisk core sounds - en_AU - ulaw.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%package en_AU-alaw
Summary: Asterisk core sounds - en_AU - alaw.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%package en_AU-wideband
Summary: Asterisk core sounds - en_AU - High Definition Audio.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%package es-ulaw
Summary: Asterisk core sounds - es - ulaw.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%package es-alaw
Summary: Asterisk core sounds - es - alaw.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%package es-wideband
Summary: Asterisk core sounds - es - High Definition Audio.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%package fr-ulaw
Summary: Asterisk core sounds - fr - ulaw.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%package fr-alaw
Summary: Asterisk core sounds - fr - alaw.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%package fr-wideband
Summary: Asterisk core sounds - fr - High Definition Audio.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%package it-ulaw
Summary: Asterisk core sounds - it - ulaw.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%package it-alaw
Summary: Asterisk core sounds - it - alaw.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%package it-wideband
Summary: Asterisk core sounds - it - High Definition Audio.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%package ja-ulaw
Summary: Asterisk core sounds - ja - ulaw.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%package ja-alaw
Summary: Asterisk core sounds - ja - alaw.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%package ja-wideband
Summary: Asterisk core sounds - ja - High Definition Audio.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%package en_GB-ulaw
Summary: Asterisk core sounds - en_GB - ulaw.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%package en_GB-alaw
Summary: Asterisk core sounds - en_GB - alaw.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%package en_GB-wideband
Summary: Asterisk core sounds - ja - High Definition Audio.
Group: Utilities/System
Provides: %{name} = %{version}-%{release}
Requires(pre): %{_sbindir}/groupadd
Requires(pre): %{_sbindir}/useradd

%description en-ulaw
This package contains Asterisk core sounds - en - ulaw.

%description en-alaw
This package contains Asterisk core sounds - en - alaw.

%description en-wideband
This package contains Asterisk core sounds - en - g722

%description en_AU-ulaw
This package contains Asterisk core sounds - en_AU - ulaw.

%description en_AU-alaw
This package contains Asterisk core sounds - en_AU - alaw.

%description en_AU-wideband
This package contains Asterisk core sounds - en_AU - sln16.

%description es-ulaw
This package contains Asterisk core sounds - es - ulaw.

%description es-alaw
This package contains Asterisk core sounds - es - alaw.

%description es-wideband
This package contains Asterisk core sounds - es - g722.

%description fr-ulaw
This package contains Asterisk core sounds - fr - ulaw.

%description fr-alaw
This package contains Asterisk core sounds - fr - alaw.

%description fr-wideband
This package contains Asterisk core sounds - fr - sln16.

%description ja-ulaw
This package contains Asterisk core sounds - ja - ulaw.

%description ja-alaw
This package contains Asterisk core sounds - ja - alaw.

%description ja-wideband
This package contains Asterisk core sounds - ja - sln16

%description it-ulaw
This package contains Asterisk core sounds - it - ulaw.

%description it-alaw
This package contains Asterisk core sounds - it - alaw.

%description it-wideband
This package contains Asterisk core sounds - it - sln16.

%description en_GB-ulaw
This package contains Asterisk core sounds - en_GB - ulaw.

%description en_GB-alaw
This package contains Asterisk core sounds - en_GB - alaw.

%description en_GB-wideband
This package contains Asterisk core sounds - en_GB - sln16.

%pre en-ulaw
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%pre en-alaw
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%pre en-wideband
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%pre en_AU-ulaw
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%pre en_AU-alaw
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%pre en_AU-wideband
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%pre es-ulaw
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%pre es-alaw
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%pre es-wideband
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%pre fr-ulaw
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%pre fr-alaw
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%pre fr-wideband
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%pre ja-ulaw
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%pre ja-alaw
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%pre ja-wideband
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%pre it-ulaw
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%pre it-alaw
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%pre it-wideband
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%pre en_GB-ulaw
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%pre en_GB-alaw
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%pre en_GB-wideband
%{_sbindir}/groupadd -r asterisk &>/dev/null || :
%{_sbindir}/useradd -r -s /bin/bash -d /home/asterisk -c 'Asterisk User' -g asterisk asterisk &>/dev/null || :

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/var/lib/asterisk/sounds/en/
mkdir -p $RPM_BUILD_ROOT/var/lib/asterisk/sounds/en_AU/
mkdir -p $RPM_BUILD_ROOT/var/lib/asterisk/sounds/es/
mkdir -p $RPM_BUILD_ROOT/var/lib/asterisk/sounds/fr/
mkdir -p $RPM_BUILD_ROOT/var/lib/asterisk/sounds/it/
mkdir -p $RPM_BUILD_ROOT/var/lib/asterisk/sounds/ja/
mkdir -p $RPM_BUILD_ROOT/var/lib/asterisk/sounds/en_GB/

tar xof %SOURCE10 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/en/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-core-sounds-en-ulaw-%{version}

tar xof %SOURCE11 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/en/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-core-sounds-en-alaw-%{version}

tar xof %SOURCE12 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/en/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-core-sounds-en-g722-%{version}

tar xof %SOURCE13 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/en/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-core-sounds-en-sln16-%{version}

tar xof %SOURCE21 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/en_AU/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-core-sounds-en_AU-ulaw-%{version}

tar xof %SOURCE22 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/en_AU/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-core-sounds-en_AU-alaw-%{version}

tar xof %SOURCE23 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/en_AU/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-core-sounds-en_AU-sln16-%{version}

tar xof %SOURCE31 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/es/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-core-sounds-es-ulaw-%{version}

tar xof %SOURCE32 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/es/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-core-sounds-es-alaw-%{version}

tar xof %SOURCE33 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/es/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-core-sounds-es-g722-%{version}

tar xof %SOURCE41 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/fr/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-core-sounds-fr-ulaw-%{version}

tar xof %SOURCE42 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/fr/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-core-sounds-fr-alaw-%{version}

tar xof %SOURCE43 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/fr/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-core-sounds-fr-sln16-%{version}

tar xof %SOURCE51 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/it/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-core-sounds-it-ulaw-%{version}

tar xof %SOURCE52 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/it/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-core-sounds-it-alaw-%{version}

tar xof %SOURCE53 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/it/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-core-sounds-it-sln16-%{version}

tar xof %SOURCE61 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/ja/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-core-sounds-ja-ulaw-%{version}

tar xof %SOURCE62 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/ja/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-core-sounds-ja-alaw-%{version}

tar xof %SOURCE63 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/ja/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-core-sounds-ja-sln16-%{version}

tar xof %SOURCE71 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/en_GB/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-core-sounds-en_GB-ulaw-%{version}

tar xof %SOURCE72 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/en_GB/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-core-sounds-en_GB-alaw-%{version}

tar xof %SOURCE73 -C $RPM_BUILD_ROOT/var/lib/asterisk/sounds/en_GB/
touch $RPM_BUILD_ROOT/var/lib/asterisk/sounds/.asterisk-core-sounds-en_GB-sln16-%{version}

%post

%clean
cd $RPM_BUILD_DIR
%{__rm} -rf %{name}-%{version}
%{__rm} -rf /var/log/%{name}-sources-%{version}-%{release}.make.err
%{__rm} -rf $RPM_BUILD_ROOT

%files en-ulaw
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/*.ulaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/*/*.ulaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/core-sounds-en.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/CHANGES-asterisk-core-en-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/CREDITS-asterisk-core-en-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/LICENSE-asterisk-core-en-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-core-sounds-en-ulaw-%{version}

%files en-alaw
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/*.alaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/*/*.alaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/core-sounds-en.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/CHANGES-asterisk-core-en-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/CREDITS-asterisk-core-en-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/LICENSE-asterisk-core-en-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-core-sounds-en-alaw-%{version}

%files en-wideband
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/*.g722
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/*/*.g722
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/*.sln16
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/*/*.sln16
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/core-sounds-en.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/CHANGES-asterisk-core-en-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/CREDITS-asterisk-core-en-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en/LICENSE-asterisk-core-en-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-core-sounds-en-g722-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-core-sounds-en-sln16-%{version}

%files en_AU-ulaw
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_AU/*.ulaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_AU/*/*.ulaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_AU/core-sounds-en_AU.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_AU/CHANGES-asterisk-core-en_AU-*
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_AU/CREDITS-asterisk-core-en_AU-*
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_AU/LICENSE-asterisk-core-en_AU-*
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-core-sounds-en_AU-ulaw-*

%files en_AU-alaw
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_AU/*.alaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_AU/*/*.alaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_AU/core-sounds-en_AU.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_AU/CHANGES-asterisk-core-en_AU-*
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_AU/CREDITS-asterisk-core-en_AU-*
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_AU/LICENSE-asterisk-core-en_AU-*
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-core-sounds-en_AU-alaw-*

%files en_AU-wideband
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_AU/*.sln16
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_AU/*/*.sln16
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_AU/core-sounds-en_AU.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_AU/CHANGES-asterisk-core-en_AU-*
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_AU/CREDITS-asterisk-core-en_AU-*
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_AU/LICENSE-asterisk-core-en_AU-*
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-core-sounds-en_AU-sln16-*

%files es-ulaw
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/es/*.ulaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/es/*/*.ulaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/es/core-sounds-es.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/es/CHANGES-asterisk-core-es-*
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/es/CREDITS-asterisk-core-es-*
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/es/LICENSE-asterisk-core-es-*
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-core-sounds-es-ulaw-*

%files es-alaw
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/es/*.alaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/es/*/*.alaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/es/core-sounds-es.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/es/CHANGES-asterisk-core-es-*
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/es/CREDITS-asterisk-core-es-*
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/es/LICENSE-asterisk-core-es-*
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-core-sounds-es-alaw-*

%files es-wideband
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/es/*.g722
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/es/*/*.g722
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/es/core-sounds-es.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/es/CHANGES-asterisk-core-es-*
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/es/CREDITS-asterisk-core-es-*
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/es/LICENSE-asterisk-core-es-*
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-core-sounds-es-g722-*

%files fr-ulaw
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/fr/*.ulaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/fr/*/*.ulaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/fr/core-sounds-fr.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/fr/CHANGES-asterisk-core-fr-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/fr/CREDITS-asterisk-core-fr-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/fr/LICENSE-asterisk-core-fr-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-core-sounds-fr-ulaw-%{version}

%files fr-alaw
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/fr/*.alaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/fr/*/*.alaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/fr/core-sounds-fr.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/fr/CHANGES-asterisk-core-fr-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/fr/CREDITS-asterisk-core-fr-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/fr/LICENSE-asterisk-core-fr-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-core-sounds-fr-alaw-%{version}

%files fr-wideband
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/fr/*.sln16
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/fr/*/*.sln16
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/fr/core-sounds-fr.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/fr/CHANGES-asterisk-core-fr-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/fr/CREDITS-asterisk-core-fr-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/fr/LICENSE-asterisk-core-fr-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-core-sounds-fr-sln16-%{version}

%files it-ulaw
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/it/*.ulaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/it/*/*.ulaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/it/core-sounds-it.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/it/CHANGES-asterisk-core-it-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/it/CREDITS-asterisk-core-it-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/it/LICENSE-asterisk-core-it-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-core-sounds-it-ulaw-%{version}

%files it-alaw
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/it/*.alaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/it/*/*.alaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/it/core-sounds-it.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/it/CHANGES-asterisk-core-it-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/it/CREDITS-asterisk-core-it-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/it/LICENSE-asterisk-core-it-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-core-sounds-it-alaw-%{version}

%files it-wideband
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/it/*.sln16
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/it/*/*.sln16
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/it/core-sounds-it.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/it/CHANGES-asterisk-core-it-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/it/CREDITS-asterisk-core-it-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/it/LICENSE-asterisk-core-it-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-core-sounds-it-sln16-%{version}

%files ja-ulaw
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/ja/*.ulaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/ja/*/*.ulaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/ja/core-sounds-ja.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/ja/CHANGES-asterisk-core-ja-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/ja/CREDITS-asterisk-core-ja-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/ja/LICENSE-asterisk-core-ja-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-core-sounds-ja-ulaw-%{version}

%files ja-alaw
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/ja/*.alaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/ja/*/*.alaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/ja/core-sounds-ja.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/ja/CHANGES-asterisk-core-ja-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/ja/CREDITS-asterisk-core-ja-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/ja/LICENSE-asterisk-core-ja-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-core-sounds-ja-alaw-%{version}

%files ja-wideband
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/ja/*.sln16
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/ja/*/*.sln16
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/ja/core-sounds-ja.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/ja/CHANGES-asterisk-core-ja-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/ja/CREDITS-asterisk-core-ja-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/ja/LICENSE-asterisk-core-ja-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-core-sounds-ja-sln16-%{version}

%files en_GB-ulaw
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_GB/*.ulaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_GB/*/*.ulaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_GB/core-sounds-en_GB.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_GB/CHANGES-asterisk-core-en_GB-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_GB/CREDITS-asterisk-core-en_GB-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_GB/LICENSE-asterisk-core-en_GB-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-core-sounds-en_GB-ulaw-%{version}

%files en_GB-alaw
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_GB/*.alaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_GB/*/*.alaw
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_GB/core-sounds-en_GB.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_GB/CHANGES-asterisk-core-en_GB-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_GB/CREDITS-asterisk-core-en_GB-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_GB/LICENSE-asterisk-core-en_GB-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-core-sounds-en_GB-alaw-%{version}

%files en_GB-wideband
%defattr(-, root, root)
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_GB/*.sln16
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_GB/*/*.sln16
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_GB/core-sounds-en_GB.txt
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_GB/CHANGES-asterisk-core-en_GB-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_GB/CREDITS-asterisk-core-en_GB-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/en_GB/LICENSE-asterisk-core-en_GB-%{version}
%attr(0664,asterisk,asterisk) /var/lib/asterisk/sounds/.asterisk-core-sounds-en_GB-sln16-%{version}

%changelog
* Wed Nov 15 2017 Stefano Fancello <stefano.fancello@nethesis.it> 1.5-3
- Create Asterisk home when creating asterisk user
