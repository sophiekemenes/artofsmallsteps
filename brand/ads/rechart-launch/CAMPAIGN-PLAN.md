# RECHART Meta kampányterv (TERVEZET, Sophie jóváhagyására vár)

`web-campaign` session, 2026-11-22. Amit Sophie jóváhagy, azt itt **JÓVÁHAGYVA** jelöljük.

## 1. Felépítés

- **1 kampány**: `RECHART_launch_2026` · cél: **Sales (Értékesítés)** · konverziós esemény: **Purchase** (a weboldal datasetje).
- **1 hirdetéscsoport** (a kis költés miatt nem bontjuk szét, így gyorsabban tanul): `UK_cold_interest`
  - Ország: **Egyesült Királyság**. Kor: **28–60**. Nem: mindenki.
  - Érdeklődés (egy csoportban, VAGY kapcsolattal): personal development, self-help, life coaching, mindfulness, journaling, career change, Brené Brown, Psychology Today.
  - Advantage+ audience: **KI** az első 7 napban, hogy tényleg hideg, érdeklődés-alapú legyen. Utána, ha jön vásárlás, kipróbálhatjuk BE-kapcsolva.
  - Elhelyezés: Advantage+ placements, de **Audience Network kizárva** (sok a véletlen kattintás).
- **Hirdetések, első kör (Sophie, 2026-11-23):** **B1** (80-as évekbeli lány, `b1-80s-girl.md`, JÓVÁHAGYVA), **D** (Draw your other map videó, 4:5 feed+Reels, 9:16 Stories, szöveg a `RECHART-LAUNCH-ADS-v1.md` D részében, JÓVÁHAGYVA), és a 3. a copy session angol hangalámondásos bézs videója (**FELFÜGGESZTVE 2026-11-23**: Sophie-nak nem tetszett a hang, a copy session új hanggal és halk zenével újragyártja; a mostani `beige-drawing_*_en.mp4` fájlokat NE használjuk): **minden elhelyezésben a `beige-drawing_4x5_en.mp4` megy** (a 9:16-osban a felső felirat a Stories/Reels felső 14%-ába esik, ott a profilnév eltakarná). Tartalék: a copy session A–F változatai.
- Korábbi terv: a RECHART copy session 6 változatából (A–F) az első körben a Sophie által kiválasztott **3**. Ha 4 nap után valamelyik egyértelműen gyenge, kicseréljük a következőre.
- **CTA gomb**: „Learn more” (hideg közönség, a sales oldalra visz, nem egyből fizetésre).
- **Advantage+ creative**: a szöveget vagy képet átíró/átalakító javítások KI (hogy a hangod és az akvarellek változatlanok maradjanak). Az elhelyezésekhez igazító vágás maradhat.
- **Céloldal**: minden hirdetés → `https://artofsmallsteps.com/wayfinder-method/` (a Find Your Bearings játék nem része a tölcsérnek).

## 2. Napi keret és futás

- **£15 / nap** (javaslat). Indítás: amint a mérés élesben megy és teszteltük.
- **Fiók-szintű költési limit**: **£300** (Ads Manager → Fizetési beállítások → Fiók költési limitje). Ez a végső biztonsági fék, akkor is megáll, ha mi elfelejtjük.
- **3 január**: az ár £69 lesz, a hirdetésszövegek ár- és dátum-sorait cserélni kell (a copy session megírta a cserét).

## 3. Leállítási szabály (előre megbeszélve, hogy ne érzésből döntsünk)

| Ha... | akkor... |
|---|---|
| £30 költés után a link-CTR 0,7% alatt van | hirdetést cserélünk (a kép vagy az első mondat nem működik) |
| £45 költés után 0 InitiateCheckout (vásárlás gomb kattintás) | szünet, megnézzük az oldalt és a hirdetést együtt |
| **£80 költés után 0 vásárlás** | **szünet**, átnézzük, mit változtassunk, csak utána indul újra |
| egy vásárlás ára (CPA) 3 nap átlagában £60 fölött van | csökkentjük a keretet vagy cserélünk hirdetést |

(£80 ≈ a jelenlegi ár kétszerese. Kisebb számmal nem lehet jó döntést hozni, nagyobbal feleslegesen sok pénz menne el.)

## 4. UTM-ek

Ads Manager → hirdetés → **URL paraméterek** mezőbe, mindegyik hirdetésnél ugyanez:

```
utm_source=meta&utm_medium=paid_social&utm_campaign=rechart_launch_2026&utm_content={{ad.name}}&utm_term={{adset.name}}
```

Hirdetésnevek: `A_feels-off_4x5`, `B_permission_4x5`, stb. (betű + rövid név + formátum), így a jelentésben is olvasható.

Az UTM-eket csak akkor látjuk, ha van analitika az oldalon (lásd 6.).

## 5. Jelentés formátuma (mindig ebben a sorrendben)

| Időszak | Költés | Kattintás (link) | Oldalmegtekintés (LPV) | Vásárlás gomb (InitiateCheckout) | Vásárlás | Egy vásárlás ára |
|---|---|---|---|---|---|---|

Plusz egy mondat: hol esik le a legtöbb ember (kattintás → oldal, oldal → gomb, vagy gomb → fizetés), és mit javaslok rá.

## 6. Nyitott kérdés Sophie-nak: analitika

Javaslat: **Vercel Web Analytics** bekapcsolása (az oldal már a Vercelen van, nem használ sütit, ezért nem kell hozzá hozzájárulás, és látszanak az UTM-ek). GA4 sütiket használ, csak elfogadás után futhatna, és sok munka egy kis oldalhoz. Kell-e?

## 7. Indulás előtti teszt (pénzköltés előtt)

1. Telefonon: Chrome és Safari, banner, "Igen" / "Nem", oldal, vásárlás gomb.
2. **Facebook és Instagram alkalmazáson belüli böngészőben**: a hirdetés előnézetéből megnyitva végigkattintani az oldalt a Stripe fizetési oldalig (fizetés nélkül).
3. Meta Events Manager → Test Events: PageView, ViewContent, InitiateCheckout látszik.
4. Make: a Purchase szerveresemény tesztje (Sophie saját vásárlásával vagy egy Stripe-ban visszatérített rendeléssel, ezt Sophie csinálja, nem mi).
