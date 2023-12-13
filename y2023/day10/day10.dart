import 'dart:io';

enum dir { north, south, east, west, noop }

class Point {
  final int x;
  final int y;
  const Point(this.x, this.y);

  @override
  bool operator ==(Object other) =>
      other is Point && (other.x, other.y) == (this.x, this.y);
}

var dirs = {
  '|': (dir.north, dir.south),
  '-': (dir.east, dir.west),
  'L': (dir.north, dir.east),
  'J': (dir.north, dir.west),
  '7': (dir.south, dir.west),
  'F': (dir.south, dir.east),
  '.': (dir.noop, dir.noop),
};

var down = {'|', '7', 'F'};

void main() async {
  String f = "";
  await File('y2023/day10/input.txt').readAsString().then((value) => f = value);
  print(f);

  var maze = f.split('\n');
  Set<Point> visited = {};

  for (var i = 0; i < maze.length; i++) {
    
  }
}
