$(document).ready(function() {  
        function onBlur() {
        	document.body.className = 'blurred';
        	$.ajax({
                url: '/requests/',
                type: 'GET',
                data: {'status': "blurred"},
                traditional: true,
                cache: false
            });
        }
        
        function onFocus(){
        	document.body.className = 'focused';
        	$.ajax({
                url: '/requests/',
                type: 'GET',
                data: {'status': "focused"},
                traditional: true,
                cache: false
            });
        }
        
        if (/*@cc_on!@*/false) { // check for Internet Explorer
        	document.onfocusin = onFocus;
        	document.onfocusout = onBlur;
        } else {
        	window.onfocus = onFocus;
        	window.onblur = onBlur;
        }
});
