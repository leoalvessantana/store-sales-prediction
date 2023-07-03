# Store Sales Prediction

<div align="center">
<img src="img/img_rossmann.jpg" width="800px" />
</div>

A empresa, o contexto e as perguntas de negócio a seguir são completamente fictícias, foram criadas apenas para o desenvolvimento do projeto, e se baseiam em um desafio do Kaggle. 

## 1. Contexto de negócio

A empresa Rossmann opera mais de 3.000 drogarias em 7 países europeus. Atualmente, os gerentes de loja da Rossmann têm a tarefa de prever suas vendas diárias com até seis semanas de antecedência. As vendas da loja são influenciadas por muitos fatores, incluindo promoções, competição, feriados escolares e estaduais, sazonalidade e localidade. 

Com milhares de gerentes prevendo vendas com base em suas circunstâncias únicas, a precisão dos resultados pode ser bastante variada. A necessidade de fazer uma previsão de vendas vem de um pedido do CFO que deseja fazer uma reforma nas lojas, porém não sabe o quanto de dinheiro pode ser destinado para esta reforma. Sua intenção é saber o faturamento das lojas para as próximas 6 semanas para assim poder adiantar o orçamento e realizar as reformas.


## 2. Premissas de Negócio
Para a construção da solução, foram consideradas as seguintes premissas:
* Foram consideradas para a previsão apenas as lojas que possuiam o valor de vendas superior a 0 na base de dados.
* Os dias em que as lojas estavam fechadas foram descartadas na realização da previsão.
* Lojas que não possuíam dados de competidores próximos tiveram o valor da distância fixada em 200.000 metros.




### 2.1. Descrição dos Dados
O conjunto de dados que representam o contexto está disponível na plataforma do Kaggle. Esse é o link: https://www.kaggle.com/c/rossmann-store-sales/data. O dataset possui os seguintes atributos:

| Atributo                          | Descrição                                                                                                                                             |
| :-------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Store                             | Identificador único de cada loja                                                                                                                      |
| Date                              | Data em que ocorreu o evento de venda                                                                                                                 |
| DayOfWeek                         | Variável numérica que representa o dia da semana                                                                                                      |
| Sales                             | Valor de vendas do dia                                                                                                                                |
| Customers                         | Quantidade de clientes na loja no dia                                                                                                                 |
| Open                              | Indicador para loja aberta = 1 ou fechada = 0                                                                                                         |
| StateHoliday                      | Indica se o dia é feriado de estado. a = Feriado público, b = Feriado de páscoa, c = Natal, 0 = Não há feriado                                        |
| SchoolHoliday                     | Indica se a loja foi ou não fechada durante o feriado escolar                                                                                         |
| StoreType                         | Indica o modelo de lojas. Pode variar entre a, b, c, d                                                                                                |
| Assortment                        | Indica o nível de variedade de produtos: a = básico, b = extra, c = estendido                                                                         |
| CompetitionDistance               | Distância (em metros) para o competidor mais próximo                                                                                                  |
| CompetitionOpenSince [Month/Year] | Indica o ano e mês em que o competidor mais próximo abriu                                                                                             |
| Promo                             | Indica se a loja está com alguma promoção ativa no dia                                                                                                |
| Promo2                            | Indica se a loja deu continuidade na promoção: 0 = loja não está participando, 1 = loja participando                                                  |
| Promo2Since [Year/Week]           | Descreve o ano e semana de quando a loja começa a a promoção extendida                                                                                |
| PromoInterval                     | Descreve os meses em que a loja iniciou a promo2, ex.: "Feb,May,Aug,Nov" significa que a loja iniciou as promoções estendidas em cada um desses meses |



## 3. Planejamento da solução
Para fazer a entrega da primeira solução de maneira o mais rápido possível, entregando valor para a empresa e possibilitando que o CFO tome decisões com mais agilidade, foi utilizado o método CRISP-DS

![](img/crisp_ds.png)


O método CRISP-DS consiste em 9 passos ciclicos, onde a cada iteração dos nove passos, o resultado de negócio vai sendo aperfeiçoado, visando entregas cada vez mais rápidas e cada vez com mais qualidade e acertivas, possibilitando assim que as equipes que irão utilizar os resultados desenvolvidos tenham um produto um produto minimamente utilizável na primeira entrega e que é aperfeiçoado ao longo do tempo.

