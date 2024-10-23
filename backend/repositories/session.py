from session.models import Session
import abc

class AbstractSessionRepository(abc.ABC):
    @abc.abstractmethod
    def create_session(self: 'AbstractSessionRepository', **data):
        return 
    
    @abc.abstractmethod
    def get_all_sessions(self: 'AbstractSessionRepository'):
        return   
    
    @abc.abstractmethod
    def get_session_by_id(self: 'AbstractSessionRepository', id):
        return  
    
class SessionRepository(AbstractSessionRepository):
    def create_session(self: AbstractSessionRepository, **data):
        return Session.objects.create(**data)
    
    def get_all_sessions(self: AbstractSessionRepository):
        return super().get_all_sessions()
    
    def get_session_by_id(self: AbstractSessionRepository, id):
        return super().get_session_by_id(id)