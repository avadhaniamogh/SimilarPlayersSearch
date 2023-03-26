from sklearn.decomposition import PCA
import pandas as pd
import numpy as np


def get_pca_results(numpy_array, df_players):
    # Reduce dimensionality to 2 principal components
    pca = PCA(n_components=2)
    results = pca.fit_transform(np.array(numpy_array))

    # min_x_y = np.min(results, axis=0)
    # max_x_y = np.max(results, axis=0)

    # Get x & y (PCA1 & PCA2) values
    x_se = pd.Series(results[:, 0])
    y_se = pd.Series(results[:, 1])

    df_player_list = df_players[
        ['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Age', 'Gls', 'Ast', 'Sh', 'SoT', 'Cmp', 'TotDist', 'Touches', 'Crs', 'Tkl', 'Blocks',
         'Int', 'Clr']]
    # Insert X & Y to players
    df_player_list.insert(loc=len(df_player_list.columns), column='X', value=x_se.values)
    df_player_list.insert(loc=len(df_player_list.columns), column='Y', value=y_se.values)

    return df_player_list
