Summary:	K Desktop Environment - games 
Summary(pl):	K Desktop Environment - gry
Name:		kdegames
Version:	1.1.1
Release:	3
Vendor:		The KDE Team
Copyright:	GPL
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/source/%{name}-%{version}.tar.bz2
Patch:		kdegames.ksnake-highscore.patch
BuildRequires:	kdelibs-devel = %{version}
BuildRequires:	libstdc++-devel
BuildRequires:	qt-devel >= 1.40
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
Requires:	qt >= 1.40
Requires:	kdelibs = %{version}
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6

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
Summary(pl):	Podbój galaktyki
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 1.40
Requires:	kdelibs = %{version} 

%description konquest
KDE version of Gnu-Lactic Konquest.

%description konquest -l pl
Podbój galaktyki.

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
Program umo¿liwia uk³adanie kilku rodzajów pasjansów.

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
Reversi to prosta gra strategiczna dla dwóch graczy.

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
Shisen-Sho to gra podobna do Mahjongg i wykorzystuj±ca ten sam zestaw ko¶ci.

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
Summary(pl):	Wy¶cig Wê¿y dla KDE
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 1.40
Requires:	kdelibs = %{version} 

%description ksnake
Snake Race is a game of speed and agility. You are a hungry snake and
are trying to eat all the apples in the room before getting out!

%description ksnake -l pl
Snake Race to gra szybko¶ciowo-zrêczno¶ciowa. Wcielasz sie w g³odnego
wê¿a próbuj±cego zje¶æ wszystkie jab³ka w pomieszczeniu.

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
Gra japoñskiego magazyniera.

%prep
%setup -q
%patch -p1

%build
export KDEDIR=%{_prefix}
CXXFLAGS="$RPM_OPT_FLAGS -Wall" \
CFLAGS="$RPM_OPT_FLAGS -Wall" \
LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=$KDEDIR \
 	--with-install-root=$RPM_BUILD_ROOT \
 	--with-pam="yes"
make KDEDIR=$KDEDIR

%install
rm -rf $RPM_BUILD_ROOT

export KDEDIR=%{_prefix}
make RUN_KAPPFINDER=no prefix=$RPM_BUILD_ROOT$KDEDIR install

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

%files kabalone -f kabalone.lang 
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Games/kabalone.kdelnk
%attr(755,root,root) %{_bindir}/kabalone

%{_datadir}/kde/doc/HTML/en/kabalone
%lang(de) %{_datadir}/kde/doc/HTML/de/kabalone
%lang(fr) %{_datadir}/kde/doc/HTML/fr/kabalone

%{_datadir}/kde/apps/kabalone
%{_datadir}/kde/icons/kabalone.xpm
%{_datadir}/kde/icons/mini/kabalone.xpm

#################################################
#             KASTEROIDS 
#################################################

%files kasteroids -f kasteroids.lang
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kasteroids
%config(missingok) /etc/X11/kde/applnk/Games/kasteroids.kdelnk

%{_datadir}/kde/doc/HTML/en/kasteroids

%{_datadir}/kde/apps/kasteroids
%{_datadir}/kde/icons/mini/kasteroids.xpm
%{_datadir}/kde/icons/kasteroids.xpm

#################################################
#             KBLACKBOX 
#################################################

%files kblackbox -f kblackbox.lang
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/kblackbox
%config(missingok) /etc/X11/kde/applnk/Games/kblackbox.kdelnk

%{_datadir}/kde/doc/HTML/en/kblackbox

%{_datadir}/kde/apps/kblackbox
%{_datadir}/kde/icons/mini/kblackbox.xpm
%{_datadir}/kde/icons/kblackbox.xpm

#################################################
#             KMAHJONGG
#################################################

%files kmahjongg -f kmahjongg.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Games/kmahjongg.kdelnk
%attr(755,root,root) %{_bindir}/kmahjongg

%{_datadir}/kde/doc/HTML/en/kmahjongg

%{_datadir}/kde/apps/kmahjongg
%{_datadir}/kde/icons/kmahjongg.xpm
%{_datadir}/kde/icons/mini/kmahjongg.xpm

#################################################
#             KMINES
#################################################

%files kmines -f kmines.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Games/kmines.kdelnk
%attr(755,root,root) %{_bindir}/kmines

%{_datadir}/kde/doc/HTML/en/kmines

