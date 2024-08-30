from django.shortcuts import render, redirect
from .models import Novel
from .forms import NovelForm


# views
  ##`Home Page `
def main(request):
  return render(request, 'main.html')

   ##novels list page
def novel_list(request):
  novels = Novel.objects.all()
  context = {'novels':novels}
  return render(request, 'novel_list.html', context)

  ##all novel details page
def all_detail(request):
  novels = Novel.objects.all()
  context = {'novels':novels}
  return render(request, 'all_detail.html', context)

  ## novel details
def novel_datail(request):
  novels = Novel.objects.all()
  context = {'novels':novels}
  return render(request, 'novel_detail.html', context)

##single novel details
def novel_details(request, id):
    novel = Novel.objects.get(id=id)
    context = {'novel': novel} 
    return render(request, 'novel_detail.html', context)

##Add Novels
def add_novel_form(request):
  form = NovelForm()
  if request.method == "POST":
    form = NovelForm(request.POST, request.FILES)
    if form.is_valid():
      # Extract data from the validated form
      novel_data = form.cleaned_data
      # Create a new novel object with the extracted data
      new_novel = Novel.objects.create(
        title=novel_data['title'],
        author=novel_data['author'],
        genre = novel_data['genre'],
        description=novel_data['description'],
        published_date=novel_data['published_date'],
        edition=novel_data['edition'],
        bnanner =novel_data['bnanner']
      )
      new_novel.save()
      return redirect('librarystore:novel_list')
  else:
    form = NovelForm()
  return render(request, 'add.html', {  'form':form })
