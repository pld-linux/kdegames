#
# TODO: Adding new games desc.

%define		_state		snapshots
%define		_ver		3.2
%define		_snap		030502

Summary:	K Desktop Environment - games
Summary(es):	K Desktop Environment - Juegos
Summary(ja):	KDE¥Ç¥¹¥¯¥È¥Ã¥×´Ä¶­ - ¥²¡¼¥à
Summary(ko):	K µ¥½ºÅ©Å¾ È¯°æ - ³îÀÌ(°ÔÀÓ)
Summary(pl):	K Desktop Environment - gry
Summary(pt_BR):	K Desktop Environment - Jogos
Summary(zh_CN):	KDEÓÎÏ·
Name:		kdegames
Version:	%{_ver}
Release:	0.%{_snap}.1
Epoch:		7
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications/Games
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
Source0:	http://team.pld.org.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
BuildRequires:	arts-devel
BuildRequires:	arts-kde-devel >= %{version}
BuildRequires:	kdelibs-devel >= %{version}
Requires:	kdelibs >= %{version}
Obsoletes:	kdegames-kabalone
Obsoletes:	kdegames-kjezz
Obsoletes:	kdegames-kpm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	%{_docdir}/kde/HTML

%define		no_install_post_chrpath		1

%description
Libraries for kdegames. Included with this package are: kasteroids,
kblackbox, kmahjongg, kmines, konquest, kpat, kpoker, kreversi, ksame,
kshisen, ksokoban, ksmiletris, ksnake, ksirtet, katomic, kjumpingcube,
ktuberling.

%description -l es
Juegos para KDE. Incluidos en este paquete: kasteroids: arcade
kmahjongg: el popular mahjongg kmines: desarmar las minas kpat: juegos
de cartas, incluso solitario kpoker: vídeo póquer kreversi: Reversi
ksame: un juego de tablero kshisen: Shisen-Sho - relacionado con el
mahjongg ksnake: corrida de las cobras ktetris: el bien conocido
tetris

%description -l ja
KDE¥Ç¥¹¥¯¥È¥Ã¥×´Ä¶­ÍÑ¤Î¥²¡¼¥à °Ê²¼¤Î¤è¤¦¤Ê¥Ñ¥Ã¥±¡¼¥¸¤¬Æþ¤Ã¤Æ¤¤¤Þ¤¹¡£

kasteroids: ¥¢¡¼¥±¡¼¥É¥²¡¼¥à, kblackbox: a strategy game with hidden
boxes and rays, kmahjongg: ¾å³¤ kmines: ¥Þ¥¤¥ó¥¹¥¤¡¼¥Ñ¡¼, kpat:
°ì¿ÍÍÑ¥È¥é¥ó¥×¥²¡¼¥à, kpoker: ¥Ý¡¼¥«, kreversi: ¥ê¥Ð¡¼¥·, ksame: same
game, kshisen: »ÍÀî¾Ê, ksnake: ¥¹¥Í¡¼¥¯¥ì¡¼¥¹, ksokoban: ÁÒ¸ËÈÖ,
ktetris: ¥Æ¥È¥ê¥¹

%description -l pl
Biblioteki dla gier KDE: kasteroids, kblackbox, kmahjongg, kmines,
konquest, kpat, kpoker, kreversi, ksame, kshisen, ksokoban,
ksmiletris, ksnake, ksirtet, katomic, kjumpingcube, ktuberling.

%description -l pt_BR
Jogos para o KDE.

Incluídos neste pacote:

kasteroids: arcade kmahjongg: o popular mahjongg kmines: desarmar as
minas kpat: jogos de cartas, inclusive paciência kpoker: vídeo-poker
kreversi: Reversi ksame: um jogo de tabuleiro kshisen: Shisen-Sho -
relacionado com o mahjongg ksnake: corrida das cobras ktetris: o bem
conhecido tetris

%package devel
Summary:	Development files for KDE games
Summary(pl):	Pliki dla programistów KDE games
Summary(pt_BR):	Arquivos de inclusão do kdegames
Group:		X11/Development/Libraries
Requires:	kdelibs-devel >= %{version}
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-atlantik = %{version}-%{release}
Requires:	%{name}-kolf = %{version}-%{release}

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
Requires:	%{name} = %{version}-%{release}
Requires:	kdebase-core >= %{version}

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
Requires:	kdelibs >= %{version}

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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
Requires:	kdebase-core >= %{version}

