# Football Fixture and Result Simulator

This is a python script that generates fixtures for football matches and simulates match results.

## Version
There are 2 versions 

## Version 1 Features

- Generates 10 random fixtures from 20 teams to represent a matchweek.
- Assigns goal probabilities to each team based on their randomized position on the list.
- Assigns random advantage to all home teams in the matchweek.
- Simulates match results by generating random scores up to 6 goals for each team independently.
- Scores are generated based on each team goal probability and home advantage.
- Ensures the total goals in a fixture do not exceed 6.
  This version is hosted on AWS Lambda as a function and can be invoked through this link https://7vkymievuc72n2o3d2faa3za340wprsk.lambda-url.us-east-1.on.aws/
## Version 2 Features

- Generates fixtures for a 38 matchweek season using a round-robin algorithm.
- Assigns goal probabilities to each team based on their randomized position on the list for each matchweek.
- Assigns a random advantage to all home teams in a matchweek.
- Simulates match results by generating random scores up to 6 goals for each team independently.
- Scores are generated based on each team goal probability and home advantage.
- Ensures the total goals in a fixture do not exceed 6 and proper error handling for score generation that exceed 6 goals.
- Home advantage and goal probabilities are randomly adjusted for each matchweek.
- Team list are randomly selected for each season.
  This version is hosted on AWS Lambda as a function and can be invoked through this link https://thqtxxgnrh46kcuutbxszf6phq0ubmgd.lambda-url.us-east-1.on.aws/
## Usage

The content of this project, including but not limited to source code, documentation, links, and any associated files, is the exclusive property of Adebanjo Matini. No part of this project may be reproduced, distributed, or transmitted in any form without the prior written permission of the author. For permission requests, inquiries, contact matiniadebanjo@gmail.com.

## Requirements

- Python 3.x

## Acknowledgments

- This script is inspired by the need to automate the generation of football fixtures and simulate match results for commercial purposes.
