import os

from pathlib import Path

content = f"""\
HAS_AUDIOVIDEO = {os.getenv("FFMC_AUDIOVIDEO", "True")}
HAS_IMAGE = {os.getenv("FFMC_IMAGE", "True")}
HAS_DOCUMENT = {os.getenv("FFMC_DOCUMENT", "True")}
"""

Path("ffmulticonverter/features.py").write_text(content)
print("Generated ffmulticonverter/features.py")
