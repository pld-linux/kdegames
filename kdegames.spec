#
# Conditional build:
%bcond_without	highscore	# without system-wide score feature
%bcond_without	i18n		# don't build i18n packages per module
#
%define		_state		stable
%define		_ver		3.2.1
#define		_snap		040110

Summary:	K Desktop Environment - games
Summary(es):	K Desktop Environment - Juegos
Summary(ja):	KDE�ǥ����ȥå״Ķ� - ������
Summary(ko):	K ����ũž ȯ�� - ����(����)
Summary(pl):	K Desktop Environment - gry
Summary(pt_BR):	K Desktop Environment - Jogos
Summary(zh_CN):	KDE��Ϸ
Name:		kdegames
#Version:	%{_ver}.%{_snap}
Version:	%{_ver}
Release:	1
Epoch:		8
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications/Games
Source0:	http://download.kde.org/%{_state}/%{_ver}/src/%{name}-%{_ver}.tar.bz2
# Source0-md5:	60b05fa22dfc0ec812ca88dacb0249aa
%if %{with i18n}
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
# Source1-md5:	251018849e20c8df708f4da263cb72da
%endif
Patch0:		%{name}-3.2branch.diff
Patch1:		%{name}-disable_install-exec-hook.patch
BuildRequires:	ed
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdegames-kabalone
Obsoletes:	kdegames-megami
Obsoletes:	kdegames-kjezz
Obsoletes:	kdegames-kpm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libraries for kdegames. Included with this package are: kasteroids,
katomic, kbackgammon, kbattleship, kblackbox, kbounce, kenolaba,
kfouleggs, kgoldrunner, kjumpingcube, klickety, klines, kmahjongg,
kmines, kolf, konquest, kpat, kpoker, kreversi, ksame, kshisen,
ksirtet, ksmiletris, ksnake, ksokoban, kspaceduel, ktron, ktuberling,
kwin4, lskat.

%description -l es
Juegos para KDE. Incluidos en este paquete:

kasteroids: arcade, katomic, kbackgammon, kbattleship, kblackbox,
kbounce, kenolaba, kfouleggs, kgoldrunner, kjumpingcube, klickety,
klines, kmahjongg: el popular mahjongg, kmines: desarmar las minas,
kolf, konquest, kpat: juegos de cartas, incluso solitario, kpoker:
v�deo p�quer, kreversi: Reversi, ksame: un juego de tablero, kshisen:
Shisen-Sho - relacionado con el mahjongg, ksirtet, ksmiletris, ksnake:
corrida de las cobras, ksokoban, kspaceduel, ktron, kwin4, lskat.

%description -l ja
KDE�ǥ����ȥå״Ķ��ѤΥ����� �ʲ��Τ褦�ʥѥå����������äƤ��ޤ���

kasteroids: ���������ɥ�����, katomic, kbackgammon, kbattleship,
kblackbox: a strategy game with hidden boxes and rays, kbounce,
kenolaba, kfouleggs, kenolaba, kgoldrunner, kjumpingcube, klickety,
klines, kmahjongg: �峤 kmines: �ޥ��󥹥����ѡ�, kolf, konquest,
kpat: ����ѥȥ��ץ�����, kpoker: �ݡ���, kreversi: ��С���, ksame:
same game, kshisen: �����, ksirtet, ksmiletris, ksnake:
���͡����졼��, ksokoban: �Ҹ���, kspaceduel, ktron, kwin4, lskat

%description -l pl
Biblioteki dla gier KDE: kasteroids, katomic, kbackgammon,
kbattleship, kblackbox, kbounce, kenolaba, kfouleggs, kgoldrunner,
kjumpingcube, klickety, klines, kmahjongg, kmines, kolf, konquest,
kpat, kpoker, kreversi, ksame, kshisen, ksirtet, ksmiletris, ksnake,
ksokoban, kspaceduel, ktron, ktuberling, kwin4, lskat.

%description -l pt_BR
Jogos para o KDE. Inclu�dos neste pacote:

kasteroids: arcade, katomic, kblackbox, kbackgammon, kbattleship,
kbounce, kenolaba, kfouleggs, kgoldrunner, kjumpingcube, klickety,
klines, kmahjongg: o popular mahjongg, kmines: desarmar as minas,
kolf, konquest, kpat: jogos de cartas, inclusive paci�ncia, kpoker:
v�deo-poker, kreversi: Reversi, ksame: um jogo de tabuleiro, kshisen:
Shisen-Sho - relacionado com o mahjongg, ksirtet, ksmiletris, ksnake:
corrida das cobras, ksokoban, kspaceduel, ktron, kwin4, lskat.

%package devel
Summary:	Development files for KDE games
Summary(pl):	Pliki przydatne tw�rcom gier dla KDE
Summary(pt_BR):	Arquivos de inclus�o do kdegames
Group:		X11/Development/Libraries
Requires:	kdelibs-devel >= 9:%{version}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-atlantik = %{epoch}:%{version}-%{release}
Requires:	%{name}-kolf = %{epoch}:%{version}-%{release}

%description devel
Development files for KDE games.

%description devel -l pl
Pliki dla programist�w KDE games.

%description devel -l pt_BR
Este pacote det�m os arquivos de inclus�o necess�rios para compilar
aplicativos que usam bibliotecas do kdegames.

%package atlantik
Summary:	KDE client for playing Monopoly-like games
Summary(pl):	Klient KDE do grania w gry typu Monopoly
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description atlantik
Atlantik is a KDE client for Monopoly-like board games to be played on
the monopd network.

%description atlantik -l pl
Atlantik to klient KDE dla gier planszowych typu Monopoly, kt�rym
mo�na gra� w sieci monopd.

%package carddecks
Summary:	KDE carddecks
Summary(pl):	Karcianki dla KDE
Summary(pt_BR):	Biblioteca de baralhos para jogos do KDE que usem cartas
Group:		X11/Applications/Games
Requires:	kdelibs >= 9:%{version}

%description carddecks
KDE carddecks.

%description carddecks -l pl
Karcianki dla KDE.

%description carddecks -l pt_BR
Biblioteca de baralhos para jogos do KDE que usem cartas.

