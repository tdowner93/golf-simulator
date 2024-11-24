from django.shortcuts import render
from .models import Player, Club, Shot

# Create your views here.

def simulate_shot(request):
    if request.method == 'POST':
        player = Player.objects.get(id=request.POST['player_id'])
        club = Club.objects.get(id=request.POST['club_id'])
        distance = request.POST['distance']
        shot = Shot(player=player, club=club, distance=distance)
        shot.save()
        return render(request, 'golf_simulator/shot_result.html', {'shot': shot})
    return render(request, 'golf_simulator/select_shot.html')

def shot_result(request, shot_id):
    # Retrieve the shot details using the shot_id passed in the URL
    shot = Shot.objects.get(id=shot_id)

    # Pass the shot object to the template
    return render(request, 'golf_simulator/shot_result.html', {'shot': shot})