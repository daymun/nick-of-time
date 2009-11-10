/*
*
* nickoftime_core.js
*  Core functions for the Nick-Of-Time pages
*
*/

/* Toggle the status message
----------------------------------*/
function showMessage(msg) {
  // Toggle the display of the message
  $('#messageText').html(msg);
  $('#message').show();
}

function hideMessage(){
  $('#message').hide();
}

/* Toggle the error message
----------------------------------*/
function showErrorMessage(msg) {
  // Toggle the display of the error message
  $('#errorMessageText').html(msg);
  $('#errorMessage').show();
}

function hideErrorMessage(){
  $('#errorMessage').hide();
}
      
/* Validate the data elements
----------------------------------*/
function validateTimeEntryForm(){

  // Validate a title was provided
  if ($('#title').val() == "")
  {
    showErrorMessage("Please enter a title for your task...");
    $('#title').focus();
    return false;
  }
  
  // Validate some code was supplied
  if ($('#task').val() == "")
  {
    showErrorMessage("Please enter at least <b>one</b> bit of information detailing the task...");
    return false;
  }
  
  // If the description is blank, confirm that the user does not want to provide a description
  
  
  // Success
  return true;
}

/* Save the TimeEntry
----------------------------------*/
function saveTimeEntry(){
  // Attempt to save the tool via Ajax
  var options = { 
        success:       callbackSaveTimeEntry, // post-submit callback 
        url:           '/',                 // override for form's 'action' attribute 
        type:          'post',                // 'get' or 'post', override for form's 'method' attribute 
        beforeSubmit:   showRequest,      // pre-submit callback 
        dataType:      'json'                 // 'xml', 'script', or 'json' (expected server response type) 

        // other available options: 
        //target:         '#output2',       // target element(s) to be updated with server response 
        //clearForm:      true              // clear all form fields after successful submit 
        //resetForm:      true              // reset the form after successful submit 
        // $.ajax options can be used here too, for example: 
        //timeout:   3000 
    };
  $('#dasform').ajaxSubmit(options);
}

/* Process the save of the form
----------------------------------*/
function callbackSaveTimeEntry(responseText, statusText){

  var jsonReturn = eval(responseText);
  alert(responseText);
  
  // jsonReturn is the JSON encoded return information
  if (jsonReturn.haserror)
  {
    showErrorMessage(jsonReturn.message);
  }
  else
  {
    // Success .. save the tool key
    $('#timekey').val(jsonReturn.timekey);
    showMessage(jsonReturn.message);
  } 
}

function showRequest(formData, jqForm, options) { 
    // formData is an array; here we use $.param to convert it to a string to display it 
    // but the form plugin does this for you automatically when it submits the data 
    var queryString = $.param(formData); 
 
    // jqForm is a jQuery object encapsulating the form element.  To access the 
    // DOM element for the form do this: 
    // var formElement = jqForm[0]; 
 
    alert('About to submit: \n\n' + queryString); 
 
    // here we could return false to prevent the form from being submitted; 
    // returning anything other than false will allow the form submit to continue 
    return true; 
}