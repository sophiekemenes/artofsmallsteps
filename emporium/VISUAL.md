# The Emporium — vizuális rendszer

## A stílus

Meleg, kézzel festett, tónusos illusztráció: tinta-kontúr plusz kitöltött szín,
sraffozással. **Nem** vonalrajz, és **nem** fotórealizmus.

Ez egy korábbi tévedés javítása. Az első javaslat tiszta metszet-kontúr volt egy
direkt színnel, és az hideg és steril lett. A „ne legyen szkeumorf" szabály túl
szélesre volt húzva: a baj nem a gazdagsággal van, hanem a hazug anyagimitációval
egy felületi elemen (vetett árnyék, fotószerű fatextúra, plasztikus gomb). Egy
gazdagon illusztrált világ nem szkeumorf. Egy olyan márkánál, aminek a melegség
az ajánlata, a steril a rosszabb hiba.

A referenciák közül: az apotékárium-címke anyagminta, nem irány, és a kinézete
mára generikus (minden kézműves szappan és gin ezt használja). A rovargyűjtemény
fiók az **információs architektúrát** adja (sok apró tétel, kitűzve, cédulával,
számozva, pásztázható rácsban). A harmadik referencia (merész csomagolás) pedig
a **humort**, ami az első kettőből teljesen hiányzik: azok halálosan komolyak.

## Paletta

