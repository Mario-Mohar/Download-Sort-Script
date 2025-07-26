import os
import shutil
import sys
from pathlib import Path
import logging
import datetime

# Konfiguration
DOWNLOAD_FOLDER = os.path.expanduser("~/Downloads")  # Funktioniert auf allen Systemen
DESKTOP_FOLDER = os.path.expanduser("~/Desktop")  # Desktop-Ordner für Backups

# Dateitypen-Kategorien
FILE_CATEGORIES = {
    "PDFs": [".pdf"],
    "Documents": [".txt", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".ods", ".odp"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".psd", ".ai", ".eps", ".raw", ".indd", ".tif", ".tiff", ".bmp", ".webp"],
    "Files": [".zip", ".rar", ".dmg", ".exe", ".pkg", ".iso", ".tar", ".gz", ".7z", ".deb", ".rpm"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".m4v"],
    "Music": [".mp3", ".m4a", ".flac", ".wav", ".aac", ".ogg", ".wma"]
}

def setup_logging():
    """Logging für bessere Nachverfolgung einrichten"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('download_sort.log', encoding='utf-8'),
            logging.StreamHandler()
        ]
    )

def create_backup():
    """Erstellt ein Backup des Downloads-Ordners auf dem Desktop"""
    download_path = Path(DOWNLOAD_FOLDER)
    desktop_path = Path(DESKTOP_FOLDER)
    
    if not download_path.exists():
        logging.warning(f"Downloads-Ordner existiert nicht: {download_path}")
        return None
    
    if not desktop_path.exists():
        logging.warning(f"Desktop-Ordner existiert nicht: {desktop_path}")
        return None
    
    # Erstelle Backup-Namen mit Zeitstempel
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"Downloads_Backup_{timestamp}"
    backup_path = desktop_path / backup_name
    
    try:
        # Kopiere den gesamten Downloads-Ordner
        shutil.copytree(download_path, backup_path, dirs_exist_ok=True)
        logging.info(f"Backup erstellt: {backup_path}")
        return backup_path
    except Exception as e:
        logging.error(f"Fehler beim Erstellen des Backups: {e}")
        return None

def create_folders(base_path):
    """Erstellt alle benötigten Ordner"""
    folders_created = []
    for category in FILE_CATEGORIES.keys():
        folder_path = Path(base_path) / category
        if not folder_path.exists():
            folder_path.mkdir(parents=True, exist_ok=True)
            folders_created.append(str(folder_path))
            logging.info(f"Ordner erstellt: {folder_path}")
    return folders_created

def get_file_category(filename):
    """Bestimmt die Kategorie einer Datei basierend auf der Endung"""
    file_ext = Path(filename).suffix.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if file_ext in extensions:
            return category
    return None

def move_file_with_conflict_handling(source, destination):
    """Verschiebt eine Datei mit Konfliktbehandlung"""
    source_path = Path(source)
    dest_path = Path(destination)
    
    if not source_path.exists():
        logging.warning(f"Quelldatei existiert nicht: {source_path}")
        return False
    
    # Wenn Ziel bereits existiert, füge Nummer hinzu
    counter = 1
    original_dest = dest_path
    while dest_path.exists():
        stem = original_dest.stem
        suffix = original_dest.suffix
        dest_path = original_dest.parent / f"{stem}_{counter}{suffix}"
        counter += 1
    
    try:
        shutil.move(str(source_path), str(dest_path))
        logging.info(f"Datei verschoben: {source_path.name} -> {dest_path}")
        return True
    except Exception as e:
        logging.error(f"Fehler beim Verschieben von {source_path}: {e}")
        return False

def sort_downloads():
    """Hauptfunktion zum Sortieren der Downloads"""
    download_path = Path(DOWNLOAD_FOLDER)
    
    if not download_path.exists():
        logging.error(f"Downloads-Ordner existiert nicht: {download_path}")
        return
    
    # Backup erstellen
    backup_path = create_backup()
    if backup_path:
        logging.info(f"Backup erfolgreich erstellt: {backup_path}")
    else:
        logging.warning("Backup konnte nicht erstellt werden - Sortierung wird fortgesetzt")
    
    # Ordner erstellen
    created_folders = create_folders(download_path)
    
    # Dateien sortieren
    moved_files = 0
    skipped_files = 0
    
    for item in download_path.iterdir():
        if item.is_file():
            category = get_file_category(item.name)
            if category:
                dest_folder = download_path / category
                dest_file = dest_folder / item.name
                
                if move_file_with_conflict_handling(item, dest_file):
                    moved_files += 1
                else:
                    skipped_files += 1
            else:
                logging.info(f"Unbekannter Dateityp übersprungen: {item.name}")
                skipped_files += 1
    
    logging.info(f"Sortierung abgeschlossen: {moved_files} Dateien verschoben, {skipped_files} übersprungen")

if __name__ == "__main__":
    setup_logging()
    logging.info("Download-Sortierung gestartet")
    sort_downloads()
    logging.info("Download-Sortierung beendet") 