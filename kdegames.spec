%define		_ver		3.0
#define		_sub_ver
%define		_rel		1

%{?_sub_ver:	%define	_version	%{_ver}%{_sub_ver}}
%{!?_sub_ver:	%define	_version	%{_ver}}
%{?_sub_ver:	%define	_release	0.%{_sub_ver}.%{_rel}}
%{!?_sub_ver:	%define	_release	%{_rel}}
%{!?_sub_ver:	%define	_ftpdir	stable}
%{?_sub_ver:	%define	_ftpdir	unstable/kde-%{version}%{_sub_ver}}

Summary:	K Desktop Environment - games
Summary(es):	K Desktop Environment - Juegos
Summary(pl):	K Desktop Environment - gry
Summary(pt_BR):	K Desktop Environment - Jogos
Name:		kdegames
Version:	%{_version}
Release:	%{_release}
Epoch:		6
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications/Games
Source0:	ftp://ftp.kde.org/pub/kde/%{_ftpdir}/%{version}/src/%{name}-%{version}.tar.bz2
Patch0:		%{name}-kpatcards.patch
BuildRequires:	XFree86-devel
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	qt-devel >= 2.2
BuildRequires:	zlib-devel
BuildRequires:	arts-devel
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML

%description
Libraries for kdegames. Included with this package are: kasteroids, kblackbox,
kmahjongg, kmines, konquest, kpat, kpoker, kreversi, ksame, kshisen, ksokoban,
ksmiletris, ksnake, ksirtet, katomic, kjumpingcube, ktuberling.

%description -l es
Juegos para KDE. Incluidos en este paquete: kasteroids: arcade kmahjongg: el
popular mahjongg kmines: desarmar las minas kpat: juegos de cartas, incluso
solitario kpoker: vídeo póquer kreversi: Reversi ksame: un juego de tablero
kshisen: Shisen-Sho - relacionado con el mahjongg ksnake: corrida de las cobras
ktetris: el bien conocido tetris

%description -l pl
Biblioteki dla gier KDE.

%description -l pt_BR
Jogos para o KDE.

Incluídos neste pacote:

kabalone: estratégia kasteroids: arcade kmahjongg: o popular mahjongg
kmines: desarmar as minas kpat: jogos de cartas, inclusive paciência
kpoker: vídeo-poker kreversi: Reversi ksame: um jogo de tabuleiro
kshisen: Shisen-Sho - relacionado com o mahjongg ksnake: corrida das
cobras ktetris: o bem conhecido tetris

%package devel
Summary:	Development files for KDE games
Summary(pl):	Pliki developerskie dla KDE games
Summary(pt_BR):	Arquivos de inclusão do kdegames
Group:		X11/Development/Libraries
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description devel
Development files for KDE games.

%description devel -l pl
Pliki developerskie dla KDE games.

%description devel -l pt_BR
Este pacote detém os arquivos de inclusão necessários para compilar
aplicativos que usam bibliotecas do kdegames.

%package carddecks
Summary:	KDE carddecks
Summary(pl):	Karcianki dla KDE
Summary(pt_BR):	Biblioteca de baralhos para jogos do KDE que usem cartas
Group:		X11/Applications/Games

%description carddecks
KDE carddecks.

%description carddecks -l pl
Karcianki dla KDE.

%description carddecks -l pt_BR
Biblioteca de baralhos para jogos do KDE que usem cartas.

#%package kabalone
#Summary:	KAbalone (strategy hexagonal game) for KDE
#Summary(pl):	KAbalone - gra strategiczna dla KDE
#Group:		X11/Applications/Games
#Requires:	qt >= 3.0.3
#Requires:	kdelibs >= %{version}
#
#%description kabalone
#KAbalone is a game like Reversi. You play against the computer on a
#board. For rules look at the HTML manual.
#
#%description kabalone -l pl
#KAbalone to gra podobna do Reversi. Zasady znajdziesz w dokumentacji.
#
#%description kabalone -l pt_BR
#Abalone para KDE (jogo hexagonal de estratégia)

