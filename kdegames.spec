%define	_prefix	/usr/X11R6

Summary:	K Desktop Environment - games 
Summary(pl):	K Desktop Environment - gry
Name:		kdegames
Version:	2.0
Release:	1
Vendor:		The KDE Team
Copyright:	GPL
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Source0:	ftp://ftp.kde.org/pub/kde/stable/2.0/distribution/generic/tar/src/%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs-devel = %{version}
BuildRequires:	libstdc++-devel
BuildRequires:	qt-devel >= 2.0
BuildRequires:	XFree86-devel
BuildRequires:	zlib-devel
Requires:	qt >= 2.0
Requires:	kdelibs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	qt >= 2.0
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
Requires:	qt >= 2.0
Requires:	kdelibs = %{version}

%description kasteroids
Asteroids clone for KDE

%description kasteroids -l pl
Klon znanej gry "Asteroids".

%package katomic
Summary:	KDE Sokoban clone	
Summary(pl):	Klon gry Sokoban dla KDE
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 2.0
Requires:	kdelibs = %{version}

%description katomic
Atomic Entertainment is a small game which resembles Sokoban. The
Object of the game is to build chemical molecules on a Sokoban like
board.

%description katomic -l pl
Atomic to ma³a gra podobna do gry Sokoban. Celem gry jest zbudowanie
chemicznych moleku³ na planszy podobnej do tej z gry Sokoban.

%package kblackbox
Summary:	A little logical game for KDE	
Summary(pl):	Prosta gra logiczna
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 2.0
Requires:	kdelibs = %{version}

%description kblackbox
A little logical game for KDE.

%description kblackbox -l pl
Prosta gra logiczna.

%package kfouleggs
Summary:	KDE kfouleggs	
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 2.0
Requires:	kdelibs = %{version}

%description kfouleggs
KDE kfouleggs

%package kjumpingcube
Summary:	A little tactical game for KDE
Summary(pl):	Prosta gra taktyczna
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 2.0
Requires:	kdelibs = %{version}

%description kjumpingcube
KJumpingCube is a simple tactical game. You can play it against the
computer or against the friend. The playing field consists of squares
that contains points. By clicking on the squares you can increase the
points, and if the poinst reach a maximum the points will jump to the
squares neighbours and take them over. Winer is the one, who owns all
squares.

%description kjumpingcube -l pl
KJumpingCube to prosta gra taktyczna. Mo¿esz w ni± graæ przeciwko
komputerowi lub przeciwko koledze. Plansza do gry zawiera pola które
z kolei posiadaj± punkty. Przez klikanie na pola zwiekszasz ilo¶æ
punktow na nich. Gdy ilo¶æ punktów na okre¶lonym polu osi±gnie 
maksymalna warto¶æ punkty przeskakuj± na s±siednie pola przejmuj±c
je tym samym na wlasno¶æ. Zwyciesca jest jeden - to ten, kto przejmie
wszystkie pola na wlasno¶æ.

%package kmahjongg
Summary:	KDE Mahjongg clone	
Summary(pl):	Klon gry Mahjongg dla KDE
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 2.0
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
Requires:	qt >= 2.0
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
Requires:	qt >= 2.0
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
Requires:	qt >= 2.0
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
Requires:	qt >= 2.0
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
Requires:	qt >= 2.0
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
Requires:	qt >= 2.0
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
Requires:	qt >= 2.0
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
Requires:	qt >= 2.0
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
Requires:	qt >= 2.0
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
Requires:	qt >= 2.0
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
Requires:	qt >= 2.0
Requires:	kdelibs = %{version} 

%description ksokoban
The japanese warehouse keeper game.

%description ksokoban -l pl
Gra japoñskiego magazyniera.

%package kspaceduel
Summary:	KDE space arcade game for two players
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 2.0
Requires:	kdelibs = %{version} 

%description kspaceduel
Each player control a ship that flies around the sun and tries to
shoot at the other ship. You can play KSpaceduel with another person,
against the computer, or you can have the computer control both ships
and play each other.

