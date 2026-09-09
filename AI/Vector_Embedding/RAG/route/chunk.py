from engine import get_db
from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session
from schema.chunk import Query,Query_Response,Citation
from service.chunk import Service
from fastapi.responses import JSONResponse
router = APIRouter(prefix="/api/v1",tags=["Chunk_Search"])
@router.post("/rag_search",response_model=list[Query_Response])
def rag_search(query:Query,db:Session = Depends(get_db)):
    results = Service.rag_search(query,db)
    if isinstance(results,Exception):
            return JSONResponse(status_code=500,content={"Error":"Internal Server Error"})
    if results:
        return JSONResponse(
    status_code=200,
    content=[
        Query_Response(
            chunk=result.content,
            citations=[
                Citation(
                    document_name=result.langchain_metadata["document_name"],
                    page_no=result.langchain_metadata["page"]
                )
            ]
        ).model_dump()
        for result in results
    ]
)
    else :
        return JSONResponse(status_code=201,content=[])

