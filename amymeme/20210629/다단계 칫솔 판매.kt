// https://programmers.co.kr/learn/courses/30/lessons/77486
// 다단계 칫솔 판매

class Solution {
    fun solution(enroll: Array<String>, referral: Array<String>, seller: Array<String>, amount: IntArray): IntArray {
        var answer = mutableListOf<Int>()
        var graph = mutableMapOf<String, String>()
        var bill = mutableMapOf<String, Int>().withDefault{_ -> 0}

        referral.forEachIndexed{ idx, refer ->
            graph[enroll[idx]] = refer
        }

        seller.forEachIndexed{ idx, originSeller ->
            var value: Int = amount[idx] * 100
            var person: String = originSeller
            while (value > 0 && person in graph.keys) {
                bill[person] = bill.getValue(person) + (value - (value * 0.1).toInt())
                person = graph[person]?:""
                value = (value * 0.1).toInt()
            }
        }

        enroll.forEachIndexed{ idx, person ->
            answer.add(bill.getValue(person))
        }
        return answer.toIntArray()
    }
}