%package kasteroids
Summary:	KDE Asteroids clone
Summary(pl):	Klon Asteroids dla KDE
Summary(pt_BR):	Destrua os aster�ides para n�o ser destru�do
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description kasteroids
Asteroids clone for KDE.

%description kasteroids -l pl
Klon znanej gry "Asteroids".

%description kasteroids -l pt_BR
Destrua os aster�ides para n�o ser destru�do.

%package katomic
Summary:	KDE Sokoban clone
Summary(pl):	Klon gry Sokoban dla KDE
Summary(pt_BR):	Jogo semelhante ao Sokoban mas o objetivo � formar mol�culas
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description katomic
Atomic Entertainment is a small game which resembles Sokoban. The
Object of the game is to build chemical molecules on a Sokoban like
board.

%description katomic -l pl
Atomic to ma�a gra podobna do gry Sokoban. Celem gry jest zbudowanie
cz�steczek chemicznych na planszy podobnej do tej z gry Sokoban.

%description katomic -l pt_BR
Jogo semelhante ao Sokoban mas o objetivo � formar mol�culas.

%package kbackgammon
Summary:	Backgammon program for KDE
Summary(pl):	Backgammon dla KDE
Summary(pt_BR):	Jogo de gam�o para KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description kbackgammon
KBackgammon is a graphical backgammon program for KDE. It supports
backgammon games with other players, games against computer engines
like GNU bg and even on-line games on the First Internet Backgammon
Server.

%description kbackgammon -l pl
KBackgammon to graficzna wersja gry backgammon dla KDE. Mo�na gra� z
innymi graczami, przeciwko komputerowi lub nawet rozegra� parti� przez
sie� korzystaj�c z Pierwszego Internetowego Serwera Backgammona.

%description kbackgammon -l pt_BR
Jogo de gam�o para KDE.

%package kbattleship
Summary:	Battleship for KDE
Summary(pl):	Statki dla KDE
Summary(pt_BR):	Jogo de batalha naval com servidor embutido
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description kbattleship
Battleship for KDE.

%description kbattleship -l pl
Statki dla KDE.

%description kbattleship -l pt_BR
Jogo de batalha naval com servidor embutido.

%package kblackbox
Summary:	A little logical game for KDE
Summary(pl):	Prosta gra logiczna
Summary(pt_BR):	Vers�o do jogo Blackbox do Emacs para KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description kblackbox
A little logical game for KDE.

%description kblackbox -l pl
Prosta gra logiczna.

%description kblackbox -l pt_BR
Vers�o do jogo Blackbox do Emacs para KDE.

%package kbounce
Summary:	Claim areas and don't get disturbed
Summary(pl):	Gra polegaj�ca na pozyskiwaniu terenu wbrew przeciwnikom
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description kbounce
Claim areas and don't get disturbed.

%description kbounce -l pl
Gra polegaj�ca na pozyskiwaniu terenu wbrew przeciwnikom.

%package kenolaba
Summary:	Abalone-like board game against the computer
Summary(pl):	Gra planszowa podobna do Abalone przeciwko komputerowi
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description kenolaba
Abalone-like board game against the computer.

%description kenolaba -l pl
Gra planszowa podobna do Abalone przeciwko komputerowi.

%package kfouleggs
Summary:	KDE kfouleggs
Summary(pl):	Gra kfouleggs dla KDE
Summary(pt_BR):	Mais um jogo que lembra o estilo Tetris
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description kfouleggs
KDE kfouleggs.

%description kfouleggs -l pl
Gra kfouleggs dla KDE.

%description kfouleggs -l pt_BR
Mais um jogo que lembra o estilo Tetris.

%package kgoldrunner
Summary:	A KDE clone of Lode Runner (TM) Commodore game
Summary(pl):	Klon gry Lode Runner dla KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description kgoldrunner
KGoldrunner is based on the Lode Runner (TM) game written in the USA
by Doug Smith in 1983 for the Apple II and Commodore 64 computers.

%description kgoldrunner -l pl
KGoldrunner jest oparty na grze Lode Runner (TM) napisanej w 1983 w
USA przez Douga Smitha na komputery Apple II i Commodore 64.

%package kjumpingcube
Summary:	A little tactical game for KDE
Summary(pl):	Prosta gra taktyczna dla KDE
Summary(pt_BR):	Jogo de estrat�gia para 2 contendores
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description kjumpingcube
KJumpingCube is a simple tactical game. You can play it against the
computer or against the friend. The playing field consists of squares
that contains points. By clicking on the squares you can increase the
points, and if the points reach a maximum the points will jump to the
squares neighbours and take them over. Winer is the one, who owns all
squares.

%description kjumpingcube -l pl
KJumpingCube to prosta gra taktyczna. Mo�na w ni� gra� przeciwko
komputerowi lub przeciwko koledze. Plansza do gry zawiera pola, kt�re
zawieraj� punkty. Przez klikanie na pola zwi�ksza si� liczb� punkt�w
na nich. Gdy liczba punkt�w na okre�lonym polu osi�gnie maksymaln�
warto��, punkty przeskakuj� na s�siednie pola przejmuj�c je tym samym
na w�asno��. Zwyci�zca jest jeden - to ten, kto przejmie wszystkie
pola na w�asno��.

%description kjumpingcube -l pt_BR
Jogo de estrat�gia para 2 contendores.

%package klickety
Summary:	A Clickomania-alike game for KDE
Summary(pl):	Gra dla KDE podobna do Clickomanii
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description klickety
Klickety is an adaptation of the (perharps) well-known Clickomania
game; it is very similar to the "same" game.

%description klickety -l pl
Klickety to adaptacja bardziej znanej gry Clickomania. Jest podobna do
gry "same".

%package klines
Summary:	Lines for KDE
Summary(pl):	Gra Lines dla KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description klines
Lines for KDE.

%description klines -l pl
Gra Lines dla KDE.

%package kmahjongg
Summary:	KDE Mahjongg clone
Summary(pl):	Klon gry Mahjongg dla KDE
Summary(pt_BR):	Vers�o do jogo Mahjongg para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description kmahjongg
This program is a clone of the well known Mahjongg game.

%description kmahjongg -l pl
Wersja KDE znanej gry Mahjongg.

