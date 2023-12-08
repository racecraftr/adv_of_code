defmodule Day6 do

  # idk what I am doing lmao

  @path "y2023/day6/input.txt"

  def winningRaces(time, dist) do
    root1 = (time + :math.sqrt(time * time - 4 * dist)) / 2
    root2 = (time - :math.sqrt(time * time - 4 * dist)) / 2
    trunc(:math.floor(root1) - :math.ceil(root2) + 1)
  end

  def getNums(string) do
    string
    |> String.split()
    |> tl()
    |> Enum.map(fn s -> Integer.parse(s) |> elem(0) end)
  end

  def getBigNum(string) do
    string
    |> String.split()
    |> tl()
    |> Enum.join("")
    |> Integer.parse() |> elem(0)
  end

  def part1 do
    File.read(@path)
    |> elem(1)
    |> String.split("\n")
    |> Enum.map(fn s -> s |> getNums end)
    |> Enum.zip()
    |> Enum.map(fn {t, d} -> winningRaces(t, d) end)
    |> Enum.reduce(1, fn v, acc -> v * acc end)
    |> IO.inspect()
  end

  def part2 do
    [time, dist] = File.read(@path)
    |> elem(1)
    |> String.split("\n")
    |> Enum.map(fn s -> s |> getBigNum end)

    winningRaces(time, dist)
    |> IO.inspect()
  end
end

Day6.part1()
Day6.part2()