%package kasteroids
Summary:	KDE Asteroids clone
Summary(pl):	Klon Asterids dla KDE
Summary(pt_BR):	Destrua os asteróides para não ser destruído
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description kasteroids
Asteroids clone for KDE.

%description kasteroids -l pl
Klon znanej gry "Asteroids".

%description kasteroids -l pt_BR
Destrua os asteróides para não ser destruído.

%package katomic
Summary:	KDE Sokoban clone
Summary(pl):	Klon gry Sokoban dla KDE
Summary(pt_BR):	Jogo semelhante ao Sokoban mas o objetivo é formar moléculas
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description katomic
Atomic Entertainment is a small game which resembles Sokoban. The
Object of the game is to build chemical molecules on a Sokoban like
board.

%description katomic -l pl
Atomic to ma³a gra podobna do gry Sokoban. Celem gry jest zbudowanie
chemicznych moleku³ na planszy podobnej do tej z gry Sokoban.

%description katomic -l pt_BR
Jogo semelhante ao Sokoban mas o objetivo é formar moléculas.

%package kbackgammon
Summary:	Backgammon program for KDE
Summary(pl):	Backgammon dla KDE
Summary(pt_BR):	Jogo de gamão para KDE
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description kbackgammon
KBackgammon is a graphical backgammon program for KDE. It supports
backgammon games with other players, games against computer engines
like GNU bg and even on-line games on the First Internet Backgammon
Server.

%description kbackgammon -l pl
KBackgammon to graficzna wersja gry backgammon dla KDE. Mo¿esz graæ z
innymi graczami, przeciwko komputerowi lub nawet rozegraæ partiê przez
sieæ korzystaj±c z Pierwszego Internetowego Serwera Backgammon.

%description kbackgammon -l pt_BR
Jogo de gamão para KDE.

%package kbattleship
Summary:	Battleship for KDE
Summary(pl):	Statki dla KDE
Summary(pt_BR):	Jogo de batalha naval com servidor embutido
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description kbattleship
Battleship for KDE.

%description kbattleship -l pl
Statki dla KDE.

%description kbattleship -l pt_BR
Jogo de batalha naval com servidor embutido.

%package kblackbox
Summary:	A little logical game for KDE
Summary(pl):	Prosta gra logiczna
Summary(pt_BR):	Versão do jogo Blackbox do Emacs para KDE
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description kblackbox
A little logical game for KDE.

%description kblackbox -l pl
Prosta gra logiczna.

%description kblackbox -l pt_BR
Versão do jogo Blackbox do Emacs para KDE.

%package kfouleggs
Summary:	KDE kfouleggs
Summary(pl):	kfouleggs dla KDE
Summary(pt_BR):	Mais um jogo que lembra o estilo Tetris
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description kfouleggs
KDE kfouleggs.

%description kfouleggs -l pl
kfouleggs dla KDE.

%description kfouleggs -l pt_BR
Mais um jogo que lembra o estilo Tetris.

#%package kjezz
#Summary:	KDE jezz
#Summary(pl):	Jezz dla KDE
#Summary(pt_BR):	Diminua a área ocupada pelas bolinhas o mais depressa possível
#Group:		X11/Applications/Games
#Requires:	qt >= 3.0.3
#Requires:	kdelibs >= %{version}
#
#%description kjezz
#KDE jezz.
#
#%description kjezz -l pl
#Jezz dla KDE.
#
#%description kjezz -l pt_BR
#Diminua a área ocupada pelas bolinhas o mais depressa possível.

%package kjumpingcube
Summary:	A little tactical game for KDE
Summary(pl):	Prosta gra taktyczna
Summary(pt_BR):	Jogo de estratégia para 2 contendores
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description kjumpingcube
KJumpingCube is a simple tactical game. You can play it against the
computer or against the friend. The playing field consists of squares
that contains points. By clicking on the squares you can increase the
points, and if the poinst reach a maximum the points will jump to the
squares neighbours and take them over. Winer is the one, who owns all
squares.

