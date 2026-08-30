# Sarah Lite Releases

Ez a repository a **Sarah Lite hivatalos publikus GitHub kiadási és letöltési helye**.

A `Dev2024-prog/SarahDiagnostic` repository tartalmazza a forráskódot, teszteket és build workflow-kat. A kész, ellenőrzött Windows telepítési csomagok és a kiadásokhoz tartozó ellenőrzési metaadatok ezen a repositoryn keresztül jelenhetnek meg.

A Sarah Lite aktuális production terjesztése ugyanakkor **nem kizárólag GitHub Release assetekre épül**: a Sarah Setup, a Sarah Assistant önfrissítése, valamint a Sarah Lite GPT single-system SYSTEM/factory csatornái aláírt R2 release manifesteket és tartalomcímzett artifactokat használnak.

A letölthető fájl önmagában nem ad használati jogosultságot: új Sarah pendrive készítéséhez és aktiválásához érvényes Sarah Lite licenc szükséges.

## Jelenlegi kiadási modell

### Windows

- `SarahSetup.exe` – a Sarah Assistant önálló Windows telepítője;
- `SarahAssistant-<verzió>-win-x64.zip` – ellenőrzött Assistant kiadási csomag / release artifact;
- `*.sha256` – az adott publikus fájl SHA-256 ellenőrzőösszege.

A Sarah Setup a telepítendő Sarah Assistant aktuális, digitálisan aláírt manifestjét az Assistant R2 csatornáról olvassa. A Sarah Assistant önfrissítése ugyanezt a hitelesített R2 release modellt használja.

### Sarah Lite Live rendszer

A jelenlegi Sarah Lite **GPT single-system IMG** architektúrát használ. Az Assistant két külön hitelesített csatornát kezel:

- **SYSTEM release** – meglévő Sarah adathordozó rendszerfrissítéséhez;
- **factory release** – új Sarah USB teljes telepítéséhez.

A több gigabájtos factory IMG tartalma aláírt, content-addressed R2 chunkokon keresztül kerül terjesztésre, ezért azt nem szükséges minden GitHub Release-ben külön, teljes méretű assetként duplikálni.

A GitHub Release tartalmazhatja a kapcsolódó release manifesteket és `sarah-release-info.json` build/audit metaadatot is.

## Hitelesség

A production kiadásoknál a bizalmi lánc része többek között:

- digitálisan aláírt release manifest;
- RSA-PSS / SHA-256 aláírás-ellenőrzés;
- SHA-256 artifact ellenőrzés;
- pontos SarahDiagnostic forráscommit rögzítése;
- a kliens által ellenőrzött kiadási és verziószerződés.

Régi tag, branch vagy korábbi fejlesztési build megléte **nem jelenti azt, hogy az aktuális production kliens arra hivatkozik**. Az aktív Setup/Assistant kiadási útvonalak a jelenlegi aláírt R2 csatornákat használják.

## Biztonság

### Felhasználóknak és letöltőknek

Ha Sarah Lite-ot vagy Sarah Assistantot töltesz le, telepítesz vagy frissítesz, kizárólag a projekt hivatalos kiadási útvonalait használd. Más forrásból származó, újracsomagolt vagy módosított Sarah kiadás hitelessége nem garantálható.

Licenckulcsot, személyes adatot vagy más érzékeny információt ne tegyél közzé nyilvános GitHub issue-ban, hozzászólásban vagy más publikus felületen.

### Fejlesztőknek és biztonsági hibát jelentőknek

Ha Sarah Lite-tal kapcsolatos biztonsági hibát vagy sérülékenységet találsz, ne nyilvános issue-ban tedd közzé a technikai részleteket. A részletes szabályokat a repository **Security Policy** dokumentuma tartalmazza.
