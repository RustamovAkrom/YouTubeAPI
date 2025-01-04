from .create import * # noqa
from .delete import * # noqa
from .update import * # noqa
from .follow import * # noqa
from .unfollow import * # noqa

import graphene


class Mutation(graphene.ObjectType):
    create_channel = CreateChannel.Field()
    update_channel = UpdateChannel.Field()
    delete_channel = DeleteChannel.Field()
    subscribe_to_channel = SubscribeToChannel.Field()
    unsubscribe_from_channel = UnsubscribeFromChannel.Field()


__all__ = ("Mutation", )
