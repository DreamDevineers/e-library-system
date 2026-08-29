from fastapi import APIRouter

router = APIRouter(prefix="/member", tags=["member"])

@router.post("/",)
def create_member():
    pass

@router.get("/",)
def list_members():
    pass

@router.get("/{member_id}")
def get_member(member_id: str):
    pass

@router.delete("/{member_id}")
def delete_member(member_id: str):
    pass