#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Megan McClaugherty (Megan.mcclaugherty@duke.edu)
# Date:   Fall 2023
#--------------------------------------------------------------

#Create a variable pointing to the data file. Supply the relative path to the file.
file_name = './data/raw/sara.txt'

#Create a file object from the file. Giving Python access to the file's contents by opening it in memory
file_object = open(file_name,'r')

#Read contents of file into a list. 
line_list = file_object.readlines()

#Close the file. Once the contents of the file have been read into the memory done in the previous two lines of code, there's no need to have the file open.
file_object.close()

#Pretend we read one line of data from the file
lineString = line_list[200]

#Split the string into a list of data items
lineData = lineString.split()

#Extract items in list into variables
record_id = lineData[0]
obs_date = lineData[2]
obs_lc = lineData[4]
obs_lat = lineData[6]
obs_lon = lineData[7]

#Print the location of sara
print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")