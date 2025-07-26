# Download-Sort Script

Ein Python-Script zur automatischen Organisation von Dateien im Downloads-Ordner.

## Funktionen

- **Automatische Kategorisierung**: Sortiert Dateien basierend auf ihrer Dateiendung
- **Automatisches Backup**: Erstellt vor jeder Sortierung ein Backup auf dem Desktop
- **Backup-Verwaltung**: Behält nur die 5 neuesten Backups und löscht alte automatisch
- **Plattformunabhängig**: Funktioniert auf Windows, macOS und Linux
- **Konfliktbehandlung**: Behandelt doppelte Dateinamen automatisch
- **Logging**: Detaillierte Protokollierung aller Aktionen
- **Konfigurierbar**: Flexible Einstellungen über YAML-Datei

## Unterstützte Dateitypen

| Kategorie | Dateiendungen |
|-----------|---------------|
| **PDFs** | .pdf |
| **Documents** | .txt, .doc, .docx, .xls, .xlsx, .ppt, .pptx, .odt, .ods, .odp |
| **Images** | .jpg, .jpeg, .png, .gif, .svg, .psd, .ai, .eps, .raw, .indd, .tif, .tiff, .bmp, .webp |
| **Files** | .zip, .rar, .dmg, .exe, .pkg, .iso, .tar, .gz, .7z, .deb, .rpm |
| **Videos** | .mp4, .avi, .mkv, .mov, .wmv, .flv, .webm, .m4v |
| **Music** | .mp3, .m4a, .flac, .wav, .aac, .ogg, .wma |

## Installation

1. **Python installieren** (falls noch nicht vorhanden):
   ```bash
   # Windows
   # Lade Python von python.org herunter
   
   # macOS
   brew install python
   
   # Linux
   sudo apt install python3
   ```

2. **Abhängigkeiten installieren**:
   ```bash
   pip install pyyaml
   ```

## Verwendung

### Einfache Verwendung
```bash
python sort_download_improved.py
```

### Mit Backup-Funktion
```bash
python sort_download_with_backup.py
```

### Mit Konfigurationsdatei
```bash
python sort_download_improved.py --config config.yaml
```

### Trockenlauf (nur anzeigen, nicht verschieben)
```bash
python sort_download_improved.py --dry-run
```

## Konfiguration

Bearbeiten Sie die `config.yaml` Datei, um:
- Downloads-Ordner zu ändern
- Neue Dateitypen hinzuzufügen
- Logging-Einstellungen anzupassen
- Konfliktbehandlung zu konfigurieren

## Sicherheit

✅ **Automatisches Backup:**
- Das Script erstellt automatisch ein Backup auf dem Desktop vor jeder Sortierung
- Backup-Namen: `Downloads_Backup_YYYYMMDD_HHMMSS`
- Nur die 5 neuesten Backups werden behalten, alte werden automatisch gelöscht

⚠️ **Wichtige Hinweise:**
- Das Script verschiebt Dateien **permanent**
- Backups werden auf dem Desktop gespeichert
- Testen Sie mit `--dry-run` vor der echten Verwendung

## Logging

Das Script erstellt eine `download_sort.log` Datei mit:
- Erstellte Ordner
- Verschobene Dateien
- Übersprungene Dateien
- Fehler und Warnungen

## Verbesserungen gegenüber dem Original

✅ **Konfigurierbare Pfade** - Funktioniert auf allen Systemen  
✅ **Automatisches Backup** - Sicherheit durch Desktop-Backups  
✅ **Backup-Verwaltung** - Automatische Bereinigung alter Backups  
✅ **Bessere Fehlerbehandlung** - Keine Abstürze bei Problemen  
✅ **Logging** - Vollständige Nachverfolgung aller Aktionen  
✅ **Konfliktbehandlung** - Automatische Umbenennung bei Duplikaten  
✅ **Modulare Struktur** - Einfach zu erweitern und warten  
✅ **Mehr Dateitypen** - Unterstützt mehr Formate  
✅ **Trockenlauf-Modus** - Sichere Tests möglich  

## Troubleshooting

### Downloads-Ordner nicht gefunden
- Überprüfen Sie den Pfad in der Konfiguration
- Verwenden Sie `~/Downloads` für den Standard-Pfad

### Berechtigungsfehler
- Stellen Sie sicher, dass Sie Schreibrechte im Downloads-Ordner haben
- Führen Sie das Script als Administrator aus (Windows)

### Dateien werden nicht verschoben
- Überprüfen Sie die Log-Datei für Details
- Stellen Sie sicher, dass die Dateiendungen in der Konfiguration stehen

## Lizenz

Dieses Script ist Open Source und kann frei verwendet werden. 