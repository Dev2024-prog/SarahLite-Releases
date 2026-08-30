# Security Policy

Ez a dokumentum azoknak szól, akik **Sarah Lite-tal kapcsolatos biztonsági hibát, sérülékenységet vagy integritási problémát találtak**.

## Mit jelents itt?

Ide tartoznak például a Sarah Lite kliensoldali biztonsági problémái:

- a Sarah Setup vagy Sarah Assistant jogosultságkezelési hibái;
- jogosulatlan rendszer- vagy fájlmódosítás lehetősége;
- Live Boot, GRUB, Debugger vagy maintenance / NoGui hozzáférési hibák;
- helyi privilege escalation;
- release-, manifest-, aláírás- vagy integritásellenőrzési megkerülések;
- provisioning, licenc- vagy device-identity manipuláció;
- olyan hibák, amelyekkel hivatalosnak tűnő módosított Sarah Lite rendszer fogadható el;
- érzékeny adat, kulcs vagy credential nem szándékos kiszivárgása;
- audit-, update- vagy recovery-folyamat biztonsági megkerülése.

## Hogyan jelents biztonsági hibát?

**Ne nyiss nyilvános GitHub issue-t a sérülékenység technikai részleteivel.**

Ha biztonsági hibát találtál:

1. ne publikálj exploitot, reprodukciós részleteket, kulcsot vagy érzékeny adatot nyilvánosan;
2. a lehető legkevesebb szükséges adattal vedd fel közvetlenül a kapcsolatot a projektgazdával;
3. írd le, melyik Sarah Lite / Sarah Assistant / Setup verzió érintett;
4. add meg a reprodukció lépéseit és a várható biztonsági hatást;
5. ha lehet, jelezd, hogy a probléma fizikai hozzáférést, normál felhasználói jogot, Administrator/root jogot vagy módosított bootkörnyezetet igényel-e.

Amíg nincs külön privát hibabejelentési csatorna megadva, **ne tedd közzé a technikai részleteket nyilvános GitHub-felületen**.

## Mit ne küldj el?

Biztonsági hibajelentéshez se küldj szükségtelen valódi érzékeny adatot.

Különösen ne kerüljön nyilvános repositoryba, issue-ba vagy hozzászólásba:

- Sarah Lite licenckulcs;
- privát aláírókulcs;
- vásárlói vagy személyes adat;
- hitelesítési token;
- jelszó vagy más secret;
- olyan teljes diagnosztikai csomag, amely személyes vagy bizalmas adatot tartalmaz.

A reprodukcióhoz lehetőleg maszkolt, teszt- vagy mesterséges adatot használj.

## Hatókör

Ennek a repositorynak a Security Policy-ja elsősorban a **Sarah Lite kiadások és a hozzájuk tartozó kliensoldali komponensek** biztonságára vonatkozik.

Ide tartozhat:

- Sarah Lite release artifact;
- Sarah Setup;
- Sarah Assistant / updater;
- Live Boot rendszer;
- GRUB / Debugger / maintenance útvonal;
- lokális storage, provisioning és update-integritás;
- a Sarah által használt kliensoldali hitelesítési és bizalmi ellenőrzések.

Külső szolgáltatók vagy platformok saját infrastruktúrájának sérülékenysége nem ennek a repositorynak a hatásköre. Ha azonban a probléma **Sarah saját integrációjából, konfigurációjából vagy hibás trust-kezeléséből** ered, az továbbra is releváns Sarah biztonsági hibának számíthat.

Engedély nélkül ne végezz támadást, terheléses tesztet vagy kihasználási kísérletet harmadik fél éles infrastruktúrája ellen.

## Hivatalos kiadások hitelessége

Sarah Lite-ot kizárólag a `Dev2024-prog/SarahLite-Releases` repository hivatalos **Releases** oldaláról használj.

A kiadások hitelességének ellenőrzésében a release által biztosított kriptográfiai adatok szolgálnak bizalmi alapként, többek között:

- `release-manifest.json` digitális aláírása;
- RSA-PSS / SHA-256 alapú aláírás-ellenőrzés;
- `SHA256SUMS.txt` és egyedi SHA-256 ellenőrzőösszegek;
- a release-hez rögzített forráscommit és buildinformáció.

Más forrásból származó, újracsomagolt vagy módosított Sarah Lite kiadás hitelessége nem garantálható.

## Felelős hibajelentés

A cél az, hogy a biztonsági probléma javítható legyen anélkül, hogy a sérülékenység idő előtt széles körben kihasználhatóvá válna.

Kérjük, adj ésszerű időt a hiba kivizsgálására és javítására, mielőtt technikai részleteket vagy reprodukciós módszert nyilvánosságra hozol.
