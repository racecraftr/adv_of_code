package y2023.day1

import java.io.File

class Day1() {
    var lines = File("y2023/day1/day1.txt").useLines { it.toList() }
    val numset = mapOf(
        "1" to 1,
        "2" to 2,
        "3" to 3,
        "4" to 4,
        "5" to 5,
        "6" to 6,
        "7" to 7,
        "8" to 8,
        "9" to 9,
        "one" to 1,
        "two" to 2,
        "three" to 3,
        "four" to 4,
        "five" to 5,
        "six" to 6,
        "seven" to 7,
        "eight" to 8,
        "nine" to 9,
    )

    fun part1() {
        var res = 0
        for (ln in lines) {
            for(c in ln.toCharArray()) {
                if (c in '0'..'9') {
                    res += 10 * (c - '0')
                    break
                }
            }
            for(c in ln.toCharArray().reversed()) {
                if (c in '0'..'9') {
                    res += c - '0'
                    break
                }
            }
        }
        println(res)
    }

    fun part2() {
        var res = 0
        for (ln in lines) {
            var (first, last) = arrayOf(0, 0)
            var (firstIdx, lastIdx) = arrayOf(ln.length, -1)
            for (entry in numset) {
                val (s, v) = entry
                val idx = ln.indexOf(s)
                if (idx in 0..<firstIdx) {
                    firstIdx = idx
                    first = v * 10
                }
            }
        }
        println(res)
    }
}

fun main() {

}