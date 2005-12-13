# Conditional build:
%bcond_without	apidocs		# do not prepare API documentation
%bcond_without	highscore	# without system-wide score feature

%define		_state		stable
%define		_kdever		3.5
%define		_ver		3.5.0

%define		_minlibsevr	9:3.5.0
%define		_minbaseevr	9:3.5.0

Summary:	K Desktop Environment - games
Summary(es):	K Desktop Environment - Juegos
Summary(ja):	KDE¥Ç¥¹¥¯¥È¥Ã¥×´Ä¶­ - ¥²¡¼¥à
Summary(ko):	K µ¥½ºÅ©Å¾ È¯°æ - ³îÀÌ(°ÔÀÓ)
Summary(pl):	K Desktop Environment - gry
Summary(pt_BR):	K Desktop Environment - Jogos
Summary(zh_CN):	KDEÓÎÏ·
Name:		kdegames
Version:	%{_ver}
Release:	1
Epoch:		8
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications/Games
Icon:		kde-games.xpm
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_kdever}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	ba86fe9280ca57698ce3be0e0242b140
Patch1:		kde-common-PLD.patch
Patch2:		%{name}-disable_install-exec-hook.patch
#BuildRequires:	unsermake
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_apidocs:BuildRequires:	doxygen}
%{?with_apidocs:BuildRequires:	graphviz}
BuildRequires:	kdelibs-devel >= %{_minlibsevr}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdegames-kabalone
Obsoletes:	kdegames-megami
Obsoletes:	kdegames-kjezz
Obsoletes:	kdegames-kpm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libraries for kdegames which contain highscore support functions.

%description -l pl
Biblioteki dla gier KDE zawieraj±ce wsparcie dla tabel wyników.

%package devel
Summary:	Development files for KDE games
Summary(pl):	Pliki przydatne twórcom gier dla KDE
Summary(pt_BR):	Arquivos de inclusão do kdegames
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-atlantik = %{epoch}:%{version}-%{release}
Requires:	%{name}-kolf = %{epoch}:%{version}-%{release}
Requires:	kdelibs-devel >= %{_minlibsevr}

%description devel
Development files for KDE games.

%description devel -l pl
Pliki dla programistów KDE games.

%description devel -l pt_BR
Este pacote detém os arquivos de inclusão necessários para compilar
aplicativos que usam bibliotecas do kdegames.

%package apidocs
Summary:	API documentation
Summary(pl):	Dokumentacja API
Group:		Documentation
Requires:	kdelibs >= %{_minlibsevr}

%description apidocs
API documentation.

%description apidocs -l pl
Dokumentacja API.

%package atlantik
Summary:	KDE client for playing Monopoly-like games
Summary(pl):	Klient KDE do grania w gry typu Monopoly
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description atlantik
Atlantik is a KDE client for Monopoly-like board games to be played on
the monopd network.

%description atlantik -l pl
Atlantik to klient KDE dla gier planszowych typu Monopoly, którym
mo¿na graæ w sieci monopd.

%package carddecks
Summary:	KDE carddecks
Summary(pl):	Karcianki dla KDE
Summary(pt_BR):	Biblioteca de baralhos para jogos do KDE que usem cartas
Group:		X11/Applications/Games
Requires:	kdelibs >= %{_minlibsevr}

%description carddecks
Backgrounds for carddecks in KDE card games.

%description carddecks -l pl
T³a dla talii kart w karcianki pod KDE.

%description carddecks -l pt_BR
Biblioteca de baralhos para jogos do KDE que usem cartas.

%package kasteroids
Summary:	KDE Asteroids clone
Summary(pl):	Klon Asteroids dla KDE
Summary(pt_BR):	Destrua os asteróides para não ser destruído
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

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
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description katomic
Atomic Entertainment is a small game which resembles Sokoban. The
Object of the game is to build chemical molecules on a Sokoban like
board.

%description katomic -l pl
Atomic to ma³a gra podobna do gry Sokoban. Celem gry jest zbudowanie
cz±steczek chemicznych na planszy podobnej do tej z gry Sokoban.

%description katomic -l pt_BR
Jogo semelhante ao Sokoban mas o objetivo é formar moléculas.

