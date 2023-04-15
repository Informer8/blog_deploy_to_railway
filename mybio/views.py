from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import Post, Comment, Category
from .forms import CommentForm, ContactForm
from django.db.models import Count

# Create your views here.
def home_page(request):
	post = Post.objects.filter(status=1).order_by('-dateTime')
	new_contact = None
	if request.method == 'POST':
		contact_form = ContactForm(data=request.POST)
		if contact_form.is_valid():
			new_contact = contact_form.save(commit=False)
			new_contact.save()
			contact_form = ContactForm()
			return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
	else:
		contact_form = ContactForm()

	context={
		'query' : post,
		'contact_form': contact_form
	}
	return render(request, "bio.html", context)

def detail(request, slug):
	post_qs  	= Post.objects.filter(status=1, slug=slug)
	single_post = Post.objects.get(status=1, slug=slug)
	try:
		next_post = single_post.get_next_by_dateTime()
	except single_post.DoesNotExist:
		next_post = None
	try:
		previous_post = single_post.get_previous_by_dateTime()
	except single_post.DoesNotExist:
		previous_post = None
	categories  = Category.objects.all().annotate(posts_count=Count('name'))

	new_comment = None
	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = single_post
			new_comment.save()
			comment_form = CommentForm()
			return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
	else:
		comment_form = CommentForm()

	context	= {
		'qs' 	  : post_qs,
		'prevpost': previous_post,
		'nextpost': next_post,
		'new_comment': new_comment,
		'comment_form': comment_form,
		'categories'  : categories
	}
	return render(request, "post.html", context)

def CategoryView(request, tags):
	slug = Category.objects.get(slug=tags)
	category_posts = Post.objects.filter(status=1, category=slug)
	category_name = Category.objects.get(name=slug)
	
	context = {
		'tags': category_name,
		'category_posts': category_posts
	}
	return render(request, 'categories.html', context)

def error_page(request, exception):
	return render(request, '404.html')