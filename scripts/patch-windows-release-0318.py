from pathlib import Path

path = Path('.github/workflows/sarah-windows-release.yml')
text = path.read_text(encoding='utf-8')
if "if ($env:SARAH_UPDATER_VERSION -ne '0.3.16')" not in text:
    raise SystemExit('Expected 0.3.16 release guard not found')
text = text.replace("if ($env:SARAH_UPDATER_VERSION -ne '0.3.16')", "if ($env:SARAH_UPDATER_VERSION -ne '0.3.18')", 1)
old = 'A $env:SARAH_UPDATER_VERSION tartalmazza a pendrive nyers ISO-írás előtti boot/metaadat takarítását, az írás utáni MBR/bootterület visszaellenőrzést és szükség esetén javító újraírást, valamint a korábbi self-update fájlzár-védelmeket. A fizikai USB boot elfogadási teszt továbbra is külön hardveres ellenőrzés.'
new = 'A $env:SARAH_UPDATER_VERSION a hitelesített ISO-t byte 0-tól írja ki anélkül, hogy előtte lenullázná az image elejét; megtartja a fizikai lemezvég stale GPT/metaadat takarítását, az MBR/bootterület visszaellenőrzését és a javított önfrissítési cserefolyamatot. A fizikai USB boot elfogadási teszt továbbra is külön hardveres ellenőrzés.'
if old not in text:
    raise SystemExit('Expected release-note sentence not found')
text = text.replace(old, new, 1)
path.write_text(text, encoding='utf-8')
print('Patched Sarah Windows release workflow for Updater 0.3.18')