%description kmahjongg -l pt_BR
Vers�o do jogo Mahjongg para o KDE.

%package kmines
Summary:	KDE minesweeper game
Summary(pl):	Saper dla KDE
Summary(pt_BR):	Vers�o do jogo 'ca�a-minas' para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description kmines
This is a very classical minesweeper written from scratch.
- 3 predefined levels (Easy: 8x8 with 10 mines, Normal: 16x16 with 40
  mines, Expert: 30x16 with 99 mines)
- Custom levels
- High Scores.

%description kmines -l pl
Wersja klasycznej gry "saper" dla KDE, napisana od zera. Cechy:
- 3 predefiniowane poziomy (�atwy - 8x8 z 10 minami, normalny - 16x16
  z 40 minami, dla ekspert�w - 30x16 z 99 minami)
- definiowalne poziomy
- lista najlepszych wynik�w.

%description kmines -l pt_BR
Vers�o do jogo 'ca�a-minas' para o KDE.

%package kolf
Summary:	Miniature golf for KDE
Summary(pl):	Mini golf
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description kolf
Kolf - miniature golf for KDE.

%description kolf -l pl
Kolf - mini golf dla KDE.

%package konquest
Summary:	KDE version of Gnu-Lactic Konquest
Summary(pl):	Podb�j galaktyki dla KDE
Summary(pt_BR):	Jogo espacial de estrat�gia
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description konquest
KDE version of Gnu-Lactic Konquest.

%description konquest -l pl
Podb�j galaktyki dla KDE.

%description konquest -l pt_BR
Jogo espacial de estrat�gia.

%package kpat
Summary:	KDE solitaire patience game
Summary(pl):	Pasjanse dla KDE
Summary(pt_BR):	Vers�o do jogo 'Paci�ncia' para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-carddecks = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description kpat
KDE solitaire patience games.

%description kpat -l pl
Program umo�liwia uk�adanie kilku rodzaj�w pasjans�w.

%description kpat -l pt_BR
Vers�o do jogo 'Paci�ncia' para o KDE.

%package kpoker
Summary:	KDE poker
Summary(pl):	Poker dla KDE
Summary(pt_BR):	Jogo de v�deo-p�quer para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-carddecks = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description kpoker
A simple video poker clone for the KDE desktop environment.

%description kpoker -l pl
Prosty poker dla KDE.

%description kpoker -l pt_BR
Jogo de v�deo-p�quer para o KDE.

%package kreversi
Summary:	KDE Reversi game
Summary(pl):	Gra Reversi dla KDE
Summary(pt_BR):	Jogo no estilo Otelo para KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description kreversi
Reversi is a simple strategy game that is played by two players. There
is only one type of piece - one side of it is black, the other white.
If a player captures a piece on the board, that piece is turned and
belongs to that player. The winner is the person that has more pieces
of his own color on the board and if there are no more moves possible.

%description kreversi -l pl
Reversi to prosta gra strategiczna dla dw�ch graczy. Jest tylko jeden
rodzaj pionu - z jednej strony czarny, z drugiej bia�y. Je�li gracz
schwyta pion na planszy, jest on obracany i nale�y do tego gracza.
Zwyci�zc� jest osoba, kt�ra ma na planszy wi�cej pion�w w swoim
kolorze w chwili, gdy nie mo�na ju� wykona� �adnego ruchu.

%description kreversi -l pt_BR
Jogo no estilo Otelo para KDE.

%package ksame
Summary:	KDE SameGame
Summary(pl):	"To Samo" dla KDE
Summary(pt_BR):	Jogo relaxante onde voc� deve remover o maior n�mero poss�vel de bolas
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description ksame
KSame is a simple game. It's played by one player, so there is only
one winner :-) You play for fun and against the highscore. It has been
inspired by SameGame, that is only famous on the Macintosh platform.

%description ksame -l pl
KSame to prosta gra dla jednego gracza. Mo�na gra� dla zabawy i dla
wyniku. Gra jest zainspirowana gr� SameGame, s�ynn� tylko na
Macintoshach.

%description ksame -l pt_BR
Jogo relaxante onde voc� deve remover o maior n�mero poss�vel de
bolinhas.

%package kshisen
Summary:	KDE Shisen-Sho
Summary(pl):	Shisen-Sho dla KDE
Summary(pt_BR):	Jogo Shisen para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description kshisen
Shisen-Sho is similar to Mahjongg and uses the same set of tiles as
Mahjongg.

%description kshisen -l pl
Shisen-Sho to gra podobna do Mahjongg i wykorzystuj�ca ten sam zestaw
ko�ci.

%description kshisen -l pt_BR
Jogo Shisen para o KDE.

%package ksirtet
Summary:	KDE Tetris
Summary(pl):	Tetris dla KDE
Summary(pt_BR):	Jogo no estilo Tetris
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

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
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description ksmiletris
This program is a clone of the well-known game Tetris.

%description ksmiletris -l pl
Kolejny klon dobrze znanego Tetrisa.

%description ksmiletris -l pt_BR
Jogo no estilo Tetris para o KDE.

%package ksnake
Summary:	KDE Snake Race
Summary(pl):	Wy�cig W�y dla KDE
Summary(pt_BR):	Jogo da cobra sempre crescente para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description ksnake
Snake Race is a game of speed and agility. You are a hungry snake and
are trying to eat all the apples in the room before getting out!

%description ksnake -l pl
Snake Race to gra szybko�ciowo-zr�czno�ciowa. Gracz wciela si� w
g�odnego w�a pr�buj�cego zje�� wszystkie jab�ka w pomieszczeniu.

%description ksnake -l pt_BR
Jogo da cobra sempre crescente para o KDE.

%package ksokoban
Summary:	KDE Sokoban
Summary(pl):	Sokoban dla KDE
Summary(pt_BR):	Jogo Sokoban ou 'Fiscal de Estoque' para o KDE
Group:		X11/Applications/Games
Requires:	kdebase-core >= 9:%{version}

%description ksokoban
The Japanese warehouse keeper game.

%description ksokoban -l pl
Gra w japo�skiego magazyniera.

%description ksokoban -l pt_BR
Jogo Sokoban ou 'Fiscal de Estoque' para o KDE.

