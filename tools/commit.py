from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def prompt(message: str, default: str | None = None) -> str:
    suffix = f" [{default}]" if default else ""
    value = input(f"{message}{suffix}: ").strip()
    return value or (default or "")


def main() -> int:
    try:
        status = run_git("status", "--short")
    except subprocess.CalledProcessError as exc:
        print(exc.stderr or exc.stdout or "無法讀取 git 狀態。")
        return 1

    if not status:
        print("目前沒有可提交的變更。")
        return 0

    print("目前變更：")
    print(status)
    print()

    stage_all = prompt("要加入所有變更嗎？(y/n)", "y").lower()
    if stage_all in {"y", "yes"}:
        run_git("add", "-A")
    else:
        files = prompt("請輸入要加入的檔案，使用空白分隔").split()
        if not files:
            print("沒有指定檔案，已取消。")
            return 1
        run_git("add", *files)

    default_message = "Update site content"
    message = prompt("commit 訊息", default_message)
    if not message:
        print("commit 訊息不能是空白。")
        return 1

    run_git("commit", "-m", message)
    print("commit 已完成。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
