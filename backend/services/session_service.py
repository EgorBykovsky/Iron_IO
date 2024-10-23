from repositories.session import  SessionRepository
from session.models import Session
import uuid

class SessionServices:
    def  __init__(self, session_repository:SessionRepository):
        self._session_repository = session_repository
        
    async def create_session(self, creator_id):
        session_uuid = uuid.uuid4()
        game_session = Session(uuid=session_uuid, creator_id=creator_id)
        return await self._session_repository.create_session(game_session)
    
    async def get_all_sessions(self):
        return await self._session_repository.get_all_sessions()
    
    async def get_session_by_id(self, id : str):
        if not (await self._is_valid_id(id)):
            raise ValueError("Invalid ID")
        return await self._session_repository.get_session_by_id(id)
       