from django.shortcuts import render,redirect
from fcuser.models import Fcuser
from django.http import Http404
from .models import Board
from .forms import BoardForm

# Create your views here.
def board_detail(request, pk):
  
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')

    return render(request, 'detail.html', {'board': board})

def board_list(request):
    boards = Board.objects.all().order_by('-id')
    return render(request, 'list.html', {'boards': boards})

def board_post(request):

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)

            

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()
            return redirect('/board/list')
    else:
        form= BoardForm()

    return render(request, 'post.html', {'form': form})