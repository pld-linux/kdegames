Summary:     K Desktop Environment - games 
Summary(pl): K Desktop Environment - gry
Name:        kdegames
Version:     1.0
Release:     7
Vendor:      The KDE Team
Copyright:   GPL
Group:       X11/KDE/Games
Group(pl):   X11/KDE/Gry
Source:      ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/tar/generic/source/%{name}-%{version}.tar.gz
Patch:       kdegames.ksnake-highscore.patch
Requires:    qt >= 1.40, kdelibs = %{version}
BuildRoot:   /tmp/%{name}-%{version}-root

%description
KDE games: KAbalone, KAsteroids, KMahjongg, KMines, KPat, KPoker, KReversi,
KSame, KShisen, KSnake and KTetris

%description -l pl
Gry KDE: KAbalone, KAsteroids, KMahjongg, KMines, KPat, KPoker, KReversi,
KSame, KShisen, KSnake i KTetris

%package -n kabalone
Summary:     KDE game
Summary(pl): Gra KDE
Group:       X11/KDE/Games
Group(pl):   X11/KDE/Gry
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kabalone
KAbalone is a game like Reversi. You play against the computer on a
board. For rules look at the HTML manual.

%description -n kabalone -l pl
KAbalone to gra podobna do Reversi.
Zasady znajdziesz w dokumentacji.

%package -n kasteroids
Summary:     KDE Asteroids clone	
Summary(pl): Klon Asterids dla KDE
Group:       X11/KDE/Games
Group(pl):   X11/KDE/Gry
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kasteroids
Asteroids clone for KDE

%description -n kasteroids -l pl
Klon znanej gry "Asteroids".

%package -n kmahjongg
Summary:     KDE Mahjongg clone	
Summary(pl): Klon gry Mahjongg dla KDE
Group:       X11/KDE/Games
Group(pl):   X11/KDE/Gry
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kmahjongg
This program is a clone of the well known Mahjongg game.

%description -n kmahjongg -l pl
Wersja KDE znanej gry Mahjongg

%package -n kmines 
Summary:     KDE minesweeper game
Summary(pl): Saper dla KDE
Group:       X11/KDE/Games
Group(pl):   X11/KDE/Gry
Requires:    qt >= 1.40, kdelibs = %{version}

%description -n kmines
This is a very classical minesweeper written from scratch.
- 3 predefined levels :
  Easy : 8x8 with 10 mines
  Normal : 16x16 with 40 mines
  Expert : 30x16 with 99 mines
- Custom levels
- High Scores

%description -n kmines -l pl
Wersja znanej gry "saper" dla KDE

%package -n kpat
Summary:     KDE solitaire patience game	
Summary(pl): Pasjanse KDE
Group:       X11/KDE/Games
Group(pl):   X11/KDE/Gry
Requires:    qt >= 1.40, kdelibs = %{version} 

%description -n kpat
KDE solitaire patience games.

%description -n kpat -l pl
Program umo¿liwia uk³adanie kilku rodzajów pasjansów.

%package -n kpoker
Summary:     KDE poker	
Summary(pl): Poker KDE
Group:       X11/KDE/Games
Group(pl):   X11/KDE/Gry
Requires:    qt >= 1.40, kdelibs = %{version} 

%description -n kpoker
A simple video poker clone for the KDE desktop environment.

%description -n kpoker -l pl
Prosy poker dla KDE.

%package -n kreversi
Summary:     KDE Reversi game	
Summary(pl): Gra Reversi dla KDE
Group:       X11/KDE/Games
Group(pl):   X11/KDE/Gry
Requires:    qt >= 1.40, kdelibs = %{version} 

%description -n kreversi
Reversi is a simple strategy game that is played by two players. There
is only one type of piece - one side of it is black, the other white.
If a player captures a piece on the board, that piece is turned and
belongs to that player. The winner is the person that has more pieces
of his own color on the board and if there are no more moves possible.

%description -n kreversi -l pl
Reversi to prosta gra strategiczna dla dwóch graczy.

%package -n ksame
Summary:     KDE SameGame	
Summary(pl): "To Samo" dla KDE
Group:       X11/KDE/Games
Group(pl):   X11/KDE/Gry
Requires:    qt >= 1.40, kdelibs = %{version} 

