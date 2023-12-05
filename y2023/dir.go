package adv2023

import (
	"adv_of_code/y2023/day1"
	"adv_of_code/y2023/day2"
	"adv_of_code/helper"
)

func no() {
	panic("invalid day!")
}

var Days = []helper.Export{
	{Part1: no, Part2: no},
	day1.Export,
	day2.Export,
}
