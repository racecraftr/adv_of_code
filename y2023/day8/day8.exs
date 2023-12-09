defmodule BasicMath do
  def gcd(a, 0), do: a
  def gcd(0, b), do: b
  def gcd(a, b), do: gcd(b, rem(a, b))

  def lcm(0, 0), do: 0
  def lcm(a, b), do: a * b / gcd(a, b)
end

defmodule Day7 do

  def get_stuff do
    content = File.read("y2023/day8/input.txt") |> elem(1)
    [dirs, lookup_str] = String.split(content, "\n\n", parts: 2)

    lookup = Map.new()

    for lookup_ln <- String.split(lookup_str, "\n") do
      lookup_ln = String.replace(lookup_ln, ~r"[\(\)\=\,]", "")
      [key, left, right] = String.split(lookup_ln, parts: 3)
      lookup = Map.put(lookup, key, {left, right})
    end

    {dirs, lookup}

  end
end

Day7.get_stuff
