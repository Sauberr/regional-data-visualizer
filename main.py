import plotly.express as px
import pandas as pd

df = pd.read_csv('input_data.csv')

fig = px.bar(df, x="Область", y="Значення", color="Місто/Район", barmode="stack",
             title="Бар Чарт за Областями та Районами",
             labels={'значення': 'Значення', 'область': 'Область', 'місце/район': 'Район'},
             height=800, width=1200)

fig.update_layout(
    xaxis_tickangle=-45,
    legend_title_text='Район',
    font=dict(size=14),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    bargap=0.5,
    bargroupgap=0.1,
    margin=dict(b=200, t=100, l=50, r=50),
)

fig.update_traces(width=0.3)

fig.show()
