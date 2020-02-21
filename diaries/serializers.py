from rest_framework import serializers

from alcohols.models import AlcoholRecord
from alcohols.serializers import AlcoholRecordSerializers
from diaries.models import Diary


class DiarySerializers(serializers.ModelSerializer):
    # alcohol_records = AlcoholRecordSerializers(many=True)
    # alcohol_records = PrimaryKeyRelatedField(many=True,read_only=True)
    # print(alcohol_records)
    alcohol_records = AlcoholRecordSerializers(many=True)

    class Meta:
        model = Diary

        fields = (
            'creator',
            'review',
            'date',
            'drunken_level',
            'hangover_level',
            'action_type',
            'alcohol_records',
            'action_type_img',
        )


# class DiaryAPIView(ObjectMultipleModelAPIView):
#     querylist = [
#         {'queryset': Diary.objects.all(), 'serializer_class': DiarySerializers},
#         {'queryset': AlcoholRecord.objects.all(), 'serializer_class': AlcoholRecordSerializers},
#
#     ]


'''
    class Post(models.Model):
        user = FK
        title
        content
        created_at
        updated_at


    class Comment(models.Model):
        user = FK
        post = FK


    class CommentSerializer:
        post = PostSerializer()

        class Meta:
            model = Comment
            fields = ('user', 'post', 'content', 'created_at', ..., )

    return
    {
        user: 1,
        post: {
            user: id,
            title: title,
            content: content,
            ...
        },
    }



    class PostSerializer:
        comment = CommentSerializer(Many=True)
        class Meta:
            model = Post
            fields = ('id', "user", "title", "content", ... , "comment")

    return
    {
        "user": pk
        "title": title,
        "content": content,
        "created_at": ...,
        # nested serializer
        "comment": [
            {
                "user": pk,
                "content": ...,
                "created_at": ,,,
            },
            ...
        ]
    }

    comment -> field 에 이미 post 를 가지고 있음
    post -> field 에 comment 를 가지고 있지 않음
    but, 나오게 하고 싶음
    Post : Comment = 1 : N
    --> comment 에서 post 를 fields 로 가지고 있고, related_name 걸 사용
    comment.post
    post.comment_set
    post.related_name -> post.comments.all()

    1. related name 사용
    2. 1 에 해당하는 serializer(PostSerializer) - field 를 추가적으로 declare
    3. fields 에 declare 한 field 명 그대로 추가


    '''