%description -n ksame
KSame is a simple game. It's played by one player, so there is only
one winner :-) You play for fun and against the highscore. It has been
inspired by SameGame, that is only famous on the Macintosh plattform.

%description -n ksame -l pl
KSame to prosta gra dla jednego gracza.

%package -n kshisen
Summary:     KDE Shisen-Sho	
Summary(pl): Shisen-Sho dla KDE
Group:       X11/KDE/Games
Group(pl):   X11/KDE/Gry
Requires:    qt >= 1.40, kdelibs = %{version} 

%description -n kshisen
Shisen-Sho is similiar to Mahjongg and uses the same set of tiles as
Mahjongg.

%description -n kshisen -l pl
Shisen-Sho to gra podobna do Mahjongg i wykorzystuj±ca ten sam zestaw ko¶ci.

%package -n ksnake
Summary:     KDE Snake Race	
Summary(pl): Wy¶cig Wê¿y dla KDE
Group:       X11/KDE/Games
Group(pl):   X11/KDE/Gry
Requires:    qt >= 1.40, kdelibs = %{version} 

%description -n ksnake
Snake Race is a game of speed and agility. You are a hungry snake and
are trying to eat all the apples in the room before getting out!

%description -n ksnake -l pl
Snake Race to gra szybko¶ciowo-zrêczno¶ciowa. Wcielasz sie w g³odnego
wê¿a próbuj±cego zje¶æ wszystkie jab³ka w pomieszczeniu.

%package -n ktetris
Summary:     KDE Tetris	
Summary(pl): Tetris dla KDE
Group:       X11/KDE/Games
Group(pl):   X11/KDE/Gry
Requires:    qt >= 1.40, kdelibs = %{version} 

%description -n ktetris
This program is a clone of the well-known game Tetris.

%description -n ktetris -l pl
Kolejny klon dobrze znanego Tetrisa.

%prep
%setup -q
%patch -p1

%build
export KDEDIR=/usr/X11R6
CXXFLAGS="$RPM_OPT_FLAGS -Wall" CFLAGS="$RPM_OPT_FLAGS -Wall" \
./configure %{_target} \
	--prefix=$KDEDIR \
 	--with-install-root=$RPM_BUILD_ROOT \
 	--with-pam="yes"
make KDEDIR=$KDEDIR

%install
rm -rf $RPM_BUILD_ROOT

export KDEDIR=/usr/X11R6
make RUN_KAPPFINDER=no prefix=$RPM_BUILD_ROOT$KDEDIR install

# create wmconfig files
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
DIR=$PWD
(cd $RPM_BUILD_ROOT/etc/X11/kde/applnk
for kdelnk in `find . -name "*.kdelnk"` ; do
  PKG=kde`basename $kdelnk|sed -e "s/\.kdelnk$//"`;
  SECT=`dirname $kdelnk|sed -e "s/^\.\/*//"`;
  kdelnk2wmconfig $PKG $kdelnk $RPM_BUILD_ROOT/etc/X11/wmconfig/$PKG KDE/$SECT pl
done)

%clean
rm -rf $RPM_BUILD_ROOT

#################################################
#             KABALONE
#################################################

%files -n kabalone 
%defattr(644, root, root, 755)
%config(missingok) /etc/X11/kde/applnk/Games/kabalone.kdelnk
%config(missingok) /etc/X11/wmconfig/kdekabalone
%attr(755, root, root) /usr/X11R6/bin/kabalone
%lang(de) /usr/X11R6/share/kde/doc/HTML/de/kabalone/
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kabalone/
/usr/X11R6/share/kde/apps/kabalone/toolbar/
/usr/X11R6/share/kde/icons/kabalone.xpm
/usr/X11R6/share/kde/icons/mini/kabalone.xpm
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kabalone.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kabalone.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kabalone.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kabalone.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kabalone.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kabalone.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kabalone.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kabalone.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kabalone.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kabalone.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kabalone.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kabalone.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kabalone.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kabalone.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kabalone.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kabalone.mo
%lang(mk) /usr/X11R6/share/locale/mk/LC_MESSAGES/kabalone.mo

#################################################
#             KASTEROIDS 
#################################################

