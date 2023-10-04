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

#Ask user for a date
user_date = input("Enter a date: ")
#Create a variable pointing to the data file. Supply the relative path to the file.
file_name = './data/raw/sara.txt'

#Create a file object from the file. Giving Python access to the file's contents by opening it in memory
file_object = open(file_name,'r')

#Read contents of file into a list. This is a line list of all the lines in the Sara.txt data file.
line_list = file_object.readlines()

#Close the file. Once the contents of the file have been read into the memory done in the previous two lines of code, there's no need to have the file open.
file_object.close()

#Initialize dictionaries
date_dict = {}
location_dict = {}

#For every iteration (line in the Sara.txt data file) it will update the variable lineString. 
for lineString in line_list:
    #Check if line is a data line (vs. just metadata type text found at the beginning of the Sara.txt doc). If the line starts with # or u, skip over it (continue).  
    if lineString[0] in ("#", "u"):
        continue

    #Split the string into a list of data items
    lineData = lineString.split()

    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]

    #Determine if location class criteria is met (will only pull records if lc is 1,2,or 3)
    if obs_lc in ("1", "2", "3"):
        #Add items to dictionaries. We use record_id because it's a unique value for each line of data
        date_dict[record_id] = obs_date
        location_dict[record_id] = (obs_lat, obs_lon)
    
    
#Initialize key list
keys = []

#Loop through items in date_dict. Items in the date_dict are the uid and the date. we're assinging key to the uid [0] and value to the date (item[1])
for item in date_dict.items():
    key = item[0]
    value = item[1]
    if value == user_date: 
        keys.append(key)

#Report if no records were found for a certain date (meaning the keys list is empty)
if len(keys) == 0:
    print(f"No records were found on {user_date}")

#Loop through keys and report locations
for key in keys: 
    location = location_dict[key]
    lat = location[0]
    lng = location[1]
    print(f"On {user_date}, Sara the turtle was seen at {lat}d Lat, {lng}d, Lng.")