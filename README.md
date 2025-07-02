# rlo-exe-masking

Цей скрипт компілює Python-скрипт у `.exe` файл за допомогою PyInstaller та маскує його ім’я за допомогою RLO (Right-To-Left Override), щоб `.exe` виглядав як `.png`.

## Що робить цей скрипт?

Компіліє Python файл у один `.exe` (без відкриття консолі!!!)
Перейменовує `.exe`, вставляючи символ RLO для маскування розширення
Створює файл, що виглядає як зображення `.png`, але є `.exe`

## Вимоги

- Python 3.x  
- [PyInstaller](https://www.pyinstaller.org/) - в терміналі прописати "pip install pyinstaller"
- Windows OS (через використання calc.exe і маскування імені)
