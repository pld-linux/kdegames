#
# Conditional build:
# _with_pixmapsubdirs - leave different depth/resolution icons
#
Summary:	K Desktop Environment - games
Summary(es):	K Desktop Environment - Juegos
Summary(ja):	KDE¥Ç¥¹¥¯¥È¥Ã¥×´Ä¶­ - ¥²¡¼¥à
Summary(ko):	K µ¥½ºÅ©Å¾ È¯°æ - ³îÀÌ(°ÔÀÓ)
Summary(pl):	K Desktop Environment - gry
Summary(pt_BR):	K Desktop Environment - Jogos
Summary(zh_CN):	KDEÓÎÏ·
Name:		kdegames
Version:	3.0.4
Release:	5
Epoch:		7
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications/Games
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n - need update!
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Source2:	%{name}-extra_icons.tar.bz2
Patch0:		%{name}-kpatcards.patch
BuildRequires:	arts-devel
BuildRequires:	awk
BuildRequires:	kdelibs-devel = %{version}
Requires:	qt >= 3.0.5
Requires:	kdelibs = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	kdegames-kabalone
Obsoletes:	kdegames-kjezz
Obsoletes:	kdegames-kpm

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML

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
Biblioteki dla gier KDE.

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
Requires:	kdegames = %{version}

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

%package kasteroids
Summary:	KDE Asteroids clone
Summary(pl):	Klon Asterids dla KDE
Summary(pt_BR):	Destrua os asteróides para não ser destruído
Group:		X11/Applications/Games
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
Requires:	kdelibs >= %{version}

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
Requires:	kdelibs >= %{version}

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
Requires:	kdelibs >= %{version}

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
Requires:	kdelibs >= %{version}

%description kbounce
Claim areas and don't get disturbed.

%description kbounce -l pl
Gra polegaj±ca na pozyskiwaniu terenu wbrew przeciwnikom.

%package kenolaba
Summary:	Kenolaba - game for KDE
Summary(pl):	Kenolaba - gra dla KDE
Group:		X11/Applications/Games
Requires:	kdelibs >= %{version}

%description kenolaba
Kenolaba - game for KDE.

%description kenolaba -l pl
Kenolaba - gra dla KDE.

%package kfouleggs
Summary:	KDE kfouleggs
Summary(pl):	kfouleggs dla KDE
Summary(pt_BR):	Mais um jogo que lembra o estilo Tetris
Group:		X11/Applications/Games
Requires:	kdelibs >= %{version}

%description kfouleggs
KDE kfouleggs.

%description kfouleggs -l pl
kfouleggs dla KDE.

%description kfouleggs -l pt_BR
Mais um jogo que lembra o estilo Tetris.

%package kjumpingcube
Summary:	A little tactical game for KDE
Summary(pl):	Prosta gra taktyczna dla KDE
Summary(pt_BR):	Jogo de estratégia para 2 contendores
Group:		X11/Applications/Games
Requires:	kdelibs >= %{version}

%description kjumpingcube
KJumpingCube is a simple tactical game. You can play it against the
computer or against the friend. The playing field consists of squares
that contains points. By clicking on the squares you can increase the
points, and if the poinst reach a maximum the points will jump to the
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

%package klines
Summary:	Lines for KDE
Summary(pl):	Gra Lines dla KDE
Group:		X11/Applications/Games
Requires:	kdelibs >= %{version}

%description klines
Lines for KDE.

%description klines -l pl
Gra Lines dla KDE.

%package kmahjongg
Summary:	KDE Mahjongg clone
Summary(pl):	Klon gry Mahjongg dla KDE
Summary(pt_BR):	Versão do jogo Mahjongg para o KDE
Group:		X11/Applications/Games
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
Requires:	kdelibs >= %{version}

%description kmines
This is a very classical minesweeper written from scratch.
- 3 predefined levels : Easy : 8x8 with 10 mines Normal : 16x16 with
  40 mines Expert : 30x16 with 99 mines
- Custom levels
- High Scores.

%description kmines -l pl
Klasyczna wersja znanej gry "saper" dla KDE, napisana od zera. Cechy:
- 3 predefiniowane poziomy (³atwy - 8x8 z 10 minami; normalny - 16x16
  z 40 minami; ekspert - 30x16 z 99 minami),
- definiowalne poziomy
- lista najlepszych wyników.

%description kmines -l pt_BR
Versão do jogo 'caça-minas' para o KDE.

