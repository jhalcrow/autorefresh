function pollForRefresh(url) {
    $.get(url,'',
        function(data, textStatus, xhr) {
                window.location.reload();
            }
          );
}
