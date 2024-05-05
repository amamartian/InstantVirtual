# Football Fixture and Result Simulator

This is a python script that generates fixtures for football matches and simulates match results.

## Version
There are 2 verions 

## Version 1 Features

- Generates 10 random fixtures from 20 teams to represent a matchweek.
- Assigns goal probabilities to each team based on their position in a predetermined list.
- Assigns a predetermined advantage to all home teams in a matchweek.
- Simulates match results by generating random scores up to 6 goals for each team indepemdently.
- Scores are generated based on each team goal probability and home advantage.
- Ensures the total goals in a fixture do not exceed 6 and proper error handling for score generation that exceed 6 goals.
  
## Version 2 Features

- Generates fixtures for a 38 matchweek season using a round-robin algorithm.
- Assigns goal probabilities to each team based on their position in a predetermined list.
- Assigns a predetermined advantage to all home teams in a matchweek.
- Simulates match results by generating random scores up to 6 goals for each team indepemdently.
- Scores are generated based on each team goal probability and home advantage.
- Ensures the total goals in a fixture do not exceed 6 and proper error handling for score generation that exceed 6 goals.
- Team list, home advantage and goal probabilities for each team can be randomly adjusted for each matchweek as desired.

## Usage

The content of this project, including but not limited to source code, documentation, and any associated files, is the exclusive property of Adebanjo Matini. No part of this project may be reproduced, distributed, or transmitted in any form without the prior written permission of the author. For permission requests, contact matiniadebanjo@gmail.com.

## Requirements

- Python 3.x

## Acknowledgments

- This script is inspired by the need to automate the generation of football fixtures and simulate match results for commercial purposes.
