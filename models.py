from typing import Optional
from pydantic import BaseModel


class Verificacao(BaseModel):
    id: Optional[int]= None
    codigo: int
    edv: int
    nome: str
    area: str