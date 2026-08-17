# Sarah Lite Releases

Ez a repository a **Sarah Lite egyetlen hivatalos GitHub letöltési helye**.

A `Dev2024-prog/SarahDiagnostic` repository a forráskódot, teszteket és build workflow-kat tartalmazza, de kész ISO- és Updater-kiadásokat nem tárol. A SarahDiagnosticból elkészült, ellenőrzött build artifactok kizárólag ide, a `SarahLite-Releases` GitHub Releases oldalára kerülnek.

A letölthető ISO önmagában nem ad használati jogosultságot: új Sarah pendrive készítéséhez és aktiválásához érvényes Sarah Lite licenc szükséges.

## Kiadási fájlok

- `SarahLite-<verzió>-amd64.iso` – bootolható diagnosztikai rendszer
- `SarahUpdater-<verzió>-win-x64.zip` – Windowsos telepítő és frissítő
- `*.sha256` / `SHA256SUMS.txt` – ellenőrzőösszegek
- build információ és audit fájlok – az adott kiadás forráscommitjának és ellenőrzéseinek nyoma

A release leírása minden új buildnél megőrzi a pontos `SarahDiagnostic` forráscommitot, így a publikus letöltés és a forrás egyértelműen összeköthető.

## Biztonság

Kizárólag ezen repository **Releases** oldalán közzétett fájlokat használd. Licenckulcsot, személyes adatot vagy hibajelentést ne küldj nyilvános GitHub-felületre.