### Passos do CRISP-DS:
1. **Problema de Negócio:** Esta etapa tem como objtive receber o problema de negócio que será resolvido. É nesta etapa que é recebido a perguta ou o pedido feito pelo dono do problema, que no caso deste projeto, é o CFO da rede Rossmann.
2. **Entendimento de Negócio:** Esta etapa tem como objetivo entender a dor do dono do problema e qual a sua real necessidade. Nesta etapa podem surgir protótipos da solução para validar com o dono do problema o que ele deseja como solução. 
3. **Coleta de Dados:** Esta etapa tem como objetivo realizar a coleta dos dados, buscando eles nas tabelas do(s) banco(s) de dados da empresa. No nosso caso acessando a plataforma do Kaggle para download dos arquivos que serão usados.
4. **Limpeza dos Dados:** Esta etapa tem como objetivo remover toda e qualquer sujeira nos dados. Um dado sujo pode ser entendido como um dado que irá atrapalhar a performance final do algoritmo de Machine Learning. Tomando o cuidado entender bem o fenômeno que está sendo estudado para que não sejam removidos dados importantes para a modelagem do problema.
5. **Exploração dos Dados:** Esta etapa tem como objetivo entender os dados e como eles se relacionam entre si. Normalmente, são criadas hipóteses acionáveis de negócio que são posteriormente validadas utilizando técnicas de análise de dados. Além da criação de novas *features* que serão utilizadas na etapa de Modelagem de Dados.
6. **Modelagem dos Dados:** Esta etapa tem como objetivo preparar os dados para que eles sejam utilizados pelos algoritmos de Machine Learning. É nesta etapa que são feitos as transformações e *encodign* dos dados, a fim de facilitar o aprendizado do algoritmo utilizado.
7. **Aplicação de Algoritmos de Machine Learning:** Esta etapa tem como objetivo selecionar e aplicar algoritmos de Machine Learning nos dados preparados nas etapas anteriores. É nesta etapa que são selecionados os algoritmos e feito a comparação de performance enetre eles, para selecionar o algoritmos que melhor performou como algoritmo final.
8. **Avaliação de Performance:** Esta etapa tem como objetivo verificar a performance do algoritmo selecionado na etapa anterior com os resultados atuais, ou *base line* atual. Neste momento é feito a tradução da performance do algoritmo para perfomance de negócio. Ou seja, quanto a solução criada tratrá de retorno financeiro para a empresa. Caso a performance seja aceitável, o algoritmo é publicado e é retornado para a etapa de entendimento de negócio novamente, a fim entender melhor possíveis lacunas e assim melhorar a performance do algoritmo selecionado. Caso a performance não seja aceitável, o algoritmo não é publicado e é retornado para a etapa de entendimento de negócio para fazer uma nova iteração e assim melhorar a performance da solução.
9. **Publicação da Solução:** Esta etapa tem como objetivo publicar o algoritmo selecionado, deixando publico e utilizável a solução criada. Em nosso caso criamos uma API que retorna as previsões das lojas. Será entregue um Bot dentro do aplicativo Telegram, facilitando assim que o CFO verifique a previsão das lojas independente do local em que ele esteja.




### 3.1 Ferramentas Utilizadas 

<div align="center">

|    <!-- -->   |                    <!-- -->                     |
|---------------|-------------------------------------------------|
|**Programação**| Python 3.9.16; <br> Jupyter Notebook; <br> VSCode. |
|**Visualização de dados**|   Matplotlib; Seaborn.  |
|**Bibliotecas de ML**|Sklearn; Xgboost; Boruta.|
|**Engenharia de software**| Flask; <br> Git; Github; <br> Render Cloud; Telegram Bot.|

</div>



# 4.0 - Alguns insights

## 4.1 Lojas com mais sortimento vendem MENOS.

<div align=center>

![H1](img/H1.png 'sadas')
</div>


## 4.2 Lojas com competidores mais próximos vendem MAIS

<div align=center>

![H2](img/H2.png 'sadas')
</div>


## 4.3 Lojas vendem MENOS aos finais de semana.

<div align=center>

![H12](img/H12.png 'sadas')
</div>



# 5.0 - Desempenho do modelo

Foram testados cinco modelos de ML, começamos pelo Average Model, utilizado como base para comparar a performance dos demais modelos. Em seguida utilizamos dois modelos lineares: Regressão linear (LR) e Regressão Linear Regularizada (LASSO); dois não lineares: Random Forest Regressor (RFR) e XGBoost Regressor (XGB). 

