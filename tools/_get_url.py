import sys
from pathlib import Path

if __name__ == "__main__":
    problemDir = Path(sys.argv[1])

    _CONTEST_ID = "CONTEST_ID"
    _PROBLEM_LEVEL = "PROBLEM_LEVEL"

    _template_url = f"https://atcoder.jp/contests/{_CONTEST_ID}/tasks/{_PROBLEM_LEVEL}"

    contest_id = problemDir.parent.name
    problem_level = f"{contest_id}_{problemDir.name.lower()}"

    _url = _template_url
    _url = _url.replace(_CONTEST_ID, contest_id)
    _url = _url.replace(_PROBLEM_LEVEL, problem_level)
    print(_url)