%description kjumpingcube -l pl
KJumpingCube to prosta gra taktyczna. Mo¿esz w ni± graæ przeciwko
komputerowi lub przeciwko koledze. Plansza do gry zawiera pola które z
kolei posiadaj± punkty. Przez klikanie na pola zwiekszasz ilo¶æ
punktow na nich. Gdy ilo¶æ punktów na okre¶lonym polu osi±gnie
maksymalna warto¶æ punkty przeskakuj± na s±siednie pola przejmuj±c je
tym samym na wlasno¶æ. Zwyciesca jest jeden - to ten, kto przejmie
wszystkie pola na wlasno¶æ.

%description kjumpingcube -l pt_BR
Jogo de estratégia para 2 contendores.

%package klines
Summary:	Lines for KDE
Summary(pl):	Lines dla KDE
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description klines
Lines for KDE.

%description klines -l pl
Lines dla KDE.

%package kmahjongg
Summary:	KDE Mahjongg clone
Summary(pl):	Klon gry Mahjongg dla KDE
Summary(pt_BR):	Versão do jogo Mahjongg para o KDE
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description kmahjongg
This program is a clone of the well known Mahjongg game.

%description kmahjongg -l pl
Wersja KDE znanej gry Mahjongg.

%description kmahjongg -l pt_BR
Versão do jogo Mahjongg para o KDE.

%package kmines
Summary:	KDE minesweeper game
Summary(pl):	Saper dla KDE
Summary(pt_BR):	Versão do jogo 'caça-minas' para o KDE
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description kmines
This is a very classical minesweeper written from scratch.
- 3 predefined levels : Easy : 8x8 with 10 mines Normal : 16x16 with
  40 mines Expert : 30x16 with 99 mines
- Custom levels
- High Scores.

%description kmines -l pl
Wersja znanej gry "saper" dla KDE.

%description kmines -l pt_BR
Versão do jogo 'caça-minas' para o KDE.

%package konquest
Summary:	KDE version of Gnu-Lactic Konquest
Summary(pl):	Podbój galaktyki
Summary(pt_BR):	Jogo espacial de estratégia
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description konquest
KDE version of Gnu-Lactic Konquest.

%description konquest -l pl
Podbój galaktyki.

%description konquest -l pt_BR
Jogo espacial de estratégia.

%package kpat
Summary:	KDE solitaire patience game
Summary(pl):	Pasjanse KDE
Summary(pt_BR):	Versão do jogo 'Paciência' para o KDE
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description kpat
KDE solitaire patience games.

%description kpat -l pl
Program umo¿liwia uk³adanie kilku rodzajów pasjansów.

%description kpat -l pt_BR
Versão do jogo 'Paciência' para o KDE.

%package kpoker
Summary:	KDE poker
Summary(pl):	Poker KDE
Summary(pt_BR):	Jogo de vídeo-pôquer para o KDE
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description kpoker
A simple video poker clone for the KDE desktop environment.

%description kpoker -l pl
Prosy poker dla KDE.

%description kpoker -l pt_BR
Jogo de vídeo-pôquer para o KDE.

%package kreversi
Summary:	KDE Reversi game
Summary(pl):	Gra Reversi dla KDE
Summary(pt_BR):	Jogo no estilo Otelo para KDE
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description kreversi
Reversi is a simple strategy game that is played by two players. There
is only one type of piece - one side of it is black, the other white.
If a player captures a piece on the board, that piece is turned and
belongs to that player. The winner is the person that has more pieces
of his own color on the board and if there are no more moves possible.

%description kreversi -l pl
Reversi to prosta gra strategiczna dla dwóch graczy.

%description kreversi -l pt_BR
Jogo no estilo Otelo para KDE.

