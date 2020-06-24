
window.onload=function(){

var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
output.innerHTML = slider.value;


slider.oninput = function() {
  output.innerHTML = this.value;
}
editor = CodeMirror.fromTextArea(document.getElementById("code"), {
        
        lineNumbers: true,
        matchBrackets: true,
        continueComments: "Enter",
        extraKeys: {"Ctrl-Q": "toggleComment"}
      });
      //.log("code");
editor.setValue("");
}

