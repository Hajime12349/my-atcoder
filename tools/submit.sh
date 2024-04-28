function execute_submit() {
    # ${workspaceFolder} == /Users/kzy/ghq/github.com/kazuya0202/atcoder
    local workspaceFolder=$1

    # ${fileDirname} == /Users/kzy/ghq/github.com/kazuya0202/atcoder/abc323/<Problem>
    local fileDirname=$2

    # ${fileBasename} == main.py
    local fileBasename=$3

    local _ATCODER_URL=$(python ${workspaceFolder}/tools/_get_url.py ${fileDirname})

    cd ${fileDirname}
    oj submit \
        ${_ATCODER_URL} \
        ${fileDirname}/${fileBasename} \
        --guess-python-interpreter pypy \
        -y
}

execute_submit $1 $2 $3