%package kbackgammon
Summary:	Backgammon program for KDE
Summary(pl):	Backgammon dla KDE
Summary(pt_BR):	Jogo de gamão para KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description kbackgammon
KBackgammon is a graphical backgammon program for KDE. It supports
backgammon games with other players, games against computer engines
like GNU bg and even on-line games on the First Internet Backgammon
Server.

%description kbackgammon -l pl
KBackgammon to graficzna wersja gry backgammon dla KDE. Mo¿na graæ z
innymi graczami, przeciwko komputerowi lub nawet rozegraæ partiê przez
sieæ korzystaj±c z Pierwszego Internetowego Serwera Backgammona.

%description kbackgammon -l pt_BR
Jogo de gamão para KDE.

%package kbattleship
Summary:	Battleship for KDE
Summary(pl):	Statki dla KDE
Summary(pt_BR):	Jogo de batalha naval com servidor embutido
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

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
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description kblackbox
KBlackbox is a game of hide and seek played on an grid of boxes. Your
opponent (the Random number generator, in this case) has hidden
several balls within this box. By shooting rays into the box and
observing where they emerge it is possible to deduce the positions of
the hidden balls. The fewer rays you use to find the balls, the better
(the lower) your score.

%description kblackbox -l pl
KBlackbox to gra w ukrywanie i szukanie rozgrywana na siatce pude³ek.
Przeciwnik (w tym wypadku generator liczb losowych) ukry³ kilka pi³ek
w tym pude³ku. Poprzez strzelanie promieniami w pude³ko i obserwowanie
jak siê wynurzaj± mo¿na wydedukowaæ po³o¿enie ukrytych pi³ek. Im mniej
promieni u¿yje siê do znalezienia pi³ek, tym lepszy (mniejszy) jest
wynik.

%description kblackbox -l pt_BR
Versão do jogo Blackbox do Emacs para KDE.

%package kbounce
Summary:	Claim areas and don't get disturbed
Summary(pl):	Gra polegaj±ca na pozyskiwaniu terenu wbrew przeciwnikom
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description kbounce
Claim areas and don't get disturbed.

%description kbounce -l pl
Gra polegaj±ca na pozyskiwaniu terenu wbrew przeciwnikom.

%package kenolaba
Summary:	Abalone-like board game against the computer
Summary(pl):	Gra planszowa podobna do Abalone przeciwko komputerowi
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description kenolaba
Abalone-like board game against the computer. Kenolaba is a simple
board strategy game that is played by two players. There are red and
yellow pieces for each player. Beginning from a position where each
player has 14 pieces, moves are drawn until one player has pushed 6 of
his opponent's pieces out of the board.

%description kenolaba -l pl
Gra planszowa podobna do Abalone przeciwko komputerowi. Kenolaba to
prosta planszowa gra strategiczna dla dwóch graczy. S± pionki czerwone
i ¿ó³te dla obu graczy. Zaczyna siê z miejsca, gdzie ka¿dy gracz ma 14
pionów i toczy siê dopóki który¶ z graczy wypchnie 6 pionów
przeciwnika poza planszê.

%package kfouleggs
Summary:	KDE kfouleggs
Summary(pl):	Gra kfouleggs dla KDE
Summary(pt_BR):	Mais um jogo que lembra o estilo Tetris
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

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
Requires:	kdebase-core >= %{_minbaseevr}

%description kgoldrunner
KGoldrunner is based on the Lode Runner (TM) game written in the USA
by Doug Smith in 1983 for the Apple II and Commodore 64 computers.

%description kgoldrunner -l pl
KGoldrunner jest oparty na grze Lode Runner (TM) napisanej w 1983 w
USA przez Douga Smitha na komputery Apple II i Commodore 64.

%package kjumpingcube
Summary:	A little tactical game for KDE
Summary(pl):	Prosta gra taktyczna dla KDE
Summary(pt_BR):	Jogo de estratégia para 2 contendores
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description kjumpingcube
KJumpingCube is a simple tactical game. You can play it against the
computer or against the friend. The playing field consists of squares
that contains points. By clicking on the squares you can increase the
points, and if the points reach a maximum the points will jump to the
squares neighbours and take them over. Winer is the one, who owns all
squares.

