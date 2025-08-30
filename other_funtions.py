def ensure_directory_will_work_on_linxu(directory):
    loops_needed = len(directory)-1
    i=0
    while(i<loops_needed):
        if (directory[i]=="\\"):
            directory = directory[:i]+"/"+directory[i+1:]
        loops_needed = len(directory)-1
        i += 1
    return directory