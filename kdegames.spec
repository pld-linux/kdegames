#
# TODO: Adding new games desc.

%define		_state		stable
%define		_ver		3.1.4

Summary:	K Desktop Environment - games
Summary(es):	K Desktop Environment - Juegos
Summary(ja):	KDE¥Ç¥¹¥¯¥È¥Ã¥×´Ä¶­ - ¥²¡¼¥à
Summary(ko):	K µ¥½ºÅ©Å¾ È¯°æ - ³îÀÌ(°ÔÀÓ)
Summary(pl):	K Desktop Environment - gry
Summary(pt_BR):	K Desktop Environment - Jogos
Summary(zh_CN):	KDEÓÎÏ·
Name:		kdegames
Version:	%{_ver}
Release:	0.5
Epoch:		8
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications/Games
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	be604fb91e24f990659f5cab2ac8decf
# generated from kde-i18n - need update!
Source1:	ftp://blysk.ds.pg.gda.pl/linux/kde-i18n-package/%{version}/kde-i18n-%{name}-%{version}.tar.bz2
# Source1-md5:	510dc744a3918fc932d9f7497638eeba
Source2:	%{name}-extra_icons.tar.bz2
# Source2-md5:	daf7940c0369bfaa7d4216a5fdecb6d7
#Patch0:	%{name}-kpatcards.patch
BuildRequires:	arts-devel
BuildRequires:	arts-kde-devel >= 8:%{version}
BuildRequires:	ed
BuildRequires:	kdelibs-devel >= 8:%{version}
Requires:	kdelibs >= 8:%{version}
Requires:	qt >= 3.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	kdegames-kabalone
Obsoletes:	kdegames-kjezz
Obsoletes:	kdegames-kpm

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_htmldir	/usr/share/doc/kde/HTML

%define		no_install_post_chrpath		1

%description
Libraries for kdegames. Included with this package are: kasteroids,
katomic, kbackgammon, kbattleship, kblackbox, kbounce, kenolaba,
kfouleggs, kjumpingcube, klickety, klines, kmahjongg, kmines, kolf,
konquest, kpat, kpoker, kreversi, ksame, kshisen, ksirtet, ksmiletris,
ksnake, ksokoban, kspaceduel, ktron, ktuberling, kwin4, lskat, megami.

%description -l es
Juegos para KDE. Incluidos en este paquete:

kasteroids: arcade, katomic, kbackgammon, kbattleship, kblackbox,
kbounce, kenolaba, kfouleggs, kjumpingcube, klickety, klines,
kmahjongg: el popular mahjongg, kmines: desarmar las minas, kolf,
konquest, kpat: juegos de cartas, incluso solitario, kpoker: vídeo
póquer, kreversi: Reversi, ksame: un juego de tablero, kshisen:
Shisen-Sho - relacionado con el mahjongg, ksirtet, ksmiletris, ksnake:
corrida de las cobras, ksokoban, kspaceduel, ktron, ktuberling, kwin4,
lskat, megami.

%description -l ja
KDE¥Ç¥¹¥¯¥È¥Ã¥×´Ä¶­ÍÑ¤Î¥²¡¼¥à °Ê²¼¤Î¤è¤¦¤Ê¥Ñ¥Ã¥±¡¼¥¸¤¬Æþ¤Ã¤Æ¤¤¤Þ¤¹¡£

kasteroids: ¥¢¡¼¥±¡¼¥É¥²¡¼¥à, katomic, kbackgammon, kbattleship,
kblackbox, kbounce, kenolaba, kfouleggs, kjumpingcube, klickety,
klines, kmahjongg: ¾å³¤ kmines: ¥Þ¥¤¥ó¥¹¥¤¡¼¥Ñ¡¼, kolf, konquest,
kpat: °ì¿ÍÍÑ¥È¥é¥ó¥×¥²¡¼¥à, kpoker: ¥Ý¡¼¥«, kreversi: ¥ê¥Ð¡¼¥·, ksame:
same game, kshisen: »ÍÀî¾Ê, ksirtet, ksmiletris, ksnake:
¥¹¥Í¡¼¥¯¥ì¡¼¥¹, ksokoban: ÁÒ¸ËÈÖ, kspaceduel, ktron, ktuberling,
kwin4, lskat, megami

