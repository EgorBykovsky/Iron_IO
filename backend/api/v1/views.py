from rest_framework.views import APIView
from rest_framework.response import  Response
from chat.models import Chat
from session.models import  Session
from users.models import  User


from .serializers import SessionSerializer,  ChatSerializers, UserSerializer
from services.session_service import SessionServices

class Session_Api(APIView):
    
    def post (self, request):
        #Создане игровой сессии
        sessionSerializer = SessionSerializer(data=request.data)
        
        if sessionSerializer.is_valid():
            sessionSerializer.save()
            return Response(status=201)
            
        else:
            return Response(status=400)  
        
    def put(self, request, session_id):
        #Обновленеи сессии
        try:
            # Получаем экземпляр игровой сессии по переданному идентификатору
            session = SessionServices.get_session_by_id(session_id)
        except Session.DoesNotExist:
            # Если сессия с указанным идентификатором не найдена, возвращаем ошибку клиента
            return Response(status=404)
        
        # Создаем экземпляр сериализатора для игровой сессии с полученными данными
        session = SessionSerializer(instance=session, data=request.data)
        
        # Проверяем, являются ли данные в запросе допустимыми
        if session.is_valid():
            # Сохраняем обновленные данные, включая перезапись поля word
            session.save()
            # Возвращаем успешный статус обновления (HTTP 200)
            return Response(status=200)
        else:
            # Если данные недопустимы, возвращаем ошибку клиента (HTTP 400)
            return Response(status=400)

class Chat_API(APIView):
    
    def get(self, request):
        session_id = request.GET.get("session_id")
        chat = Chat.objects.filter(session_id=session_id)
        serializer = ChatSerializers(chat, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        session_id = request.data.get("session_id")
        dialog = ChatSerializers(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user, session_id=session_id)
            return Response(status=201)
        else:
            return Response(status=400)       
     
class Add_user_to_session_api(APIView):      
    
    def post(self, request):
        session_uuid = request.data.get('session_uuid')  # Получаем UUID сессии из запроса
        user_uuid = request.data.get('user_uuid')  # Получаем UUID пользователя из запроса
        
        try:
            session = Session.objects.get(uuid=session_uuid)  # Получаем сессию по UUID
        except Session.DoesNotExist:
            return Response({"error": "Session does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        # Проверяем, существует ли пользователь
        try:
            user = User.objects.get(uuid=user_uuid)
        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        # Проверяем, что пользователь не является создателем сессии
        if user.uuid == session.creator.uuid:
            return Response({"error": "User is the creator of the session"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Проверяем, что пользователь еще не добавлен в эту сессию
        if user.session == session:
            return Response({"error": "User is already added to the session"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Добавляем пользователя в сессию
        user.session = session
        user.save()
        
        return Response(status=status.HTTP_201_CREATED)