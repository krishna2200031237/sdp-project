from django.shortcuts import render, redirect

from DjangoProjects.TTM.review.forms import ReviewForm
from DjangoProjects.TTM.review.models import TouristReview


# Create your views here.



def review_list(request):
    if request.method == 'GET':
        reviews = TouristReview.objects.all()
        return render(request,'reviewpage.html', {'review':reviews})





def add_review(request):
    if request.method == 'POST' :
        form = ReviewForm(request.POST,request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user=request.user
            review.save()
            return redirect('review_list')
        else:
            form = ReviewForm()

        return render(request, 'reviewpage.html', {'form':form})