%package ksame
Summary:	KDE SameGame
Summary(pl):	"To Samo" dla KDE
Summary(pt_BR):	Jogo relaxante onde você deve remover o maior número possível de bolas
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description ksame
KSame is a simple game. It's played by one player, so there is only
one winner :-) You play for fun and against the highscore. It has been
inspired by SameGame, that is only famous on the Macintosh plattform.

%description ksame -l pl
KSame to prosta gra dla jednego gracza.

%description ksame -l pt_BR
Jogo relaxante onde você deve remover o maior número possível de
bolinhas

%package kshisen
Summary:	KDE Shisen-Sho
Summary(pl):	Shisen-Sho dla KDE
Summary(pt_BR):	Jogo Shisen para o KDE
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description kshisen
Shisen-Sho is similiar to Mahjongg and uses the same set of tiles as
Mahjongg.

%description kshisen -l pl
Shisen-Sho to gra podobna do Mahjongg i wykorzystuj±ca ten sam zestaw
ko¶ci.

%description kshisen -l pt_BR
Jogo Shisen para o KDE.

%package ksirtet
Summary:	KDE Tetris
Summary(pl):	Tetris dla KDE
Summary(pt_BR):	Jogo no estilo Tetris
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description ksirtet
This program is a clone of the well-known game Tetris.

%description ksirtet -l pl
Kolejny klon dobrze znanego Tetrisa.

%description ksirtet -l pt_BR
Jogo no estilo Tetris.

%package ksmiletris
Summary:	KDE Tetris
Summary(pl):	Tetris dla KDE
Summary(pt_BR):	Jogo no estilo Tetris para o KDE
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description ksmiletris
This program is a clone of the well-known game Tetris.

%description ksmiletris -l pl
Kolejny klon dobrze znanego Tetrisa.

%description ksmiletris -l pt_BR
Jogo no estilo Tetris para o KDE.

%package ksnake
Summary:	KDE Snake Race
Summary(pl):	Wy¶cig Wê¿y dla KDE
Summary(pt_BR):	Jogo da cobra sempre crescente para o KDE
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description ksnake
Snake Race is a game of speed and agility. You are a hungry snake and
are trying to eat all the apples in the room before getting out!

%description ksnake -l pl
Snake Race to gra szybko¶ciowo-zrêczno¶ciowa. Wcielasz sie w g³odnego
wê¿a próbuj±cego zje¶æ wszystkie jab³ka w pomieszczeniu.

%description ksnake -l pt_BR
Jogo da cobra sempre crescente para o KDE.

%package ksokoban
Summary:	KDE Sokoban
Summary(pl):	Sokoban dla KDE
Summary(pt_BR):	Jogo Sokoban ou 'Fiscal de Estoque' para o KDE
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description ksokoban
The japanese warehouse keeper game.

%description ksokoban -l pl
Gra japoñskiego magazyniera.

%description ksokoban -l pt_BR
Jogo Sokoban ou 'Fiscal de Estoque' para o KDE.

%package kspaceduel
Summary:	KDE space arcade game for two players
Summary(pl):	Gra arcade pod KDE dla dwóch graczy
Summary(pt_BR):	Versão do jogo Duelo Espacial para o KDE
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description kspaceduel
Each player control a ship that flies around the sun and tries to
shoot at the other ship. You can play KSpaceduel with another person,
against the computer, or you can have the computer control both ships
and play each other.

%description kspaceduel -l pl
Ka¿dy z graczy kieruje statkiem, który lata dooko³a s³oñca i próbuje
zestarzeliæ drugi statek. Mo¿esz graæ w KSpaceduel z inn± osob±, z
komputerem, lub mo¿esz pozwoliæ aby computer kierowa³ oboma statkami.

%description kspaceduel -l pt_BR
Versão do jogo Duelo Espacial para o KDE.

%package ktron
Summary:	Tron clone for KDE
Summary(pl):	Klon Tron dla KDE
Summary(pt_BR):	Versão do jogo Tron / Motos de Luz para o KDE
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

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

%description ktron -l pt_BR
Versão do jogo Tron / Motos de Luz para o KDE.

