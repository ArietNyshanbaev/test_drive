from .models import Category, Blog, Coment
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
# Create your views here.
def mainpage(request):
	"""This is the main page or so called root page"""
	#initialize variables
	args={}
	args.update(csrf(request))

	if request.POST:
		title = request.POST['title']
		description = request.POST['description']
		body = request.POST['body']
		category = request.POST['category']

		category = get_object_or_404(Category, pk=category)

		new_post = Blog.objects.create(title=title, description=description, body=body, category=category)
		new_post.save()
	
	categories = Category.objects.all()
	last_posts = Blog.objects.all().order_by('-created')[:15]
	args['last_posts'] = last_posts
	args['categories'] = categories
	
	return render_to_response('blog/mainpage.html',args)

def by_category(request, category_id):
	"""return rendered blogs page for particular category"""
	#initialize variables
	args={}

	#getting data form models
	this_category = get_object_or_404(Category, pk=category_id)
	categories = Category.objects.all().exclude(pk=category_id).order_by('category')
	posts = Blog.objects.filter(category=this_category)
	#sort news by date so that last news pop up first
	#context data initialization into dictionary 'args'
	args['this_category'] = this_category
	args['categories'] = categories
	args['posts'] = posts


	return render_to_response('blog/by_categories.html',args)

def post_info(request, post_id):
	"""return rendered blogs page with more info for particular post"""
	#initialize variables
	args={}
	args.update(csrf(request))
	this_post = get_object_or_404(Blog, pk=post_id)
	coments = Coment.objects.filter(blog=this_post)
	if request.POST:
		coment = request.POST['coment']
		new_coment = Coment.objects.create(coment=coment,blog=this_post)
		new_coment.save()
	#getting data form models
	args['this_post'] = this_post
	args['coments'] = coments


	return render_to_response('blog/post_info.html',args)


	


	