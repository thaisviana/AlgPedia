$(function() {
	$('.js-login-link').click(function(ev){
		ev.preventDefault();
		var next = location.pathname;
		window.location.href = $(this).attr('href') + '?next=' + next;
	});

	prettyPrint();

	$('.user-reputation').each(function() {
		$rep = $(this).data('reputation_value');
		if($rep != null){$rep = $rep.substring(1, 7);}
		$(this).mouseover(function () {
			var val;
			if($(this).data('reputation_value') != "#"){
				val = $(this).data('reputation_value').substring(1, 7);
			} else {
				val = "Not evaluated yet";
			}
			return overlib(val, ABOVE);
		});
		$(this).mouseout(function () {
			return nd();
		});
	});

	$('.impl-reputation').each(function() {
		$rep = $(this).data('reputation_value');
		if($rep != null){$rep = $rep.substring(1, 7);}
		$(this).mouseover(function () {
			var val;
			if($(this).data('reputation_value') != "#"){
				val = $(this).data('reputation_value').substring(1, 7);
			} else {
				val = "Not evaluated yet";
			}
			return overlib(val, ABOVE);
		});
		$(this).mouseout(function () {
			return nd();
		});

		var star_0 = ""
		var star_1 = ""

		var img;
		$rep = parseFloat($rep);
		if($rep == 0 || isNaN($rep)){
			img = star_0 + star_0 + star_0 + star_0+ star_0;
		}else if($rep < 0.2){
			img = star_1 + star_0 + star_0 + star_0+ star_0;
		}else if(0.2 <= $rep && $rep < 0.4){
			img = star_1 + star_1 + star_0 + star_0+ star_0;
		}else if(0.4 <= $rep && $rep < 0.6){
			img = star_1 + star_1 + star_1 + star_0+ star_0;
		}else if(0.6 <= $rep && $rep < 0.8){
			img = star_1 + star_1 + star_1 + star_1+ star_0;
		}else if(0.8 <= $rep){
			img = star_1 + star_1 + star_1 + star_1+ star_1;
		}
		$(this).html(img);
	});

	// tinyMCE.init({
	// 	// General options
	// 	mode : "textareas",
	// 	plugins : "",
    //
	// 	// Theme options
	// 	theme_advanced_buttons1 : "",
	// });

	$("#logout").click(function(event) {
		event.preventDefault();
		bootbox.alert("Thank you for using AlgPedia.");
		setTimeout(function () {
			document.location.href = $("#logout").attr('href'); // redireciona pra url nova
        }, 1000);

	});


	$("#add_implementation").click(function(){
		if($('#logged').val()== 'false'){
			bootbox.alert("You have to login first");
		}else{
			var form = document.forms[0];
			var alg_id = form['algorithm_id'].value;
			window.location = "/add/alg/id/"+alg_id;
		}
	});

	$('.textarea').wysihtml5();

	$('.signup').click(function() {
		bootbox.alert("Thank you for registering.");
		$( "form:first" ).submit();
	});

	$("#add_algorithm").click(function() {
		event.preventDefault();
		if($('#logged').val()== 'false'){
			bootbox.alert("You have to login first");
		}else{
			var form = document.forms[0];
			var classification_id = form['classification_id'].value;

			window.location = "/add/cat/id/"+classification_id;
		}
	});
	$("#add_algorithm").mouseover(function () {
		return overlib("Add an algorithm", ABOVE);
	});
	$("#add_algorithm").mouseout(function () {
		return nd();
	});
	$("#add_implementation").mouseover(function () {
		return overlib("Add implementation", ABOVE);
	});
	$("#add_implementation").mouseout(function () {
		return nd();
	});
	//$("#add_evaluation").mouseover(function () {
	$(".add_evaluation").mouseover(function () {
		return overlib("Add implementation evaluation", ABOVE);
	});
	//$("#add_evaluation").mouseout(function () {
	$(".add_evaluation").mouseout(function () {
		return nd();
	});
	$("#rdf").mouseover(function () {
		return overlib("This content is available in RDF", ABOVE);
	});
	$("#rdf").mouseout(function () {
		return nd();
	});
	$(".js-accept").mouseover(function () {
		return overlib("Accept Implementation", ABOVE);
	});
	$(".js-accept").mouseout(function () {
		return nd();
	});
	$(".js-refuse").mouseover(function () {
		return overlib("Refuse Implementation", ABOVE);
	});
	$(".js-refuse").mouseout(function () {
		return nd();
	});

	$.widget("custom.catcomplete", $.ui.autocomplete, {
		_renderMenu: function( ul, items ) {
			var that = this,
			currentCategory = "";
			$.each( items, function( index, item ) {
				if ( item.category != currentCategory ) {
					ul.append( "<li class='ui-autocomplete-category'>" + item.category_label + "</li>" );
					currentCategory = item.category;
				}
				that._renderItemData( ul, item );
			});
		}
	});
	$(".search-input").catcomplete({
		source : url_global_search_autocomplete,
		minLength : 2,
		select : function(event, ui) {
			window.location.href = ui.item.url;
		},
		focus: function( event, ui ) {
			event.preventDefault();
		}
	});
});
