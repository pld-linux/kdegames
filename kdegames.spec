Summary:	K Desktop Environment - games 
Summary(pl):	K Desktop Environment - gry
Name:		kdegames
Version:	1.1.2
Release:	2
Vendor:		The KDE Team
Copyright:	GPL
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/source/%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs-devel = %{version}
BuildRequires:	libstdc++-devel
BuildRequires:	qt-devel >= 1.40
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
Requires:	qt >= 1.40
Requires:	kdelibs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6

%description
KDE games: KAbalone, KAsteroids, KBlackbox, KMahjongg, KMines,
Konquest, KPat, KPoker, KReversi, KSame, KShisen, KSirtet, KSmiletris,
KSnake and KSokoban.

%description -l pl
Gry KDE: KAbalone, KAsteroids, KBlackbox, KMahjongg, KMines,
Konquest, KPat, KPoker, KReversi, KSame, KShisen, KSirtet, KSmiletris,
KSnake i KSokoban.

%package kabalone
Summary:	KDE game
Summary(pl):	Gra KDE
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 1.40
Requires:	kdelibs = %{version}

%description kabalone
KAbalone is a game like Reversi. You play against the computer on a
board. For rules look at the HTML manual.

%description kabalone -l pl
KAbalone to gra podobna do Reversi.
Zasady znajdziesz w dokumentacji.

%package kasteroids
Summary:	KDE Asteroids clone	
Summary(pl):	Klon Asterids dla KDE
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 1.40
Requires:	kdelibs = %{version}

%description kasteroids
Asteroids clone for KDE

%description kasteroids -l pl
Klon znanej gry "Asteroids".

%package kblackbox
Summary:	A little logical game for KDE	
Summary(pl):	Prosta gra logiczna
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 1.40
Requires:	kdelibs = %{version}

%description kblackbox
A little logical game for KDE.

%description kblackbox -l pl
Prosta gra logiczna.

%package kmahjongg
Summary:	KDE Mahjongg clone	
Summary(pl):	Klon gry Mahjongg dla KDE
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 1.40
Requires:	kdelibs = %{version}

%description kmahjongg
This program is a clone of the well known Mahjongg game.

%description kmahjongg -l pl
Wersja KDE znanej gry Mahjongg

%package kmines 
Summary:	KDE minesweeper game
Summary(pl):	Saper dla KDE
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 1.40
Requires:	kdelibs = %{version}

%description kmines
This is a very classical minesweeper written from scratch.
- 3 predefined levels :
  Easy : 8x8 with 10 mines
  Normal : 16x16 with 40 mines
  Expert : 30x16 with 99 mines
- Custom levels
- High Scores

%description kmines -l pl
Wersja znanej gry "saper" dla KDE

%package konquest
Summary:	KDE version of Gnu-Lactic Konquest
Summary(pl):	Podb�j galaktyki
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 1.40
Requires:	kdelibs = %{version} 

%description konquest
KDE version of Gnu-Lactic Konquest.

%description konquest -l pl
Podb�j galaktyki.

%package kpat
Summary:	KDE solitaire patience game	
Summary(pl):	Pasjanse KDE
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 1.40
Requires:	kdelibs = %{version} 

%description kpat
KDE solitaire patience games.

%description kpat -l pl
Program umo�liwia uk�adanie kilku rodzaj�w pasjans�w.

%package kpoker
Summary:	KDE poker	
Summary(pl):	Poker KDE
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 1.40
Requires:	kdelibs = %{version} 

%description kpoker
A simple video poker clone for the KDE desktop environment.

%description kpoker -l pl
Prosy poker dla KDE.

%package kreversi
Summary:	KDE Reversi game	
Summary(pl):	Gra Reversi dla KDE
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 1.40
Requires:	kdelibs = %{version} 

%description kreversi
Reversi is a simple strategy game that is played by two players. There
is only one type of piece - one side of it is black, the other white.
If a player captures a piece on the board, that piece is turned and
belongs to that player. The winner is the person that has more pieces
of his own color on the board and if there are no more moves possible.

%description kreversi -l pl
Reversi to prosta gra strategiczna dla dw�ch graczy.

%package ksame
Summary:	KDE SameGame	
Summary(pl):	"To Samo" dla KDE
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 1.40
Requires:	kdelibs = %{version} 

%description ksame
KSame is a simple game. It's played by one player, so there is only
one winner :-) You play for fun and against the highscore. It has been
inspired by SameGame, that is only famous on the Macintosh plattform.

%description ksame -l pl
KSame to prosta gra dla jednego gracza.

%package kshisen
Summary:	KDE Shisen-Sho	
Summary(pl):	Shisen-Sho dla KDE
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 1.40
Requires:	kdelibs = %{version} 

%description kshisen
Shisen-Sho is similiar to Mahjongg and uses the same set of tiles as
Mahjongg.

