// https://programmers.co.kr/learn/courses/30/lessons/42888
// 오픈채팅방

class Solution {
    fun solution(record: Array<String>): Array<String> {
        var answer = mutableListOf<String>()
        var users = mutableMapOf<String, String>()

        for (r in record) {
            val row = r.split(" ")
            if (row.size < 3) {
                continue
            }
            users[row[1]] = row[2]
        }

        for (r in record) {
            val row = r.split(" ")
            when (row[0]) {
                "Enter" -> answer.add("${users[row[1]]}님이 들어왔습니다.")
                "Leave" -> answer.add("${users[row[1]]}님이 나갔습니다.")
            }
        }
        return answer.toTypedArray()
    }
}