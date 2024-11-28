from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm

def publish_feedback(request):
    feedbacks = Feedback.objects.filter(approved=True, published=True).order_by('-created_at')
    
    return render(request, 'feedback/feedback.html', {'feedbacks': feedbacks})
    
def send_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.approved = False
            feedback.published = False
            feedback.save()
            return redirect('feedback_sent')
    else:
        form = FeedbackForm()
        
    return render(request, 'feedback/send_feedback.html', {'form': form})

def feedback_sent(request):
    return render(request, 'feedback/feedback_sent.html')