%description kjumpingcube -l pl
KJumpingCube to prosta gra taktyczna. Mo¿na w ni± graæ przeciwko
komputerowi lub przeciwko koledze. Plansza do gry zawiera pola, które
zawieraj± punkty. Przez klikanie na pola zwiêksza siê liczbê punktów
na nich. Gdy liczba punktów na okre¶lonym polu osi±gnie maksymaln±
warto¶æ, punkty przeskakuj± na s±siednie pola przejmuj±c je tym samym
na w³asno¶æ. Zwyciêzca jest jeden - to ten, kto przejmie wszystkie
pola na w³asno¶æ.

%description kjumpingcube -l pt_BR
Jogo de estratégia para 2 contendores.

%package klickety
Summary:	A Clickomania-alike game for KDE
Summary(pl):	Gra dla KDE podobna do Clickomanii
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

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
Requires:	kdebase-core >= %{_minbaseevr}

%description klines
Lines for KDE. The main rules of game is as simple as possible: you
move (using mouse) marbles from cell to cell and build lines
(horizontal, vertical or diagonal). When a line contains 5 or more
marbles - they are removed from the field and your score grows. After
each of your turns computer drops three more marbles onto the field.

%description klines -l pl
Gra Lines dla KDE. Podstawowe zasady gry s± najprostsze jak to
mo¿liwe: przesuwa siê (przy u¿yciu muszy) klocki z pola na pole i
buduje linie (poziome, pionowe lub uko¶ne). Kiedy linia zawiera 5 lub
wiêcej klocków - s± usuwane z pola i wynik wzrasta. Po ka¿dym ruchu
gracza komputer zrzuca trzy dodatkowe klocki.

%package kmahjongg
Summary:	KDE Mahjongg clone
Summary(pl):	Klon gry Mahjongg dla KDE
Summary(pt_BR):	Versão do jogo Mahjongg para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

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
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description kmines
This is a very classical minesweeper written from scratch.
- 3 predefined levels (Easy: 8x8 with 10 mines, Normal: 16x16 with 40
  mines, Expert: 30x16 with 99 mines)
- Custom levels
- High Scores.

%description kmines -l pl
Wersja klasycznej gry "saper" dla KDE, napisana od zera. Cechy:
- 3 predefiniowane poziomy (³atwy - 8x8 z 10 minami, normalny - 16x16
  z 40 minami, dla ekspertów - 30x16 z 99 minami)
- definiowalne poziomy
- lista najlepszych wyników.

%description kmines -l pt_BR
Versão do jogo 'caça-minas' para o KDE.

%package knetwalk
Summary:	KDE knetwalk
Summary(pl):	knetwalk dla KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description knetwalk
The aim of this game is to connect the network with a minimum amount
of clicks.

%description knetwalk -l pl
Celem tej gry jest po³±czenie sieci minimaln± liczb± klikniêæ.

%package kolf
Summary:	Miniature golf for KDE
Summary(pl):	Mini golf
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description kolf
Kolf is a miniature golf game with block graphics and a 2D top-down
view. Courses are dynamic, and up to 10 people can play at once in
competition.

%description kolf -l pl
Kolf to miniaturowa gra w golfa z blokowa grafik± i dwuwymiarowym
widokiem. Rundy s± dynamiczne, a w zawodach mo¿e graæ do 10 osób
naraz.

%package konquest
Summary:	KDE version of Gnu-Lactic Konquest
Summary(pl):	Podbój galaktyki - wersja KDE gry Gnu-Lactic Konquest
Summary(pt_BR):	Jogo espacial de estratégia
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description konquest
This the KDE version of Gnu-Lactic Konquest, a multi-player strategy
game. The goal of the game is to expand your interstellar empire
across the galaxy and of course, crush your rivals in the process.

%description konquest -l pl
To jest wersja KDE gry Gnu-Lactic Konquest - gry strategicznej dla
wielu graczy. Celem gry jest rozszerzenie imperium miêdzygwiezdnego
poprzez galaktyki, i oczywi¶cie niszczenie w tym czasie przeciwników.

%description konquest -l pt_BR
Jogo espacial de estratégia.

