# https://www.acmicpc.net/problem/1504
# 특정한 최단 경로

import kotlin.math.sqrt

fun getPrimeList(N: Int): List<Int> {
    val sieve = BooleanArray(N + 1) { true }
    for (i in 2..sqrt(N.toDouble()).toInt()) { // N 포함
        if (!sieve[i]) continue
        for (j in i + i..N step i) sieve[j] = false
    }
    return sieve.withIndex().filter { it.index > 1 && it.value }.map { it.index }
}

fun solution(N: Int): Int {
    var count = 0
    val primeList = getPrimeList(N)
    val len = primeList.size

    if (len == 0) return 0

    var left = 0
    var localSum = primeList[left]
    var right = 0

    while (left < len) {
        while (right < len - 1 && localSum + primeList[right + 1] <= N) {
            right += 1
            localSum += primeList[right]
        }
        if (localSum == N) {
            count += 1
        }
        localSum -= primeList[left]
        left += 1
    }
    return count
}


fun main() {
    val n: Int = readLine()!!.toInt()
    println(solution(n))
}
