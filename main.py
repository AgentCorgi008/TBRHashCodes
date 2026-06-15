import base64
import hashlib
import json
from pathlib import Path

developer_mode = False

paths = [
    "game/code/mechanics/battle_system/api/battle_manager.rpyc",
    "game/code/mechanics/battle_system/screens/fight_system_screens.rpyc",
    "game/code/mechanics/pc/codes/codes.rpyc",
    "game/code/mechanics/phone/gallery/gallery.rpyc",
    "game/code/mechanics/phone/studies/studies.rpyc",
    "game/code/mechanics/pc/easter_eggs/ee.rpyc",
    "game/code/mechanics/pc/easter_eggs/ee_screens.rpyc"
]

current_dir = Path.cwd().parent.parent / "Develop" / "Projects" / "TBR Retransmitter"

hashes = {}

# Розрахунок хешів
for path in paths:
    full_path = current_dir / path
    with open(full_path, 'rb') as f:
        data = f.read()
        sha256 = hashlib.sha256(data).hexdigest()
        rel_path = "/".join(path.split("/")[1:])
        hashes[rel_path] = sha256
# Створення Python-блоку як рядка

code_block = "_if = False\ne_hs = {\n"
for k, v in hashes.items():
    code_block += f'    "{k}": \'{v}\',\n'
code_block += "}\n"

code_block += "if not isinstance(Codes.check_code, _M):\n    Codes.check_code = _M(Codes.check_code)\nval()\n"

code_block += "if _if:\n    EasterEggPlayer.SCREEN_NAME = 'trash_bin'"

print(code_block)

# Кодування в Base64
encoded = base64.b64encode(code_block.encode("utf-8")).decode("utf-8")

# Вивід результату
print("======= Base64 Block =======")
print(encoded)
print("\n======= Full Python Snippet =======")
print(f'exec(base64.b64decode("{encoded}").decode())')

# Зберігаємо в JSON
output = {
    "hb": encoded
}

# Директорія для збереження
target_path = current_dir / "game" / "cache"
target_path.mkdir(parents=True, exist_ok=True)

# Збереження у файл
with open(target_path / "hash_block.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=4)

print("✅ JSON-файл збережено до game/cache/hash_block.json")
