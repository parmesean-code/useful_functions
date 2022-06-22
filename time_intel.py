def format_duration(seconds):
    years = seconds // 31536000
    days = (seconds - years * 31536000) // 86400
    hours = (seconds - years * 31536000 - days * 86400) // 3600
    mins = (seconds - years * 31536000 - days * 86400 - hours * 3600) // 60
    secs = (seconds - years * 31536000 - days * 86400 - hours * 3600 - mins * 60)
    
    time = {'year': years, 'day': days, 'hour': hours, 'minute': mins, 'second': secs}
    new_time = {k:v for (k,v) in time.items() if v > 0}

    cnt = len(new_time)
    output = ''
    
    if seconds == 0:
        return 'now'
    else:
        for (k, v) in new_time.items():
            if v > 1:
                k += 's'
            pass
            if cnt > 2:
                output += f'{v} {k}, '
                cnt -= 1
            elif cnt == 2:
                output += f'{v} {k} and '
                cnt -= 1
            else:
                output += f'{v} {k}'
        return output