%files -n kasteroids 
%defattr(644, root, root, 755)
%attr(755, root, root) /usr/X11R6/bin/kasteroids
%config(missingok) /etc/X11/kde/applnk/Games/kasteroids.kdelnk
%config(missingok) /etc/X11/wmconfig/kdekasteroids
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kasteroids/
/usr/X11R6/share/kde/apps/kasteroids/
/usr/X11R6/share/kde/icons/mini/kasteroids.xpm
/usr/X11R6/share/kde/icons/kasteroids.xpm
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kasteroids.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kasteroids.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kasteroids.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kasteroids.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kasteroids.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kasteroids.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kasteroids.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kasteroids.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kasteroids.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kasteroids.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kasteroids.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/kasteroids.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kasteroids.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kasteroids.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kasteroids.mo
%lang(mk) /usr/X11R6/share/locale/mk/LC_MESSAGES/kasteroids.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kasteroids.mo

#################################################
#             KMAHJONGG
#################################################

%files -n kmahjongg
%defattr(644, root, root, 755)
%config(missingok) /etc/X11/kde/applnk/Games/kmahjongg.kdelnk
%config(missingok) /etc/X11/wmconfig/kdekmahjongg
%attr(755, root, root) /usr/X11R6/bin/kmahjongg
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/
/usr/X11R6/share/kde/apps/kmahjongg/
/usr/X11R6/share/kde/icons/kmahjongg.xpm
/usr/X11R6/share/kde/icons/mini/kmahjongg.xpm
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kmahjongg.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kmahjongg.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kmahjongg.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kmahjongg.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kmahjongg.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kmahjongg.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kmahjongg.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kmahjongg.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kmahjongg.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kmahjongg.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kmahjongg.mo

#################################################
#             KMINES
#################################################

%files -n kmines
%defattr(644, root, root, 755)
%config(missingok) /etc/X11/kde/applnk/Games/kmines.kdelnk
%config(missingok) /etc/X11/wmconfig/kdekmines
%attr(755, root, root) /usr/X11R6/bin/kmines
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kmines/
/usr/X11R6/share/kde/icons/mini/kmines.xpm
/usr/X11R6/share/kde/icons/kmines.xpm
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kmines.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kmines.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kmines.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kmines.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kmines.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kmines.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kmines.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kmines.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kmines.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kmines.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kmines.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kmines.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kmines.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kmines.mo

#################################################
#             KPAT
#################################################

%files -n kpat
%defattr(644, root, root, 755)
%config(missingok) /etc/X11/kde/applnk/Games/kpat.kdelnk
%config(missingok) /etc/X11/wmconfig/kdekpat
%attr(755, root, root) /usr/X11R6/bin/kpat
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kpat/
/usr/X11R6/share/kde/apps/kpat/
/usr/X11R6/share/kde/icons/mini/kpat.xpm
/usr/X11R6/share/kde/icons/kpat.xpm
/usr/X11R6/share/kde/icons/kpat-lq.xpm
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kpat.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kpat.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kpat.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kpat.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kpat.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kpat.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kpat.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kpat.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kpat.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kpat.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kpat.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kpat.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kpat.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kpat.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kpat.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kpat.mo

#################################################
#             KPOKER
#################################################

%files -n kpoker
%defattr(644, root, root, 755)
%config(missingok) /etc/X11/kde/applnk/Games/kpoker.kdelnk
%config(missingok) /etc/X11/wmconfig/kdekpoker
%attr(755, root, root) /usr/X11R6/bin/kpoker
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kpoker/
/usr/X11R6/share/kde/apps/kpoker/
/usr/X11R6/share/kde/icons/mini/kpoker.xpm
/usr/X11R6/share/kde/icons/kpoker.xpm
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kpoker.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kpoker.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kpoker.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kpoker.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kpoker.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kpoker.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kpoker.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kpoker.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kpoker.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kpoker.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kpoker.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kpoker.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kpoker.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kpoker.mo

#################################################
#             KREVERSI
#################################################

%files -n kreversi
%defattr(644, root, root, 755)
%config(missingok) /etc/X11/kde/applnk/Games/kreversi.kdelnk
%config(missingok) /etc/X11/wmconfig/kdekreversi
%attr(755, root, root) /usr/X11R6/bin/kreversi
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kreversi/
/usr/X11R6/share/kde/apps/kreversi/
/usr/X11R6/share/kde/icons/mini/kreversi.xpm
/usr/X11R6/share/kde/icons/kreversi.xpm
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kreversi.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kreversi.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kreversi.mo
%lang(el) /usr/X11R6/share/locale/el/LC_MESSAGES/kreversi.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kreversi.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kreversi.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kreversi.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kreversi.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kreversi.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kreversi.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kreversi.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kreversi.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kreversi.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/kreversi.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kreversi.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kreversi.mo

