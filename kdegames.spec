#
# TODO: Adding new games desc.

%bcond_without highscore	# without system-wide score feature

%define		_state		snapshots
%define		_ver		3.1.95
%define		_snap		040110

Summary:	K Desktop Environment - games
Summary(es):	K Desktop Environment - Juegos
Summary(ja):	KDE¥Ç¥¹¥¯¥È¥Ã¥×´Ä¶­ - ¥²¡¼¥à
Summary(ko):	K µ¥½ºÅ©Å¾ È¯°æ - ³îÀÌ(°ÔÀÓ)
Summary(pl):	K Desktop Environment - gry
Summary(pt_BR):	K Desktop Environment - Jogos
Summary(zh_CN):	KDEÓÎÏ·
Name:		kdegames
#Version:	%{_ver}.%{_snap}
Version:	%{_ver}
Release:	1
Epoch:		8
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications/Games
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
Source0:	http://ep09.pld-linux.org/~djurban/kde/%{name}-%{version}.tar.bz2
# Source0-md5:	53410b3feab1c520cbf42a0bb17f5c56
Patch0:		%{name}-disable_install-exec-hook.patch
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
vídeo póquer, kreversi: Reversi, ksame: un juego de tablero, kshisen:
Shisen-Sho - relacionado con el mahjongg, ksirtet, ksmiletris, ksnake:
corrida de las cobras, ksokoban, kspaceduel, ktron, kwin4, lskat.

%description -l ja
KDE¥Ç¥¹¥¯¥È¥Ã¥×´Ä¶­ÍÑ¤Î¥²¡¼¥à °Ê²¼¤Î¤è¤¦¤Ê¥Ñ¥Ã¥±¡¼¥¸¤¬Æþ¤Ã¤Æ¤¤¤Þ¤¹¡£

kasteroids: ¥¢¡¼¥±¡¼¥É¥²¡¼¥à, katomic, kbackgammon, kbattleship,
kblackbox: a strategy game with hidden boxes and rays, kbounce,
kenolaba, kfouleggs, kenolaba, kgoldrunner, kjumpingcube, klickety,
klines, kmahjongg: ¾å³¤ kmines: ¥Þ¥¤¥ó¥¹¥¤¡¼¥Ñ¡¼, kolf, konquest,
kpat: °ì¿ÍÍÑ¥È¥é¥ó¥×¥²¡¼¥à, kpoker: ¥Ý¡¼¥«, kreversi: ¥ê¥Ð¡¼¥·, ksame:
same game, kshisen: »ÍÀî¾Ê, ksirtet, ksmiletris, ksnake:
¥¹¥Í¡¼¥¯¥ì¡¼¥¹, ksokoban: ÁÒ¸ËÈÖ, kspaceduel, ktron, kwin4, lskat

%description -l pl
Biblioteki dla gier KDE: kasteroids, katomic, kbackgammon,
kbattleship, kblackbox, kbounce, kenolaba, kfouleggs, kgoldrunner,
kjumpingcube, klickety, klines, kmahjongg, kmines, kolf, konquest,
kpat, kpoker, kreversi, ksame, kshisen, ksirtet, ksmiletris, ksnake,
ksokoban, kspaceduel, ktron, ktuberling, kwin4, lskat.

%description -l pt_BR
Jogos para o KDE. Incluídos neste pacote:

kasteroids: arcade, katomic, kblackbox, kbackgammon, kbattleship,
kbounce, kenolaba, kfouleggs, kgoldrunner, kjumpingcube, klickety,
klines, kmahjongg: o popular mahjongg, kmines: desarmar as minas,
kolf, konquest, kpat: jogos de cartas, inclusive paciência, kpoker:
vídeo-poker, kreversi: Reversi, ksame: um jogo de tabuleiro, kshisen:
Shisen-Sho - relacionado com o mahjongg, ksirtet, ksmiletris, ksnake:
corrida das cobras, ksokoban, kspaceduel, ktron, kwin4, lskat.

%package devel
Summary:	Development files for KDE games
Summary(pl):	Pliki przydatne twórcom gier KDE
Summary(pt_BR):	Arquivos de inclusão do kdegames
Group:		X11/Development/Libraries
Requires:	kdelibs-devel >= 9:%{version}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-atlantik = %{epoch}:%{version}-%{release}
Requires:	%{name}-kolf = %{epoch}:%{version}-%{release}

%description devel
Development files for KDE games.

%description devel -l pl
Pliki dla programistów KDE games.

%description devel -l pt_BR
Este pacote detém os arquivos de inclusão necessários para compilar
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
Atlantik to klient KDE dla gier planszowych typu Monopoly, którym
mo¿na graæ w sieci monopd.

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
Summary(pt_BR):	Destrua os asteróides para não ser destruído
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

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
Requires:	kdebase-core >= 9:%{version}

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
Requires:	kdebase-core >= 9:%{version}

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
Summary(pt_BR):	Versão do jogo Blackbox do Emacs para KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description kblackbox
A little logical game for KDE.

%description kblackbox -l pl
Prosta gra logiczna.

