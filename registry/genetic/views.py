from django.shortcuts import render_to_response

def entry(request):
    return render_to_response("genetic/variation/index.html")
