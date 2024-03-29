from django import template
from lists import models as list_models

register = template.Library()


@register.simple_tag(takes_context=True)
def on_favs(context, room):
    # context를 통해서 user정보 확인
    # print(context, room)
    user = context.request.user
    if user.is_authenticated:
        the_list = list_models.List.objects.get_or_none(
            user=user, name="My Favourites Houses"
        )
        if the_list is not None:
            # 있다면 True가 반환됨
            return room in the_list.rooms.all()
        else:
            return False
    else:
        return False