%package kpat
Summary:	KDE solitaire patience game
Summary(pl):	Pasjanse dla KDE
Summary(pt_BR):	Versão do jogo 'Paciência' para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-carddecks = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description kpat
KDE solitaire patience games.

%description kpat -l pl
Program dla KDE umo¿liwiaj±cy uk³adanie kilku rodzajów pasjansów.

%description kpat -l pt_BR
Versão do jogo 'Paciência' para o KDE.

%package kpoker
Summary:	KDE poker
Summary(pl):	Poker dla KDE
Summary(pt_BR):	Jogo de vídeo-pôquer para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-carddecks = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description kpoker
A simple video poker clone for the KDE desktop environment.

%description kpoker -l pl
Prosty poker dla KDE.

%description kpoker -l pt_BR
Jogo de vídeo-pôquer para o KDE.

%package kreversi
Summary:	KDE Reversi game
Summary(pl):	Gra Reversi dla KDE
Summary(pt_BR):	Jogo no estilo Otelo para KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description kreversi
Reversi is a simple strategy game that is played by two players. There
is only one type of piece - one side of it is black, the other white.
If a player captures a piece on the board, that piece is turned and
belongs to that player. The winner is the person that has more pieces
of his own color on the board and if there are no more moves possible.

%description kreversi -l pl
Reversi to prosta gra strategiczna dla dwóch graczy. Jest tylko jeden
rodzaj pionu - z jednej strony czarny, z drugiej bia³y. Je¶li gracz
schwyta pion na planszy, jest on obracany i nale¿y do tego gracza.
Zwyciêzc± jest osoba, która ma na planszy wiêcej pionów w swoim
kolorze w chwili, gdy nie mo¿na ju¿ wykonaæ ¿adnego ruchu.

%description kreversi -l pt_BR
Jogo no estilo Otelo para KDE.

%package ksame
Summary:	KDE SameGame
Summary(pl):	"To Samo" dla KDE
Summary(pt_BR):	Jogo relaxante onde você deve remover o maior número possível de bolas
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description ksame
KSame is a simple game. It's played by one player, so there is only
one winner :-) You play for fun and against the highscore. It has been
inspired by SameGame, that is only famous on the Macintosh platform.

%description ksame -l pl
KSame to prosta gra dla jednego gracza. Mo¿na graæ dla zabawy i dla
wyniku. Gra jest zainspirowana gr± SameGame, s³ynn± tylko na
Macintoshach.

%description ksame -l pt_BR
Jogo relaxante onde você deve remover o maior número possível de
bolinhas.

%package kshisen
Summary:	KDE Shisen-Sho
Summary(pl):	Shisen-Sho dla KDE
Summary(pt_BR):	Jogo Shisen para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description kshisen
Shisen-Sho is similar to Mahjongg and uses the same set of tiles as
KMahjongg. The object of the game is to remove all tiles from the
field.

%description kshisen -l pl
Shisen-Sho to gra podobna do Mahjongg i wykorzystuj±ca ten sam zestaw
kostek. Celem gry jest usuniêcie wszystkich kostek z planszy.

%description kshisen -l pt_BR
Jogo Shisen para o KDE.

%package ksirtet
Summary:	KDE Tetris
Summary(pl):	Tetris dla KDE
Summary(pt_BR):	Jogo no estilo Tetris
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

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
Requires:	kdebase-core >= %{_minbaseevr}

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
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description ksnake
Snake Race is a game of speed and agility. You are a hungry snake and
are trying to eat all the apples in the room before getting out!

%description ksnake -l pl
Snake Race to gra szybko¶ciowo-zrêczno¶ciowa. Gracz wciela siê w
g³odnego wê¿a próbuj±cego zje¶æ wszystkie jab³ka w pomieszczeniu.

%description ksnake -l pt_BR
Jogo da cobra sempre crescente para o KDE.

%package ksokoban
Summary:	KDE Sokoban
Summary(pl):	Sokoban dla KDE
Summary(pt_BR):	Jogo Sokoban ou 'Fiscal de Estoque' para o KDE
Group:		X11/Applications/Games
Requires:	kdebase-core >= %{_minbaseevr}

