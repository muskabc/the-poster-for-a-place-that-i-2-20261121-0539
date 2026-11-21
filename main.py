"""Copy the pre-rendered poster to the output directory as entry.png.

Only the standard library is used. The output directory comes from the
MAKEFUN_OUTPUT_DIR environment variable, defaulting to /output.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def _sha256_of(path):
    hasher = hashlib.sha256()
    with open(path, "rb") as stream:
        block = stream.read(32768)
        while block:
            hasher.update(block)
            block = stream.read(32768)
    return hasher.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != os.path.getsize(src):
        raise RuntimeError("entry.png copy incomplete")
    if _sha256_of(dst) != _sha256_of(src):
        raise RuntimeError("entry.png copy content differs from source")


if __name__ == "__main__":
    main()
