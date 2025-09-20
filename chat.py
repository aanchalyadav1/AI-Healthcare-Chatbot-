from fastapi import APIRouter
from pydantic import BaseModel
from app.services.safety import SafetyService
from app.services.llm_client import LLMClient

router = APIRouter()
safety = SafetyService()
llm = LLMClient()

class Message(BaseModel):
    session_id: str
    user_id: str = None
    text: str

@router.post("/message")
async def message(msg: Message):
    risk = safety.check_risk(msg.text)
    intent = safety.detect_intent(msg.text)
    if risk == "high":
        return {
            "type":"crisis",
            "message":"If you are in immediate danger, call emergency services. Here are helplines.",
            "helplines": safety.get_local_helplines()
        }
    resp = llm.get_response(msg.text, intent=intent)
    return {"type":"ok","message":resp,"intent":intent}
