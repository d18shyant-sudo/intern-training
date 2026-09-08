from engine import get_db
from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session
from schema.chunk import Query,Query_Response
from service.chunk import Service
from fastapi.responses import JSONResponse
router = APIRouter(prefix="/api/v1",tags=["Chunk_Search"])
@router.post("/fixed_chunk_search",response_model=list[Query_Response])
def fixed_chunk_search(query:Query,db:Session = Depends(get_db)):
    results = Service.fixed_chunk_search(query,db)
    if isinstance(results,Exception):
            return JSONResponse(status_code=500,content={"Error":"Internal Server Error"})
    if results:
        return JSONResponse(status_code=200,content=[result.chunk for result in results])
    else :
        return JSONResponse(status_code=404,content={"Error:No such Content"})
@router.post("/recursive_chunk_search",response_model=list[Query_Response])
def recursive_chunk_search(query:Query,db:Session = Depends(get_db)):
    results = Service.recursive_chunk_search(query,db)
    if isinstance(results,Exception):
            return JSONResponse(status_code=500,content={"Error":"Internal Server Error"})
    if results:
        return JSONResponse(status_code=200,content=[result.chunk for result in results])
    else :
        return JSONResponse(status_code=404,content={"Error:No such Content"})
@router.post("/structure_chunk_search",response_model=list[Query_Response])
def structure_chunk_search(query:Query,db:Session = Depends(get_db)):
    results = Service.structure_chunk_search(query,db)
    if isinstance(results,Exception):
            return JSONResponse(status_code=500,content={"Error":"Internal Server Error"})
    if results:
        return JSONResponse(status_code=200,content=[result.chunk for result in results])
    else :
        return JSONResponse(status_code=404,content={"Error:No such Content"})