%description ksokoban
The Japanese warehouse keeper game.

%description ksokoban -l pl
Gra w japoñskiego magazyniera.

%description ksokoban -l pt_BR
Jogo Sokoban ou 'Fiscal de Estoque' para o KDE.

%package kspaceduel
Summary:	KDE space arcade game for two players
Summary(pl):	Gra zrêczno¶ciowa pod KDE dla dwóch graczy
Summary(pt_BR):	Versão do jogo Duelo Espacial para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description kspaceduel
Each player control a ship that flies around the sun and tries to
shoot at the other ship. You can play KSpaceduel with another person,
against the computer, or you can have the computer control both ships
and play each other.

%description kspaceduel -l pl
Ka¿dy z graczy kieruje statkiem, który lata dooko³a s³oñca i próbuje
zestrzeliæ drugi statek. Mo¿na graæ w KSpaceduel z inn± osob±, z
komputerem, lub pozwoliæ, aby komputer kierowa³ obydwoma statkami.

%description kspaceduel -l pt_BR
Versão do jogo Duelo Espacial para o KDE.

%package ktron
Summary:	Trone clone for KDE
Summary(pl):	Klon Trone dla KDE
Summary(pt_BR):	Versão do jogo Tron / Motos de Luz para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description ktron
KTron is a simple Trone-Clone for the KDE. You can play KTron against
the computer or a friend.

The aim of the game is to live longer then your opponent. To do That,
avoid running into a wall, your own tail and that of your opponent.

%description ktron -l pl
KTron to prosty klon Trone dla KDE. Mo¿na graæ w KTron przeciwko
komputerowi lub koledze.

Celem gry jest prze¿ycie d³u¿ej ni¿ przeciwnik. Aby tego dokonaæ
trzeba unikaæ uderzenia w ¶cianê, ogon w³asny lub przeciwnika.

%description ktron -l pt_BR
Versão do jogo Tron / Motos de Luz para o KDE.

%package ktuberling
Summary:	KDE game for small children
Summary(pl):	Gra dla ma³ych dzieci
Summary(pt_BR):	Jogo de desenho do 'Homem-batata' para crianças
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description ktuberling
It is a potato editor. That means that you can drag and drop eyes,
mouths, moustache, and other parts of face and goodies onto a
potato-like guy.

There is no winer. The only purpose is to make the funniest faces you
can.

%description ktuberling -l pl
KTuberling to edytor ziemniaków. Oznacza to, ¿e mo¿na uk³adaæ oczy,
usta, w±sy oraz inne czê¶ci twarzy na postaæ podobn± do ziemniaka.

W grze nie ma zwyciêzcy. Jedynym celem gry jest stworzenie
najzabawniejszej twarzy, jak± siê da u³o¿yæ.

%description ktuberling -l pt_BR
Jogo de desenho do 'Homem-batata' para crianças.

%package kwin4
Summary:	Four wins for KDE
Summary(pl):	Gra "cztery wygrywa" dla KDE
Summary(pt_BR):	Jogo de estratégia que lembra um pouco o Otelo
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

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
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-carddecks = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minbaseevr}

%description lskat
Lieutenant skat (from German Offiziersskat) is a card game for two
players. It is roughly played according to the rules of Skat but with
only two players and simplified rules. Every player has a set of cards
in front of him/her, half of them covered and half of them open. Both
players try to win more than 60 of the 120 possible points. After 16
moves all cards are played and the game ends.

%description lskat -l pl
Lieutenant skat (oficerski skat, od niemieckiego Offizierskat) to gra
karciana dla dwóch graczy. Jest rozgrywana z grubsza na zasadach
skata, ale tylko miêdzy dwoma graczami i z uproszczonymi zasadami.
Ka¿dy gracz ma zestaw kart przed sob±, z których po³owa jest zakryta,
a po³owa odkryta. Obaj gracze próbuj± wygraæ ponad 60 ze 120 mo¿liwych
punktów. Po 16 ruchach wszystkie karty s± rozegrane i gra siê koñczy.

%description lskat -l pt_BR
Jogo de cartas Lieutenant Skat para KDE

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%{__sed} -i -e '/\[Desktop Entry\]/aEncoding=UTF-8' \
	klickety/klickety.desktop