A ház földszíne nem változik programonként. Minden oldal `paper` (#FBF1E3),
a szöveg `text`, az elválasztók `hairline`. **A programot az akcentusai
különböztetik meg, nem a papírja.**

Az Emporium tokenjei be vannak írva az Art of Small Steps design systembe
(`tokens.json` + a README Colour fejezete):

| token | hex | kontraszt paperen | szerep |
| --- | --- | --- | --- |
| `emporium-teal` | #123C3B | 10,8:1 | címek, elsődleges gombok, az oldalankénti egy sötét sáv |
| `emporium-rust` | #A4492F | 5,3:1 | linkek, eyebrow, kézírásos jegyzetek |
| `emporium-turquoise` | #25A9A6 | 2,6:1 | ritka élénk kiemelés. **Papíron soha nem szöveg.** Tealen 4,2:1, tehát 24px fölött. |
| `emporium-brass` | #B68A45 | 2,8:1 | öreg arany illusztráción és festett kereten belül. **Soha nem szöveg.** |

**Nincs második krém.** Egy `paper`-hez közeli pergamen (pl. #F4E5C9, ami 1,11:1
hozzá képest) hibának látszik, nem döntésnek: vagy pontosan egyezz, vagy térj el
látványosan. Ugyanígy nincs második szövegszín: a `text` és az `ink` már létezik.

**Nyitott:** a pult képének saját tealje **#0B4E49**, világosabb és zöldebb, mint
az `emporium-teal`. Vagy a paletta igazodik hozzá, vagy a pult. Két teal ne legyen.

## A tárgyak

### A három szabály

1. **A fűszer metafora, nem áru.** Polconként legfeljebb **egy** valódi fűszeres
   üveg. Ha négyben tényleg kardamom áll, az oldal élelmiszerboltot ígér.
2. **Minden polcon legyen legalább egy tárgy, ami kicsit rosszul van**: olyan
   munkát végez, amire nem találták ki, vagy látszik rajta, hogy valaki épp
   letette.
3. **Viktoriánus ünnepélyesség egy jelentéktelen tárgyon: ez maga a vicc.**

### Ízcsoportonként

**Sós** — alap, földelés, a hétköznapi dolgok rendbetétele. *Legyártva.*
Stoppolófa félig megstoppolt zoknival · fakanál laposra kopva · egy pár bakancs
kifűzve · üveg durva sóval *(az egy valódi fűszer)* · horpadt bádog ébresztőóra.

**Édes** — kedvesség, öröm, valami, amit magadnak adsz. *Legyártva.*
Csorba csésze növénnyel benőve · süti egy harapással · ágymelegítő kötött
huzatban · kerti virágok befőttesüvegben · kockacukor sárgaréz csipesszel.
*Ez a leggyengébb polc, közel van egy általános cottagecore-hoz. Ide jön a
gombolyaggal játszó macska.*

**Savanyú** — csipkelődés, pimaszság, szemtelenség. *Legyártva.*
Üveg sárgaréz kulcsokkal, egyik sem nyit semmit · üveg páratlan zoknikkal ·
jól használt csúzli · gumibélyegző és elhasznált bélyegzőpárna · kilazult
ajtókopogtató.

**Keserű** — amit kerülgetsz. *Legyártva, ezen lóg a vörös macska.*
**Kézitükör, lefelé fordítva** *(a lista legerősebb tárgya)* · barna hivatalos
boríték felbontatlanul · poros ugrálókötél · üveg kávébabbal *(az egy valódi
fűszer)* · óra, amiről levették a mutatókat.
*Ez a mérce a többihez: a tükör, a boríték és a kötél hármasban már mindent
elmond, a kávébab és az óra ugyanazt ismétli.*

**Csípős** — bátorság, kockázat. *Legyártva, a legtisztább a hatból.*
Egyetlen görkorcsolya · elégett gyufaszál félig nyitott gyufásdoboz mellett ·
összetekert, zsineggel átkötött térkép, sosem kinyitva · lecsavart
kerékpárcsengő · üveg szárított csilivel *(az egy valódi fűszer)*.

**Új lábas** — eszköz- vagy helyszínváltás (hatodik tengely, nem íz).
*Legyártva, ezen alszik a fekete macska.*
Lábas, amiben növény nő · távcső fordítva letéve · üveg használt buszjegyekkel ·
teáskanna kaktusszal · konyhai időzítő.

### Visszatérő szereplők

- **A csorba, kék virágos csésze** — a folytonosság horgonya a cégtáblához
- **A sárgaréz tetejű üvegek** — a bolt tárolórendszere
- **Egy pár kerek szemüveg, épp letéve** — a boltos nyoma

## A macskák: szereplőgárda, nem kabala

Sophie-nak több macskája van, és a kincsesterkep.hu macska-bölcsesség
generátoraiban már szerepelnek (lásd a repóban a `cat-wisdom/` mappát). A boltban
ugyanazok az állatok élnek, és ez a **híd a magyar és az angol oldal között**:
sehol nincs kiírva, de ettől lesz a bolt lakott hely, nem összerakott arculat.

- **A türkizszemű szürke cirmos a cégtáblán marad, és csak ott.** Az a bolt
  cégére, az a maradandó.
- **A többi macska a boltban mozog**: a vörös lóg a keserű polcról, a fekete
  alszik az új lábason. A vörös-fehér még nem bukkant fel.
- **Képernyőnként egy macska, soha nem kettő.** A ritkaság az, amitől esemény
  marad.
- **Minden macska mindig ugyanúgy nézzen ki.** Kell egy szereplőlap, macskánként
  egy mondat a színéről, és azt kell minden generáláskor szó szerint bemásolni.
- **Minden macska mást csináljon**, egy mozdulat csak egyszer. Eddig:
  kikukucskál a tábla szalagja mögül, lóg a polcról, alszik. Tervezett: alszik a
  feliratkozó szakaszon, gombolyagozik az édes polcon.

A lógós macska azért működik, mert **kitör a sávból**: lelóg a polcról az alatta
lévő üres helybe, és ettől a polc tárgy lesz egy falon, nem dekoratív csík.
Ez egyben magasabb sávot kér (2:1 a szokásos 3:1 helyett).

## Gyártási és megrendelési szabályok

- **Tárgyanként külön kép, nem jelenet**, átlátszó vagy sima háttérrel, hogy
  elhelyezhető legyen. Egy kész jelenetet nem lehet újrarendezni, és
  töréspontonként más számú tárgy kell.
- **Három tárgy polconként** az új méretnél. Mobilon nagyobban, nem ugyanaz
  kicsiben.
- **Sziluett-próba**: 60 pixelen is felismerhető legyen.
- **Semmi felirat, semmi logó.** A generált szöveg kibetűzhetetlen; a címkékre
  valódi betű kerül. (A buszjegyes üvegen most véletlenül olvasható szám van.)
- **Semmi, ami évül**: konkrét telefon, márka, autó nem.
- **Türkiz képernyőnként egyszer.** Figyelni kell rá: a deszka kopott türkiz
  festéke, a bögrék és az óra együtt már sok belőle.
- **A háttér legyen eleve #FBF1E3**, vagy marad a körbevágás.

## Körbevágás: mikor és hogyan

A `assets/` mappában a legtöbb kép ki van vágva átlátszó háttérre. A módszer a
kép **négy széléről indított kitöltés**, ami csak a külső, összefüggő hátteret
szedi ki, ezért a belső világos felületek (a tábla szalagja, a szemüveg lencséi,
az üvegek üvege) sértetlenek maradnak.

**Két korlátja van, és mindkettő számít:**

1. **A zárt területekhez nem jut el.** A mérleg láncai közötti rések és a
   virágok közti lyukak megtartják az eredeti hátteret. Papír alapon ez
   láthatatlan (krém a krémen), **sötét alapon viszont kivilágít.**
2. **Textúrás háttéren nem működik.** A beégetett, vignettás teal háttér
   foltokban marad, és közben belevág a pult saját türkiz frontjába.

**Ezért a szabály:** amit papíron használunk, azt nyugodtan vágjuk. Amit sötét
alapra teszünk, azt **eleve a végleges háttérrel kell generálni**, nem kivágni.
A pult ezért teal háttérrel készült, és a sáv háttere a kép szélének színére
(#083A37) van állítva, hogy a vignetta észrevétlenül folytatódjon.
