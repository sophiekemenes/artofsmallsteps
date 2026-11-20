# The Emporium — oldalszerkezet

Drótváz: `wireframe/`, élő vászon
https://claude.ai/artifact/4tP7N67oGGDnzUmB7ikfUG

## Az alapötlet: a görgetés a séta a boltban

A fejléc egy utcán megállító, láncon lógó cégtábla. Lefelé görgetve a képernyő
széléről polcok nyúlnak be, hol jobbról, hol balról. A navigáció és a
márkametafora ugyanaz a mozdulat, és ezzel a legvédhetőbb megkülönböztető
tapasztalhatóvá válik.

## A sávok sorrendje

1. **A tábla.** A láncok a képernyő tetejéig futnak, levegő alatta, nem fölötte:
   így olvasódik úgy, hogy valahol fent oda van csavarozva, csak nem látod.
   A lap háttere pontosan a kép krémje legyen, hogy ne legyen látható varrat.
2. **Rövid keret.** Két-három mondat: ki ez, mi történik itt, mennyibe kerül.
   **Ide nem jön dekoráció.** A lap ritmusa: tábla gazdag, rövid keret csupasz,
   pult gazdag, polcok gazdagok de ismétlődőek, sztori csupasz, boltos egy
   macskával. A rövid keret az egyetlen csendes pillanat a lap elején, és a
   dolga, hogy gyorsan elolvasd.
3. **A pult.** `#counter` horgony, a mai csipet, Take a pinch, és egy halk
   *First time in? Start at the door.* visszaút.
4. **Az ízek.** Ízenként egy polc, hat polc. Mindegyik alatt a neve és egy sor,
   mellette a sztori szövege.
5. **A polcon lévő áru.** A fizetős dolgok. Itt áll a bolt általános készlete
   (az első, fűszeres polc), jobbról benyúlva, ahol a könyv a képernyő szélének
   dőlhet.
6. **A bőséges sztori**, lenyitható szövegekben, hogy ne váljon fallá.
7. **A boltos és a feliratkozás.** Ide alszik majd egy macska.

Nincs fejlécmenü (egy boltban nincs navigációs sáv a bejárat fölött, és a
görgetés maga a navigáció) és nincs lábléc a drótvázban. Jogi lábléc és egy link
a RECHART felé a hetes sáv alá jön.

## Miért a harmadik sávban van a pult

Egy hidegen érkezőnek a Take a pinch gomb keret nélkül értelmetlen, kap egy
véletlen utasítást. De ehhez nem kell a teljes sztori, elég a rövid keret.
A bőséges magyarázat a pult alatt él, és azt olvassa el, aki marad.

## A polcok mérete és iránya

- **Desktopon mind egyforma, 440 pixel széles**, vagyis nagyjából az oldal
  harmada, felváltva balról és jobbról lógnak be ötven pixellel, mellettük a
  szöveg. A keret levágja, ami kilóg. Nem baj, ha egy tárgyból lecsípődik.
- **Mobilon teljes szélesség**, váltott oldalon kifutva, mert nincs mellette hely.
- A méret megmondja a tárgyszámot: egy harmad szélességű polcon öt tárgy apró és
  kásás, három viszont pont jó. **A következő kör eleve három tárggyal
  készüljön**, ne a meglévő képeket kicsinyítsük.

### Kétféle polc, tudatosan

- **Benyúló polc**: egy konzol, az egyik vége a képernyő széléhez fut, a tárgyak
  lelóghatnak azon a végén. Tükrözött változat kell a másik oldalra, és egyetlen
  tárgy sem lóghat le azon a szélen, amelyik a képernyő széle lesz.
- **Teljes polc**: két konzol, végig ér, bármilyen szélességen működik, nem kell
  tükrözni. Cserébe elveszik a séta ritmusa; ezt pótolja a váltott eltolás.

## A pult

**A pult nem polc, és nem szabad polcnak látszania.** A polc az, amit
nézegetsz; a pult az, ahol kiszolgálnak. Nehezebb, közelebb van, szemből nézed.

