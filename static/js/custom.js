//namespace
var my_name_space = my_name_space || {};
my_name_space.ma = my_name_space.ma || {};

my_name_space.ma.editing = false;

my_name_space.ma.enableButtons = function() {
	$("#toggle-edit").click( function() {
		$("label").remove(".error");
		
		if(my_name_space.ma.editing) {
			my_name_space.ma.editing = false;
			$(".edit-actions").addClass("hidden");
			$(this).html("Edit");
		} else {
			my_name_space.ma.editing = true;
			$(".edit-actions").removeClass("hidden");
			$(this).html("Done");
		}
	});
	
	$("#add-entry-link").click( function() {
		console.log("Adding?");
		$("#entry-modal .modal-title").html("Add a new entry!");
		$("#entry-modal button[type=submit]").html("Add Entry");
		
		$("#entry-modal input[name=input-title]").val("");
		$("#entry-modal input[name=input-category]").prop("checked", false);
		$("#entry-modal input[name=input-length]").val("");
		$("#entry-modal input[name=input-rating]").val("1");
		$("#entry-modal input[name=entity_key]").val("").prop("disabled", true);
	});
	
	$(".edit-movie-entry").click( function () {
		entityKey = $(this).find(".entity-key").html();
		$("#entry-modal input[name=entity_key]").val(entityKey).prop("disabled", false);
		
		$("#entry-modal .modal-title").html("Edit entry");
		$("#entry-modal button[type=submit]").html("Update");
		
		title = $(this).find(".hidden-title").html();
		category = $(this).find(".hidden-category-item");
		length = $(this).find(".hidden-length").html();
		rating = $(this).find(".hidden-rating").html();
		type = $(this).find(".hidden-type");

		$("#entry-modal input[name=input-title]").val(title);
		
		$(category).each( function() {
			value = $(this).html();
			entity = "#entry-modal input[value='" + value + "']";
			$(entity).prop("checked", true);
		});

		$("#entry-modal input[name=input-length]").val(length);

		$("#entry-modal select[name=input-rating]").val(rating).prop("selected", true);
		
		$(type).each( function() {
			value = $(this).html();
			entity = "#entry-modal input[value='" + value + "']";
			$(entity).prop("checked", true);
		});
		

	});
	
	$(".delete-movie-entry").click( function() {
		entityKey = $(this).find(".entity-key").html();
		$("#delete-modal input[name=entity_key]").val(entityKey);
	})
};

my_name_space.ma.AttachEventHandlers = function() {
	$("#entry-modal").on('shown.bs.modal', function() {
		$("input[name=input-title]").focus();
	});
};

$(document).ready( function() {
	my_name_space.ma.enableButtons();
	my_name_space.ma.AttachEventHandlers();
});
