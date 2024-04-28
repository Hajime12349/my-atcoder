function execute_test() {
    # ${workspaceFolder} == /Users/kzy/ghq/github.com/kazuya0202/atcoder
    local workspaceFolder=$1

    # ${fileDirname} == /Users/kzy/ghq/github.com/kazuya0202/atcoder/abc323/<Problem>
    local fileDirname=$2

    # ${fileBasename} == main.py
    local fileBasename=$3

    cd ${fileDirname}
    oj test \
        -c "python ${fileBasename}" \
        -d "${fileDirname}/test"
}

execute_test $1 $2 $3
