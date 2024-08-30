from django.shortcuts import render, redirect
from .models import Novel, Contact
from .forms import NovelForm, ContactForm, ContactForm1


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

#contact form frormed from forms.Form, require cleaning
def contact(request):
  form = ContactForm()
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      Contact.objects.create(
        name=form.cleaned_data['name'],
        email=form.cleaned_data['email'],
        subject=form.cleaned_data['subject'],
        message=form.cleaned_data['message'],
        subscribe=form.cleaned_data['subscribe'],
      )
      return render(request, 'success.html', { 'name':form.cleaned_data['name'] })
  else:
    form = ContactForm()
  return render(request, 'contact.html', { 'form':form })

#contact form formed from forms.ModelForm, no cleaning required
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm1(request.POST)
        if form.is_valid():
            form.save()  # This saves the form data directly to the database
            return render(request, 'success.html', { 'form':form})  # Replace 'success_url' with the URL you want to redirect to
    else:
        form = ContactForm1()
    
    return render(request, 'contact1.html', {'form': form})