%description kblackbox -l pt_BR
Versão do jogo Blackbox do Emacs para KDE.

%package kbounce
Summary:	Claim areas and don't get disturbed
Summary(pl):	Gra polegaj±ca na pozyskiwaniu terenu wbrew przeciwnikom
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description kbounce
Claim areas and don't get disturbed.

%description kbounce -l pl
Gra polegaj±ca na pozyskiwaniu terenu wbrew przeciwnikom.

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
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description kgoldrunner
TODO.

%description kgoldrunner -l pl
TODO.

%package kjumpingcube
Summary:	A little tactical game for KDE
Summary(pl):	Prosta gra taktyczna dla KDE
Summary(pt_BR):	Jogo de estratégia para 2 contendores
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
Summary(pt_BR):	Versão do jogo Mahjongg para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

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
Requires:	kdebase-core >= 9:%{version}

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
Summary(pl):	Podbój galaktyki dla KDE
Summary(pt_BR):	Jogo espacial de estratégia
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description konquest
KDE version of Gnu-Lactic Konquest.

%description konquest -l pl
Podbój galaktyki dla KDE.

%description konquest -l pt_BR
Jogo espacial de estratégia.

%package kpat
Summary:	KDE solitaire patience game
Summary(pl):	Pasjanse dla KDE
Summary(pt_BR):	Versão do jogo 'Paciência' para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-carddecks = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

%description kpat
KDE solitaire patience games.

%description kpat -l pl
Program umo¿liwia uk³adanie kilku rodzajów pasjansów.

%description kpat -l pt_BR
Versão do jogo 'Paciência' para o KDE.

%package kpoker
Summary:	KDE poker
Summary(pl):	Poker dla KDE
Summary(pt_BR):	Jogo de vídeo-pôquer para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-carddecks = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

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
Requires:	kdebase-core >= 9:%{version}

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
Requires:	kdebase-core >= 9:%{version}

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
Requires:	kdebase-core >= 9:%{version}

%description kshisen
Shisen-Sho is similar to Mahjongg and uses the same set of tiles as
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
Summary(pl):	Wy¶cig Wê¿y dla KDE
Summary(pt_BR):	Jogo da cobra sempre crescente para o KDE
Group:		X11/Applications/Games
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}

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
Requires:	kdebase-core >= 9:%{version}

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
Requires:	kdebase-core >= 9:%{version}

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
Requires:	kdebase-core >= 9:%{version}

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
Requires:	kdebase-core >= 9:%{version}

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

%prep
#%setup -q -n %{name}-%{_snap}
%setup -q
%patch0 -p1

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

for f in *.lang; do
	if grep -q %{name}-%{version}-apidocs $f; then
		grep -v %{name}-%{version}-apidocs $f > $f.tmp
		mv $f.tmp $f
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
%lang(en) %{_kdedocdir}/en/%{name}-%{version}-apidocs
%{_includedir}/*
%{_libdir}/libatlantic.so
%{_libdir}/libatlantikclient.so
%{_libdir}/libatlantikui.so
%{_libdir}/libkdegames.so
%{_libdir}/libkolf.so

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
%{_iconsdir}/*/*/apps/katomic.png

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
%attr(755,root,root) %{_bindir}/kbounce
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
%{?with_highscore:%attr(660,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/kfouleggs.scores}
%attr(755,root,root) %{_bindir}/kfouleggs
%{_datadir}/apps/kfouleggs
%{_datadir}/config.kcfg/kfouleggs.kcfg
%{_desktopdir}/kde/kfouleggs.desktop

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
%{?with_highscore:%attr(660,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/klickety.scores}
%attr(755,root,root) %{_bindir}/klickety
%{_datadir}/apps/klickety
%{_desktopdir}/kde/klickety.desktop

%files klines -f klines.lang
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

%files kmines -f kmines.lang
%defattr(644,root,root,755)
%{?with_highscore:%attr(660,root,games) %config(noreplace) %verify(not size mtime md5) /var/games/kmines.scores}
%attr(755,root,root) %{_bindir}/kmines
%{_datadir}/apps/kmines
%{_desktopdir}/kde/kmines.desktop
%{_iconsdir}/*/*/apps/kmines.png

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
%{_desktopdir}/kde/kshisen.desktop
%{_iconsdir}/*/*/apps/kshisen.png

%files ksirtet -f ksirtet.lang
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

%files ksnake -f ksnake.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/ksnake
%{_datadir}/apps/ksnake
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
%{_iconsdir}/*/*/apps/ktron.png

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
%{_desktopdir}/kde/kwin4.desktop
%{_iconsdir}/*/*/apps/kwin4.png

%files lskat -f lskat.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/lskat
%attr(755,root,games) %{_bindir}/lskatproc
%{_datadir}/apps/lskat
%{_desktopdir}/kde/lskat.desktop
%{_iconsdir}/[!l]*/*/apps/lskat.png

#%files megami -f megami.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/megami
#%{_datadir}/apps/megami
#%{_desktopdir}/kde/megami.desktop
#%{_iconsdir}/*/*/apps/megami.png
