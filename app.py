from flask import Flask
from flask import render_template
from flask import request
from flask import Response
import model
import json

import process

app = Flask(__name__)


@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method == 'POST':
        player_rk = request.form['rk']
        player_count = request.form['count']

        df_players = process.load_players()
        numpy_array = df_players[
                ['Gls', 'Ast', 'Sh', 'SoT', 'Cmp', 'TotDist', 'Touches', 'Crs', 'Tkl', 'Blocks', 'Int', 'Clr']].values.astype(int)

        if numpy_array.size > 0:

            df_player_list = model.get_pca_results(numpy_array, df_players)
            # print(df_player_list.head())
            selected_rk = int(player_rk)
            selected_row = df_player_list.loc[df_player_list['Rk'] == selected_rk]
            # print(selected_row)

            df_player_list['dist'] = df_player_list.apply(lambda row: process.calculate_distance(row['X'], row['Y'],
                                                                                                 selected_row['X'],
                                                                                                 selected_row['Y']), axis=1)

            sorted_df_player_list = df_player_list.sort_values(by=['dist'], ascending=True, ignore_index=True)
            print(sorted_df_player_list)

            df_similar_players = sorted_df_player_list.loc[1:int(player_count), ["Rk", "Player", "Pos", "Squad", "Age", "Gls", "Ast", "X", "Y"]]
            print(df_similar_players)
            return df_similar_players.to_json(orient='records')


@app.route("/squad", methods=["POST", "GET"])
def squad():
    if request.method == 'POST':
        squad_name = request.form['squad_name']
        # print(squad_name)
        df_players = process.load_players()
        df_squad_players = df_players[df_players["Squad"] == squad_name]
        df_squad_players_subset = df_squad_players[["Rk", "Player", "Pos"]]
        return df_squad_players_subset.to_json(orient='records')


@app.route("/")
def index():
    df_squads = process.load_squads()
    squads = df_squads["Squad"]
    # print(squads.tolist())
    return render_template("index.html", squads=squads.tolist())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)