%package konquest
Summary:	KDE version of Gnu-Lactic Konquest
Summary(pl):	Podbój galaktyki
Summary(pt_BR):	Jogo espacial de estratégia
Group:		X11/Applications/Games
Requires:	kdelibs >= %{version}

%description konquest
KDE version of Gnu-Lactic Konquest.

%description konquest -l pl
Podbój galaktyki.

%description konquest -l pt_BR
Jogo espacial de estratégia.

%package kpat
Summary:	KDE solitaire patience game
Summary(pl):	Pasjanse dla KDE
Summary(pt_BR):	Versão do jogo 'Paciência' para o KDE
Group:		X11/Applications/Games
Requires:	kdegames-carddecks = %{version}
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
Requires:	kdegames-carddecks = %{version}
Requires:	kdelibs >= %{version}

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
Requires:	kdelibs >= %{version}

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
Requires:	kdelibs >= %{version}

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
Requires:	kdelibs >= %{version}

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
Requires:	kdelibs >= %{version}

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
Requires:	kdelibs >= %{version}

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
Requires:	kdelibs >= %{version}

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
Requires:	kdelibs >= %{version}

%description ktron
KTron is a simple Trone-Clone for the KDE. You can play KTron against
the computer or a friend.

The aim of the game is to live longer then your opponent. To do That,
avoid running into a wall, your own tail and that of your opponent.

%description ktron -l pl
KTron to prosty klon Trone dla KDE. Mo¿ena graæ w KTron przeciwko
komputerowi lub koledze.

Celem gry jest prze¿yæ d³u¿ej ni¿ przeciwnik. Aby tego dokonaæ trzeba
unikaæ uderzenia w ¶cianê, ogon w³asny lub przeciwnika.

%description ktron -l pt_BR
Versão do jogo Tron / Motos de Luz para o KDE.

%package ktuberling
Summary:	KDE game for small children
Summary(pl):	Gra dla ma³ych dzieci
Summary(pt_BR):	Jogo de desenho do 'Homem-batata' para crianças
Group:		X11/Applications/Games
Requires:	kdelibs >= %{version}

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
Requires:	kdelibs >= %{version}

%description lskat
Lieutnant Skat.

%description lskat -l pl
Lskat dla KDE.

%description lskat -l pt_BR
Jogo de cartas Lieutenant Skat para KDE

%prep
%setup -q
%patch0 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \
	--with-qt-dir=%{_prefix} \
	--with-pam="yes" \
	--disable-rpath \
	--enable-final
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Amusements

%{__make} DESTDIR=$RPM_BUILD_ROOT install

mv -f $RPM_BUILD_ROOT%{_applnkdir}/{Toys/ktuberling.desktop,Amusements}
mv -f $RPM_BUILD_ROOT%{_applnkdir}/Games/{TacticStrategy,Strategy}

for i in $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/48x48/apps/*
do
%if %{?_with_pixmapsubdirs:1}%{!?_with_pixmapsubdirs:0}
	ln -sf `echo $i | sed "s:^$RPM_BUILD_ROOT%{_pixmapsdir}/::"` $RPM_BUILD_ROOT%{_pixmapsdir}	
%else
	cp -af $i $RPM_BUILD_ROOT%{_pixmapsdir}
%endif
done

bzip2 -dc %{SOURCE2} | tar xf - -C $RPM_BUILD_ROOT%{_pixmapsdir}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

for f in `find $RPM_BUILD_ROOT%{_applnkdir} -name '.directory' -o -name '*.desktop'` ; do
	awk -v F=$f '/^Icon=/ && !/\.xpm$/ && !/\.png$/ { $0 = $0 ".png";} { print $0; } END { if(F == ".directory") print "Type=Directory"; }' < $f > $f.tmp
	mv -f $f{.tmp,}
done

%find_lang kasteroids	--with-kde
%find_lang katomic	--with-kde
%find_lang kbackgammon	--with-kde
%find_lang kbattleship	--with-kde
%find_lang kblackbox	--with-kde
%find_lang kbounce	--with-kde
%find_lang kenolaba	--with-kde
%find_lang kfouleggs	--with-kde
%find_lang kjumpingcube	--with-kde
%find_lang klines	--with-kde
%find_lang kmahjongg	--with-kde
%find_lang kmines	--with-kde
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
%find_lang libkdegames	--with-kde
%find_lang libkdehighscores	--with-kde
%find_lang multiplayers	--with-kde
%find_lang lskat	--with-kde

cat libkdehighscores.lang	>> libkdegames.lang
cat multiplayers.lang		>> libkdegames.lang

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   ksirtet -p /sbin/ldconfig
%postun ksirtet -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f libkdegames.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_datadir}/apps/kdegames/pics/*
%{_datadir}/apps/sounds/*/*.wav
%attr(755,root,root) %{_libdir}/libkdegames.so.*.*
%attr(755,root,root) %{_libdir}/libkdehighscores.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_includedir}/kgame
%attr(755,root,root) %{_libdir}/libkdegames.so
%attr(755,root,root) %{_libdir}/libksirtet*.so
%attr(755,root,root) %{_libdir}/libkdehighscores.so
%attr(755,root,root) %{_libdir}/libkdegames.la
%attr(755,root,root) %{_libdir}/libksirtet*.la
%attr(755,root,root) %{_libdir}/libkdehighscores.la
%{_pixmapsdir}/*/*/*/highscore.*
%{_pixmapsdir}/*/*/*/roll.*

