def solution(video_len, pos, op_start, op_end, commands):
    video_len_num = calculate(video_len)
    pos_num = calculate(pos)
    op_start_num = calculate(op_start)
    op_end_num = calculate(op_end)

    for command in commands:
        if op_start_num <= pos_num <= op_end_num:
            pos_num = op_end_num
        
        if command == "next":
            pos_num = min(video_len_num, pos_num + 10)
        else: # "prev"
            pos_num = max(0, pos_num - 10)
        
        if op_start_num <= pos_num <= op_end_num:
            pos_num = op_end_num
        
    minutes = pos_num // 60
    seconds = pos_num % 60
    
    return f"{minutes:02d}:{seconds:02d}"

def calculate(time):
    minutes, seconds = map(int, time.split(":"))

    return minutes * 60 + seconds
