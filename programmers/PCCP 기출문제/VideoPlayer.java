// 1번 동영상 재생기
// 2025-09-03 Wed
class VideoPlayer {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {

        int video_len_num = calculate(video_len);
        int pos_num = calculate(pos);
        int op_start_num = calculate(op_start);
        int op_end_num = calculate(op_end);
        
        for (String command : commands) {
            if (pos_num >= op_start_num && pos_num <= op_end_num) {
                pos_num = op_end_num;
            }
            
            if (command.equals("next")) {
                pos_num = Math.min(video_len_num, pos_num + 10);
            } else {
                pos_num = Math.max(0, pos_num - 10);
            }

            if (pos_num >= op_start_num && pos_num <= op_end_num) {
                pos_num = op_end_num;
            }
        }
        
        int minutes = pos_num / 60;
        int seconds = pos_num % 60;
        
        return String.format("%02d:%02d", minutes, seconds);
    }
    
    private int calculate(String time) {
        String[] time_array = time.split(":");
        
        return Integer.parseInt(time_array[0]) * 60 + Integer.parseInt(time_array[1]);
    }

    public static void main(String[] args) {
        VideoPlayer solution = new VideoPlayer();
        // String answer = solution.solution("34:33", "13:00", "00:55", "02:55", new String[]{"next", "prev"});
        // String answer = solution.solution("10:55", "00:05", "00:15", "06:55", new String[]{"prev", "next", "next"});
        String answer = solution.solution("07:22", "04:05", "00:15", "04:07", new String[]{"next"});

        System.out.println(answer);
    }
}
