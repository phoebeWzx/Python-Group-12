#install xlsxwrite lib to python
cd XlsxWriter
sudo python setup.py install
#conbime all source data to the final
cat *.csv > final.csv
#convert it to xlsx file
python convert.py