Para avaliar a performace dos modelos utilizamos as seguintes métricas:  Erro absoluto médio (MAE), Erro absoluto médio percentual (MAPE) e a Raiz quadrática do erro quadrático médio (RMSE). O MAE e MAPE conseguem explicar o desempenho comercial do modelo. O MAE mostra o quanto a previsão do modelo está errada, em média; já o MAPE tem interpretação semelhante, mas em termos percentuais. O RMSE não possui uma interpretação útil do ponto de vista financeiro, entretanto é muito bom para nos dizer o quão bom nosso modelo descreve o fenômeno, quanto menor o RMSE melhor é a performance do modelo. Aplicamos nos modelos o método de Cross-Validation e confirmamos que os modelos não lineares se saiam melhores. Embora a RFR apresente um menor RMSE seguiremos com o XGB regressor devido ao desempenho semelhante, mas principalmente pelo menor tempo de processamento quando comparado com o RFR.

Após ter escolhido o modelo partimos para escolha dos melhores parametros para o aprendizado do modelo. A técnia utilizada aqui foi a Random Search, que, aleatoriamente, procura os parâmetros do modelo que apresentam a melhor performance. Feito isso obtemos as seguintes métricas:

<div align="center">

| Model Name |  MAE  |  MAPE (%) |       RMSE       | 
|:----------:|:-----:|:---------:|:----------------:|
|     XGB    | 655.3 |	  9.5    |	     950.5      |
</div>


Para analisar o desempenho do modelo iremos observar quatro gráficos. No primeiro  "Valores reais e previstos pelo modelo", observa-se claramente que os valores reais e previstos seguem a mesma curva de comportamento ou seja, os dois valores seguem as mesmas tendências, por mais que haja erros inerentes ao processo. No próximo, "Taxa de erro (Previsão / Real"), observa-se que os valores das taxas orbitam o valor 1, que indica igualdade entre valores previstos e reais, indicando que o modelo está relativamente próximo da realidade. Já no terceiro gráfico, "Distribuição de erros absolutos", tem-se uma distribuição dos erros absolutos aproximando-se de uma distribuição normal, embora com assimetria à esquerda, mas com maior frequência de erros absolutos próximos a zero. Por fim, o gráfico "Valores dos erros em relação aos erros previstos" mostra novamente que a maioria dos valores preditos possuem erros absolutos tendendo a zero.

<div align=center>

![P](img/model_performance.png 'sadas')
</div>

Com estas análises de erro pode-se concluir que o modelo possui bom desempenho. Cabe a uma análise posterior decidir se a magnitude desses erros é satisfatória para responder a questão de negócio ou se será necessária a aplicação de um novo ciclo do CRISP.


## 5.1 Performance do ponto de vista financeiro:

A seguir é exibido o resultado das previsões em termos financeiros das próximas seis semanas, preditos utilizando o modelo XGBoost. Na primeira tabela temos os resultados de cinco lojas, na segunda previsões de toda a receita das lojas Rossmann: 

<div align="center">PREVISÕES DE CINCO LOJAS ROSSMANN

| store |predictions (€)|worst_scenario (€)|best_scenario (€)| MAE (€) |MAPE (%)|
|:-----:|:-------------:|:----------------:|:---------------:|:-------:|:------:|
|   1   |   160907.6    |     160590.1     |     161225.2    |  317.5  |  7.2   |
|   2   |   172382.4    |     172017.2     |     172747.5    |  365.1  |  7.3   |
|   3   |   259990.4    |     259371.1     |     260609.6    |  619.2  |  8.7   |
|   4   |   342472.3    |     341542.1     |     343402.4    |  930.1  |  8.9   |
|   5   |   177314.9    |     176842.7     |     177787.1    |  472.2  |  10.0  |

</div>


<div align="center">PREVISÃO DA RECEITA TOTAL DAS LOJAS ROSSMANN


|**Scenarios**:|  predictions   | worst_scenario   | best_scenario |
|:-------:|:--------------:|:----------------:|:-------------:|
|**Values**:|€282,430,784.0 | €281,696,979.7  |€283,165,598.9|
</div>







## Obervação
Projeto em desenvolvimento. Atualmente estamos na ultima etapa, que é de colocar o modelo em produção.