%description kspaceduel -l pl
Ka¿dy z graczy kieruje statkiem, który lata dooko³a s³oñca i próbuje
zestarzeliæ drugi statek. Mo¿esz graæ w KSpaceduel z inn± osob±,
z komputerem, lub mo¿esz pozwoliæ aby computer kierowa³ oboma statkami.

%package ktron
Summary:	Tron clone for KDE
Summary(pl):	Klon Tron dla KDE
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 2.0
Requires:	kdelibs = %{version} 

%description ktron
KTron is a simple Trone-Clone for the KDE. You can play KTron against
the computer or a friend.

The aim of the game is to live longer then your opponent. To do That,
avoid running into a wall, your own tail and that of your opponent.

%description ktron -l pl
KTron to prosty klon Trone dla KDE. Mo¿esz graæ w KTron przeciwko
komputerowi lub koledze.

Celem gry jest prze¿yæ d³u¿ej ni¿ przeciwnik. Aby tego dokonaæ unikaj
uderzenia w ¶cianê, ogon w³asny lub przeciwnika.

%package ktuberling
Summary:	KDE game for small children
Summary(pl):	Gra dla ma³ych dzieci
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 2.0
Requires:	kdelibs = %{version} 

%description ktuberling
It is a potato editor. That means that you can drag and drop eyes,
mouths, moustache, and other parts of face and goodies onto
a potato-like guy.

There is no winer. The only purpose is to make the funniest faces
you can.

%description ktuberling -l pl
KTuberling to edytor ziemniaków. Oznacza to, ¿e mo¿esz uk³adaæ oczy,
usta, w±sy oraz inne czê¶ci twarzy na postaæ podobn± do ziemniaka.

W grze nie ma zwyciêzcy. Jedynym celem gry jest stworzenie 
najzabawniejszej twarzy, jak± sie da u³o¿yæ.

%package lskat
Summary:	KDE lskat
Summary(pl):	Lskat dla KDE
Group:		X11/KDE/Games
Group(pl):	X11/KDE/Gry
Requires:	qt >= 2.0
Requires:	kdelibs = %{version} 

%description lskat
Lieutnant Skat

%prep
%setup -q

%build
export KDEDIR=%{_prefix}
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
%{__make} kde_htmldir=$RPM_BUILD_ROOT/%{_datadir}/doc/kde/HTML \
          RUN_KAPPFINDER=no prefix=$RPM_BUILD_ROOT$KDEDIR install

install -d $RPM_BUILD_ROOT/var/lib/games/ksnake/
touch $RPM_BUILD_ROOT/var/lib/games/ksnake/highScores

%find_lang kabalone --with-kde
%find_lang kasteroids --with-kde
%find_lang katomic --with-kde
%find_lang kblackbox --with-kde
%find_lang kfouleggs --with-kde
%find_lang kjumpingcube --with-kde
%find_lang kmahjongg --with-kde
%find_lang kmines --with-kde
%find_lang konquest --with-kde
%find_lang kpat --with-kde
%find_lang kpoker --with-kde
%find_lang kreversi --with-kde
%find_lang ksame --with-kde
%find_lang kshisen --with-kde
%find_lang ksirtet --with-kde
%find_lang ksmiletris --with-kde
%find_lang ksnake --with-kde
%find_lang ksokoban --with-kde
%find_lang kspaceduel --with-kde
%find_lang ktron --with-kde
%find_lang ktuberling --with-kde
%find_lang lskat --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             KABALONE
#################################################

%files -f kabalone.lang kabalone 
%defattr(644,root,root,755)
%config(missingok) %{_datadir}/applnk/Games/kabalone.desktop
%attr(755,root,root) %{_bindir}/kabalone
%{_datadir}/apps/kabalone/
%{_datadir}/icons/hicolor/*x*/apps/kabalone.png
%{_datadir}/icons/locolor/*x*/apps/kabalone.png

#################################################
#             KASTEROIDS 
#################################################

%files -f kasteroids.lang kasteroids 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kasteroids
%config(missingok) %{_datadir}/applnk/Games/kasteroids.desktop
%{_datadir}/apps/kasteroids/
%{_datadir}/icons/hicolor/*x*/apps/kasteroids.png
%{_datadir}/icons/locolor/*x*/apps/kasteroids.png

