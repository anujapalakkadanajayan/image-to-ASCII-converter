from PIL import Image
from pathlib import Path

def read_input(file_path : str, filter_type : str) -> Image.Image:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Image doesn't exists on the given {path}.")
    elif path.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
        raise ValueError(f"Unsupported file format.")
    else:
        if filter_type == "rgb":
            return Image.open(path).convert("RGB")
        elif filter_type == "greyscale":
            return Image.open(path).convert("L")
        else:
            raise ValueError(f"Supported filter values:RGB,GREYSCALE")    
