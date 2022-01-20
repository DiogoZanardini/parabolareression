#Bibliotecas
import pandas as pd
import streamlit as st
import seaborn as sns
from numpy import power, where
from numpy.random import randint, seed
#from sklearn.model_selection import train_test_split
#from sklearn.tree import DecisionTreeRegressor
#from seaborn import scatterplot
from matplotlib import pyplot as plt
plt.style.use('seaborn')

arr = []
seed(369)
for i in range(601):
    x = i/100
    y1 = (-power( ((2/3) * x - 2), 2) + 4)
    y2 = y1 + randint(-12, 12)*0.10
    arr.append([x,round(y1, 4),round(y2, 4) ])


df = pd.DataFrame(arr, columns = ['x','y1','y2'])
filtro = (df.loc[:,'y2']<=df.loc[:,'y1'])
df['y3'] = where(filtro, 1, 0)

#X_train, X_test, y_train, y_test = train_test_split(
#    df.drop(['y3'], axis=1),df['y3'], test_size=.3, random_state=0)

st.title('Regressão Logistica na Parábola')
st.write('Arraste os sliders para mover o ponto no gráfico e verificar sua classiicação abaixo:')
ax_x = st.slider('Eixo X:', min_value= 0.0, max_value=6.0, value=3.0, step=.0625)
ax_y = st.slider('Eixo Y:', min_value=-1.0, max_value=5.0, value=2.0, step=.0625)

#model = DecisionTreeRegressor()
#model.fit(X_train, y_train)
reg = -power((2/3 * ax_x - 2), 2) + 4
#pred = model.predict([[ax_x, reg, ax_y]])[0]

#if pred == 1.0:
#    st.subheader('A coordenada está DENTRO da \"zona verde\"')
#elif pred == 0.0:
#    st.subheader('A coordenada está FORA da \"zona verde\"')

fig = plt.figure(figsize=(12, 6))
sctr = sns.scatterplot(data=df, x='x',y='y2',size=1, hue='y3')
sctr = sns.scatterplot(x=[ax_x],y=[ax_y], s=400, marker='+', color='black')
sctr.set_xlabel('Eixo X', fontsize = 20)
sctr.set_ylabel('Eixo Y', fontsize = 20)
sctr.set_title('Distribuição classificada dos dados', fontsize = 20)

st.pyplot(fig)
