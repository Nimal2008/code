import 'dart:io';

//import 'package:flutter/material.dart';

void main() {
  print('Please enter your age');
  String? age = stdin.readLineSync();
  int currentAge = int.parse(age!);
  int agern = 100 - currentAge;
  print('Your current age is $agern ');
}

class Student {
  Student(this.name, this.age);
  String name;
  int age;
}

List<Student> studentList = [
  Student('Nimal', 15),
  Student('Jai', 9),
  Student('Deep', 10),
  Student('Charu', 8),
  Student('Sree', 8)
];