%{__sed} -i -e 's/Terminal=0/Terminal=false/' \
	atlantik/atlantik.desktop \
	kasteroids/kasteroids.desktop \
	kbackgammon/kbackgammon.desktop \
	kblackbox/kblackbox.desktop \
	kbattleship/kbattleship/kbattleship.desktop \
	kgoldrunner/src/KGoldrunner.desktop \
	kjumpingcube/kjumpingcube.desktop \
	klines/klines.desktop \
	kmahjongg/kmahjongg.desktop \
	konquest/konquest.desktop \
	kpoker/kpoker.desktop \
	kreversi/kreversi.desktop \
	ksmiletris/ksmiletris.desktop \
	ksnake/ksnake.desktop \
	kspaceduel/kspaceduel.desktop \
	ksokoban/data/ksokoban.desktop \
	ktron/ktron.desktop \
	ktuberling/ktuberling.desktop \
	kwin4/kwin4.desktop \
	lskat/lskat.desktop
for f in `find . -name \*.desktop`; do
	if grep -q '^Categories=.*[^;]$' $f; then
		sed -i -e 's/\(^Categories=.*$\)/\1;/' $f
	fi
	if grep -q '\[ven\]' $f; then
		sed -i -e 's/\[ven\]/[ve]/' $f
	fi
done

cp -p libkdegames/highscore/INSTALL README.highscore

%build
cp /usr/share/automake/config.sub admin

export UNSERMAKE=/usr/share/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final \
	%{?with_highscore:--enable-highscore-dir=/var/games} \
	--with-qt-libraries=%{_libdir} \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full}

%{__make}

%{?with_apidocs:%{__make} apidox}

%install
rm -rf $RPM_BUILD_ROOT
rm -f *.lang

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%if %{with highscore}
install -d $RPM_BUILD_ROOT/var/games
touch $RPM_BUILD_ROOT/var/games/k{fouleggs,lickety,mines,sirtet,bounce}.scores
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
%find_lang kmahjongg	--with-kde
%find_lang kmines	--with-kde
%find_lang kolf		--with-kde
%find_lang konquest	--with-kde
%find_lang kpat		--with-kde
%find_lang kpoker	--with-kde
%find_lang kreversi	--with-kde
%find_lang ksame	--with-kde
%find_lang kshisen	--with-kde
%find_lang ksirtet	--with-kde
%find_lang ksmiletris	--with-kde
%find_lang ksnake	--with-kde
%find_lang ksokoban	--with-kde
%find_lang kspaceduel	--with-kde
%find_lang ktron	--with-kde
%find_lang ktuberling	--with-kde
%find_lang kwin4	--with-kde
%find_lang lskat	--with-kde

# Omit apidocs entries
sed -i 's/.*apidocs.*//' *.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post			-p /sbin/ldconfig
%postun			-p /sbin/ldconfig

%post	atlantik	-p /sbin/ldconfig
%postun	atlantik	-p /sbin/ldconfig

%post	kolf		-p /sbin/ldconfig
%postun	kolf		-p /sbin/ldconfig

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
%attr(755,root,root) %{_libdir}/libatlantic.so
%attr(755,root,root) %{_libdir}/libatlantikclient.so
%attr(755,root,root) %{_libdir}/libatlantikui.so
%attr(755,root,root) %{_libdir}/libkdegames.so
%attr(755,root,root) %{_libdir}/libkolf.so
%{_includedir}/*

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_kdedocdir}/en/%{name}-apidocs
%endif

%files carddecks
%defattr(644,root,root,755)
%{_datadir}/apps/carddecks

%files atlantik -f atlantik.lang
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

%files kasteroids -f kasteroids.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kasteroids
%{_datadir}/apps/kasteroids
%{_datadir}/config.kcfg/kasteroids.kcfg
%{_desktopdir}/kde/kasteroids.desktop
%{_iconsdir}/*/*/apps/kasteroids.png

%files katomic -f katomic.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/katomic
%{_datadir}/apps/katomic
%{_desktopdir}/kde/katomic.desktop
%{_iconsdir}/*/*/apps/katomic.*

