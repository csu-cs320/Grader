#!/bin/bash
FILES=$1/*
# mkdir tmp
chmod -R 744 diff_format
rm -rf diff_format
rm -rf temp_result
rm -rf cheatcheck
rm -rf unprocessed
mkdir diff_format
chmod -R 744 diff_format
for f in $FILES
do
  echo "Processing $f file..."
  if [ "${f: -3}" == "tbz" ] || [ "${f: -2}" == "bz" ]; then
  echo "+++++++++++++++++++++++++++++++++" >> temp_result
  echo $f >> temp_result 
  rm -rf tmp/
  mkdir tmp
  tar -xjf $f -C tmp/
  cd tmp/
  echo "---------------------------------" >> ../cheatcheck
  echo $f >> ../cheatcheck
  git checkout python-data-structures-tests tests >> ../cheatcheck || echo "***********************" >> ../cheatcheck
  python do.py tests &>> ../temp_result
  # python tmp/do.py tests |& tee -a temp_result
  # python tmp/do.py tests >> temp_result
  echo "Done!"
  cd ../
  else
    echo "+++++++++++++++++++++++++++++++" >> unprocessed
    echo $f >> unprocessed
    echo "!!!!!!!!!!!!!!!!!"
    echo "Different format!"
    echo "!!!!!!!!!!!!!!!!!"
    cp -R $f diff_format/
  fi
done

rm -rf tmp/

python src.py $1 $2 $3