#################################################
#             KATOMIC
#################################################

%files -f katomic.lang katomic
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/katomic
%config(missingok) %{_datadir}/applnk/Games/katomic.desktop
%{_datadir}/apps/katomic/
%{_datadir}/icons/locolor/*x*/apps/katomic.png

#################################################
#             KBLACKBOX 
#################################################

%files -f kblackbox.lang kblackbox
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kblackbox
%config(missingok) %{_datadir}/applnk/Games/kblackbox.desktop
%{_datadir}/apps/kblackbox/
%{_datadir}/icons/hicolor/*x*/apps/kblackbox.png
%{_datadir}/icons/locolor/*x*/apps/kblackbox.png

#################################################
#             KFOULEGGS
#################################################

%files -f kfouleggs.lang kfouleggs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfouleggs
%config(missingok) %{_datadir}/applnk/Games/kfouleggs.desktop
%{_datadir}/apps/kfouleggs/

#################################################
#             KJUMPINGCUBE
#################################################

%files -f kjumpingcube.lang kjumpingcube
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjumpingcube
%config(missingok) %{_datadir}/applnk/Games/kjumpingcube.desktop
%{_datadir}/icons/locolor/*x*/apps/kjumpingcube.png

#################################################
#             KMAHJONGG
#################################################

%files -f kmahjongg.lang kmahjongg
%defattr(644,root,root,755)
%config(missingok) %{_datadir}/applnk/Games/kmahjongg.desktop
%attr(755,root,root) %{_bindir}/kmahjongg
%{_datadir}/apps/kmahjongg/
%{_datadir}/icons/hicolor/*x*/apps/kmahjongg.png
%{_datadir}/icons/locolor/*x*/apps/kmahjongg.png

#################################################
#             KMINES
#################################################

%files -f kmines.lang kmines
%defattr(644,root,root,755)
%config(missingok) %{_datadir}/applnk/Games/kmines.desktop
%attr(755,root,root) %{_bindir}/kmines
%{_datadir}/icons/hicolor/*x*/apps/kmines.png
%{_datadir}/icons/locolor/*x*/apps/kmines.png

#################################################
#             KONQUEST
#################################################

%files -f konquest.lang konquest
%defattr(644,root,root,755)
%config(missingok) %{_datadir}/applnk/Games/konquest.desktop
%attr(755,root,root) %{_bindir}/konquest
%{_datadir}/apps/konquest/
%{_datadir}/icons/hicolor/*x*/apps/konquest.png
%{_datadir}/icons/locolor/*x*/apps/konquest.png

#################################################
#             KPAT
#################################################

%files -f kpat.lang kpat
%defattr(644,root,root,755)
%config(missingok) %{_datadir}/applnk/Games/kpat.desktop
%attr(755,root,root) %{_bindir}/kpat
%{_datadir}/apps/kpat/
%{_datadir}/icons/hicolor/*x*/apps/kpat.png
%{_datadir}/icons/locolor/*x*/apps/kpat.png

#################################################
#             KPOKER
#################################################

%files -f kpoker.lang kpoker
%defattr(644,root,root,755)
%config(missingok) %{_datadir}/applnk/Games/kpoker.desktop
%attr(755,root,root) %{_bindir}/kpoker
%{_datadir}/apps/kpoker/
%{_datadir}/icons/hicolor/*x*/apps/kpoker.png
%{_datadir}/icons/locolor/*x*/apps/kpoker.png

#################################################
#             KREVERSI
#################################################

%files -f kreversi.lang kreversi
%defattr(644,root,root,755)
%config(missingok) %{_datadir}/applnk/Games/kreversi.desktop
%attr(755,root,root) %{_bindir}/kreversi
%{_datadir}/apps/kreversi/
%{_datadir}/icons/hicolor/*x*/apps/kpoker.png
%{_datadir}/icons/locolor/*x*/apps/kpoker.png

#################################################
#            KSAME 
#################################################

%files -f ksame.lang ksame
%defattr(644,root,root,755)
%config(missingok) %{_datadir}/applnk/Games/ksame.desktop
%attr(755,root,root) %{_bindir}/ksame
%{_datadir}/apps/ksame/
%{_datadir}/icons/hicolor/*x*/apps/ksame.png
%{_datadir}/icons/locolor/*x*/apps/ksame.png