%files carddecks
%defattr(644,root,root,755)
%{_datadir}/apps/carddecks

#################################################
#             KASTEROIDS
#################################################

%files -f kasteroids.lang kasteroids
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kasteroids
%{_applnkdir}/Games/Arcade/kasteroids.desktop
%{_datadir}/apps/kasteroids
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/kasteroids.png}
%{_pixmapsdir}/kasteroids.png

#################################################
#             KATOMIC
#################################################

%files -f katomic.lang katomic
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/katomic
%{_applnkdir}/Games/Strategy/katomic.desktop
%{_datadir}/apps/katomic
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/katomic.png}
%{_pixmapsdir}/katomic.png

#################################################
#             KBACKGAMMON
#################################################

%files -f kbackgammon.lang kbackgammon
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbackgammon
%attr(755,root,root) %{_libdir}/kbackgammon.so
%{_applnkdir}/Games/Board/kbackgammon.desktop
%{_datadir}/apps/kbackgammon
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/kbackgammon*.png}
%{_pixmapsdir}/kbackgammon*.png

#################################################
#             KBATTLESHIP
#################################################

%files -f kbattleship.lang kbattleship
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbattleship
%{_applnkdir}/Games/Board/kbattleship.desktop
%{_datadir}/apps/kbattleship
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/kbattleship.png}
%{_pixmapsdir}/kbattleship.png

#################################################
#             KBLACKBOX
#################################################

%files -f kblackbox.lang kblackbox
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kblackbox
%{_applnkdir}/Games/Board/kblackbox.desktop
%{_datadir}/apps/kblackbox
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/kblackbox.png}
%{_pixmapsdir}/kblackbox.png

#################################################
#             KFOULEGGS
#################################################

%files -f kfouleggs.lang kfouleggs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfouleggs
%{_applnkdir}/Games/Arcade/kfouleggs.desktop
%{_datadir}/apps/kfouleggs

%files -f kjumpingcube.lang kjumpingcube
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kjumpingcube
%{_applnkdir}/Games/Strategy/kjumpingcube.desktop
%{_datadir}/apps/kjumpingcube
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/kjumpingcube.png}
%{_pixmapsdir}/kjumpingcube.png

#################################################
#             KLINES
#################################################

%files -f klines.lang klines
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klines
%{_applnkdir}/Games/Strategy/klines.desktop
%{_datadir}/apps/klines
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/klines.png}
%{_pixmapsdir}/klines.png

#################################################
#             KMAHJONGG
#################################################

#%files kmahjongg
%files -f kmahjongg.lang kmahjongg
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmahjongg
%{_applnkdir}/Games/Board/kmahjongg.desktop
%{_datadir}/apps/kmahjongg
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/kmahjongg.png}
%{_pixmapsdir}/kmahjongg.png

#################################################
#             KMINES
#################################################

%files -f kmines.lang kmines
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmines
%{_applnkdir}/Games/Strategy/kmines.desktop
%{_datadir}/apps/kmines
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/kmines.png}
%{_pixmapsdir}/kmines.png

#################################################
#             KONQUEST
#################################################

%files -f konquest.lang konquest
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konquest
%{_applnkdir}/Games/Strategy/konquest.desktop
%{_datadir}/apps/konquest
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/konquest.png}
%{_pixmapsdir}/konquest.png

#################################################
#             KPAT
#################################################

%files -f kpat.lang kpat
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpat
%{_applnkdir}/Games/Card/kpat.desktop
%{_datadir}/apps/kpat
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/kpat.png}
%{_pixmapsdir}/kpat.png

#################################################
#             KPOKER
#################################################

%files -f kpoker.lang kpoker
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpoker
%{_applnkdir}/Games/Card/kpoker.desktop
%{_datadir}/apps/kpoker
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/kpoker.png}
%{_pixmapsdir}/kpoker.png