%package ktuberling
Summary:	KDE game for small children
Summary(pl):	Gra dla ma³ych dzieci
Summary(pt_BR):	Jogo de desenho do 'Homem-batata' para crianças
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description ktuberling
It is a potato editor. That means that you can drag and drop eyes,
mouths, moustache, and other parts of face and goodies onto a
potato-like guy.

There is no winer. The only purpose is to make the funniest faces you
can.

%description ktuberling -l pl
KTuberling to edytor ziemniaków. Oznacza to, ¿e mo¿esz uk³adaæ oczy,
usta, w±sy oraz inne czê¶ci twarzy na postaæ podobn± do ziemniaka.

W grze nie ma zwyciêzcy. Jedynym celem gry jest stworzenie
najzabawniejszej twarzy, jak± sie da u³o¿yæ.

%description ktuberling -l pt_BR
Jogo de desenho do 'Homem-batata' para crianças.

%package kwin4
Summary:	Four wins for KDE
Summary(pl):	Gra "cztery wygrywa" dla KDE
Summary(pt_BR):	Jogo de estratégia que lembra um pouco o Otelo
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description kwin4
Four wins is a game for two players. Each player is represented by a
colour (yellow and red). The goal of the game is to get four connected
pieces of your colour into a row, column or any diagonal. This is done
by placing one of your pieces into any of the seven columns. A piece
will begin to fill a column from the bottom, i.e. it will fall down
until it reaches the ground level or another stone. After a move is
done it is the turn of the other player. This is repeated until the
game is over, i.e. one of the players has four pieces in a row, column
or diagonal or no more moves are possbile because the board is filled.

%description kwin4 -l pl
Cztery wygrywa jest gr± dla dwóch graczy. Ka¿dy gracz jest
reprezentowany przez kolor (¿ó³ty b±d¼ czerwony). Celem gry jest
ustawienie czterech klocków twojego koloru w rz±d, kolumnê lub po
przek±tnej. Klocki wype³niaj± kolumny od do³u, tj. spadaj± dopóki nie
dosiêgn± pod³o¿a b±d¼ innego klocka. Gra trwa do momentu uzyskania ww.
uk³adu b±d¼ do zape³nienia tablicy.

%description kwin4 -l pt_BR
Jogo de estratégia que lembra um pouco o Otelo.

%package lskat
Summary:	KDE lskat
Summary(pl):	Lskat dla KDE
Summary(pt_BR):	Jogo de cartas Lieutenant Skat para KDE
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description lskat
Lieutnant Skat.

%description lskat -l pl
Lskat dla KDE.

%description lskat -l pt_BR
Jogo de cartas Lieutenant Skat para KDE

%package kbounce
Summary:	Claim areas and don't get disturbed
#Summary(pl):	
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description kbounce
Claim areas and don't get disturbed.

#%description kbounce -l pl

%package kenolaba
Summary:	-
Summary(pl):	-
Group:		X11/Applications/Games
Requires:	qt >= 3.0.3
Requires:	kdelibs >= %{version}

%description kenolaba
-

%description kenolaba -l pl
-

%prep
%setup -q
%patch0 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \
	--with-qt-dir=%{_prefix} \
	--with-pam="yes" \
	--enable-final
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Amusements

%{__make} DESTDIR=$RPM_BUILD_ROOT install

mv $RPM_BUILD_ROOT%{_applnkdir}/Toys/ktuberling.desktop \
	$RPM_BUILD_ROOT%{_applnkdir}/Amusements

