from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Novel
from .forms import NovelForm

def novel_list(request):
    novels = Novel.objects.all()
    return render(request, 'novel_list.html', {'novels': novels})

class NovelCreateView(CreateView):
    model = Novel
    form_class = NovelForm
    success_url = '/novels/'

class NovelUpdateView(UpdateView):
    model = Novel
    form_class = NovelForm
    template_name_suffix = '_update_form'  # Optional: Customize template name
    success_url = '/novels/'

class NovelDeleteView(DeleteView):
    model = Novel
    success_url = '/novels/'


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