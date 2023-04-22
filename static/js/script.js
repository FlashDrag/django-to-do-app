const todoList = $(".todo-list");
const todoListItems = $(".todo-list li");

todoListItems.each(function(index) {
    if ($(this).data('item_done') === 'True') {
        $(this).addClass('completed');
        $(this).find('input[type="checkbox"]').prop('checked', true);
    }
});


todoList.on('change', '.checkbox', function (e) {
    const id = $(this).closest("li").data('item_id');
    location.href = `/toggle/${id}`
});