#%find_lang kabalone --with-kde
%find_lang kasteroids --with-kde
%find_lang katomic --with-kde
%find_lang kbackgammon --with-kde
%find_lang kbattleship --with-kde
%find_lang kblackbox --with-kde
%find_lang kbounce --with-kde
%find_lang kenolaba --with-kde
%find_lang kfouleggs --with-kde
#%find_lang kjezz --with-kde
%find_lang kjumpingcube --with-kde
%find_lang klines --with-kde
#%find_lang kmahjongg --with-kde
%find_lang kmines --with-kde
%find_lang konquest --with-kde
%find_lang kpat --with-kde
%find_lang kpoker --with-kde
%find_lang kreversi --with-kde
%find_lang ksame --with-kde
%find_lang kshisen --with-kde
%find_lang ksirtet --with-kde
#%find_lang ksmiletris --with-kde
%find_lang ksnake --with-kde
%find_lang ksokoban --with-kde
%find_lang kspaceduel --with-kde
%find_lang ktron --with-kde
%find_lang ktuberling --with-kde
%find_lang kwin4 --with-kde
%find_lang lskat --with-kde

%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkdegames.so.*.*
%{_datadir}/apps/kdegames/pics/*
%{_libdir}/libkdegames.la
%{_libdir}/libkdehighscores.la
%{_libdir}/libkdehighscores.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_includedir}/kgame
%{_libdir}/libkdegames.so
%{_libdir}/libksirtet*.so
%{_libdir}/libkdehighscores.so
%{_pixmapsdir}/*/*/*/highscore.*
%{_pixmapsdir}/*/*/*/roll.*

%files carddecks
%defattr(644,root,root,755)
%{_datadir}/apps/carddecks/*

#################################################
#             KABALONE
#################################################

#%files -f kabalone.lang kabalone
#%defattr(644,root,root,755)
#%{_applnkdir}/Games/Board/kabalone.desktop
#%attr(755,root,root) %{_bindir}/kabalone
#%{_datadir}/apps/kabalone/*
#%{_pixmapsdir}/hicolor/*x*/apps/kabalone.png

#################################################
#             KASTEROIDS
#################################################

%files -f kasteroids.lang kasteroids
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kasteroids
%{_applnkdir}/Games/Arcade/kasteroids.desktop
%{_datadir}/apps/kasteroids/*
%{_pixmapsdir}/hicolor/*x*/apps/kasteroids.png

#################################################
#             KATOMIC
#################################################

%files -f katomic.lang katomic
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/katomic
%{_applnkdir}/Games/TacticStrategy/katomic.desktop
%{_datadir}/apps/katomic/*
%{_pixmapsdir}/hicolor/*x*/apps/katomic.png

#################################################
#             KBACKGAMMON
#################################################

%files -f kbackgammon.lang kbackgammon
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbackgammon
%attr(755,root,root) %{_libdir}/kbackgammon.??
%{_applnkdir}/Games/Board/kbackgammon.desktop
%{_datadir}/apps/kbackgammon/*
%{_pixmapsdir}/hicolor/*x*/apps/kbackgammon*.png

#################################################
#             KBATTLESHIP
#################################################

%files -f kbattleship.lang kbattleship
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbattleship
%{_applnkdir}/Games/Board/kbattleship.desktop
%{_datadir}/apps/kbattleship/*
%{_pixmapsdir}/hicolor/*x*/apps/kbattleship.png


#################################################
#             KBLACKBOX
#################################################

%files -f kblackbox.lang kblackbox
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kblackbox
%{_applnkdir}/Games/Board/kblackbox.desktop
%{_datadir}/apps/kblackbox/*
%{_pixmapsdir}/hicolor/*x*/apps/kblackbox.png

#################################################
#             KFOULEGGS
#################################################

%files -f kfouleggs.lang kfouleggs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfouleggs
%{_applnkdir}/Games/Arcade/kfouleggs.desktop
%{_datadir}/apps/kfouleggs/*

#################################################
#             KJEZZ
#################################################

#%files -f kjezz.lang kjezz
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kjezz
#%{_applnkdir}/Games/Arcade/kjezz.desktop
#%{_datadir}/apps/kjezz/*
#%{_pixmapsdir}/hicolor/*x*/apps/kjezz.png
#%{_pixmapsdir}/locolor/*x*/apps/kjezz.png

#################################################
#             KJUMPINGCUBE
#################################################

