import argparse
import shutil
from pathlib import Path
import kagglehub


def copy_into_input(downloaded: Path, input_dir: Path, is_comp: bool) -> Path:
    name = downloaded.name if is_comp else downloaded.parent.parent.name
    target = input_dir / name

    if target.exists():
        shutil.rmtree(target)

    shutil.move(str(downloaded), str(target))
    return target


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("resource_name")
    p.add_argument("--input-dir", default="input")
    p.add_argument("--comp", action="store_true")
    args = p.parse_args()

    input_dir = Path(args.input_dir).resolve()
    input_dir.mkdir(parents=True, exist_ok=True)

    downloaded = Path(
        kagglehub.competition_download(args.resource_name)
        if args.comp else kagglehub.dataset_download(args.resource_name)
    )

    print(f"Cache Path: {downloaded}")

    final_path = copy_into_input(downloaded, input_dir, args.comp)
    print(f"Data available in {final_path}")


if __name__ == "__main__":
    main()