%description -l pl
Biblioteki dla gier KDE: kasteroids, katomic, kbackgammon,
kbattleship, kblackbox, kbounce, kenolaba, kfouleggs, kjumpingcube,
klickety, klines, kmahjongg, kmines, kolf, konquest, kpat, kpoker,
kreversi, ksame, kshisen, ksirtet, ksmiletris, ksnake, ksokoban,
kspaceduel, ktron, ktuberling, kwin4, lskat, megami.

%description -l pt_BR
Jogos para o KDE. Incluídos neste pacote:

kasteroids: arcade, katomic, kbackgammon, kbattleship, kblackbox,
kbounce, kenolaba, kfouleggs, kjumpingcube, klickety, klines,
kmahjongg: o popular mahjongg, kmines: desarmar as minas, kolf,
konquest, kpat: jogos de cartas, inclusive paciência, kpoker:
vídeo-poker, kreversi: Reversi, ksame: um jogo de tabuleiro, kshisen:
Shisen-Sho - relacionado com o mahjongg, ksirtet, ksmiletris, ksnake:
corrida das cobras, ksokoban, kspaceduel, ktron, ktuberling, kwin4,
lskat, megami.

%package devel
Summary:	Development files for KDE games
Summary(pl):	Pliki przydatne twórcom gier KDE
Summary(pt_BR):	Arquivos de inclusão do kdegames
Group:		X11/Development/Libraries
Requires:	kdelibs-devel >= 8:%{version}
Requires:	%{name} = %{epoch}:%{version}
Requires:	%{name}-atlantik = %{epoch}:%{version}
Requires:	%{name}-kolf = %{epoch}:%{version}

%description devel
Development files for KDE games.

%description devel -l pl
Pliki dla programistów KDE games.

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

%package atlantik
Summary:	KDE client for playing Monopoly-like games
Summary(pl):	Klient KDE do grania w gry typu Monopoly
Group:		X11/Applications/Games
Requires:	kdebase-core >= %{version}

%description atlantik
Atlantik is a KDE client for Monopoly-like board games to be played on
the monopd network.

%description atlantik -l pl
Atlantik to klient KDE dla gier planszowych typu Monopoly, którym
mo¿na graæ w sieci monopd.

%package kasteroids
Summary:	KDE Asteroids clone
Summary(pl):	Klon Asteroids dla KDE
Summary(pt_BR):	Destrua os asteróides para não ser destruído
Group:		X11/Applications/Games
Requires:	kdebase-core >= %{version}

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
Requires:	kdebase-core >= %{version}

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
Requires:	kdebase-core >= %{version}

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
Requires:	kdebase-core >= %{version}

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
Requires:	kdebase-core >= %{version}

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
Requires:	kdebase-core >= %{version}

%description kbounce
Claim areas and don't get disturbed.

%description kbounce -l pl
Gra polegaj±ca na pozyskiwaniu terenu wbrew przeciwnikom.

%package kenolaba
Summary:	Abalone-like board game against the computer
Summary(pl):	Gra planszowa podobna do Abalone przeciwko komputerowi
Group:		X11/Applications/Games
Requires:	kdebase-core >= %{version}

%description kenolaba
Abalone-like board game against the computer.

%description kenolaba -l pl
Gra planszowa podobna do Abalone przeciwko komputerowi.

%package kfouleggs
Summary:	KDE kfouleggs
Summary(pl):	Gra kfouleggs dla KDE
Summary(pt_BR):	Mais um jogo que lembra o estilo Tetris
Group:		X11/Applications/Games
Requires:	kdebase-core >= %{version}

%description kfouleggs
KDE kfouleggs.

%description kfouleggs -l pl
Gra kfouleggs dla KDE.

%description kfouleggs -l pt_BR
Mais um jogo que lembra o estilo Tetris.

%package kjumpingcube
Summary:	A little tactical game for KDE
Summary(pl):	Prosta gra taktyczna dla KDE
Summary(pt_BR):	Jogo de estratégia para 2 contendores
Group:		X11/Applications/Games
Requires:	kdebase-core >= %{version}

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
Requires:	kdebase-core >= %{version}

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
Requires:	kdebase-core >= %{version}

%description klines
Lines for KDE.

%description klines -l pl
Gra Lines dla KDE.

%package kmahjongg
Summary:	KDE Mahjongg clone
Summary(pl):	Klon gry Mahjongg dla KDE
Summary(pt_BR):	Versão do jogo Mahjongg para o KDE
Group:		X11/Applications/Games
Requires:	kdebase-core >= %{version}

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
Requires:	kdebase-core >= %{version}

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
Requires:	kdebase-core >= %{version}

