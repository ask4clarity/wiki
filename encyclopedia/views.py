from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django import forms
from markdown2 import Markdown


from . import util

class NewPage(forms.Form):
	title = forms.CharField()


def index(request):
	entries = util.list_entries()
	return render(request, "encyclopedia/index.html", {
    	"entries": entries,
    })   	


def title(request, title):
	if util.get_entry(title) == None:
		return HttpResponse("Entry not found!")
	else:
		return render(request, "encyclopedia/title.html", {
			"info": util.get_entry(title),
			"title": title
		})

def results(request):
	entries = util.list_entries()
	search = request.GET
	for entry in entries:
		if search["q"] == entry:
			return render(request, "encyclopedia/title.html", {
				"info": util.get_entry(entry),
				"title": entry
			})
		
	return render(request, "encyclopedia/results.html", {
		"entries": entries,
		"search": search["q"]
	})

def new_page(request):
	entries = util.list_entries()
	if request.method == "POST":
		form = request.POST
		title = form["title"]
		content = form["content"]
		for entry in entries:
			if title == entry:
				return HttpResponse("Entry already exists!")
		util.save_entry(title, content)
		return render(request, "encyclopedia/title.html", {
			"info": util.get_entry(title),
			"title": title
		})

	return render(request, "encyclopedia/new_page.html", {
		"form": NewPage()
	})

def edit(request, title):
	if request.method == "POST":
		form = request.POST
		content = form["content"]
		util.save_entry(title, content)
		return render(request, "encyclopedia/title.html", {
			"info": content,
			"title": title
		})

	return render(request, "encyclopedia/edit.html", {
		"info": util.get_entry(title),
		"name": title
	})

