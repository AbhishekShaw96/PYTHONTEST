# frontend_app/views.py

from django.shortcuts import render

def login_view(request):
    if request.method == 'POST':
        # Handle POST request for login, but for now just render the page
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Normally here you would call the auth-service API, but for now, we just skip this part.
        return render(request, 'login.html', {'message': 'Login successful!'})

    return render(request, 'login.html')


def playlist_view(request):
    # Normally you would call the video-service API here, but we'll skip that too.
    # For now, just render the playlist page directly.
    
    videos = [
        {"title": "Video 1", "url": "#"},
        {"title": "Video 2", "url": "#"},
        {"title": "Video 3", "url": "#"},
    ]
    
    return render(request, 'playlist.html', {'videos': videos})
