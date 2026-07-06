function ArticleComment(ArticleId) {
    var message = $('#article_comment').val()
    if (message !== ''){
        var parent_id = $('#parent').val()
    $.get('/article/comments', {
        'article_id': ArticleId,
        'message': message,
        'parent_id': parent_id
    }).then(res => {
        $('#comments').html(res)
        $('#article_comment').val('')
        $('#parent').val('')
    })
    }
}


function Parent(ParentId) {
    $('#parent').val(ParentId)
    document.getElementById('scroll').scrollIntoView({behavior: 'smooth'})
}


function AddToOrder(ProductId, Status) {
    var count = $('#product_count').val()
    if (Status !== 'detail') {
        count = 1
    }
    if (count > 10 || count < 1) {
        count = 1
    }
    $.get('/user-basket/add-to-order', {
        'product_id': ProductId,
        'count': count
    })
}


function DeleteOrder(ProductId) {
    $.get('/user-basket/delete-order', {
        'product_id': ProductId,
    }).then(res => {
        $('#order_items').html(res)
    })
}


function ChangeCount(ProductId, Status) {
    $.get('/user-basket/change-count', {
        'product_id': ProductId,
        'status': Status
    }).then(res => {
        $('#order_items').html(res)
    })
}


function ProductImages(Value){
    $('#original_photo').attr('src',Value)
    $('#large_image').attr('href',Value)
}


function PriceFilter(){
    var start_price=$('#sl2').val().split(',')[0]
    var end_price=$('#sl2').val().split(',')[1]
    $('#start_price').val(start_price)
    $('#end_price').val(end_price)
    $('#filter_form').submit()
}


function FillPage(PageNumber){
    $('#page').val(PageNumber)
    $('#filter_form').submit()
}