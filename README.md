# AtCoder

# Links

- [AtCoder](https://atcoder.jp/home)
- [AtCoder Problems / ichiya_x](https://kenkoooo.com/atcoder/#/table/ichiya_x)
- [Notion log](https://www.notion.so/ichiya/20f67a5994874c24bd177793e1b93931?pvs=4) - more details about settings

# Settings

## Requirements

- atcoder-tools
- online-judge-tools

```shell
pip install atcoder-tools online-judge-tools
```

## Login

It is required to download and submit problems.

```shell
oj login https://atcoder.jp
```

> [!NOTE]
> **atcoder-tools**
> The first time you execute `atcoder-tools` command, you are asked to log in.

## Create `~/.atcodertools.toml`

Copy `atcodertools.toml` in current directory to `~/.atcodertools.toml`.

```shell
cp atocodertools.toml ~/.atcodertools
```

## Configure keybinding

1. Open `keybindings.json` in vscode. (`Command Pallete` > `Preferences: Open Keyboard Shortcuts (JSON)`)
2. Append below to `keybindings.json`:
    ```json
    {
        "key": "ctrl+shift+c",
        "command": "workbench.action.tasks.runTask",
        "when": "editorTextFocus",
        "args": "AtCoder_Test"
    },
    {
        "key": "cmd+ctrl+shift+s",
        "command": "workbench.action.tasks.runTask",
        "when": "editorTextFocus",
        "args": "AtCoder_Submit"
    }
    ```

> [!NOTE]
> `AtCoder_Test` and `AtCoder_Submit` are task names in `.vscode/tasks.json`.

# Usage

## Download problems

```shell
sh tools/download_problem.sh <CONTEST_ID>
# e.g. sh download_problem.sh abc326
```

### Download problems sequentially

before executing below command, edit variables (`start`, `end`) in `tools/seq_download_problem.py`

```shell
python tools/seq_download_problems.py
```

## Write a program

```shell
<CONTEST_ID>/<PROBLEM_LEVEL>/main.py
# e.g. abc326/A/main.py
```

## Test

in `<CONTEST_ID>/<PROBLEM_LEVEL>/main.py`

Execute with shortcut (<kbd>shift</kbd> + <kbd>ctrl</kbd> + <kbd>c</kbd>) in macOS.
<br />
Then open new terminal and execute test automatically.

This shortcut is added to `keybindings.json` in vscode.


## Submit

Execute with shortcut (<kbd>cmd</kbd> + <kbd>shift</kbd> + <kbd>ctrl</kbd> + <kbd>s</kbd>) in macOS.
<br />
Then open new terminal and execute submit automatically.

This shortcut is added to `keybindings.json` in vscode.
