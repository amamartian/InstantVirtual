import random

# List of teams
teams = ['MCI', 'LIV', 'ARS', 'CHE', 'NEW', 'MNU', 'AST', 'BHA', 'BRE', 'TOT', 'WOL', 'WHU', 'FUL', 'FOR', 'BOU', 'CRY', 'EVE', 'LUT', 'SHU', 'BUR']

# Assign goal probabilities to each team based on their position in the list
total_teams = len(teams)
goal_probabilities = {team: 15 - i * 0.5 for i, team in enumerate(teams)}

# Generate fixtures for the season
fixtures = []

# Generate round-robin fixtures
for i in range(len(teams) - 1):
    round_fixtures = []
    for j in range(len(teams) // 2):
        home = teams[j]
        away = teams[len(teams) - 1 - j]
        round_fixtures.append((home, away))
    fixtures.append(round_fixtures)
    # Rotate the teams list for the next round
    teams = [teams[0]] + [teams[-1]] + teams[1:-1]

# Reverse the fixtures for the reverse matchweeks
reverse_fixtures = [[(away, home) for home, away in matchday] for matchday in fixtures]

# Combine original and reverse fixtures
combined_fixtures = fixtures + reverse_fixtures

# Shuffle the fixtures within each matchday
for matchday in combined_fixtures:
    random.shuffle(matchday)

# Randomize the order of matchweeks
random.shuffle(combined_fixtures)
    
# Display the combined fixtures
for matchweek, matchday in enumerate(combined_fixtures, 1):
    print(f"Matchweek {matchweek} Fixtures:")
    for home_team, away_team in matchday:
        print(f"{home_team} vs {away_team}")
    print()
    
# Define a function to calculate goal probability based on team's position
    def goal_probability(team):
        return goal_probabilities[team]
        
# Generate random match results for the fixtures        
results = {}
for matchday, matchday_fixtures in enumerate(combined_fixtures, 1):
    matchday_results = {}
    for home_team, away_team in matchday_fixtures:

    # Get goal probabilities for home and away teams
        home_probability = goal_probability(home_team) 
        away_probability = goal_probability(away_team)

        # Generate random scores for each team based on goal probabilities
        home_score = sum(1 for _ in range(6) if random.randint(0, 30) < home_probability)
        away_score = sum(1 for _ in range(6) if random.randint(0, 40) < away_probability)

        # Ensure the total goals in a fixture doesn't exceed 6
        total_goals = home_score + away_score
        if total_goals > 6:
            excess_goals = total_goals - 6
            # If the total excess goals are odd, replace it with the next higher even number
            if excess_goals % 2 != 0:
                excess_goals += 1
            # Determine the number of excess goals each team receives
            home_excess_goals = excess_goals // 2
            away_excess_goals = excess_goals - home_excess_goals
           
            # Update the scores by distributing excess goals evenly between the teams
            home_score -= home_excess_goals
            away_score -= away_excess_goals

        results[(home_team, away_team)] = (home_score, away_score)
# Display results for each matchday
print("\nResults:")
for matchday, matchday_fixtures in enumerate(combined_fixtures, 1):
    print(f"\nMatchday {matchday} results:")
    for home_team, away_team in matchday_fixtures:
        home_score, away_score = results.get((home_team, away_team), (0, 0))
        result_string = f"{home_team} {home_score}-{away_score} {away_team}"
        print(result_string.ljust(20))
    print()