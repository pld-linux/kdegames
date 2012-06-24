#
# Conditional build:
%bcond_without	highscore	# without system-wide score feature
#
%define		_state		stable
%define		_ver		3.2.3
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
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	801b257188acca5e525a997bd03f1234
Icon:		kde-games.xpm
Patch100:	%{name}-branch.diff
Patch0:		%{name}-disable_install-exec-hook.patch
BuildRequires:	ed
BuildRequires:	autoconf
BuildRequires:	unsermake >= 040511
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdegames-kabalone
Obsoletes:	kdegames-megami
Obsoletes:	kdegames-kjezz
Obsoletes:	kdegames-kpm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libraries for kdegames which contain highscore support functions.

%description -l pl
Biblioteki dla gier KDE zawieraj�ce wsparcie dla tabel wynik�w.

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
Backgrounds for carddecks in KDE card games.

%description carddecks -l pl
T�a dla talii kart w karcianki pod KDE.

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
KBlackbox is a game of hide and seek played on an grid of boxes. Your
opponent (the Random number generator, in this case) has hidden
several balls within this box. By shooting rays into the box and
observing where they emerge it is possible to deduce the positions of
the hidden balls. The fewer rays you use to find the balls, the better
(the lower) your score.

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
Abalone-like board game against the computer. Kenolaba is a simple
board strategy game that is played by two players. There are red and
yellow pieces for each player. Beginning from a position where each
player has 14 pieces, moves are drawn until one player has pushed 6 of
his opponent's pieces out of the board.

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
KDE kfouleggs (a tetris clone).

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
Lines for KDE. The main rules of game is as simple as possible: you
move (using mouse) marbles from cell to cell and build lines
(horizontal, vertical or diagonal). When a line contains 5 or more
marbles - they are removed from the field and your score grows. After
each of your turns computer drops three more marbles onto the field.

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
Kolf is a miniature golf game with block graphics and a 2d top-down
view. Courses are dynamic, and up to 10 people can play at once in
competition.

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
This the KDE version of Gnu-Lactic Konquest, a multi-player strategy
game. The goal of the game is to expand your interstellar empire
across the galaxy and of course, crush your rivals in the process.

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
KMahjongg. The object of the game is to remove all tiles from the
field.

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
Lieutenant skat (from German Offiziersskat) is a card game for two
players. It is roughly played according to the rules of Skat but with
only two players and simplified rules. Every player has a set of cards
in front of him/her, half of them covered and half of them open. Both
players try to win more than 60 of the 120 possible points. After 16
moves all cards are played and the game ends.

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

%prep
#%setup -q -n %{name}-%{_snap}
%setup -q
%patch100 -p1
%patch0 -p1

%build
cp %{_datadir}/automake/config.sub admin
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
export UNSERMAKE=%{_datadir}/unsermake/unsermake
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
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

mv $RPM_BUILD_ROOT%{_iconsdir}/{lo,hi}color/16x16/apps/lskat.png

cp libkdegames/highscore/INSTALL ./README.highscore

%if %{with highscore}
install -d $RPM_BUILD_ROOT/var/games
touch $RPM_BUILD_ROOT/var/games/k{fouleggs,lickety,mines,sirtet}.scores
%endif

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

%files atlantik
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
%{_kdedocdir}/en/atlantik

%files kasteroids
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kasteroids
%{_datadir}/apps/kasteroids
%{_datadir}/config.kcfg/kasteroids.kcfg
%{_desktopdir}/kde/kasteroids.desktop
%{_iconsdir}/*/*/apps/kasteroids.png
%{_kdedocdir}/en/kasteroids

%files katomic
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/katomic
%{_datadir}/apps/katomic
%{_desktopdir}/kde/katomic.desktop
%{_iconsdir}/*/*/apps/katomic.png
%{_kdedocdir}/en/katomic

%files kbackgammon
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbackgammon
%{_datadir}/apps/kbackgammon
%{_desktopdir}/kde/kbackgammon.desktop
%{_iconsdir}/*/*/apps/kbackgammon*.png
%{_kdedocdir}/en/kbackgammon

%files kbattleship
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbattleship
%{_datadir}/apps/kbattleship
%{_desktopdir}/kde/kbattleship.desktop
%{_iconsdir}/*/*/apps/kbattleship.png
%{_kdedocdir}/en/kbattleship

%files kblackbox
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kblackbox
%{_datadir}/apps/kblackbox
%{_desktopdir}/kde/kblackbox.desktop
%{_iconsdir}/*/*/apps/kblackbox.png
%{_kdedocdir}/en/kblackbox

%files kbounce
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbounce
%{_datadir}/apps/kbounce
%{_desktopdir}/kde/kbounce.desktop
%{_iconsdir}/[!l]*/*/*/kbounce*
%{_kdedocdir}/en/kbounce

%files kenolaba
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kenolaba
%{_datadir}/apps/kenolaba
%{_desktopdir}/kde/kenolaba.desktop
%{_iconsdir}/*/*/*/kenolaba*
%{_kdedocdir}/en/kenolaba

