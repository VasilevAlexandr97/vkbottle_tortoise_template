from vk_bot.database.models.user import User
from vkbottle import BaseMiddleware
from vkbottle.bot import Message


class RegistrationMiddleware(BaseMiddleware[Message]):
    async def pre(self) -> dict:
        user_data = await self.event.get_user()
        user, _ = await User.get_or_create(vk_id=self.event.from_id,
                                           defaults=dict())
        self.send({"user": user})