%files -f kjumpingcube.lang kjumpingcube
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjumpingcube
%{_applnkdir}/Games/TacticStrategy/kjumpingcube.desktop
%{_pixmapsdir}/hicolor/*x*/apps/kjumpingcube.png
%{_datadir}/apps/kjumpingcube/*

#################################################
#             KLINES
#################################################

%files -f klines.lang klines
%defattr(644,root,root,755)
%{_applnkdir}/Games/TacticStrategy/klines.desktop
%attr(755,root,root) %{_bindir}/klines
%{_datadir}/apps/klines/*
%{_pixmapsdir}/hicolor/*x*/apps/klines.png

#################################################
#             KMAHJONGG
#################################################

#%files -f kmahjongg.lang kmahjongg
%files kmahjongg
%defattr(644,root,root,755)
%{_applnkdir}/Games/Board/kmahjongg.desktop
%attr(755,root,root) %{_bindir}/kmahjongg
%{_datadir}/apps/kmahjongg/*
%{_pixmapsdir}/hicolor/*x*/apps/kmahjongg.png

#################################################
#             KMINES
#################################################

%files -f kmines.lang kmines
%defattr(644,root,root,755)
%{_applnkdir}/Games/TacticStrategy/kmines.desktop
%attr(755,root,root) %{_bindir}/kmines
%{_pixmapsdir}/hicolor/*x*/apps/kmines.png
%{_datadir}/apps/kmines/*

#################################################
#             KONQUEST
#################################################

%files -f konquest.lang konquest
%defattr(644,root,root,755)
%{_applnkdir}/Games/TacticStrategy/konquest.desktop
%attr(755,root,root) %{_bindir}/konquest
%{_datadir}/apps/konquest/*
%{_pixmapsdir}/hicolor/*x*/apps/konquest.png

#################################################
#             KPAT
#################################################

%files -f kpat.lang kpat
%defattr(644,root,root,755)
%{_applnkdir}/Games/Card/kpat.desktop
%attr(755,root,root) %{_bindir}/kpat
%{_datadir}/apps/kpat/*
%{_pixmapsdir}/hicolor/*x*/apps/kpat.png

#################################################
#             KPOKER
#################################################

%files -f kpoker.lang kpoker
%defattr(644,root,root,755)
%{_applnkdir}/Games/Card/kpoker.desktop
%attr(755,root,root) %{_bindir}/kpoker
%{_datadir}/apps/kpoker/*
%{_pixmapsdir}/hicolor/*x*/apps/kpoker.png

#################################################
#             KREVERSI
#################################################

%files -f kreversi.lang kreversi
%defattr(644,root,root,755)
%{_applnkdir}/Games/Board/kreversi.desktop
%attr(755,root,root) %{_bindir}/kreversi
%{_datadir}/apps/kreversi/*
%{_pixmapsdir}/hicolor/*x*/apps/kreversi.png

#################################################
#            KSAME
#################################################

%files -f ksame.lang ksame
%defattr(644,root,root,755)
%{_applnkdir}/Games/TacticStrategy/ksame.desktop
%attr(755,root,root) %{_bindir}/ksame
%{_datadir}/apps/ksame/*
%{_pixmapsdir}/hicolor/*x*/apps/ksame.png

#################################################
#             KSIRTET
#################################################

%files -f ksirtet.lang ksirtet
%defattr(644,root,root,755)
%{_applnkdir}/Games/Arcade/ksirtet.desktop
%attr(755,root,root) %{_bindir}/ksirtet
%{_libdir}/libksirtet*.la
%{_libdir}/libksirtet*.so.*.*.*
%{_datadir}/apps/ksirtet/*
%{_pixmapsdir}/hicolor/*x*/apps/ksirtet.png

#################################################
#             KSMILETRIS
#################################################

