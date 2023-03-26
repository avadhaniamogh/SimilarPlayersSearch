import process
import model
import visualize

output_file_name_similar_players = "similar_players.csv"


if __name__ == '__main__':

    df_squads = process.load_squads()
    # print(df_squads.head(10))
    squads = df_squads["Squad"]
    # print(squads)
    # print(type(squads))

    df_players = process.load_players()

    numpy_array = df_players[
        ['Gls', 'Ast', 'Sh', 'SoT', 'Cmp', 'TotDist', 'Touches', 'Crs', 'Tkl', 'Blocks', 'Int', 'Clr']].values.astype(int)

    if numpy_array.size > 0:

        df_player_list = model.get_pca_results(numpy_array, df_players)
        selected_rk = 295  # 5
        selected_row = df_player_list.loc[df_player_list['Rk'] == selected_rk]
        print(selected_row.X)
        print(type(selected_row.X))

        df_player_list['dist'] = df_player_list.apply(lambda row: process.calculate_distance(row['X'], row['Y'],
                                                                                             selected_row['X'],
                                                                                             selected_row['Y']), axis=1)

        sorted_df_player_list = df_player_list.sort_values(by=['dist'], ascending=True, ignore_index=True)
        print(sorted_df_player_list)

        df_similar_players = sorted_df_player_list.loc[1:10, ["Rk", "Player", "Pos", "Squad", "Age", "Gls", "Ast",
                                                              "X", "Y"]]
        print(df_similar_players)

        df_similar_players_plus_selected = sorted_df_player_list.loc[:10, :]
        df_similar_players_plus_selected.to_csv(output_file_name_similar_players, sep='\t', encoding='utf-8')

        # visualize.get_scatter_plot(df_player_list, selected_row)
    else:
        print("No players fall in this category.")
