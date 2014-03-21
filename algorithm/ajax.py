from algorithm.forms import TagForm
from algorithm.models import Implementation
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from inoa.http.responses import JsonResponse


@login_required
def moderator_add(request):
	user = request.user
	g = Group.objects.get(name='Moderator')
	g.user_set.add(user)
	return JsonResponse({'success': True})

@login_required
@user_passes_test(lambda u: u.is_moderator(), login_url='/access_denied/')
def moderator_action(request):
	action = request.POST.get('action')
	imp_id = request.POST.get('implementation_id')

	implementation = get_object_or_404(Implementation, id=imp_id)

	if action == 'accept':
		implementation.visible = True
		implementation.save()
	elif action == 'refuse':
		implementation.delete()

	return JsonResponse({'success': True})

@login_required
def tag_add(request):
	ctx = {'success': True}
	form = TagForm(request.POST)
	if form.is_valid():
		tag = form.save()
		ctx['tag'] = {'id': tag.id, 'name': tag.name}
	else:
		ctx['success'] = False
		ctx['errors'] = form.errors

	return JsonResponse(ctx)