#%files -f ksmiletris.lang ksmiletris
%files ksmiletris
%defattr(644,root,root,755)
%{_applnkdir}/Games/Arcade/ksmiletris.desktop
%attr(755,root,root) %{_bindir}/ksmiletris
%{_datadir}/apps/ksmiletris/*
%{_pixmapsdir}/hicolor/*x*/apps/ksmiletris.png

#################################################
#             KSHISEN
#################################################

%files -f kshisen.lang kshisen
%defattr(644,root,root,755)
%{_applnkdir}/Games/Board/kshisen.desktop
%attr(755,root,root) %{_bindir}/kshisen
%{_datadir}/apps/kshisen/*
%{_pixmapsdir}/hicolor/*x*/apps/kshisen.png

#################################################
#             KSNAKE
#################################################

%files -f ksnake.lang ksnake
%defattr(644,root,root,755)
%{_applnkdir}/Games/Arcade/ksnake.desktop
%attr(755,root,games) %{_bindir}/ksnake
%{_datadir}/apps/ksnake/*
%{_pixmapsdir}/hicolor/*x*/apps/ksnake.png

#################################################
#             KSOKOBAN
#################################################

%files -f ksokoban.lang ksokoban
%defattr(644,root,root,755)
%{_applnkdir}/Games/TacticStrategy/ksokoban.desktop
%attr(755,root,root) %{_bindir}/ksokoban
%{_pixmapsdir}/hicolor/*x*/apps/ksokoban.png

#################################################
#             KSPACEDUEL
#################################################

%files -f kspaceduel.lang kspaceduel
%defattr(644,root,root,755)
%{_applnkdir}/Games/Arcade/kspaceduel.desktop
%attr(755,root,games) %{_bindir}/kspaceduel
%{_datadir}/apps/kspaceduel/*
%{_pixmapsdir}/hicolor/*x*/apps/kspaceduel.png
%{_pixmapsdir}/locolor/*x*/apps/kspaceduel.png

#################################################
#             KTRON
#################################################

%files -f ktron.lang ktron
%defattr(644,root,root,755)
%{_applnkdir}/Games/Arcade/ktron.desktop
%attr(755,root,games) %{_bindir}/ktron
%{_datadir}/apps/ktron/*
%{_pixmapsdir}/hicolor/*x*/apps/ktron.png

#################################################
#             KTUBERLING
#################################################

%files -f ktuberling.lang ktuberling
%defattr(644,root,root,755)
%{_applnkdir}/Amusements/ktuberling.desktop
%attr(755,root,games) %{_bindir}/ktuberling
%{_datadir}/apps/ktuberling/*
%{_pixmapsdir}/hicolor/*x*/apps/ktuberling.png

#################################################
#             KWIN4
#################################################

%files -f kwin4.lang kwin4
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwin4*
%{_applnkdir}/Games/Board/kwin4.desktop
%{_datadir}/apps/kwin4/*
%{_pixmapsdir}/hicolor/*x*/apps/kwin4.png

#################################################
#             LSKAT
#################################################

%files -f lskat.lang lskat
%defattr(644,root,root,755)
%{_applnkdir}/Games/Card/lskat.desktop
%attr(755,root,games) %{_bindir}/lskat
%attr(755,root,games) %{_bindir}/lskatproc
%{_datadir}/apps/lskat/*
%{_pixmapsdir}/hicolor/*x*/apps/lskat.png
%{_pixmapsdir}/locolor/*x*/apps/lskat.png

#################################################
#             KBOUNCE
#################################################

%files -f kbounce.lang kbounce
%defattr(644,root,root,755)
%{_bindir}/kbounce
%{_datadir}/apps/kbounce
%{_applnkdir}/Games/Arcade/kbounce.desktop
%{_pixmapsdir}/*/*/*/kbounce*

#################################################
#             KENOLABA
#################################################

%files -f kenolaba.lang kenolaba
%defattr(644,root,root,755)
%{_bindir}/kenolaba
%{_datadir}/apps/kenolaba
%{_applnkdir}/Games/Board/kenolaba.desktop
%{_pixmapsdir}/*/*/*/kenolaba*
