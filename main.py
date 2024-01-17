from typing import List , Optional

from fastapi.responses import JSONResponse
from fastapi import Response

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status 
from models import Verificacao

app = FastAPI()

verificacoes = {
    1: {"codigo":511938,
        "edv": 12345678,
        "nome": "Joao victor",
        "area": "ETS"
    },
    2: {"codigo":511638,
        "edv": 89012342,
        "nome": "Sarah ",
        "area": "ETS"
    },
    3: {"codigo":511638,
        "edv": 89012342,
        "nome": "Murilo Campos",
        "area": "ETS"
    },
    4: {"codigo":511638,
        "edv": 89012342,
        "nome": "Vitoria",
        "area": "ETS"
    },
    5: {"codigo":511638,
        "edv": 89012342,
        "nome": "Mirela",
        "area": "ETS"
    },
    6: {"codigo":511638,
        "edv": 89012342,
        "nome": "Stella arthoa",
        "area": "ETS"
    },

}

@app.get('/Verificacao')
async def get_verificacao():
    return verificacoes

@app.get('/Verificacao/{cadastrado_id}')
async def get_verificacao_by_id(cadastrado_id: int):
    verificacao = verificacoes[cadastrado_id]
    verificacao.update({"id": cadastrado_id})
    return verificacao

@app.post('/Verificacao', status_code=status.HTTP_201_CREATED)
async def post_verificacao(verificacao: Verificacao):
    next_id: int =  len(verificacoes) + 1
    verificacoes[next_id] = verificacao
    del verificacao.id
    return verificacao

@app.put('/Verificacao/{verificacao_id}')
async def put_verificacao(verificacao_id: int, verificacao: Verificacao):
    if verificacao_id in verificacoes:
        verificacoes[verificacao_id] = verificacao
        del verificacao.id
        return verificacao
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe verificacao com o ID {verificacao_id}")
    
    

@app.delete('/Verificacao/{verificacao_id}')
async def delete_verificacao(verificacao_id: int):
    if verificacao_id in verificacoes:
        del verificacoes[verificacao_id]
        #return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe verificacao com o ID {verificacao_id}")



 


 

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)
