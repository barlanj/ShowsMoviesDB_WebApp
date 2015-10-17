$("#form-add-entry").validate({
	rules : {
		'input-title' : {
			required : true,
			maxlength : 255,
		},
		'input-length' : {
			required : true,
			min : 0,
			max : 999,
			digits : true
		}
	}
});
