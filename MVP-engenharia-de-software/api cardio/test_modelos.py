from model.avaliador import Avaliador
from model.carregador import Carregador
from model.modelo import Model

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_dados = "database/cardio_train.csv"
colunas = ['age', 'gender','height','weight', 'ap_hi', 'ap_lo']

# Carga dos dados
dataset = carregador.carregar_dados(url_dados, colunas)

# Verifique o número real de colunas no seu DataFrame
print(f"Número total de colunas: {len(dataset.columns)}")


# Separando em dados de entrada e saída
X = dataset.iloc[:, 1:7]
Y = dataset.iloc[:, 1]

    
# Método para testar o modelo de Regressão Logística a partir do arquivo correspondente
# O nome do método a ser testado necessita começar com "test_"
def test_modelo_lr():  
    # Importando o modelo de regressão logística
    lr_path = 'ml_model/cardio_lr.pkl'
    modelo_lr = modelo.carrega_modelo(lr_path)

    # Obtendo as métricas da Regressão Logística
    acuracia_lr, recall_lr, precisao_lr, f1_lr = avaliador.avaliar(modelo_lr, X, Y)
    
    # Testando as métricas da Regressão Logística 
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_lr >= 0.75 
    assert recall_lr >= 0.5 
    assert precisao_lr >= 0.5 
    assert f1_lr >= 0.5 
 
# Método para testar modelo KNN a partir do arquivo correspondente
def test_modelo_knn():
    # Importando modelo de KNN
    knn_path = 'ml_model/cardio_knn.pkl'
    modelo_knn = modelo.carrega_modelo(knn_path)

    # Obtendo as métricas do KNN
    acuracia_knn, recall_knn, precisao_knn, f1_knn = avaliador.avaliar(modelo_knn, X, Y)
    
    # Testando as métricas do KNN
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_knn >= 0.75
    assert recall_knn >= 0.5 
    assert precisao_knn >= 0.5 
    assert f1_knn >= 0.5 
    

    print(X)
    print(f"--------------------")
    print(Y)