%description kshisen -l pl
Shisen-Sho to gra podobna do Mahjongg i wykorzystuj�ca ten sam zestaw ko�ci.

%package ksirtet
Summary:	KDE Tetris	
Summary(pl):	Tetris dla KDE
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 1.40
Requires:	kdelibs = %{version} 

%description ksirtet
This program is a clone of the well-known game Tetris.

%description ksirtet -l pl
Kolejny klon dobrze znanego Tetrisa.

%package ksmiletris
Summary:	KDE Tetris	
Summary(pl):	Tetris dla KDE
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 1.40
Requires:	kdelibs = %{version} 

%description ksmiletris
This program is a clone of the well-known game Tetris.

%description ksmiletris -l pl
Kolejny klon dobrze znanego Tetrisa.

%package ksnake
Summary:	KDE Snake Race	
Summary(pl):	Wy�cig W�y dla KDE
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 1.40
Requires:	kdelibs = %{version} 

%description ksnake
Snake Race is a game of speed and agility. You are a hungry snake and
are trying to eat all the apples in the room before getting out!

%description ksnake -l pl
Snake Race to gra szybko�ciowo-zr�czno�ciowa. Wcielasz sie w g�odnego
w�a pr�buj�cego zje�� wszystkie jab�ka w pomieszczeniu.

%package ksokoban
Summary:	KDE Sokoban	
Summary(pl):	Sokoban dla KDE
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 1.40
Requires:	kdelibs = %{version} 

%description ksokoban
The japanese warehouse keeper game.

%description ksokoban -l pl
Gra japo�skiego magazyniera.

%prep
%setup -q

%build
export KDEDIR=%{_prefix}
CXXFLAGS="$RPM_OPT_FLAGS -Wall -fno-rtti" \
CFLAGS="$RPM_OPT_FLAGS -Wall" \
LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=$KDEDIR \
 	--with-install-root=$RPM_BUILD_ROOT \
	--with-qt-dir=%{_prefix} \
 	--with-pam="yes"
%{__make} KDEDIR=$KDEDIR

%install
rm -rf $RPM_BUILD_ROOT

export KDEDIR=%{_prefix}
%{__make} RUN_KAPPFINDER=no prefix=$RPM_BUILD_ROOT$KDEDIR install

install -d $RPM_BUILD_ROOT/var/lib/games/ksnake/
touch $RPM_BUILD_ROOT/var/lib/games/ksnake/highScores

%find_lang kabalone
%find_lang kasteroids
%find_lang kblackbox
%find_lang kmahjongg
%find_lang kmines
%find_lang konquest
%find_lang kpat
%find_lang kpoker
%find_lang kreversi
%find_lang ksame
%find_lang kshisen
%find_lang ksirtet
%find_lang ksmiletris
%find_lang ksnake
%find_lang ksokoban

%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             KABALONE
#################################################

%files -f kabalone.lang kabalone 
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Games/kabalone.kdelnk
%attr(755,root,root) /usr/X11R6/bin/kabalone
%lang(de) %{_datadir}/kde/doc/HTML/de/kabalone/
%lang(en) %{_datadir}/kde/doc/HTML/en/kabalone/
%lang(fr) %{_datadir}/kde/doc/HTML/fr/kabalone/
%{_datadir}/kde/apps/kabalone/
%{_datadir}/kde/icons/kabalone.xpm
%{_datadir}/kde/icons/mini/kabalone.xpm

#################################################
#             KASTEROIDS 
#################################################

%files -f kasteroids.lang kasteroids 
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/kasteroids
%config(missingok) /etc/X11/kde/applnk/Games/kasteroids.kdelnk
%lang(en) %{_datadir}/kde/doc/HTML/en/kasteroids/
%{_datadir}/kde/apps/kasteroids/
%{_datadir}/kde/icons/mini/kasteroids.xpm
%{_datadir}/kde/icons/kasteroids.xpm

#################################################
#             KBLACKBOX 
#################################################

%files -f kblackbox.lang kblackbox
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/kblackbox
%config(missingok) /etc/X11/kde/applnk/Games/kblackbox.kdelnk
%lang(en) %{_datadir}/kde/doc/HTML/en/kblackbox/
%{_datadir}/kde/apps/kblackbox/
%{_datadir}/kde/icons/mini/kblackbox.xpm
%{_datadir}/kde/icons/kblackbox.xpm

#################################################
#             KMAHJONGG
#################################################

%files -f kmahjongg.lang kmahjongg
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Games/kmahjongg.kdelnk
%attr(755,root,root) /usr/X11R6/bin/kmahjongg
%lang(en) %{_datadir}/kde/doc/HTML/en/
%{_datadir}/kde/apps/kmahjongg/
%{_datadir}/kde/icons/kmahjongg.xpm
%{_datadir}/kde/icons/mini/kmahjongg.xpm

#################################################
#             KMINES
#################################################

