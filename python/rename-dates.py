import os
import re
import datetime

def find_date(filename):
    """parse a filename and return the date string in a currently hard-coded format"""
    full_date = None
    time_string = None
    remaining_text = None

    # will extension only matter in cases where we are going to change the filename? ex. where we dont find a date
    extension = "." + filename.split(".")[-1] # get extension and re-attach dot

    regex = re.compile("20[1-2][0-9]") # year will be in 2010s or 2020s
    year = regex.findall(filename)[0] if len(regex.findall(filename)) > 0 else None
    if year:
        # some files have time strings attached as well
        remaining_partition = filename.partition(year)[-1]
        # skip over any possible other strings and ensure correct order
        # achieved by limiting month to 12
        date_digits = "".join([char for char in remaining_partition if char.isnumeric()])[0:4]
        if int(date_digits[0:2]) <= 12:
            month, day = date_digits[0:2], date_digits[2:4]
            pass
        else:
            day, month = date_digits[0:2], date_digits[2:4]
            pass
        # only look for a time string in year as well, assuming there is an underscore separating off the time string
        # this also removes the extension, the fact that all of those earlier examined 'time strings'
        #   happened to be 7 chars long instead of 6(hh:mm:ss) was because the 7th char was the '4' in 'mp4'!
        # the potentially variable-length list of the remaining information then re-assembles at the end through "".join
        remaining_partition_no_date = "".join(remaining_partition.split("_")[-1].split(extension)[:-1])
        #then two cases, either where there are only numbers or numbers and then text
        time_string = "".join(filter(str.isnumeric,remaining_partition_no_date))
        remaining_text = "".join(filter(str.isalpha, remaining_partition_no_date))

        full_date = "-".join([year, month, day])
        pass
    else:
        pass

    return full_date, time_string, remaining_text

    # what 
# the remaining numbers in the string by the end of find_date could
#   represent dates, times, or nothing I can interpret

for filename in os.listdir(os.getcwd()):
    date_string, time_string, remaining_text = None, None, None
    date_string, time_string, remaining_text = find_date(filename)
    if date_string:
        extension = filename.split(".")[-1]
        new_filename = "{0}_{1}_{2}.{3}".format(date_string, time_string, remaining_text, extension)
        print(new_filename)
        pass
    else:
        print(filename)
    pass
