from django.shortcuts import redirect, render, HttpResponse
from main import forms, models

# Create your views here.
def home(request):
    polls = models.Poll.objects.all()
    context = {
        'polls': polls
    }
    return render( request, 'main/home.html', context)

def create(request):
    if request.method == "POST":
        form = forms.CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.CreatePollForm()

    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)

def vote(request, pk):
    poll = models.Poll.objects.get(pk=pk)
    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option_one':
            poll.option_one_count += 1
        elif selected_option == 'option_two':
            poll.option_two_count += 1
        elif selected_option == 'option_three':
            poll.option_three_count += 1
        elif selected_option == 'option_four':
            poll.option_four_count += 1
        else: return HttpResponse(400, 'Please select option!')

        poll.save()
        return redirect('result', pk)

    context = {
        'poll': poll
    }
    return render( request, 'main/vote.html', context)

def results(request, pk):
    poll = models.Poll.objects.get(pk=pk)
    context = {
        'poll': poll
    }
    return render( request, 'main/results.html', context)