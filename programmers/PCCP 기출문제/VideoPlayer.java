// 1번 동영상 재생기
// 2025-09-03 Wed
class VideoPlayer {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        String answer = "hello, algorithms";
        return answer;
    }

    public static void main(String[] args) {
        VideoPlayer solution = new VideoPlayer();
        String answer = solution.solution("34:33", "13:00", "00:55", "02:55", new String[]{"next", "prev"});

        System.out.println(answer);
    }
}
