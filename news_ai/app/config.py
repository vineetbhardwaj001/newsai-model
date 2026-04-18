# =========================
# 🤖 AI MODEL SETTINGS
# =========================

MODEL_SUMMARY = "sshleifer/distilbart-cnn-12-6"

# Fallback (if model fails)
MODEL_FALLBACK = "t5-small"

# =========================
# 📏 INPUT CONTROL
# =========================

MAX_INPUT_LENGTH = 1000        # max chars sent to model
SUMMARY_MAX_LENGTH = 120
SUMMARY_MIN_LENGTH = 50

ELI10_MAX_LENGTH = 100

# =========================
# ⚡ CACHE SETTINGS
# =========================

CACHE_TTL = 600               # 10 minutes
CACHE_MAX_SIZE = 200

# =========================
# 🌍 LANGUAGE SETTINGS
# =========================

SUPPORTED_LANGS = ["en", "hi", "ta", "bn"]

DEFAULT_LANG = "en"

# =========================
# 🧹 PROCESSING FLAGS
# =========================

ENABLE_CLEANING = True
ENABLE_TRANSLATION = True

# =========================
# 🚫 SAFETY SETTINGS
# =========================

STRICT_SUMMARY_MODE = True   # prevents hallucination