%description kolf
Kolf - miniature golf for KDE.

%description kolf -l pl
Kolf - mini golf dla KDE.

%package konquest
Summary:	KDE version of Gnu-Lactic Konquest
Summary(pl):	Podbój galaktyki dla KDE
Summary(pt_BR):	Jogo espacial de estratégia
Group:		X11/Applications/Games
Requires:	kdebase-core >= %{version}

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
Requires:	kdegames-carddecks = %{epoch}:%{version}
Requires:	kdebase-core >= %{version}

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
Requires:	kdegames-carddecks = %{epoch}:%{version}
Requires:	kdebase-core >= %{version}

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
Requires:	kdebase-core >= %{version}

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
Requires:	kdebase-core >= %{version}

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
Requires:	kdebase-core >= %{version}

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
Requires:	kdebase-core >= %{version}

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
Requires:	kdebase-core >= %{version}

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
Requires:	kdebase-core >= %{version}

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
Requires:	kdebase-core >= %{version}

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
Requires:	kdebase-core >= %{version}

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
Requires:	kdebase-core >= %{version}

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
Requires:	kdebase-core >= %{version}

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
Requires:	kdebase-core >= %{version}

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
Requires:	kdebase-core >= %{version}

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
Requires:	kdebase-core >= %{version}

%description megami
Popular Gambling Game.

%description megami -l pl
Popularna gra hazardowa.

%prep
%setup -q
#%patch0 -p1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

for plik in `find ./ -name \*.desktop | grep -l '\[nb\]'` ; do
	echo $plik
	echo -e ',s/\[nb\]/[no]/\n,w' | ed $plik
done