%package kspaceduel
Summary:	KDE space arcade game for two players
Summary(pl):	Gra zr�czno�ciowa pod KDE dla dw�ch graczy
Summary(pt_BR):	Vers�o do jogo Duelo Espacial para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description kspaceduel
Each player control a ship that flies around the sun and tries to
shoot at the other ship. You can play KSpaceduel with another person,
against the computer, or you can have the computer control both ships
and play each other.

%description kspaceduel -l pl
Ka�dy z graczy kieruje statkiem, kt�ry lata dooko�a s�o�ca i pr�buje
zestrzeli� drugi statek. Mo�na gra� w KSpaceduel z inn� osob�, z
komputerem, lub pozwoli�, aby komputer kierowa� obydwoma statkami.

%description kspaceduel -l pt_BR
Vers�o do jogo Duelo Espacial para o KDE.

%package ktron
Summary:	Trone clone for KDE
Summary(pl):	Klon Trone dla KDE
Summary(pt_BR):	Vers�o do jogo Tron / Motos de Luz para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description ktron
KTron is a simple Trone-Clone for the KDE. You can play KTron against
the computer or a friend.

The aim of the game is to live longer then your opponent. To do That,
avoid running into a wall, your own tail and that of your opponent.

%description ktron -l pl
KTron to prosty klon Trone dla KDE. Mo�na gra� w KTron przeciwko
komputerowi lub koledze.

Celem gry jest prze�ycie d�u�ej ni� przeciwnik. Aby tego dokona�
trzeba unika� uderzenia w �cian�, ogon w�asny lub przeciwnika.

%description ktron -l pt_BR
Vers�o do jogo Tron / Motos de Luz para o KDE.

%package ktuberling
Summary:	KDE game for small children
Summary(pl):	Gra dla ma�ych dzieci
Summary(pt_BR):	Jogo de desenho do 'Homem-batata' para crian�as
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description ktuberling
It is a potato editor. That means that you can drag and drop eyes,
mouths, moustache, and other parts of face and goodies onto a
potato-like guy.

There is no winer. The only purpose is to make the funniest faces you
can.

%description ktuberling -l pl
KTuberling to edytor ziemniak�w. Oznacza to, �e mo�na uk�ada� oczy,
usta, w�sy oraz inne cz�ci twarzy na posta� podobn� do ziemniaka.

W grze nie ma zwyci�zcy. Jedynym celem gry jest stworzenie
najzabawniejszej twarzy, jak� si� da u�o�y�.

%description ktuberling -l pt_BR
Jogo de desenho do 'Homem-batata' para crian�as.

%package kwin4
Summary:	Four wins for KDE
Summary(pl):	Gra "cztery wygrywa" dla KDE
Summary(pt_BR):	Jogo de estrat�gia que lembra um pouco o Otelo
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description kwin4
Four wins is a game for two players. Each player is represented by a
colour (yellow and red). The goal of the game is to get four connected
pieces of your colour into a row, column or any diagonal. This is done
by placing one of your pieces into any of the seven columns. A piece
will begin to fill a column from the bottom, i.e. it will fall down
until it reaches the ground level or another stone. After a move is
done it is the turn of the other player. This is repeated until the
game is over, i.e. one of the players has four pieces in a row, column
or diagonal or no more moves are possible because the board is filled.

%description kwin4 -l pl
Cztery wygrywa jest gr� dla dw�ch graczy. Ka�dy gracz jest
reprezentowany przez kolor (��ty b�d� czerwony). Celem gry jest
ustawienie czterech klock�w twojego koloru w rz�d, kolumn� lub po
przek�tnej. Klocki wype�niaj� kolumny od do�u, tj. spadaj� dop�ki nie
dosi�gn� pod�o�a b�d� innego klocka. Gra trwa do momentu uzyskania ww.
uk�adu b�d� do zape�nienia tablicy.

%description kwin4 -l pt_BR
Jogo de estrat�gia que lembra um pouco o Otelo.

%package lskat
Summary:	KDE lskat
Summary(pl):	Lskat dla KDE
Summary(pt_BR):	Jogo de cartas Lieutenant Skat para KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-carddecks = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description lskat
Lieutnant Skat.

%description lskat -l pl
Lskat dla KDE.

%description lskat -l pt_BR
Jogo de cartas Lieutenant Skat para KDE

%package megami
Summary:	Popular Gambling Game
Summary(pl):	Popularna gra hazardowa
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-carddecks = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description megami
Popular Gambling Game.

%description megami -l pl
Popularna gra hazardowa.

%package i18n
Summary:	Common internationalization and localization files for kdegames
Summary(pl):	Wsp�dzielone pliki umi�dzynarodawiaj�ce dla kdegames
Group:		X11/Applications
Requires:	kdelibs-i18n >= 9:%{version}

%description i18n
Common internationalization and localization files for kdegames.

%description i18n -l pl
Pliki umi�dzynarodawiaj�ce wsp�lne dla kdegames.

%package kmahjongg-i18n
Summary:	Internationalization and localization files for kmahjongg
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kmahjongga
Group:		X11/Applications
Requires:	%{name}-kmahjongg = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kmahjongg-i18n
Internationalization and localization files for kmahjongg.

%description kmahjongg-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kmahjongga.

%package ksmiletris-i18n
Summary:	Internationalization and localization files for ksmiletris
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla ksmiletrisa
Group:		X11/Applications
Requires:	%{name}-ksmiletris = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description ksmiletris-i18n
Internationalization and localization files for ksmiletris.

%description ksmiletris-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla ksmiletrisa.

%package atlantik-i18n
Summary:	Internationalization and localization files for atlantik
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla atlantika
Group:		X11/Applications
Requires:	%{name}-atlantik = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description atlantik-i18n
Internationalization and localization files for atlantik.

%description atlantik-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla atlantika.

%package kasteroids-i18n
Summary:	Internationalization and localization files for kasteroids
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kasteroids
Group:		X11/Applications
Requires:	%{name}-kasteroids = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kasteroids-i18n
Internationalization and localization files for kasteroids.

%description kasteroids-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kasteroids.

%package katomic-i18n
Summary:	Internationalization and localization files for katomic
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla katomic
Group:		X11/Applications
Requires:	%{name}-katomic = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description katomic-i18n
Internationalization and localization files for katomic.

