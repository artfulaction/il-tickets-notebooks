"""
program to read a line from the 'data\parking_tickets.csv'
and write it to another file

uses:
    max_lines - number of observations to put into each file
    file_number - sequentially numbers each sub-file

"""
max_lines = 250000
fin = open('data//hacknight_ticket_sample_data_2015.csv', 'r')
# get the Headings - first line in file
line = fin.readline() #this reads in each line
headings = line #saving the heading for the file

file_number = 0 #number of output files

while line:
    file_number += 1
    # create the output file
    fout = open('data//' + str(max_lines) + 'rec_parking_data' + str(file_number).zfill(4) + '.csv', 'w')
    # write the headings to the output file
    fout.write(headings)

    line_count = 0
    # loop over a preset number of
    # while it hasn't hit the end of the file (line=TRUE) read in line, if there
    #is data, then write another line.
    while (line) and (line_count < max_lines):
        line = fin.readline()
        if line:
            fout.write(line)
            line_count += 1
    fout.close()
fin.close()
