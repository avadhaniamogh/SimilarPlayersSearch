import matplotlib.pyplot as plt
from mplcursors import cursor


def get_scatter_plot(df_player_list, selected_row):
    tt = df_player_list["Player"].values

    fig, ax = plt.subplots(1, figsize=(12, 6))
    sc = ax.scatter(df_player_list["X"], df_player_list["Y"])
    plt.plot(selected_row.X, selected_row.Y, 'g*')

    cur = cursor(sc, hover=True)

    @cur.connect("add")
    def on_add(sel):
        sel.annotation.set(text=tt[sel.index])

    plt.show()