%description kbounce
Claim areas and don't get disturbed.

%description kbounce -l pl
Gra polegaj±ca na pozyskiwaniu terenu wbrew przeciwnikom.

%package kenolaba
Summary:	Abalone-like board game against the computer
Summary(pl):	Gra planszowa podobna do Abalone przeciwko komputerowi
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-carddecks = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-carddecks = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-carddecks = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}
Requires:	kdebase-core >= %{version}

%description megami
Popular Gambling Game.

%description megami -l pl
Popularna gra hazardowa.

%prep
%setup -q -n %{name}-%{_snap}

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

for plik in `find ./ -name \*.desktop` ; do
	if [ -d $plik ]; then
		echo $plik
		sed -e 's/\[nb\]/[no]/g' $plik > ${plik}.1
		mv -f ${plik}.1 $plik
	fi
done

%configure \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

cd $RPM_BUILD_ROOT%{_pixmapsdir}
mv {locolor,crystalsvg}/16x16/apps/lskat.png
cd -

%find_lang atlantik	--with-kde
%find_lang kasteroids	--with-kde
%find_lang katomic	--with-kde
%find_lang kbackgammon	--with-kde
%find_lang kbattleship	--with-kde
%find_lang kblackbox	--with-kde
%find_lang kbounce	--with-kde
%find_lang kenolaba	--with-kde
%find_lang kfouleggs	--with-kde
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
%find_lang megami	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_libdir}/libkdegames.la
%attr(755,root,root) %{_libdir}/libkdegames.so.*
%{_datadir}/apps/kdegames
%{_pixmapsdir}/*/*/actions/endturn.png
%{_pixmapsdir}/*/*/*/highscore.png
%{_pixmapsdir}/*/*/*/roll.png

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

%files -f atlantik.lang atlantik
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
%{_desktopdir}/atlantik.desktop
%{_pixmapsdir}/*/*/apps/atlantik.png

%files -f kasteroids.lang kasteroids
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kasteroids
%{_datadir}/apps/kasteroids
%{_desktopdir}/kasteroids.desktop
%{_pixmapsdir}/*/*/apps/kasteroids.png

%files -f katomic.lang katomic
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/katomic
%{_datadir}/apps/katomic
%{_desktopdir}/katomic.desktop
%{_pixmapsdir}/*/*/apps/katomic.png

%files -f kbackgammon.lang kbackgammon
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbackgammon
%{_datadir}/apps/kbackgammon
%{_desktopdir}/kbackgammon.desktop
%{_pixmapsdir}/*/*/apps/kbackgammon*.png

%files -f kbattleship.lang kbattleship
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbattleship
%{_datadir}/apps/kbattleship
%{_desktopdir}/kbattleship.desktop
%{_pixmapsdir}/*/*/apps/kbattleship.png


%files -f kblackbox.lang kblackbox
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kblackbox
%{_datadir}/apps/kblackbox
%{_desktopdir}/kblackbox.desktop
%{_pixmapsdir}/*/*/apps/kblackbox.png

%files -f kbounce.lang kbounce
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbounce
%{_datadir}/apps/kbounce
%{_desktopdir}/kbounce.desktop
%{_pixmapsdir}/[!l]*/*/*/kbounce*

%files -f kenolaba.lang kenolaba
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kenolaba
%{_datadir}/apps/kenolaba
%{_desktopdir}/kenolaba.desktop
%{_pixmapsdir}/*/*/*/kenolaba*

%files -f kfouleggs.lang kfouleggs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfouleggs
%{_datadir}/apps/kfouleggs
%{_desktopdir}/kfouleggs.desktop

%files -f kjumpingcube.lang kjumpingcube
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjumpingcube
%{_datadir}/apps/kjumpingcube
%{_desktopdir}/kjumpingcube.desktop
%{_pixmapsdir}/*/*/apps/kjumpingcube.png

%files -f klickety.lang klickety
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klickety
%{_datadir}/apps/klickety
%{_desktopdir}/klickety.desktop

%files -f klines.lang klines
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klines
%{_datadir}/apps/klines
%{_desktopdir}/klines.desktop