%description katomic-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla katomic.

%package kbackgammon-i18n
Summary:	Internationalization and localization files for kbackgammon
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kbackgammona
Group:		X11/Applications
Requires:	%{name}-kbackgammon = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kbackgammon-i18n
Internationalization and localization files for kbackgammon.

%description kbackgammon-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kbackgammona.

%package kbattleship-i18n
Summary:	Internationalization and localization files for kbattleship
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kbattleship
Group:		X11/Applications
Requires:	%{name}-kbattleship = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kbattleship-i18n
Internationalization and localization files for kbattleship.

%description kbattleship-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kbattleship.

%package kblackbox-i18n
Summary:	Internationalization and localization files for kblackbox
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kblackboksa
Group:		X11/Applications
Requires:	%{name}-kblackbox = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kblackbox-i18n
Internationalization and localization files for kblackbox.

%description kblackbox-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kblackboksa.

%package kbounce-i18n
Summary:	Internationalization and localization files for kbounce
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kbounce
Group:		X11/Applications
Requires:	%{name}-kbounce = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kbounce-i18n
Internationalization and localization files for kbounce.

%description kbounce-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kbounce.

%package kenolaba-i18n
Summary:	Internationalization and localization files for kenolaba
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kenolaby
Group:		X11/Applications
Requires:	%{name}-kenolaba = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kenolaba-i18n
Internationalization and localization files for kenolaba.

%description kenolaba-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kenolaby.

%package kfouleggs-i18n
Summary:	Internationalization and localization files for kfouleggs
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kfouleggs
Group:		X11/Applications
Requires:	%{name}-kfouleggs = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kfouleggs-i18n
Internationalization and localization files for kfouleggs.

%description kfouleggs-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kfouleggs.

%package kgoldrunner-i18n
Summary:	Internationalization and localization files for kgoldrunner
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kgoldrunnera
Group:		X11/Applications
Requires:	%{name}-kgoldrunner = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kgoldrunner-i18n
Internationalization and localization files for kgoldrunner.

%description kgoldrunner-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kgoldrunnera.

%package kjumpingcube-i18n
Summary:	Internationalization and localization files for kjumpingcube
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kjumpingcube
Group:		X11/Applications
Requires:	%{name}-kjumpingcube = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kjumpingcube-i18n
Internationalization and localization files for kjumpingcube.

%description kjumpingcube-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kjumpingcube.

%package klickety-i18n
Summary:	Internationalization and localization files for klickety
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla klickety
Group:		X11/Applications
Requires:	%{name}-klickety = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description klickety-i18n
Internationalization and localization files for klickety.

%description klickety-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla klickety.

%package klines-i18n
Summary:	Internationalization and localization files for klines
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla klines
Group:		X11/Applications
Requires:	%{name}-klines = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description klines-i18n
Internationalization and localization files for klines.

%description klines-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla klines.

%package kmines-i18n
Summary:	Internationalization and localization files for kmines
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kmines
Group:		X11/Applications
Requires:	%{name}-kmines = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kmines-i18n
Internationalization and localization files for kmines.

%description kmines-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kmines.

%package kolf-i18n
Summary:	Internationalization and localization files for kolf
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kolfa
Group:		X11/Applications
Requires:	%{name}-kolf = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kolf-i18n
Internationalization and localization files for kolf.

%description kolf-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kolfa.

%package konquest-i18n
Summary:	Internationalization and localization files for konquest
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla konquesta
Group:		X11/Applications
Requires:	%{name}-konquest = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description konquest-i18n
Internationalization and localization files for konquest.

%description konquest-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla konquesta.

%package kpat-i18n
Summary:	Internationalization and localization files for kpat
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kpata
Group:		X11/Applications
Requires:	%{name}-kpat = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kpat-i18n
Internationalization and localization files for kpat.

%description kpat-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kpata.

%package kpoker-i18n
Summary:	Internationalization and localization files for kpoker
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kpokera
Group:		X11/Applications
Requires:	%{name}-kpoker = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kpoker-i18n
Internationalization and localization files for kpoker.

%description kpoker-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kpokera.

%package kreversi-i18n
Summary:	Internationalization and localization files for kreversi
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kreversi
Group:		X11/Applications
Requires:	%{name}-kreversi = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kreversi-i18n
Internationalization and localization files for kreversi.

%description kreversi-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kreversi.

%package ksame-i18n
Summary:	Internationalization and localization files for ksame
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla ksame
Group:		X11/Applications
Requires:	%{name}-ksame = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description ksame-i18n
Internationalization and localization files for ksame.

%description ksame-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla ksame.

%package kshisen-i18n
Summary:	Internationalization and localization files for kshisen
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kshisen
Group:		X11/Applications
Requires:	%{name}-kshisen = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kshisen-i18n
Internationalization and localization files for kshisen.

%description kshisen-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kshisen.

%package ksirtet-i18n
Summary:	Internationalization and localization files for ksirtet
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla ksirteta
Group:		X11/Applications
Requires:	%{name}-ksirtet = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description ksirtet-i18n
Internationalization and localization files for ksirtet.

%description ksirtet-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla ksirteta.

%package ksnake-i18n
Summary:	Internationalization and localization files for ksnake
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla ksnake'a
Group:		X11/Applications
Requires:	%{name}-ksnake = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description ksnake-i18n
Internationalization and localization files for ksnake.

%description ksnake-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla ksnake'a.

%package ksokoban-i18n
Summary:	Internationalization and localization files for ksokoban
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla ksokobana
Group:		X11/Applications
Requires:	%{name}-ksokoban = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description ksokoban-i18n
Internationalization and localization files for ksokoban.

%description ksokoban-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla ksokobana.

%package kspaceduel-i18n
Summary:	Internationalization and localization files for kspaceduel
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kspaceduel
Group:		X11/Applications
Requires:	%{name}-kspaceduel = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kspaceduel-i18n
Internationalization and localization files for kspaceduel.

%description kspaceduel-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kspaceduel.

%package ktron-i18n
Summary:	Internationalization and localization files for ktron
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla ktrona
Group:		X11/Applications
Requires:	%{name}-ktron = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description ktron-i18n
Internationalization and localization files for ktron.