#################################################
#             KREVERSI
#################################################

%files -f kreversi.lang kreversi
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kreversi
%{_applnkdir}/Games/Board/kreversi.desktop
%{_datadir}/apps/kreversi
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/kreversi.png}
%{_pixmapsdir}/kreversi.png

#################################################
#            KSAME
#################################################

%files -f ksame.lang ksame
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksame
%{_applnkdir}/Games/Strategy/ksame.desktop
%{_datadir}/apps/ksame
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/ksame.png}
%{_pixmapsdir}/ksame.png

#################################################
#             KSIRTET
#################################################

%files -f ksirtet.lang ksirtet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksirtet
%{_applnkdir}/Games/Arcade/ksirtet.desktop
%{_libdir}/libksirtet*.so.*.*.*
%{_datadir}/apps/ksirtet
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/ksirtet.png}
%{_pixmapsdir}/ksirtet.png

#################################################
#             KSMILETRIS
#################################################

#%files ksmiletris
%files -f ksmiletris.lang ksmiletris
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksmiletris
%{_applnkdir}/Games/Arcade/ksmiletris.desktop
%{_datadir}/apps/ksmiletris
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/ksmiletris.png}
%{_pixmapsdir}/ksmiletris.png

#################################################
#             KSHISEN
#################################################

%files -f kshisen.lang kshisen
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kshisen
%{_applnkdir}/Games/Board/kshisen.desktop
%{_datadir}/apps/kshisen
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/kshisen.png}
%{_pixmapsdir}/kshisen.png

#################################################
#             KSNAKE
#################################################

%files -f ksnake.lang ksnake
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/ksnake
%{_applnkdir}/Games/Arcade/ksnake.desktop
%{_datadir}/apps/ksnake
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/ksnake.png}
%{_pixmapsdir}/ksnake.png

#################################################
#             KSOKOBAN
#################################################

%files -f ksokoban.lang ksokoban
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksokoban
%{_applnkdir}/Games/Strategy/ksokoban.desktop
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/ksokoban.png}
%{_pixmapsdir}/ksokoban.png

#################################################
#             KSPACEDUEL
#################################################

%files -f kspaceduel.lang kspaceduel
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/kspaceduel
%{_applnkdir}/Games/Arcade/kspaceduel.desktop
%{_datadir}/apps/kspaceduel
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*x*/apps/kspaceduel.png}
%{_pixmapsdir}/kspaceduel.png

#################################################
#             KTRON
#################################################

%files -f ktron.lang ktron
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/ktron
%{_applnkdir}/Games/Arcade/ktron.desktop
%{_datadir}/apps/ktron
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/ktron.png}
%{_pixmapsdir}/ktron.png

#################################################
#             KTUBERLING
#################################################

%files -f ktuberling.lang ktuberling
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/ktuberling
%{_applnkdir}/Amusements/ktuberling.desktop
%{_datadir}/apps/ktuberling
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/ktuberling.png}
%{_pixmapsdir}/ktuberling.png

#################################################
#             KWIN4
#################################################

%files -f kwin4.lang kwin4
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwin4*
%{_applnkdir}/Games/Board/kwin4.desktop
%{_datadir}/apps/kwin4
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/kwin4.png}
%{_pixmapsdir}/kwin4.png

#################################################
#             LSKAT
#################################################

%files -f lskat.lang lskat
%defattr(644,root,root,755)
%attr(755,root,games) %{_bindir}/lskat
%attr(755,root,games) %{_bindir}/lskatproc
%{_applnkdir}/Games/Card/lskat.desktop
%{_datadir}/apps/lskat
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*x*/apps/lskat.png}
%{_pixmapsdir}/lskat.png

#################################################
#             KBOUNCE
#################################################

%files -f kbounce.lang kbounce
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbounce
%{_applnkdir}/Games/Arcade/kbounce.desktop
%{_datadir}/apps/kbounce
%{?_with_pixmapsubdirs:%{_pixmapsdir}/*color/*x*/apps/kbounce.png}
%{_pixmapsdir}/kbounce.png

#################################################
#             KENOLABA
#################################################

%files -f kenolaba.lang kenolaba
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kenolaba
%{_applnkdir}/Games/Board/kenolaba.desktop
%{_datadir}/apps/kenolaba
%{?_with_pixmapsubdirs:%{_pixmapsdir}/hicolor/*x*/apps/kenolaba.png}
%{_pixmapsdir}/kenolaba.png
