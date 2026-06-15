import base64


def proc_encoded(code):
    # 2. Ділимо на 15 частин
    chunk_count = 15
    chunk_size = len(code) // chunk_count
    remainder = len(code) % chunk_count

    parts = []
    start = 0
    for i in range(chunk_count):
        extra = 1 if i < remainder else 0  # розподіляємо залишок
        end = start + chunk_size + extra
        parts.append(code[start:end])
        start = end

    # 3. Формуємо список рядків
    print("parts = [")
    for part in parts:
        print(f'    "{part}",')
    print("]")


code_block = """
with open(renpy.loader.transfn("cache/hash_block.json"), "r", encoding="utf-8") as f:
    _h_d = json.load(f)
"""

code_block2 = "original_confirm = Confirm\nConfirm = _CW()\n"
code_block2 += "CS = confirm_smg\nsafe_access = Show('inform_message', None, refuse_smg_access)"

encoded = base64.b64encode(code_block.encode("utf-8")).decode("utf-8")
encoded2 = base64.b64encode(code_block2.encode("utf-8")).decode("utf-8")

print(code_block)
print(f'exec(base64.b64decode("{encoded}").decode())')
proc_encoded(encoded)

print(code_block2)
print(f'exec(base64.b64decode("{encoded2}").decode())')
proc_encoded(encoded2)