%{_datadir}/kde/icons/mini/kmines.xpm
%{_datadir}/kde/icons/kmines.xpm

#################################################
#             KONQUEST
#################################################

%files konquest -f konquest.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Games/Konquest.kdelnk
%attr(755,root,root) %{_bindir}/konquest

%{_datadir}/kde/doc/HTML/en/konquest

%{_datadir}/kde/apps/konquest
%{_datadir}/kde/icons/mini/konquest.xpm
%{_datadir}/kde/icons/konquest.xpm

#################################################
#             KPAT
#################################################

%files kpat -f kpat.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Games/kpat.kdelnk
%attr(755,root,root) %{_bindir}/kpat

%{_datadir}/kde/doc/HTML/en/kpat

%{_datadir}/kde/apps/kpat
%{_datadir}/kde/icons/mini/kpat.xpm
%{_datadir}/kde/icons/kpat.xpm
%{_datadir}/kde/icons/kpat-lq.xpm

#################################################
#             KPOKER
#################################################

%files kpoker -f kpoker.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Games/kpoker.kdelnk
%attr(755,root,root) %{_bindir}/kpoker

%{_datadir}/kde/doc/HTML/en/kpoker

%{_datadir}/kde/apps/kpoker
%{_datadir}/kde/icons/mini/kpoker.xpm
%{_datadir}/kde/icons/kpoker.xpm

#################################################
#             KREVERSI
#################################################

%files kreversi -f kreversi.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Games/kreversi.kdelnk
%attr(755,root,root) %{_bindir}/kreversi

%{_datadir}/kde/doc/HTML/en/kreversi

%{_datadir}/kde/apps/kreversi
%{_datadir}/kde/icons/mini/kreversi.xpm
%{_datadir}/kde/icons/kreversi.xpm

#################################################
#            KSAME 
#################################################

%files ksame -f ksame.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Games/ksame.kdelnk
%attr(755,root,root) %{_bindir}/ksame

%{_datadir}/kde/doc/HTML/en/ksame
%{_datadir}/kde/apps/ksame
%{_datadir}/kde/icons/mini/ksame.xpm
%{_datadir}/kde/icons/ksame.xpm

#################################################
#             KSIRTET
#################################################

%files ksirtet -f ksirtet.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Games/ksirtet.kdelnk
%attr(755,root,root) %{_bindir}/ksirtet

%{_datadir}/kde/doc/HTML/en/ksirtet

%{_datadir}/kde/icons/mini/ksirtet.xpm
%{_datadir}/kde/icons/ksirtet.xpm

#################################################
#             KSMILETRIS
#################################################

%files ksmiletris -f ksmiletris.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Games/ksmiletris.kdelnk
%attr(755,root,root) %{_bindir}/ksmiletris

%{_datadir}/kde/doc/HTML/en/ksmiletris

%{_datadir}/kde/apps/ksmiletris
%{_datadir}/kde/icons/mini/ksmiletris.xpm
%{_datadir}/kde/icons/ksmiletris.xpm

#################################################
#             KSHISEN
#################################################

%files kshisen -f kshisen.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Games/kshisen.kdelnk
%attr(755,root,root) %{_bindir}/kshisen

%{_datadir}/kde/doc/HTML/en/kshisen

%{_datadir}/kde/apps/kshisen
%{_datadir}/kde/icons/mini/kshisen.xpm
%{_datadir}/kde/icons/kshisen.xpm

#################################################
#             KSNAKE
#################################################

%files ksnake -f ksnake.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Games/ksnake.kdelnk
%attr(4755,root,games) %{_bindir}/ksnake

%{_datadir}/kde/doc/HTML/en/ksnake

%{_datadir}/kde/apps/ksnake
%{_datadir}/kde/icons/mini/ksnake.xpm
%{_datadir}/kde/icons/ksnake.xpm
%attr(664,root,games) %ghost /var/state/games/ksnake/highScores

#################################################
#             KSOKOBAN
#################################################

%files ksokoban -f ksokoban.lang
%defattr(644,root,root,755)

%config(missingok) /etc/X11/kde/applnk/Games/ksokoban.kdelnk
%attr(755,root,root) %{_bindir}/ksokoban

%{_datadir}/kde/doc/HTML/en/ksokoban

%{_datadir}/kde/icons/mini/ksokoban.xpm
%{_datadir}/kde/icons/ksokoban.xpm