%description ktron-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla ktrona.

%package ktuberling-i18n
Summary:	Internationalization and localization files for ktuberling
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla ktuberlinga
Group:		X11/Applications
Requires:	%{name}-ktuberling = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description ktuberling-i18n
Internationalization and localization files for ktuberling.

%description ktuberling-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla ktuberlinga.

%package kwin4-i18n
Summary:	Internationalization and localization files for kwin4
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla kwin4
Group:		X11/Applications
Requires:	%{name}-kwin4 = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kwin4-i18n
Internationalization and localization files for kwin4.

%description kwin4-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla kwin4.

%package lskat-i18n
Summary:	Internationalization and localization files for lskat
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla lskata
Group:		X11/Applications
Requires:	%{name}-lskat = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description lskat-i18n
Internationalization and localization files for lskat.

%description lskat-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla lskata.

%package megami-i18n
Summary:	Internationalization and localization files for megami
Summary(pl):	Pliki umi�dzynarodawiaj�ce dla megami
Group:		X11/Applications
Requires:	%{name}-megami = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description megami-i18n
Internationalization and localization files for megami.

%description megami-i18n -l pl
Pliki umi�dzynarodawiaj�ce dla megami.

%prep
#%setup -q -n %{name}-%{_snap}
%setup -q
#%patch0 -p1
%patch1 -p1

%build
cp %{_datadir}/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--with-qt-libraries=%{_libdir} \
	--enable-final \
	%{?with_highscore:--enable-highscore-dir=/var/games}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

mv $RPM_BUILD_ROOT%{_iconsdir}/{lo,hi}color/16x16/apps/lskat.png

cp libkdegames/highscore/INSTALL ./README.highscore

%if %{with highscore}
install -d $RPM_BUILD_ROOT/var/games
touch $RPM_BUILD_ROOT/var/games/k{fouleggs,lickety,mines,sirtet}.scores
%endif

%if %{with i18n}
if [ -f "%{SOURCE1}" ] ; then
	bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT
	for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo; do
		if [ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] ; then
		rm -f $f
		fi
	done
else
	echo "No i18n sources found and building --with i18n. FIXIT!"
	exit 1
fi
%endif

%find_lang atlantik	--with-kde
%find_lang kasteroids	--with-kde
%find_lang katomic	--with-kde
%find_lang kbackgammon	--with-kde
%find_lang kbattleship	--with-kde
%find_lang kblackbox	--with-kde
%find_lang kbounce	--with-kde
%find_lang kenolaba	--with-kde
%find_lang kfouleggs	--with-kde
%find_lang kgoldrunner	--with-kde
%find_lang kjumpingcube	--with-kde
%find_lang klickety	--with-kde
%find_lang klines	--with-kde
%find_lang kmines	--with-kde
%find_lang kolf		--with-kde
%find_lang konquest	--with-kde
%find_lang kpat		--with-kde
%find_lang kpoker	--with-kde
%find_lang kreversi	--with-kde
%find_lang ksame	--with-kde
%find_lang kshisen	--with-kde
%find_lang ksirtet	--with-kde
%find_lang ksnake	--with-kde
%find_lang ksokoban	--with-kde
%find_lang kspaceduel	--with-kde
%find_lang ktron	--with-kde
%find_lang ktuberling	--with-kde
%find_lang kwin4	--with-kde
%find_lang lskat	--with-kde

%if %{with i18n}
%find_lang libksirtet	--with-kde
cat libksirtet.lang >> ksirtet.lang
%find_lang kmahjongg	--with-kde
%find_lang ksmiletris	--with-kde

> i18n.lang
%find_lang desktop_kdegames	--with-kde
cat desktop_kdegames.lang >> i18n.lang
%find_lang libkdegames	--with-kde
cat libkdegames.lang >> i18n.lang
%find_lang libkdehighscores	--with-kde
cat libkdehighscores.lang >> i18n.lang

