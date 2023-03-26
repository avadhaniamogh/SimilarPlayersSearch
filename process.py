import pandas as pd
from pathlib import Path
import math

# Directory path
laliga_data_path = Path("data/LaLiga/")


def load_squads():
    # Squads file paths
    squads_file_path = laliga_data_path / "Squads.csv"

    #Load squads csv
    df_squads = pd.read_csv(squads_file_path, encoding='utf-8')

    return df_squads


def load_players():
    # Individual file paths
    std_stats_file = laliga_data_path / "Standard_stats.csv"
    shooting_file = laliga_data_path / "Shooting.csv"
    passing_file = laliga_data_path / "Passing.csv"
    possession_file = laliga_data_path / "Possession.csv"
    misc_file = laliga_data_path / "Misc.csv"
    def_acts_file = laliga_data_path / "Defensive_actions.csv"

    # Load csv to dfs
    df_std_stats = pd.read_csv(std_stats_file, encoding='utf-8')
    df_shooting = pd.read_csv(shooting_file, encoding='utf-8')
    df_passing = pd.read_csv(passing_file, encoding='utf-8')
    df_possession = pd.read_csv(possession_file, encoding='utf-8')
    df_misc = pd.read_csv(misc_file, encoding='utf-8')
    df_def_acts = pd.read_csv(def_acts_file, encoding='utf-8')

    # Select relevant columns
    df_std_stats = df_std_stats[['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Age', 'Gls', 'Ast']]
    df_shooting = df_shooting[['Rk', 'Sh', 'SoT']]
    df_passing = df_passing[['Rk', 'Cmp', 'TotDist']]
    df_possession = df_possession[['Rk', 'Touches']]
    df_misc = df_misc[['Rk', 'Crs']]
    df_def_acts = df_def_acts[['Rk', 'Tkl', 'Blocks', 'Int', 'Clr']]

    # Fill NA in dfs
    df_std_stats.fillna(0, inplace=True)
    df_shooting.fillna(0, inplace=True)
    df_passing.fillna(0, inplace=True)
    df_possession.fillna(0, inplace=True)
    df_misc.fillna(0, inplace=True)
    df_def_acts.fillna(0, inplace=True)

    # Merge all dfs
    df_players = df_std_stats.merge(df_shooting, on='Rk').merge(df_passing, on='Rk').merge(df_possession,
                                                                                           on='Rk').merge(df_misc,
                                                                                                          on='Rk').merge(
        df_def_acts, on='Rk')

    return df_players


def calculate_distance(x, y, orig_x, orig_y):
    return math.dist([orig_x, orig_y], [x, y])




