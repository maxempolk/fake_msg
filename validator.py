def is_time(time_str):
    if ":" in time_str:
        if time_str.split(":")[0].isdigit() and time_str.split(":")[-1].isdigit():
            hours = int( time_str.split(":")[0] )
            minuts = int( time_str.split(":")[-1] )
            if (hours >= 0 and hours < 24) and (minuts >= 0 and minuts < 60):
                return True
    return False

def valid(message):
    if message != None and message != "":
        if len(message.split()) >= 2:
            if message.split()[0] and is_time(message.split()[-1]):
                return True
    return False