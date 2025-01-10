from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from boto3.dynamodb.conditions import Key
from django.conf import settings

class VideoPlaylistAPIView(APIView):
    def get(self, request, user_id, *args, **kwargs):
        # Query DynamoDB table for the user playlist
        try:
            response = settings.video_playlist_table.query(
                KeyConditionExpression=Key('user_id').eq(user_id)
            )
            videos = response.get('Items', [])
            
            # If no videos are found, return an empty list
            if not videos:
                return Response({'message': 'No videos found in the playlist'}, status=status.HTTP_404_NOT_FOUND)
            
            # Return the video data
            return Response({'videos': videos}, status=status.HTTP_200_OK)
        
        except (NoCredentialsError, PartialCredentialsError):
            return Response({'error': 'Invalid AWS credentials'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