#################################################
#            KSAME 
#################################################

%files -n ksame
%defattr(644, root, root, 755)
%config(missingok) /etc/X11/kde/applnk/Games/ksame.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeksame
%attr(755, root, root) /usr/X11R6/bin/ksame
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/ksame/
/usr/X11R6/share/kde/apps/ksame/
/usr/X11R6/share/kde/icons/mini/ksame.xpm
/usr/X11R6/share/kde/icons/ksame.xpm
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/ksame.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/ksame.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/ksame.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/ksame.mo
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/ksame.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/ksame.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/ksame.mo

#################################################
#             KSHISEN
#################################################

%files -n kshisen
%defattr(644, root, root, 755)
%config(missingok) /etc/X11/kde/applnk/Games/kshisen.kdelnk
%config(missingok) /etc/X11/wmconfig/kdekshisen
%attr(755, root, root) /usr/X11R6/bin/kshisen
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/kshisen/
/usr/X11R6/share/kde/apps/kshisen/
/usr/X11R6/share/kde/icons/mini/kshisen.xpm
/usr/X11R6/share/kde/icons/kshisen.xpm
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/kshisen.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/kshisen.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/kshisen.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/kshisen.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/kshisen.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/kshisen.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/kshisen.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/kshisen.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/kshisen.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/kshisen.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/kshisen.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/kshisen.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/kshisen.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/kshisen.mo

#################################################
#             KSNAKE
#################################################

%files -n ksnake
%defattr(644, root, root, 755)
%config(missingok) /etc/X11/kde/applnk/Games/ksnake.kdelnk
%config(missingok) /etc/X11/wmconfig/kdeksnake
%attr(4755,root,games) /usr/X11R6/bin/ksnake
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/ksnake/
/usr/X11R6/share/kde/apps/ksnake/
/usr/X11R6/share/kde/icons/mini/ksnake.xpm
/usr/X11R6/share/kde/icons/ksnake.xpm
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/ksnake.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/ksnake.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/ksnake.mo
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/ksnake.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/ksnake.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/ksnake.mo
%attr(664,root,games) %ghost /var/lib/games/ksnake/highScores

#################################################
#             KTETRIS
#################################################

%files -n ktetris
%defattr(644, root, root, 755)
%config(missingok) /etc/X11/kde/applnk/Games/ktetris.kdelnk
%config(missingok) /etc/X11/wmconfig/kdektetris
%attr(755, root, root) /usr/X11R6/bin/ktetris
%lang(en) /usr/X11R6/share/kde/doc/HTML/en/ktetris/
/usr/X11R6/share/kde/icons/mini/ktetris.xpm
/usr/X11R6/share/kde/icons/ktetris.xpm
%lang(cs) /usr/X11R6/share/locale/cs/LC_MESSAGES/ktetris.mo
%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/ktetris.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/ktetris.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/ktetris.mo
%lang(hr) /usr/X11R6/share/locale/hr/LC_MESSAGES/ktetris.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/ktetris.mo
%lang(nl) /usr/X11R6/share/locale/nl/LC_MESSAGES/ktetris.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/ktetris.mo
%lang(pl) /usr/X11R6/share/locale/pl/LC_MESSAGES/ktetris.mo
%lang(pt) /usr/X11R6/share/locale/pt*/LC_MESSAGES/ktetris.mo
%lang(ro) /usr/X11R6/share/locale/ro/LC_MESSAGES/ktetris.mo
%lang(sk) /usr/X11R6/share/locale/sk/LC_MESSAGES/ktetris.mo
%lang(zh) /usr/X11R6/share/locale/zh*/LC_MESSAGES/ktetris.mo

%changelog
* Wed Dec  8 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0-7]
- recompiled against libstdc++.so.2.9.

* Thu Oct 13 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0-5]
- added Group(pl) fields,
- fixes in %files.

* Sun Oct 11 1998 Jacek Konieczny <jajcus@zeus.polsl.gliwice.pl>
  [1.0-4]
- hiscore file for ksnake moved to /var/lib/games,
- created new spec based on kdebase.spec.
