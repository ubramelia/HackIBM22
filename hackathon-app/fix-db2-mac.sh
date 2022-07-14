# Only need to execute this when running on mac
set -ex
py_folder=$(ls venv/lib | head -n 1)
cd "venv/lib/$py_folder/site-packages/"

db2_binary=$(ls ibm_db.cpython* | head -n 1)
echo "$db2_binary"
install_name_tool -change libdb2.dylib "$(pwd)/clidriver/lib/libdb2.dylib" "$db2_binary"

if test -f "$PWD/clidriver/lib/libdb2.dylib"; then
    rm -rf libdb2.dylib
fi

ln -s "/usr/local/lib/$py_folder/site-packages/clidriver/lib/libdb2.dylib" libdb2.dylib