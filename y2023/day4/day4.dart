
import 'dart:io';
import 'dart:convert';

const path = 'y2023/day4/input.txt';
List<String> lines = List.empty(growable: true);

(Set<int>, List<int>) parseLine(String line) {
  var [_, data] = line.split(r'\: +');
  data = data.trim();
  var [winning, yours] = data.split(' | ');
  winning = winning.trim();
  yours = yours.trim();
  return (
    winning.split(r' +').map((e) => int.parse(e)).toSet(),
    yours.split(r' +').map((e) => int.parse(e)).toList()
  );
}

int getNumMatched(String ln) {
  var (winning, yours) = parseLine(ln);
  return yours.where((element) => winning.contains(element)).length;
}

void part1() {
  var res = 0;
  lines.forEach((ln){
    var n = getNumMatched(ln);
    res += ((n < 1) ? 0 : 1);
  });
  print(res);
}

void main(List<String> args) {
  new File(path)
      .openRead()
      .map(utf8.decode)
      .transform(new LineSplitter())
      .forEach((element) {
    lines.add(element);
  });
  print(lines);
  part1();
}