for i in $RPM_BUILD_ROOT%{_datadir}/apps/sounds/* ;
do
	echo $i
	if [ -d $i ] ; then
	z=`echo $i|sed -e s,${RPM_BUILD_ROOT}%{_datadir}/apps/sounds/,,`
	echo %lang\($z\) %{_datadir}/apps/sounds/$z >> ktuberling.lang
	fi
done
%endif

files="atlantik \
kasteroids \
katomic \
kbackgammon \
kbattleship \
kblackbox \
kbounce \
kenolaba \
kfouleggs \
kgoldrunner \
kjumpingcube \
klickety \
klines \
kmines \
kolf	 \
konquest \
kpat	 \
kpoker \
kreversi \
ksame \
kshisen \
ksirtet \
ksnake \
ksokoban \
kspaceduel \
ktron \
ktuberling \
kwin4 \
lskat"

for i in $files; do
	echo "%defattr(644,root,root,755)" > ${i}_en.lang
	grep en\/ ${i}.lang|grep -v apidocs >> ${i}_en.lang
	grep -v apidocs $i.lang|grep -v en\/ > ${i}.lang.1
	mv ${i}.lang.1 ${i}.lang
done

durne=`ls -1 *.lang|grep -v _en`

for i in $durne; 
do
	echo $i >> control
	grep -v en\/ $i|grep -v apidocs >> ${i}.1
	if [ -f ${i}.1 ] ; then
		mv ${i}.1 ${i}
	fi
done

%clean
rm -rf $RPM_BUILD_ROOT

%post			-p /sbin/ldconfig
%postun			-p /sbin/ldconfig

%post	atlantik	-p /sbin/ldconfig
%postun	atlantik	-p /sbin/ldconfig

%post	kolf		-p /sbin/ldconfig
%postun	kolf		-p /sbin/ldconfig

%if %{with highscore}
%post 	kfouleggs
cat << EOF

 *******************************************************
 *                                                     *
 * NOTE:                                               *
 * You must set sgid "games" for kfouleggs binary      *
 * to use system-wide highscore file.                  *
 *                                                     *
 * See the README.highscore stored in kdegames package *
 * documentation for details.                          *
 *                                                     *
 *******************************************************

EOF

%post 	klickety
cat << EOF

 *******************************************************
 *                                                     *
 * NOTE:                                               *
 * You must set sgid "games" for klickety binary       *
 * to use system-wide highscore file.                  *
 *                                                     *
 * See the README.highscore stored in kdegames package *
 * documentation for details.                          *
 *                                                     *
 *******************************************************

EOF

%post 	kmines
cat << EOF

 *******************************************************
 *                                                     *
 * NOTE:                                               *
 * You must set sgid "games" for kmines binary         *
 * to use system-wide highscore file.                  *
 *                                                     *
 * See the README.highscore stored in kdegames package *
 * documentation for details.                          *
 *                                                     *
 *******************************************************

EOF

%post 	ksirtet
cat << EOF

 *******************************************************
 *                                                     *
 * NOTE:                                               *
 * You must set sgid "games" for ksirtet binary        *
 * to use system-wide highscore file.                  *
 *                                                     *
 * See the README.highscore stored in kdegames package *
 * documentation for details.                          *
 *                                                     *
 *******************************************************

EOF
%endif

%if %{with i18n}
%files ksmiletris-i18n -f ksmiletris.lang
%files kmahjongg-i18n -f kmahjongg.lang
%files i18n -f i18n.lang

%files atlantik-i18n -f atlantik.lang
%files kasteroids-i18n -f kasteroids.lang
%files katomic-i18n -f katomic.lang
%files kbackgammon-i18n -f kbackgammon.lang
%files kbattleship-i18n -f kbattleship.lang
%files kblackbox-i18n -f kblackbox.lang
%files kbounce-i18n -f kbounce.lang
%files kenolaba-i18n -f kenolaba.lang
%files kfouleggs-i18n -f kfouleggs.lang
%files kgoldrunner-i18n -f kgoldrunner.lang
%files kjumpingcube-i18n -f kjumpingcube.lang
%files klickety-i18n -f klickety.lang
%files klines-i18n -f klines.lang
%files kmines-i18n -f kmines.lang
%files kolf-i18n -f kolf.lang
%files konquest-i18n -f konquest.lang
%files kpat-i18n -f kpat.lang
%files kpoker-i18n -f kpoker.lang
%files kreversi-i18n -f kreversi.lang
%files ksame-i18n -f ksame.lang
%files kshisen-i18n -f kshisen.lang
%files ksirtet-i18n -f ksirtet.lang
%files ksnake-i18n -f ksnake.lang
%files ksokoban-i18n -f ksokoban.lang
%files kspaceduel-i18n -f kspaceduel.lang
%files ktron-i18n -f ktron.lang
%files ktuberling-i18n -f ktuberling.lang
%files kwin4-i18n -f kwin4.lang
%files lskat-i18n -f lskat.lang
#%files megami-i18n -f megami.lang
%endif

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README README.highscore
%{_libdir}/libkdegames.la
%attr(755,root,root) %{_libdir}/libkdegames.so.*.*.*
%{_datadir}/apps/kdegames
%{_iconsdir}/*/*/actions/endturn.png
%{_iconsdir}/*/*/*/highscore.png
%{_iconsdir}/*/*/*/roll.png

%files devel
%defattr(644,root,root,755)
##%lang(en) %{_kdedocdir}/en/%{name}-apidocs
%attr(755,root,root) %{_libdir}/libatlantic.so
%attr(755,root,root) %{_libdir}/libatlantikclient.so
%attr(755,root,root) %{_libdir}/libatlantikui.so
%attr(755,root,root) %{_libdir}/libkdegames.so
%attr(755,root,root) %{_libdir}/libkolf.so
%{_includedir}/*

%files carddecks
%defattr(644,root,root,755)
%{_datadir}/apps/carddecks

%files atlantik -f atlantik_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/atlantik
%{_libdir}/libatlantic.la
%attr(755,root,root) %{_libdir}/libatlantic.so.*.*.*
%{_libdir}/libatlantikclient.la
%attr(755,root,root) %{_libdir}/libatlantikclient.so.*.*.*
%{_libdir}/libatlantikui.la
%attr(755,root,root) %{_libdir}/libatlantikui.so.*
%{_libdir}/kde3/kio_atlantik.la
%attr(755,root,root) %{_libdir}/kde3/kio_atlantik.so
%{_datadir}/apps/atlantik
%{_datadir}/services/atlantik.protocol
%{_desktopdir}/kde/atlantik.desktop
%{_iconsdir}/*/*/apps/atlantik.png

%files kasteroids -f kasteroids_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kasteroids
%{_datadir}/apps/kasteroids
%{_datadir}/config.kcfg/kasteroids.kcfg
%{_desktopdir}/kde/kasteroids.desktop
%{_iconsdir}/*/*/apps/kasteroids.png

%files katomic -f katomic_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/katomic
%{_datadir}/apps/katomic
%{_desktopdir}/kde/katomic.desktop
%{_iconsdir}/*/*/apps/katomic.png

%files kbackgammon -f kbackgammon_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbackgammon
%{_datadir}/apps/kbackgammon
%{_desktopdir}/kde/kbackgammon.desktop
%{_iconsdir}/*/*/apps/kbackgammon*.png

%files kbattleship -f kbattleship_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbattleship
%{_datadir}/apps/kbattleship
%{_desktopdir}/kde/kbattleship.desktop
%{_iconsdir}/*/*/apps/kbattleship.png

%files kblackbox -f kblackbox_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kblackbox
%{_datadir}/apps/kblackbox
%{_desktopdir}/kde/kblackbox.desktop
%{_iconsdir}/*/*/apps/kblackbox.png

%files kbounce -f kbounce_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbounce
%{_datadir}/apps/kbounce
%{_desktopdir}/kde/kbounce.desktop
%{_iconsdir}/[!l]*/*/*/kbounce*

%files kenolaba -f kenolaba_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kenolaba
%{_datadir}/apps/kenolaba
%{_desktopdir}/kde/kenolaba.desktop
%{_iconsdir}/*/*/*/kenolaba*

