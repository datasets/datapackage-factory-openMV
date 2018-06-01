for i in ./* # iterate over all files in current dir
do
    if [ -d "$i" ] # if it's a directory
    then
        cp process.py "$i"/scripts/ # copy process.py into all script folders
    fi
done