%files kfouleggs
%defattr(644,root,root,755)
%{?with_highscore:%attr(660,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/kfouleggs.scores}
%attr(755,root,root) %{_bindir}/kfouleggs
%{_datadir}/apps/kfouleggs
%{_datadir}/config.kcfg/kfouleggs.kcfg
%{_desktopdir}/kde/kfouleggs.desktop
%{_kdedocdir}/en/kfouleggs

%files kgoldrunner
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgoldrunner
%{_datadir}/apps/kgoldrunner
%{_desktopdir}/kde/KGoldrunner.desktop
%{_iconsdir}/hicolor/*/apps/kgoldrunner.png
%{_kdedocdir}/en/kgoldrunner

%files kjumpingcube
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjumpingcube
%{_datadir}/apps/kjumpingcube
%{_datadir}/config.kcfg/kjumpingcube.kcfg
%{_desktopdir}/kde/kjumpingcube.desktop
%{_iconsdir}/*/*/apps/kjumpingcube.png
%{_kdedocdir}/en/kjumpingcube

%files klickety
%defattr(644,root,root,755)
%{?with_highscore:%attr(660,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/klickety.scores}
%attr(755,root,root) %{_bindir}/klickety
%{_datadir}/apps/klickety
%{_desktopdir}/kde/klickety.desktop
%{_kdedocdir}/en/klickety

%files klines
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klines
%{_datadir}/apps/klines
%{_datadir}/config.kcfg/klines.kcfg
%{_desktopdir}/kde/klines.desktop
%{_iconsdir}/*/*/apps/klines.png
%{_kdedocdir}/en/klines

%files kmahjongg
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmahjongg
%{_datadir}/apps/kmahjongg
%{_datadir}/config.kcfg/kmahjongg.kcfg
%{_desktopdir}/kde/kmahjongg.desktop
%{_iconsdir}/*/*/apps/kmahjongg.png

%files kmines
%defattr(644,root,root,755)
%{?with_highscore:%attr(660,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/kmines.scores}
%attr(755,root,root) %{_bindir}/kmines
%{_datadir}/apps/kmines
%{_desktopdir}/kde/kmines.desktop
%{_iconsdir}/*/*/apps/kmines.png
%{_kdedocdir}/en/kmines

%files kolf
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
%{_kdedocdir}/en/kolf

%files konquest
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konquest
%{_datadir}/apps/konquest
%{_desktopdir}/kde/konquest.desktop
%{_iconsdir}/*/*/apps/konquest.png
%{_kdedocdir}/en/konquest

%files kpat
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpat
%{_datadir}/apps/kpat
%{_desktopdir}/kde/kpat.desktop
%{_iconsdir}/*/*/apps/kpat.png
%{_kdedocdir}/en/kpat

%files kpoker
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpoker
%{_datadir}/apps/kpoker
%{_desktopdir}/kde/kpoker.desktop
%{_iconsdir}/*/*/apps/kpoker.png
%{_kdedocdir}/en/kpoker

%files kreversi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kreversi
%{_datadir}/apps/kreversi
%{_datadir}/config.kcfg/kreversi.kcfg
%{_desktopdir}/kde/kreversi.desktop
%{_iconsdir}/*/*/apps/kreversi.png
%{_kdedocdir}/en/kreversi

%files ksame
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksame
%{_datadir}/apps/ksame
%{_desktopdir}/kde/ksame.desktop
%{_iconsdir}/*/*/apps/ksame.png
%{_kdedocdir}/en/ksame

%files kshisen
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kshisen
%{_datadir}/apps/kshisen
%{_desktopdir}/kde/kshisen.desktop
%{_iconsdir}/*/*/apps/kshisen.png
%{_kdedocdir}/en/kshisen

%files ksirtet
%defattr(644,root,root,755)
%{?with_highscore:%attr(660,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/ksirtet.scores}
%attr(755,root,root) %{_bindir}/ksirtet
%{_datadir}/apps/ksirtet
%{_datadir}/config.kcfg/ksirtet.kcfg
%{_desktopdir}/kde/ksirtet.desktop
%{_iconsdir}/*/*/apps/ksirtet.png
%{_kdedocdir}/en/ksirtet

%files ksmiletris
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksmiletris
%{_datadir}/apps/ksmiletris
%{_desktopdir}/kde/ksmiletris.desktop
%{_iconsdir}/*/*/apps/ksmiletris.png

%files ksnake
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/ksnake
%{_datadir}/apps/ksnake
%{_desktopdir}/kde/ksnake.desktop
%{_iconsdir}/*/*/apps/ksnake.png
%{_kdedocdir}/en/ksnake

%files ksokoban
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksokoban
%{_desktopdir}/kde/ksokoban.desktop
%{_iconsdir}/*/*/apps/ksokoban.png
%{_kdedocdir}/en/ksokoban

%files kspaceduel
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/kspaceduel
%{_datadir}/apps/kspaceduel
%{_datadir}/config.kcfg/kspaceduel.kcfg
%{_desktopdir}/kde/kspaceduel.desktop
%{_iconsdir}/[!l]*/*/apps/kspaceduel.png
%{_kdedocdir}/en/kspaceduel

%files ktron
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/ktron
%{_datadir}/apps/ktron
%{_datadir}/config.kcfg/ktron.kcfg
%{_desktopdir}/kde/ktron.desktop
%{_iconsdir}/*/*/apps/ktron.png
%{_kdedocdir}/en/ktron

%files ktuberling
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/ktuberling
%{_datadir}/apps/ktuberling
%{_desktopdir}/kde/ktuberling.desktop
%{_iconsdir}/*/*/apps/ktuberling.png
%{_kdedocdir}/en/ktuberling

%files kwin4
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwin4*
%{_datadir}/apps/kwin4
%{_desktopdir}/kde/kwin4.desktop
%{_iconsdir}/*/*/apps/kwin4.png
%{_kdedocdir}/en/kwin4

%files lskat
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/lskat
%attr(755,root,games) %{_bindir}/lskatproc
%{_datadir}/apps/lskat
%{_desktopdir}/kde/lskat.desktop
%{_iconsdir}/[!l]*/*/apps/lskat.png
%{_kdedocdir}/en/lskat

#%files megami -f megami_en.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/megami
#%{_datadir}/apps/megami
#%{_desktopdir}/kde/megami.desktop
#%{_iconsdir}/*/*/apps/megami.png
