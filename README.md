# My solutions to Google Foobar

> [Google Foobar](https://foobar.withgoogle.com/) is Google's secret hiring challenge made up of 5 different levels with increasing difficulty. Each level has between one and three questions. Levels 1 to 3 are 7 days per question, level 4 is 15 days per question and level 5 is 22 days for one question.

## Progress

*Current level: **5***   
*Challenges left to complete level: **1***

|Level|Status|
|-|-|
|[Level 1](https://github.com/dhruvnps/google-foobar/tree/master/Level%201)|**100%**|
|[Level 2](https://github.com/dhruvnps/google-foobar/tree/master/Level%202)|**100%**|
|[Level 3](https://github.com/dhruvnps/google-foobar/tree/master/Level%203)|**100%**|
|[Level 4](https://github.com/dhruvnps/google-foobar/tree/master/Level%204)|**100%**|
|Level 5|0%|

## Overview

### Level 1

Part 1: **[re-id](https://github.com/dhruvnps/google-foobar/tree/master/Level%201/re-id)**
> Involves genereating prime numbers upto a certain point. This was achieved by iterating through every odd number greater than 3 and checking for primality. The primality test involved checking for divisibilty with all numbers 6n±1 from 6 to the square root of the number being tested.

### Level 2

Part 1: **[elevator-maintenance](https://github.com/dhruvnps/google-foobar/tree/master/Level%202/elevator-maintenance)**
> Involves sorting a list of version numbers. This was done by sorting the list of version numbers giving precedence to the first value in the version number.

Part 2: **[please-pass-the-coded-messages](https://github.com/dhruvnps/google-foobar/tree/master/Level%202/please-pass-the-coded-messages)**
> Involves finding the largest multiple of three that can be made by concatenating some or all of the integers in a list. This can be solved using the fact that the digits of a multiple of three add to a value that is divisible by three. The remainder of using all digits in the list can be found to be either 1 or 2. Digits can then be removed from the list accordingly and the reverse of the remaining list concatenated will be the maximum.

### Level 3

Part 1: **[find-the-access-codes](https://github.com/dhruvnps/google-foobar/tree/master/Level%203/find-the-access-codes)**
> Involves finding the number of lucky triples in a list of intgers. A lucky triple is a triple where the first number divides the second which divides the third, and the numbers appear sequentially in the list. This can be solved by finding overlapping pairs of numbers where the first divides the second.

Part 2: **[prepare-the-bunnies-escape](https://github.com/dhruvnps/google-foobar/tree/master/Level%203/prepare-the-bunnies-escape)**
> A pathfinding problem in which you must find the shortest path in a maze where a maximum of one wall can be broken. This problem was solved by using a breadth first algorithm to create a matrix of the distance of each point in the maze from the start and from the end. The minimum value when the start and end distance matrices are added will be the minimum distance.

Part 3: **[fuel-injection-perfection](https://github.com/dhruvnps/google-foobar/tree/master/Level%203/fuel-injection-perfection)**
> Involves reducing a number to 1 using the least number of operations. The allowed operations are: +1, -1, ÷2. This problem can be solved by finding the pattern using the binary representation of the value.

### Level 4

Part 1: **[escape-pods](https://github.com/dhruvnps/google-foobar/tree/master/Level%204/escape-pods)**
> A maximum flow problem with multiple entrance and exit rooms, and intermedeate rooms connected to one another by uni-directional corridors each having a maximum capacity. The maximum flow was found using the Ford Fulkerson method with a breadth first search.

Part 2: **[bringing-a-gun-to-a-guard-fight](https://github.com/dhruvnps/google-foobar/tree/master/Level%204/bringing-a-gun-to-a-guard-fight)**
> Involves a room with specified dimentions in which there are two specified points, A and B. A laser can be shot from point A which can reflect off the walls of the room. The laser will stop if it hits A or B, or if the laser has traveled a given maximum distance. The number of angles the the laser can be shot from A such that it hits B and not A must be found. This problem can be solved by reflecting the room in across each wall. The angles that the laser can travel from A to any reflection of B without hitting a reflection of A can then be found.