#################################################
#             KSIRTET
#################################################

%files -f ksirtet.lang ksirtet
%defattr(644,root,root,755)
%config(missingok) %{_datadir}/applnk/Games/ksirtet.desktop
%attr(755,root,root) %{_bindir}/ksirtet
%{_datadir}/apps/ksirtet/
%{_datadir}/icons/hicolor/*x*/apps/ksirtet.png
%{_datadir}/icons/locolor/*x*/apps/ksirtet.png

#################################################
#             KSMILETRIS
#################################################

%files -f ksmiletris.lang ksmiletris
%defattr(644,root,root,755)
%config(missingok) %{_datadir}/applnk/Games/ksmiletris.desktop
%attr(755,root,root) %{_bindir}/ksmiletris
%{_datadir}/apps/ksmiletris/
%{_datadir}/icons/hicolor/*x*/apps/ksmiletris.png
%{_datadir}/icons/locolor/*x*/apps/ksmiletris.png

#################################################
#             KSHISEN
#################################################

%files -f kshisen.lang kshisen
%defattr(644,root,root,755)
%config(missingok) %{_datadir}/applnk/Games/kshisen.desktop
%attr(755,root,root) %{_bindir}/kshisen
%{_datadir}/apps/kshisen/
%{_datadir}/icons/hicolor/*x*/apps/kshisen.png
%{_datadir}/icons/locolor/*x*/apps/kshisen.png

#################################################
#             KSNAKE
#################################################

%files -f ksnake.lang ksnake
%defattr(644,root,root,755)
%config(missingok) %{_datadir}/applnk/Games/ksnake.desktop
%attr(4755,root,games) %{_bindir}/ksnake
%{_datadir}/apps/ksnake/
%{_datadir}/icons/hicolor/*x*/apps/ksnake.png
%{_datadir}/icons/locolor/*x*/apps/ksnake.png
%attr(664,root,games) %ghost /var/lib/games/ksnake/highScores

#################################################
#             KSOKOBAN
#################################################

%files -f ksokoban.lang ksokoban
%defattr(644,root,root,755)
%config(missingok) %{_datadir}/applnk/Games/ksokoban.desktop
%attr(755,root,root) %{_bindir}/ksokoban
%{_datadir}/icons/hicolor/*x*/apps/ksokoban.png
%{_datadir}/icons/locolor/*x*/apps/ksokoban.png

#################################################
#             KSPACEDUEL
#################################################

%files -f kspaceduel.lang kspaceduel
%defattr(644,root,root,755)
%config(missingok) %{_datadir}/applnk/Games/kspaceduel.desktop
%attr(4755,root,games) %{_bindir}/kspaceduel
%{_datadir}/apps/kspaceduel/
%{_datadir}/icons/locolor/*x*/apps/kspaceduel.png

#################################################
#             KTRON
#################################################

%files -f ktron.lang ktron
%defattr(644,root,root,755)
%config(missingok) %{_datadir}/applnk/Games/ktron.desktop
%attr(4755,root,games) %{_bindir}/ktron
%{_datadir}/apps/ktron/
%{_datadir}/icons/locolor/*x*/apps/ktron.png

#################################################
#             KTUBERLING
#################################################

%files -f ktuberling.lang ktuberling
%defattr(644,root,root,755)
%config(missingok) %{_datadir}/applnk/Games/ktuberling.desktop
%attr(4755,root,games) %{_bindir}/ktuberling
%{_datadir}/apps/ktuberling/
%{_datadir}/icons/locolor/*x*/apps/ktuberling.png

#################################################
#             LSKAT
#################################################

%files -f lskat.lang lskat
%defattr(644,root,root,755)
%config(missingok) %{_datadir}/applnk/Games/lskat.desktop
%attr(4755,root,games) %{_bindir}/lskat
%{_datadir}/apps/lskat/
%{_datadir}/icons/hicolor/*x*/apps/lskat.png
%{_datadir}/icons/locolor/*x*/apps/lskat.png