%files kfouleggs -f kfouleggs_en.lang
%defattr(644,root,root,755)
%{?with_highscore:%attr(660,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/kfouleggs.scores}
%attr(755,root,root) %{_bindir}/kfouleggs
%{_datadir}/apps/kfouleggs
%{_datadir}/config.kcfg/kfouleggs.kcfg
%{_desktopdir}/kde/kfouleggs.desktop

%files kgoldrunner -f kgoldrunner_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgoldrunner
%{_datadir}/apps/kgoldrunner
%{_desktopdir}/kde/KGoldrunner.desktop
%{_iconsdir}/hicolor/*/apps/kgoldrunner.png

%files kjumpingcube -f kjumpingcube_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjumpingcube
%{_datadir}/apps/kjumpingcube
%{_datadir}/config.kcfg/kjumpingcube.kcfg
%{_desktopdir}/kde/kjumpingcube.desktop
%{_iconsdir}/*/*/apps/kjumpingcube.png

%files klickety -f klickety_en.lang
%defattr(644,root,root,755)
%{?with_highscore:%attr(660,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/klickety.scores}
%attr(755,root,root) %{_bindir}/klickety
%{_datadir}/apps/klickety
%{_desktopdir}/kde/klickety.desktop

%files klines -f klines_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klines
%{_datadir}/apps/klines
%{_datadir}/config.kcfg/klines.kcfg
%{_desktopdir}/kde/klines.desktop
%{_iconsdir}/*/*/apps/klines.png

%files kmahjongg
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmahjongg
%{_datadir}/apps/kmahjongg
%{_datadir}/config.kcfg/kmahjongg.kcfg
%{_desktopdir}/kde/kmahjongg.desktop
%{_iconsdir}/*/*/apps/kmahjongg.png

%files kmines -f kmines_en.lang
%defattr(644,root,root,755)
%{?with_highscore:%attr(660,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/kmines.scores}
%attr(755,root,root) %{_bindir}/kmines
%{_datadir}/apps/kmines
%{_desktopdir}/kde/kmines.desktop
%{_iconsdir}/*/*/apps/kmines.png

%files kolf -f kolf_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kolf
%{_libdir}/libkdeinit_kolf.la
%attr(755,root,root) %{_libdir}/libkdeinit_kolf.so
%{_libdir}/libkolf.la
%attr(755,root,root) %{_libdir}/libkolf.so.*.*.*
%{_libdir}/kde3/kolf.la
%attr(755,root,root) %{_libdir}/kde3/kolf.so
%{_datadir}/config/magic
%{_datadir}/apps/kolf
%{_datadir}/mimelnk/application/*
%{_desktopdir}/kde/kolf.desktop
%{_iconsdir}/*/*/apps/kolf.png

%files konquest -f konquest_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konquest
%{_datadir}/apps/konquest
%{_desktopdir}/kde/konquest.desktop
%{_iconsdir}/*/*/apps/konquest.png

%files kpat -f kpat_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpat
%{_datadir}/apps/kpat
%{_desktopdir}/kde/kpat.desktop
%{_iconsdir}/*/*/apps/kpat.png

%files kpoker -f kpoker_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpoker
%{_datadir}/apps/kpoker
%{_desktopdir}/kde/kpoker.desktop
%{_iconsdir}/*/*/apps/kpoker.png

%files kreversi -f kreversi_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kreversi
%{_datadir}/apps/kreversi
%{_datadir}/config.kcfg/kreversi.kcfg
%{_desktopdir}/kde/kreversi.desktop
%{_iconsdir}/*/*/apps/kreversi.png

%files ksame -f ksame_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksame
%{_datadir}/apps/ksame
%{_desktopdir}/kde/ksame.desktop
%{_iconsdir}/*/*/apps/ksame.png

%files kshisen -f kshisen_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kshisen
%{_datadir}/apps/kshisen
%{_desktopdir}/kde/kshisen.desktop
%{_iconsdir}/*/*/apps/kshisen.png

%files ksirtet -f ksirtet_en.lang
%defattr(644,root,root,755)
%{?with_highscore:%attr(660,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/ksirtet.scores}
%attr(755,root,root) %{_bindir}/ksirtet
%{_datadir}/apps/ksirtet
%{_datadir}/config.kcfg/ksirtet.kcfg
%{_desktopdir}/kde/ksirtet.desktop
%{_iconsdir}/*/*/apps/ksirtet.png

%files ksmiletris
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksmiletris
%{_datadir}/apps/ksmiletris
%{_desktopdir}/kde/ksmiletris.desktop
%{_iconsdir}/*/*/apps/ksmiletris.png

%files ksnake -f ksnake_en.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/ksnake
%{_datadir}/apps/ksnake
%{_desktopdir}/kde/ksnake.desktop
%{_iconsdir}/*/*/apps/ksnake.png

%files ksokoban -f ksokoban_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksokoban
%{_desktopdir}/kde/ksokoban.desktop
%{_iconsdir}/*/*/apps/ksokoban.png

%files kspaceduel -f kspaceduel_en.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/kspaceduel
%{_datadir}/apps/kspaceduel
%{_datadir}/config.kcfg/kspaceduel.kcfg
%{_desktopdir}/kde/kspaceduel.desktop
%{_iconsdir}/[!l]*/*/apps/kspaceduel.png

%files ktron -f ktron_en.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/ktron
%{_datadir}/apps/ktron
%{_datadir}/config.kcfg/ktron.kcfg
%{_desktopdir}/kde/ktron.desktop
%{_iconsdir}/*/*/apps/ktron.png

%files ktuberling -f ktuberling_en.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/ktuberling
%{_datadir}/apps/ktuberling
%{_desktopdir}/kde/ktuberling.desktop
%{_iconsdir}/*/*/apps/ktuberling.png

%files kwin4 -f kwin4_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwin4*
%{_datadir}/apps/kwin4
%{_desktopdir}/kde/kwin4.desktop
%{_iconsdir}/*/*/apps/kwin4.png

%files lskat -f lskat_en.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/lskat
%attr(755,root,games) %{_bindir}/lskatproc
%{_datadir}/apps/lskat
%{_desktopdir}/kde/lskat.desktop
%{_iconsdir}/[!l]*/*/apps/lskat.png

#%files megami -f megami_en.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/megami
#%{_datadir}/apps/megami
#%{_desktopdir}/kde/megami.desktop
#%{_iconsdir}/*/*/apps/megami.png