%files -f kmines.lang kmines
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Games/kmines.kdelnk
%attr(755,root,root) /usr/X11R6/bin/kmines
%lang(en) %{_datadir}/kde/doc/HTML/en/kmines/
%{_datadir}/kde/icons/mini/kmines.xpm
%{_datadir}/kde/icons/kmines.xpm

#################################################
#             KONQUEST
#################################################

%files -f konquest.lang konquest
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Games/Konquest.kdelnk
%attr(755,root,root) /usr/X11R6/bin/konquest
%lang(en) %{_datadir}/kde/doc/HTML/en/konquest/
%{_datadir}/kde/apps/konquest/
%{_datadir}/kde/icons/mini/konquest.xpm
%{_datadir}/kde/icons/konquest.xpm

#################################################
#             KPAT
#################################################

%files -f kpat.lang kpat
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Games/kpat.kdelnk
%attr(755,root,root) /usr/X11R6/bin/kpat
%lang(en) %{_datadir}/kde/doc/HTML/en/kpat/
%{_datadir}/kde/apps/kpat/
%{_datadir}/kde/icons/mini/kpat.xpm
%{_datadir}/kde/icons/kpat.xpm
%{_datadir}/kde/icons/kpat-lq.xpm

#################################################
#             KPOKER
#################################################

%files -f kpoker.lang kpoker
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Games/kpoker.kdelnk
%attr(755,root,root) /usr/X11R6/bin/kpoker
%lang(en) %{_datadir}/kde/doc/HTML/en/kpoker/
%{_datadir}/kde/apps/kpoker/
%{_datadir}/kde/icons/mini/kpoker.xpm
%{_datadir}/kde/icons/kpoker.xpm

#################################################
#             KREVERSI
#################################################

%files -f kreversi.lang kreversi
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Games/kreversi.kdelnk
%attr(755,root,root) /usr/X11R6/bin/kreversi
%lang(en) %{_datadir}/kde/doc/HTML/en/kreversi/
%{_datadir}/kde/apps/kreversi/
%{_datadir}/kde/icons/mini/kreversi.xpm
%{_datadir}/kde/icons/kreversi.xpm

#################################################
#            KSAME 
#################################################

%files -f ksame.lang ksame
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Games/ksame.kdelnk
%attr(755,root,root) /usr/X11R6/bin/ksame
%lang(en) %{_datadir}/kde/doc/HTML/en/ksame/
%{_datadir}/kde/apps/ksame/
%{_datadir}/kde/icons/mini/ksame.xpm
%{_datadir}/kde/icons/ksame.xpm

#################################################
#             KSIRTET
#################################################

%files -f ksirtet.lang ksirtet
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Games/ksirtet.kdelnk
%attr(755,root,root) /usr/X11R6/bin/ksirtet
%lang(en) %{_datadir}/kde/doc/HTML/en/ksirtet/
%{_datadir}/kde/icons/mini/ksirtet.xpm
%{_datadir}/kde/icons/ksirtet.xpm

#################################################
#             KSMILETRIS
#################################################

%files -f ksmiletris.lang ksmiletris
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Games/ksmiletris.kdelnk
%attr(755,root,root) /usr/X11R6/bin/ksmiletris
%lang(en) %{_datadir}/kde/doc/HTML/en/ksmiletris/
%{_datadir}/kde/apps/ksmiletris/
%{_datadir}/kde/icons/mini/ksmiletris.xpm
%{_datadir}/kde/icons/ksmiletris.xpm

#################################################
#             KSHISEN
#################################################

%files -f kshisen.lang kshisen
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Games/kshisen.kdelnk
%attr(755,root,root) /usr/X11R6/bin/kshisen
%lang(en) %{_datadir}/kde/doc/HTML/en/kshisen/
%{_datadir}/kde/apps/kshisen/
%{_datadir}/kde/icons/mini/kshisen.xpm
%{_datadir}/kde/icons/kshisen.xpm

#################################################
#             KSNAKE
#################################################

%files -f ksnake.lang ksnake
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Games/ksnake.kdelnk
%attr(4755,root,games) /usr/X11R6/bin/ksnake
%lang(en) %{_datadir}/kde/doc/HTML/en/ksnake/
%{_datadir}/kde/apps/ksnake/
%{_datadir}/kde/icons/mini/ksnake.xpm
%{_datadir}/kde/icons/ksnake.xpm
%attr(664,root,games) %ghost /var/lib/games/ksnake/highScores

#################################################
#             KSOKOBAN
#################################################

%files -f ksokoban.lang ksokoban
%defattr(644,root,root,755)
%config(missingok) /etc/X11/kde/applnk/Games/ksokoban.kdelnk
%attr(755,root,root) /usr/X11R6/bin/ksokoban
%lang(en) %{_datadir}/kde/doc/HTML/en/ksokoban/
%{_datadir}/kde/icons/mini/ksokoban.xpm
%{_datadir}/kde/icons/ksokoban.xpm
