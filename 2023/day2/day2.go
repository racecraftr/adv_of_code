package day2

import (
	"adv_of_code/helper"
	"os"
	"strconv"
	"strings"
)

func initLines() []string {
	ct, err := os.ReadFile("2023/day2/input.txt")
	helper.Check(err)
	return strings.Split(string(ct), "\n")
}

func getGame(ln string) string {
	parsedLn := ln[:len(ln)-1]
	parsedLn = strings.ReplaceAll(parsedLn, " ", "")
	parsedLn = strings.ReplaceAll(parsedLn, "red", "r")
	parsedLn = strings.ReplaceAll(parsedLn, "green", "g")
	parsedLn = strings.ReplaceAll(parsedLn, "blue", "b")
	game := strings.Split(parsedLn, ":")[1]
	return game
}

func parseCubes(cubes string) (byte, int) {
	L := len(cubes) - 1
	cType := cubes[L]
	num, err := strconv.Atoi(cubes[:L])
	helper.Check(err)
	return cType, num
}

func setIsPossible(set string) bool {
	init := map[byte]int{
		'r': 12,
		'g': 13,
		'b': 14,
	}
	for _, cubes := range strings.Split(set, ",") {
		cType, num := parseCubes(cubes)
		if init[cType]-num < 0 {
			return false
		}
	}
	return true
}

func Part1() {
	res := 0
	for i, ln := range initLines() {
		game := getGame(ln)
		gameOk := true
		sets := strings.Split(game, ";")
		for _, set := range sets {
			if gameOk = !setIsPossible(set); !gameOk {
				break
			}
		}
		if gameOk {
			res += (i + 1)
		}
	}
	print(res)
}

func minRequired(sets []string) int {
	resMap := map[byte]int{
		'r': 0,
		'g': 0,
		'b': 0,
	}
	for _, set := range sets {
		for _, cubes := range strings.Split(set, ",") {
			cType, num := parseCubes(cubes)
			if num > resMap[cType] {
				resMap[cType] = num
			}
		}
	}
	res := 1
	for _, n := range resMap {
		res *= n
	}
	return res
}

func Part2() {
	res := 0
	for _, ln := range initLines() {
		game := getGame(ln)
		sets := strings.Split(game, ";")
		res += minRequired(sets)
	}
	print(res)
}

var Export = helper.Export{
	Part1: Part1,
	Part2: Part2,
}