**A pult a lap egyetlen sötét sávja.** A márkakönyv szerint oldalanként egy
sötét felület van. A pult a jelöltje: ez a legfontosabb blokk, és ha ez az
egyetlen sötét folt a krém lapon, akkor nem kell odaírni, hogy „itt vagy".
A térbeli olvasat is igaz lesz: a sötét nem egy sáv, hanem a bolt belseje a pult
mögött, te pedig kívül állsz a megvilágított fánál.

**A pult képe bútor, üres hellyel, nem feliratos kép.** A mai csipet szövege
valódi betű, nem a képre rajzolva, különben nem kereshető, nem olvassa fel a
képolvasó, nem fordítható és nem cserélhető.

**A szöveg nem állhat a fán.** A pult lapja közepesen barna, erősen erezett;
azon bármilyen betű rosszul olvasható. Ezért a szöveg egy **krém kártyán** ül
(`paper-light`, #FFF8EE), enyhén megdöntve, hajszálkerettel.

- **Desktopon** a kártya a pult üres közepén fekszik.
- **Mobilon** a kártya az elülső élen át, a festett panelen ül és a sötétbe lóg
  alá. Így a pult lapja a mérleggel, a címkékkel, a ceruzával és a szemüveggel
  érintetlen marad, és a kártya jelentése is jobb lesz: nem rajta hever, hanem
  **feléd tolták át az élen.** Ezzel nem kell külön mobil kivágás.

A mérleg **üres serpenyője** a mechanika képi otthona: a *That's your three*
után az üres serpenyő magától elmondja, hogy mára ennyi volt.

## Belépési pontok: horgony, nem második oldal és nem detektálás

**Ne detektálj böngészőben, hogy ki járt már itt.** Három helyen bukik:
eszközönként külön (aki laptopon találta meg, telefonon újra új látogató,
miközben a telefon a fő belépő a levélből), az iOS Safari hét nap után törölheti
a szkript írta localStorage-ot (vagyis épp a heti visszatérő kapja újra a
bemutatkozást), és villog, ha a döntés betöltés után JS-ben születik.

**A levél linkje `#counter` horgonyra visz**, ugyanarra az egy oldalra.
Determinisztikus, nincs tárolás, nincs villogás, egy oldalt kell karbantartani,
és felfelé görgetve a bolt eleje felé sétálsz, ami nem kerülőút, hanem a metafora.

**Második oldal csak kiváltó feltételre:** ha a bemutatkozó rész annyira
meghízik, hogy a pulthoz érkező mérhetően vár rá mobilneten.

## Személyesítés

Az Életkaland oldalon a feliratkozót néven szólítja az oldal. Ez megmarad, de
jobb helyre kerül:

- **A név a levél linkjéből jöjjön, ne a böngészőből**: a link vigyen egy
  azonosítót, így a pult bármelyik eszközön tudja, ki jött, már az első
  kattintásra, és túléli a Safari takarítását.
- **Ne a nevet tedd az URL-be**, hanem azonosítót, amit az oldal felold: egy
  továbbküldött link különben más nevén köszön.
- **A köszönés egyszer szóljon, a pultnál.** A boltos egyszer néz fel.
- A tárolás jó kis szívességekre (melyik ízt húztad utoljára, egy egyszeri súgó
  elrejtése): ezek lágyan hibáznak. Verzióválasztásra soha.

## Mozgás és teljesítmény

- **Ne animáld görgetésre.** Nehéz, a mobilböngészőkben csúnya, és szembe megy a
  pozicionálással: egy oldal, ami mozog, amikor nézed, követeli a figyelmedet.
  Egy bolt nem mozdul meg, amikor belépsz. A polc egyszerűen ott van.
- **Vetett árnyék nincs.** A mélység vonalvastagsággal és átfedéssel készül, nem
  blurral: vastagabb vonal az elülső élen, vékony a hátsón, a tárgyak egy
  hajszálnyit rálógnak a deszka élére.
- **Betűkészlet: három szerep, nem öt család.** A háziak jók ide: Cormorant
  Garamond (display), Lora (szöveg), Shadows Into Light Two (kézírás). Az utóbbi
  az, amivel a piros firka valódi szövegként szedhető.
- Minden kép WebP, töréspontonként méretezve. A 2,6 MB-os PNG-ből 250–400 kB lesz.
