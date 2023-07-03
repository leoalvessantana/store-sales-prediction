import pickle
import pandas as pd
from flask import Flask, Response, request
from waitress import serve
from rossmann.Rossmann import Rossmann

# loading model
model = pickle.load( open( 'C:/Users/leona/Documents/repos/ds_producao/model/model_rossmann.pkl', 'rb') )

# initialize API
app = Flask( __name__ )

@app.route( '/rossmann/predict', methods=['POST'] )  # craindo a rota "endpoint" , recebe apenas o metodo POST

def rossmann_predict():

    # pegando o dado
    test_json = request.get_json()

    if test_json: # caso tenha dado
        
        if isinstance( test_json, dict ): # unique example
            test_raw = pd.DataFrame( test_json, index=[0] )
        else: # multiple example
            test_raw = pd.DataFrame( test_json, columns=test_json[0].keys() )

        # Instantiate Rossmann class
        pipeline = Rossmann()

        # data cleaning
        df1 = pipeline.data_cleaning( test_raw )

        # feature engineering
        df2 = pipeline.feature_engineering( df1 )

        # data preparation
        df3 = pipeline.data_preparation( df2 )

        # prediction
        df_response = pipeline.get_prediction( model, test_raw, df3 ) 

        return df_response

    else: # caso não tenha dado, retorna vazio
        return Response( '{}', status=200, mimetype='application/json' )

    
if __name__ == '__main__':
    app.run(host='0.0.0.0')

# if __name__ == "__main__":
#     serve(app, host="0.0.0.0", port=8080)

    