%configure \
	--with-qt-dir=%{_prefix} \
	--with-pam="yes" \
	--disable-rpath \
	--enable-final
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Amusements,%{_mandir}/man6}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_applnkdir}/{Games/Kidsgames/*,Amusements}
mv -f $RPM_BUILD_ROOT%{_applnkdir}/Games/{TacticStrategy,Strategy}

cd $RPM_BUILD_ROOT%{_pixmapsdir}
mv {locolor,crystalsvg}/16x16/apps/lskat.png
cd -

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_pixmapsdir}
for i in {atlantik,kasteroids,kbackgammon,kblackbox,kenolaba,kmines}.png \
	 {kolf,konquest,kpoker,kreversi,ksame,kshisen,ksirtet}.png \
	 {ksmiletris,ksnake,ksokoban,kwin4,lskat}.png; do
	ln -s crystalsvg/48x48/apps/$i $RPM_BUILD_ROOT%{_pixmapsdir}/$i
done

for i in `find $RPM_BUILD_ROOT%{_applnkdir} -type f`; do
	if grep '^Icon=.[^.]*$' $i >/dev/null; then
		echo -e ',s/\(^Icon=.*$\)/\\1.png/\n,w' | ed $i
	fi
done

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT
for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo; do
	[ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] && rm -f $f
done

%find_lang	atlantik		--with-kde
%find_lang	kasteroids		--with-kde
%find_lang	katomic			--with-kde
%find_lang	kbackgammon		--with-kde
%find_lang	kbattleship		--with-kde
%find_lang	kblackbox		--with-kde
%find_lang	kbounce			--with-kde
%find_lang	kenolaba		--with-kde
%find_lang	kfouleggs		--with-kde
%find_lang	kjumpingcube		--with-kde
%find_lang	klickety		--with-kde
%find_lang	klines			--with-kde
%find_lang	kmahjongg		--with-kde
%find_lang	kmines			--with-kde
%find_lang	kolf			--with-kde
%find_lang	konquest		--with-kde
%find_lang	kpat			--with-kde
%find_lang	kpoker			--with-kde
%find_lang	kreversi		--with-kde
%find_lang	ksame			--with-kde
%find_lang	kshisen			--with-kde
%find_lang	ksirtet			--with-kde
%find_lang	ksmiletris		--with-kde
%find_lang	ksnake			--with-kde
%find_lang	ksokoban		--with-kde
%find_lang	kspaceduel		--with-kde
%find_lang	ktron			--with-kde
%find_lang	ktuberling		--with-kde
%find_lang	kwin4			--with-kde
%find_lang	libkdegames		--with-kde
%find_lang	libksirtet		--with-kde
%find_lang	libkdehighscores	--with-kde
%find_lang	lskat			--with-kde
%find_lang	megami			--with-kde

cat libkdehighscores.lang >> kmines.lang

# seems required by klickety, kfouleggs and ksirtet (statically linked code) 
cat libksirtet.lang >> libkdegames.lang

# missing
#%find_lang	kio_atlantik		--with-kde
# cat kio_atlantik.lang >> atlantik.lang

# obsolete ?
#%find_lang	multiplayers		--with-kde
#cat multiplayers.lang >> libkdegames.lang

for i in debian/*.man; do
	echo -e ',s:kdeopt\.man:kdeopt.6:\n,w' | ed $i || :
	install $i $RPM_BUILD_ROOT%{_mandir}/man6/`basename $i | sed 's/man$/6/'`
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f libkdegames.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_libdir}/libkdegames.la
%attr(755,root,root) %{_libdir}/libkdegames.so.*
%{_datadir}/apps/kdegames
%{_pixmapsdir}/*/*/actions/endturn.png
%{_pixmapsdir}/*/*/*/highscore.png
%{_pixmapsdir}/*/*/*/roll.png
%{_mandir}/man6/kdeopt.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/libatlantic.so
%{_libdir}/libatlantikclient.so
%{_libdir}/libatlantikui.so
%{_libdir}/libkdegames.so
%{_libdir}/libkolf.so

%files carddecks
%defattr(644,root,root,755)
%{_datadir}/apps/carddecks

#################################################
#             ATLANTIK
#################################################

%files atlantik -f atlantik.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/atlantik
%{_libdir}/libatlantic.la
%attr(755,root,root) %{_libdir}/libatlantic.so.*
%{_libdir}/libatlantikclient.la
%attr(755,root,root) %{_libdir}/libatlantikclient.so.*
%{_libdir}/libatlantikui.la
%attr(755,root,root) %{_libdir}/libatlantikui.so.*
%{_libdir}/kde3/kio_atlantik.la
%attr(755,root,root) %{_libdir}/kde3/kio_atlantik.so
%{_datadir}/apps/atlantik
%{_datadir}/services/atlantik.protocol
%{_applnkdir}/Games/Board/atlantik.desktop
%{_pixmapsdir}/*/*/apps/atlantik.png
%{_pixmapsdir}/atlantik.png
%{_mandir}/man6/atlantik.*

#################################################
#             KASTEROIDS
#################################################

%files kasteroids -f kasteroids.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kasteroids
%{_datadir}/apps/kasteroids
%{_applnkdir}/Games/Arcade/kasteroids.desktop
%{_pixmapsdir}/*/*/apps/kasteroids.png
%{_pixmapsdir}/kasteroids.png
%{_mandir}/man6/kasteroids.*

#################################################
#             KATOMIC
#################################################

%files katomic -f katomic.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/katomic
%{_datadir}/apps/katomic
%{_applnkdir}/Games/Strategy/katomic.desktop
%{_pixmapsdir}/*/*/apps/katomic.png
%{_pixmapsdir}/katomic.png
%{_mandir}/man6/katomic.*

#################################################
#             KBACKGAMMON
#################################################

%files kbackgammon -f kbackgammon.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbackgammon
%{_datadir}/apps/kbackgammon
%{_applnkdir}/Games/Board/kbackgammon.desktop
%{_pixmapsdir}/*/*/apps/kbackgammon*.png
%{_pixmapsdir}/kbackgammon.png
%{_mandir}/man6/kbackgammon.*

#################################################
#             KBATTLESHIP
#################################################

%files kbattleship -f kbattleship.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbattleship
%{_datadir}/apps/kbattleship
%{_applnkdir}/Games/Board/kbattleship.desktop
%{_pixmapsdir}/*/*/apps/kbattleship.png
%{_pixmapsdir}/kbattleship.png
%{_mandir}/man6/kbattleship.*

#################################################
#             KBLACKBOX
#################################################

%files kblackbox -f kblackbox.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kblackbox
%{_datadir}/apps/kblackbox
%{_applnkdir}/Games/Board/kblackbox.desktop
%{_pixmapsdir}/*/*/apps/kblackbox.png
%{_pixmapsdir}/kblackbox.png
%{_mandir}/man6/kblackbox.*

#################################################
#             KBOUNCE
#################################################

%files kbounce -f kbounce.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbounce
%{_datadir}/apps/kbounce
%{_applnkdir}/Games/Arcade/kbounce.desktop
%{_pixmapsdir}/[!l]*/*/*/kbounce*
%{_pixmapsdir}/kbounce.png
%{_mandir}/man6/kbounce.*

#################################################
#             KENOLABA
#################################################

%files kenolaba -f kenolaba.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kenolaba
%{_datadir}/apps/kenolaba
%{_applnkdir}/Games/Board/kenolaba.desktop
%{_pixmapsdir}/*/*/*/kenolaba*
%{_pixmapsdir}/kenolaba.png
%{_mandir}/man6/kenolaba.*

#################################################
#             KFOULEGGS
#################################################

%files kfouleggs -f kfouleggs.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfouleggs
%{_datadir}/apps/kfouleggs
%{_applnkdir}/Games/Arcade/kfouleggs.desktop
%{_mandir}/man6/kfouleggs.*

#################################################
#             KJUMPINGCUBE
#################################################

%files kjumpingcube -f kjumpingcube.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjumpingcube
%{_datadir}/apps/kjumpingcube
%{_applnkdir}/Games/Strategy/kjumpingcube.desktop
%{_pixmapsdir}/*/*/apps/kjumpingcube.png
%{_pixmapsdir}/kjumpingcube.png
%{_mandir}/man6/kjumpingcube.*

#################################################
#             KLICKETY
#################################################

%files klickety -f klickety.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klickety
%{_datadir}/apps/klickety
%{_applnkdir}/Games/Arcade/klickety.desktop
%{_mandir}/man6/klickety.*

#################################################
#             KLINES
#################################################

%files klines -f klines.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klines
%{_datadir}/apps/klines
%{_applnkdir}/Games/Strategy/klines.desktop
%{_pixmapsdir}/*/*/apps/klines.png
%{_pixmapsdir}/klines.png
%{_mandir}/man6/klines.*

#################################################
#             KMAHJONGG
#################################################

%files kmahjongg -f kmahjongg.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmahjongg
%{_datadir}/apps/kmahjongg
%{_applnkdir}/Games/Board/kmahjongg.desktop
%{_pixmapsdir}/*/*/apps/kmahjongg.png
%{_pixmapsdir}/kmahjongg.png
%{_mandir}/man6/kmahjongg.*

#################################################
#             KMINES
#################################################

%files kmines -f kmines.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmines
%{_datadir}/apps/kmines
%{_applnkdir}/Games/Strategy/kmines.desktop
%{_pixmapsdir}/*/*/apps/kmines.png
%{_pixmapsdir}/kmines.png
%{_mandir}/man6/kmines.*

#################################################
#             KOLF
#################################################

%files kolf -f kolf.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kolf
%{_libdir}/libkolf.la
%attr(755,root,root) %{_libdir}/libkolf.so.*
%{_libdir}/kde3/kolf.la
%attr(755,root,root) %{_libdir}/kde3/kolf.so
%{_datadir}/config/magic
%{_datadir}/apps/kolf
%{_datadir}/mimelnk/application/*
%{_applnkdir}/Games/Arcade/kolf.desktop
%{_pixmapsdir}/*/*/apps/kolf.png
%{_pixmapsdir}/kolf.png
%{_mandir}/man6/kolf.*

#################################################
#             KONQUEST
#################################################

%files konquest -f konquest.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konquest
%{_datadir}/apps/konquest
%{_applnkdir}/Games/Strategy/konquest.desktop
%{_pixmapsdir}/*/*/apps/konquest.png
%{_pixmapsdir}/konquest.png
%{_mandir}/man6/konquest.*

#################################################
#             KPAT
#################################################

%files kpat -f kpat.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpat
%{_datadir}/apps/kpat
%{_applnkdir}/Games/Card/kpat.desktop
%{_pixmapsdir}/*/*/apps/kpat.png
%{_pixmapsdir}/kpat.png
%{_mandir}/man6/kpat.*

#################################################
#             KPOKER
#################################################

%files kpoker -f kpoker.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpoker
%{_datadir}/apps/kpoker
%{_applnkdir}/Games/Card/kpoker.desktop
%{_pixmapsdir}/*/*/apps/kpoker.png
%{_pixmapsdir}/kpoker.png
%{_mandir}/man6/kpoker.*

#################################################
#             KREVERSI
#################################################

%files kreversi -f kreversi.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kreversi
%{_datadir}/apps/kreversi
%{_applnkdir}/Games/Board/kreversi.desktop
%{_pixmapsdir}/*/*/apps/kreversi.png
%{_pixmapsdir}/kreversi.png
%{_mandir}/man6/kreversi.*

#################################################
#            KSAME
#################################################

%files ksame -f ksame.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksame
%{_datadir}/apps/ksame
%{_applnkdir}/Games/Strategy/ksame.desktop
%{_pixmapsdir}/*/*/apps/ksame.png
%{_pixmapsdir}/ksame.png
%{_mandir}/man6/ksame.*

#################################################
#             KSHISEN
#################################################

%files kshisen -f kshisen.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kshisen
%{_datadir}/apps/kshisen
%{_applnkdir}/Games/Board/kshisen.desktop
%{_pixmapsdir}/*/*/apps/kshisen.png
%{_pixmapsdir}/kshisen.png
%{_mandir}/man6/kshisen.*

#################################################
#             KSIRTET
#################################################

%files ksirtet -f ksirtet.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksirtet
%{_datadir}/apps/ksirtet
%{_applnkdir}/Games/Arcade/ksirtet.desktop
%{_pixmapsdir}/*/*/apps/ksirtet.png
%{_pixmapsdir}/ksirtet.png
%{_mandir}/man6/ksirtet.*

#################################################
#             KSMILETRIS
#################################################

%files ksmiletris -f ksmiletris.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksmiletris
%{_datadir}/apps/ksmiletris
%{_applnkdir}/Games/Arcade/ksmiletris.desktop
%{_pixmapsdir}/*/*/apps/ksmiletris.png
%{_pixmapsdir}/ksmiletris.png
%{_mandir}/man6/ksmiletris.*

#################################################
#             KSNAKE
#################################################

%files ksnake -f ksnake.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/ksnake
%{_datadir}/apps/ksnake
%{_applnkdir}/Games/Arcade/ksnake.desktop
%{_pixmapsdir}/*/*/apps/ksnake.png
%{_pixmapsdir}/ksnake.png
%{_mandir}/man6/ksnake.*

#################################################
#             KSOKOBAN
#################################################

%files ksokoban -f ksokoban.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksokoban
%{_applnkdir}/Games/Strategy/ksokoban.desktop
%{_pixmapsdir}/*/*/apps/ksokoban.png
%{_pixmapsdir}/ksokoban.png
%{_mandir}/man6/ksokoban.*

#################################################
#             KSPACEDUEL
#################################################

%files kspaceduel -f kspaceduel.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/kspaceduel
%{_datadir}/apps/kspaceduel
%{_applnkdir}/Games/Arcade/kspaceduel.desktop
%{_pixmapsdir}/[!l]*/*/apps/kspaceduel.png
%{_pixmapsdir}/kspaceduel.png
%{_mandir}/man6/kspaceduel.*

#################################################
#             KTRON
#################################################

%files ktron -f ktron.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/ktron
%{_datadir}/apps/ktron
%{_applnkdir}/Games/Arcade/ktron.desktop
%{_pixmapsdir}/*/*/apps/ktron.png
%{_pixmapsdir}/ktron.png
%{_mandir}/man6/ktron.*

#################################################
#             KTUBERLING
#################################################

%files ktuberling -f ktuberling.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/ktuberling
%{_datadir}/apps/ktuberling
%{_applnkdir}/Amusements/ktuberling.desktop
%{_pixmapsdir}/*/*/apps/ktuberling.png
%{_pixmapsdir}/ktuberling.png
%{_mandir}/man6/ktuberling.*

#################################################
#             KWIN4
#################################################

%files kwin4 -f kwin4.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwin4*
%{_datadir}/apps/kwin4
%{_applnkdir}/Games/Board/kwin4.desktop
%{_pixmapsdir}/*/*/apps/kwin4.png
%{_pixmapsdir}/kwin4.png
%{_mandir}/man6/kwin4.*


#################################################
#             LSKAT
#################################################

%files lskat -f lskat.lang
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/lskat
%attr(755,root,games) %{_bindir}/lskatproc
%{_datadir}/apps/lskat
%{_applnkdir}/Games/Card/lskat.desktop
%{_pixmapsdir}/[!l]*/*/apps/lskat.png
%{_pixmapsdir}/lskat.png
%{_mandir}/man6/lskat*

#################################################
#             MEGAMI
#################################################

%files megami -f megami.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/megami
%{_datadir}/apps/megami
%{_applnkdir}/Games/Card/megami.desktop
%{_pixmapsdir}/*/*/apps/megami.png
%{_pixmapsdir}/megami.png
%{_mandir}/man6/megami.*
