$(function() {	
	prettyPrint();
	
	$rep = $('.impl-reputation').data('reputation_value');
	if($rep != null){$rep = $rep.substring(1, 5);}
	$('.impl-reputation').html('Reputation : <img src="/algorithm/static/images/glyphicons/glyphicons_048_dislikes.png" alt="" />');
	//var star_0 = "<img src='/algorithm/static/images/glyphicons/glyphicons_048_dislikes.png' alt='"+$rep+"'  width='22' height='22'/>";
	//var star_1 = "<img src='/algorithm/static/images/glyphicons/glyphicons_049_star.png' alt='"+$rep+"' width='22' height='22' />";
	var star_0 = "";
	var star_1 = "<img src='/algorithm/static/images/glyphicons/star.png' alt='"+$rep+"' width='22' height='22'/>";
	
	if($rep == 0.0){
		$('.impl-reputation').html('Reputation : 0.0 '+ star_0 + star_0 + star_0 + star_0+ star_0);
	}else if($rep <= 0.2){
		$('.impl-reputation').html('Reputation : '+ star_1 + star_0 + star_0 + star_0+ star_0);
	}else if(0.2 <= $rep < 0.4){
		$('.impl-reputation').html('Reputation : '+ star_1 + star_1 + star_0 + star_0+ star_0);
	}else if(0.4 <= $rep < 0.6){
		$('.impl-reputation').html('Reputation : '+star_1 + star_1 + star_1 + star_0+ star_0);
	}else if(0.6 <= $rep < 0.8){
		$('.impl-reputation').html('Reputation : '+ star_1 + star_1 + star_1 + star_1+ star_0);
	}else if(0.8 <= $rep < 1.0){
		$('.impl-reputation').html('Reputation : '+ star_1 + star_1 + star_1 + star_1+ star_1);
	}
	$(".impl-reputation").mouseover(function () {
		return overlib(""+$rep+"", ABOVE);
	});
	$(".impl-reputation").mouseout(function () {
		return nd();
	});
	tinyMCE.init({
		// General options
		mode : "textareas",
		plugins : "",
		
		// Theme options
		theme_advanced_buttons1 : "",
	});

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
});