%files kbackgammon -f kbackgammon.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbackgammon
%{_datadir}/apps/kbackgammon
%{_desktopdir}/kde/kbackgammon.desktop
%{_iconsdir}/*/*/apps/kbackgammon*.png

%files kbattleship -f kbattleship.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbattleship
%{_datadir}/apps/kbattleship
%{_datadir}/apps/zeroconf/_kbattleship._tcp
%{_desktopdir}/kde/kbattleship.desktop
%{_iconsdir}/*/*/apps/kbattleship.png

%files kblackbox -f kblackbox.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kblackbox
%{_datadir}/apps/kblackbox
%{_desktopdir}/kde/kblackbox.desktop
%{_iconsdir}/*/*/apps/kblackbox.png

%files kbounce -f kbounce.lang
%defattr(644,root,root,755)
%if %{with highscore}
%attr(2755,root,games) %{_bindir}/kbounce
%else
%attr(755,root,root) %{_bindir}/kbounce
%endif
%attr(660,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/kbounce.scores
%{_datadir}/apps/kbounce
%{_desktopdir}/kde/kbounce.desktop
%{_iconsdir}/[!l]*/*/*/kbounce*

%files kenolaba -f kenolaba.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kenolaba
%{_datadir}/apps/kenolaba
%{_desktopdir}/kde/kenolaba.desktop
%{_iconsdir}/*/*/*/kenolaba*

%files kfouleggs -f kfouleggs.lang
%defattr(644,root,root,755)
%if %{with highscore}
%attr(660,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/kfouleggs.scores
%attr(2755,root,games) %{_bindir}/kfouleggs
%else
%attr(755,root,root) %{_bindir}/kfouleggs
%endif
%{_datadir}/apps/kfouleggs
%{_iconsdir}/*/*/apps/kfouleggs.png
%{_datadir}/config.kcfg/kfouleggs.kcfg
%{_desktopdir}/kde/kfouleggs.desktop
#%{_iconsdir}/crystalsvg/*/*/kfouleggs*

%files kgoldrunner -f kgoldrunner.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kgoldrunner
%{_datadir}/apps/kgoldrunner
%{_desktopdir}/kde/KGoldrunner.desktop
%{_iconsdir}/hicolor/*/apps/kgoldrunner.png

%files kjumpingcube -f kjumpingcube.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjumpingcube
%{_datadir}/apps/kjumpingcube
%{_datadir}/config.kcfg/kjumpingcube.kcfg
%{_desktopdir}/kde/kjumpingcube.desktop
%{_iconsdir}/*/*/apps/kjumpingcube.png

%files klickety -f klickety.lang
%defattr(644,root,root,755)
%if %{with highscore}
%attr(660,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/klickety.scores
%attr(2755,root,games) %{_bindir}/klickety
%else
%attr(755,root,root) %{_bindir}/klickety
%endif
%{_datadir}/apps/klickety
%{_iconsdir}/*/*/apps/klickety.png
%{_desktopdir}/kde/klickety.desktop
#%{_iconsdir}/crystalsvg/*/apps/klickety.*

%files klines -f klines.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klines
%{_datadir}/apps/klines
%{_datadir}/config.kcfg/klines.kcfg
%{_desktopdir}/kde/klines.desktop
%{_iconsdir}/*/*/apps/klines.png

%files kmahjongg -f kmahjongg.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmahjongg
%{_datadir}/apps/kmahjongg
%{_datadir}/config.kcfg/kmahjongg.kcfg
%{_desktopdir}/kde/kmahjongg.desktop
%{_iconsdir}/*/*/apps/kmahjongg.png

%files kmines -f kmines.lang
%defattr(644,root,root,755)
%if %{with highscore}
%attr(660,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/kmines.scores
%attr(2755,root,games) %{_bindir}/kmines
%else
%attr(755,root,root) %{_bindir}/kmines
%endif
%{_datadir}/apps/kmines
%{_desktopdir}/kde/kmines.desktop
%{_iconsdir}/*/*/apps/kmines.png

%files knetwalk
%defattr(644,root,root,755)
%doc knetwalk/{AUTHORS,TODO}
%attr(755,root,games) %{_bindir}/knetwalk
%{_datadir}/apps/knetwalk
%{_desktopdir}/kde/lskat.desktop
%{_iconsdir}/[!l]*/*/apps/knetwalk.png

%files kolf -f kolf.lang
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

%files konquest -f konquest.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konquest
%{_datadir}/apps/konquest
%{_desktopdir}/kde/konquest.desktop
%{_iconsdir}/*/*/apps/konquest.png

%files kpat -f kpat.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpat
%{_datadir}/apps/kpat
%{_desktopdir}/kde/kpat.desktop
%{_iconsdir}/*/*/apps/kpat.png

%files kpoker -f kpoker.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpoker
%{_datadir}/apps/kpoker
%{_desktopdir}/kde/kpoker.desktop
%{_iconsdir}/*/*/apps/kpoker.png

%files kreversi -f kreversi.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kreversi
%{_datadir}/apps/kreversi
%{_datadir}/config.kcfg/kreversi.kcfg
%{_desktopdir}/kde/kreversi.desktop
%{_iconsdir}/*/*/apps/kreversi.png
%{_iconsdir}/crystalsvg/*/*/lastmoves.*
%{_iconsdir}/crystalsvg/*/*/legalmoves.*

%files ksame -f ksame.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksame
%{_datadir}/apps/ksame
%{_desktopdir}/kde/ksame.desktop
%{_iconsdir}/*/*/apps/ksame.png

%files kshisen -f kshisen.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kshisen
%{_datadir}/apps/kshisen
%{_datadir}/config.kcfg/kshisen.kcfg
%{_desktopdir}/kde/kshisen.desktop
%{_iconsdir}/*/*/apps/kshisen.png

%files ksirtet -f ksirtet.lang
%defattr(644,root,root,755)
%if %{with highscore}
%attr(660,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/ksirtet.scores
%attr(2755,root,games) %{_bindir}/ksirtet
%else
%attr(755,root,root) %{_bindir}/ksirtet
%endif
%{_datadir}/apps/ksirtet
%{_datadir}/config.kcfg/ksirtet.kcfg
%{_desktopdir}/kde/ksirtet.desktop
%{_iconsdir}/*/*/apps/ksirtet.png

%files ksmiletris -f ksmiletris.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksmiletris
%{_datadir}/apps/ksmiletris
%{_desktopdir}/kde/ksmiletris.desktop
%{_iconsdir}/*/*/apps/ksmiletris.png

%files ksnake -f ksnake.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/ksnake
%{_datadir}/apps/ksnake
%{_datadir}/config.kcfg/ksnake.kcfg
%{_desktopdir}/kde/ksnake.desktop
%{_iconsdir}/*/*/apps/ksnake.png

%files ksokoban -f ksokoban.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksokoban
%{_desktopdir}/kde/ksokoban.desktop
%{_iconsdir}/*/*/apps/ksokoban.png

%files kspaceduel -f kspaceduel.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/kspaceduel
%{_datadir}/apps/kspaceduel
%{_datadir}/config.kcfg/kspaceduel.kcfg
%{_desktopdir}/kde/kspaceduel.desktop
%{_iconsdir}/[!l]*/*/apps/kspaceduel.png

%files ktron -f ktron.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/ktron
%{_datadir}/apps/ktron
%{_datadir}/config.kcfg/ktron.kcfg
%{_desktopdir}/kde/ktron.desktop
%{_iconsdir}/*/*/apps/ktron.*

%files ktuberling -f ktuberling.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/ktuberling
%{_datadir}/apps/ktuberling
%{_desktopdir}/kde/ktuberling.desktop
%{_iconsdir}/*/*/apps/ktuberling.png

%files kwin4 -f kwin4.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwin4*
%{_datadir}/apps/kwin4
%{_datadir}/config.kcfg/kwin4.kcfg
%{_desktopdir}/kde/kwin4.desktop
%{_iconsdir}/*/*/apps/kwin4.png

%files lskat -f lskat.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/lskat
%attr(755,root,games) %{_bindir}/lskatproc
%{_datadir}/apps/lskat
%{_desktopdir}/kde/lskat.desktop
%{_iconsdir}/[!l]*/*/apps/lskat.png
