
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView

from cms.models import Book, Impression
from cms.forms import BookForm, ImpressionForm


class ImpressionList(ListView):
    context_object_name = 'impressions'
    template_name = 'cms/impression_list.html'
    paginate_by = 2  # 1ページ最大2件ずつページング

    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['book_id'])  # 親書籍
        impressions = book.impressions.all().order_by('id')  # 書籍の子の感想
        self.object_list = impressions

        context = self.get_context_data(object_list=self.object_list, book=book)
        return self.render_to_response(context)

# Create your views here.
def book_list(request):
    # return HttpResponse('書籍の一覧')
    books = Book.objects.all().order_by('id')
    return render(
        request,
        'cms/book_list.html',  # 使用するテンプレート
        {'books': books})  # テンプレートに渡すデータ


def book_edit(request, book_id=None):
    if book_id:  # mod
        book = get_object_or_404(Book, pk=book_id)
    else:  # add
        book = Book()

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():  # validation
            book = form.save(commit=False)
            book.save()
            return redirect('cms:book_list')
    else:  # GET
        form = BookForm(instance=book)

    return render(request, 'cms/book_edit.html', dict(form=form, book_id=book_id))


def book_del(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('cms:book_list')


def impression_edit(request, book_id, impression_id=None):
    book = get_object_or_404(Book, pk=book_id)  # 親の書籍
    if impression_id:  # mod
        impression = get_object_or_404(Impression, pk=impression_id)
    else:  # add
        impression = Impression()
    
    if request.method == 'POST':
        form = ImpressionForm(request.POST, instance=impression)  # POSTされたrequestデータからフォームを作成
        if form.is_valid():
            impression = form.save(commit=False)
            impression.book = book
            impression.save()
            return redirect('cms:impression_list', book_id=book_id)
    else:  # GET
        form = ImpressionForm(instance=impression)  # impressionインスタンスからフォームを作成
    
    return render(
        request,
        'cms/impression_edit.html',
        dict(form=form, book_id=book_id, impression_id=impression_id))


def impression_del(request, book_id, impression_id):
    impression = get_object_or_404(Impression, pk=impression_id)
    impression.delete()
    return redirect('cms:impression_list', book_id=book_id)
