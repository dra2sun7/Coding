int("123\n")    # ✅ 정상 작동 → 123
int("   456  ") # ✅ 정상 작동 → 456

int("\n")       # ❌ ValueError: invalid literal for int() with base 10
int("   ")      # ❌ ValueError