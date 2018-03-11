from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from .forms import UploadFileForm

from .models import ProposedLink

def add_links(f):
    message = ""
    for row in f:
        r = row.decode("utf-8").split(",")
        if len(r) != 9:
            message += ("malformed_line: %s\n" % row)
        un, s1id, s2id, s1pos, s2pos = r[0], r[1], r[2], r[3], r[4]
        s1words, s2words, s1def, s2def = r[5], r[6], r[7], r[8],
        l = ProposedLink(assigned_user=un, synset1id=int(s1id), synset2id=int(s2id), synset1pos=s1pos, synset2pos=s2pos,
                         synset1words=s1words, synset2words=s2words, synset1def=s1def, synset2def=s2def)
        l.save()
    if message:
        return message
    return "upload sucsessful"

def upload_file(request):
    user = request.user
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        message = add_links(myfile)
        return render(request, 'linker/upload.html', {
            'last_link': message
        })
    return render(request, 'linker/upload.html')

def link(request):
    user = request.user
    if not user.is_authenticated:
        return render(request, 'linker/evaluate.html', {
            'user': user,
            'error_message': "no such user",
        })
    return get_link(request, user)

def get_link(request, user):
    try:
        link = ProposedLink.objects.filter(assigned_user=user.username, link_weight=0)[0]
    except (KeyError, IndexError):
        return render(request, 'linker/evaluate.html', {
            'user': user,
            'error_message': "No more links to evaluate for this user",
        })
    else :
        context = {
            "user": user,
            "s1": link.synset1(),
            "s2": link.synset2()
        }
        return render(request, 'linker/evaluate.html', context)

def rate_link(request, s1id, s2id, rating):
    user = request.user
    if not user.is_authenticated:
        return render(request, 'linker/evaluate.html', {
            'user': user,
            'error_message': "no such user",
        })
    if rating < 0:
        return render(request, 'linker/evaluate.html', {
            'user': user,
            'error_message': "invalid rating value",
        })
    try:
        possible_link = get_object_or_404(ProposedLink, assigned_user=user.username, synset1id=s1id, synset2id=s2id)
        possible_link.assign_weight(rating)
    except (KeyError, ProposedLink.DoesNotExist):
        return render(request, 'linker/evaluate.html', {
            'user': user,
            'error_message': "no such propossed link",
        })
    return get_link(request, user)