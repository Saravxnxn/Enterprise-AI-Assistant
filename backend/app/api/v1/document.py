from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.repositories.document_repository import DocumentRepository
from app.schemas.document import DocumentResponse
from app.schemas.response import success_response
from app.services.document_service import DocumentService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post("/upload")
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):

    service = DocumentService(DocumentRepository(db))

    try:

        # Temporary until JWT integration
        user_id = 1

        document = service.upload(
            file=file,
            user_id=user_id,
        )

        return success_response(
            message="Document Uploaded",
            data=DocumentResponse.model_validate(document),
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        ) from e


@router.get("")
def get_documents(
    db: Session = Depends(get_db),
):

    service = DocumentService(DocumentRepository(db))

    documents = service.list_documents()

    return success_response(
        message="Documents",
        data=[DocumentResponse.model_validate(d) for d in documents],
    )


@router.get("/{document_id}")
def get_document(
    document_id: int,
    db: Session = Depends(get_db),
):

    service = DocumentService(DocumentRepository(db))

    document = service.get_document(document_id)

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    return success_response(
        message="Document",
        data=DocumentResponse.model_validate(document),
    )


@router.delete("/{document_id}")
def delete_document(
    document_id: int,
    db: Session = Depends(get_db),
):

    service = DocumentService(DocumentRepository(db))

    document = service.get_document(document_id)

    if not document:
        raise HTTPException(
            status_code=404,
            detail="Document not found",
        )

    service.delete_document(document)

    return success_response(
        message="Document Deleted",
        data=None,
    )