%files kmahjongg
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmahjongg
%{_datadir}/apps/kmahjongg
%{_desktopdir}/kmahjongg.desktop
%{_pixmapsdir}/*/*/apps/kmahjongg.png

%files -f kmines.lang kmines
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmines
%{_datadir}/apps/kmines
%{_desktopdir}/kmines.desktop
%{_pixmapsdir}/*/*/apps/kmines.png

%files -f kolf.lang kolf
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kolf
%{_libdir}/libkolf.la
%attr(755,root,root) %{_libdir}/libkolf.so.*
%{_libdir}/kde3/kolf.la
%attr(755,root,root) %{_libdir}/kde3/kolf.so
%{_datadir}/config/magic
%{_datadir}/apps/kolf
%{_datadir}/mimelnk/application/*
%{_desktopdir}/kolf.desktop
%{_pixmapsdir}/*/*/apps/kolf.png

%files -f konquest.lang konquest
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konquest
%{_datadir}/apps/konquest
%{_desktopdir}/konquest.desktop
%{_pixmapsdir}/*/*/apps/konquest.png

%files -f kpat.lang kpat
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpat
%{_datadir}/apps/kpat
%{_desktopdir}/kpat.desktop
%{_pixmapsdir}/*/*/apps/kpat.png

%files -f kpoker.lang kpoker
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpoker
%{_datadir}/apps/kpoker
%{_desktopdir}/kpoker.desktop
%{_pixmapsdir}/*/*/apps/kpoker.png

%files -f kreversi.lang kreversi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kreversi
%{_datadir}/apps/kreversi
%{_desktopdir}/kreversi.desktop
%{_pixmapsdir}/*/*/apps/kreversi.png

%files -f ksame.lang ksame
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksame
%{_datadir}/apps/ksame
%{_desktopdir}/ksame.desktop
%{_pixmapsdir}/*/*/apps/ksame.png

%files -f kshisen.lang kshisen
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kshisen
%{_datadir}/apps/kshisen
%{_desktopdir}/kshisen.desktop
%{_pixmapsdir}/*/*/apps/kshisen.png

%files -f ksirtet.lang ksirtet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksirtet
%{_datadir}/apps/ksirtet
%{_desktopdir}/ksirtet.desktop
%{_pixmapsdir}/*/*/apps/ksirtet.png

%files ksmiletris
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksmiletris
%{_datadir}/apps/ksmiletris
%{_desktopdir}/ksmiletris.desktop
%{_pixmapsdir}/*/*/apps/ksmiletris.png

%files -f ksnake.lang ksnake
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/ksnake
%{_datadir}/apps/ksnake
%{_desktopdir}/ksnake.desktop
%{_pixmapsdir}/*/*/apps/ksnake.png

%files -f ksokoban.lang ksokoban
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksokoban
%{_desktopdir}/ksokoban.desktop
%{_pixmapsdir}/*/*/apps/ksokoban.png

%files -f kspaceduel.lang kspaceduel
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/kspaceduel
%{_datadir}/apps/kspaceduel
%{_desktopdir}/kspaceduel.desktop
%{_pixmapsdir}/[!l]*/*/apps/kspaceduel.png

%files -f ktron.lang ktron
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/ktron
%{_datadir}/apps/ktron
%{_desktopdir}/ktron.desktop
%{_pixmapsdir}/*/*/apps/ktron.png

%files -f ktuberling.lang ktuberling
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/ktuberling
%{_datadir}/apps/ktuberling
%{_desktopdir}/ktuberling.desktop
%{_pixmapsdir}/*/*/apps/ktuberling.png

%files -f kwin4.lang kwin4
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwin4*
%{_datadir}/apps/kwin4
%{_desktopdir}/kwin4.desktop
%{_pixmapsdir}/*/*/apps/kwin4.png

%files -f lskat.lang lskat
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/lskat
%attr(755,root,games) %{_bindir}/lskatproc
%{_datadir}/apps/lskat
%{_desktopdir}/lskat.desktop
%{_pixmapsdir}/[!l]*/*/apps/lskat.png

%files -f megami.lang megami
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/megami
%{_datadir}/apps/megami
%{_desktopdir}/megami.desktop
%{_pixmapsdir}/*/*/apps/megami.png
