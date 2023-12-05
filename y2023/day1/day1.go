package day1

import (
	"adv_of_code/helper"
	"os"
	"strings"
)

func Part1() {
	ct, err := os.ReadFile("y2023/day1/day1.txt")
	helper.Check(err)
	lines := strings.Split(string(ct), "\n")
	res := 0
	for _, ln := range lines {
		for _, c := range ln {
			if '0' <= c && c <= '9' {
				res += 10 * int(c-'0')
				break
			}
		}
		for i := len(ln) - 1; i >= 0; i-- {
			c := ln[i]
			if '0' <= c && c <= '9' {
				res += int(c - '0')
				break
			}
		}
	}
	print(res)
}

var numMap = map[string]int{
	"1":     1,
	"2":     2,
	"3":     3,
	"4":     4,
	"5":     5,
	"6":     6,
	"7":     7,
	"8":     8,
	"9":     9,
	"one":   1,
	"two":   2,
	"three": 3,
	"four":  4,
	"five":  5,
	"six":   6,
	"seven": 7,
	"eight": 8,
	"nine":  9,
}

func Part2() {
	ct, err := os.ReadFile("2023/day1/day1.txt")
	helper.Check(err)
	lines := strings.Split(string(ct), "\n")
	res := 0
	for _, ln := range lines {
		first, last := 0, 0
		fIdx, lIdx := len(ln)+1, -1
		for s, v := range numMap {
			idx := strings.Index(ln, s)
			if idx >= 0 && idx < fIdx {
				fIdx = idx
				first = v * 10
			}
			idx = strings.LastIndex(ln, s)
			if idx >= lIdx {
				lIdx = idx
				last = v
			}
		}
		res = first + last
	}
	print(res)
}

var Export = helper.Export{
	Part1: Part1,
	Part2: Part2,
}
