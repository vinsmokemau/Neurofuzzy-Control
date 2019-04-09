import wfdb

record = wfdb.rdrecord('100') 
wfdb.plot_wfdb(record=record, title='Record 100 from Physionet Challenge 2015') 
display(record.__dict__)
