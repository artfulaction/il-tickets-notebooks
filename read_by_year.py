"""
program to read the parking_tickets.csv file and break it into
smaller files by year.

Assumes:
 headings are first line in file.
 year is beginning of second element in observation list.
 observations are already in consecutive date order.
 """
fin = open('data//hacknight_ticket_sample_data_2015.csv', 'r')
# read first line in file
line = fin.readline()
# save first line as headings
headings = line
# create variable for yet-to-be-created output files
file_year = 'tbd'
# process observations
while line:
    line = fin.readline()
    if line:
        line_as_list = line.split(sep=',')
        obs_year = (line_as_list[1][0:4])
        if (obs_year == file_year):
            fout.write(line)
        else:
            # create the output file
            fout = open('data//' + obs_year + '_p_t.csv', 'w')
            # write the headings to the new output file
            fout.write(headings)
            # write the current observation to the file
            fout.write(line)
            file_year = obs_year
fout.close()
fin.close()
