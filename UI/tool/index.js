function  calc_score()
{
  document.getElementById("score").innerHTML = "Score: "+ 10;
}

var server_addr="http://0.0.0.0:80";
function show_errors(){
  let myForm = document.getElementById('question_generator');
  let formData = new FormData(myForm);
  values = [];
  for (var value of formData.values()) {
    values.push(value);
  }
  var route="/get_error_msgs"
  var data_file = server_addr+route;
  var http_request = new XMLHttpRequest();
  var language = values[0];
  var category = values[1];
  var program = values[2];
  var file = values[3];
  var params = JSON.stringify([language, category, program, file]);
  http_request.onreadystatechange = function() {//Call a function when the state changes.
      if(http_request.readyState == 4) {
          var response = http_request.responseText;
          p = document.getElementById("error_msg");
          p.innerHTML = response;
      }
  }
  http_request.open('POST', data_file, true);
  http_request.send(params);
}
function get_file(folder){
  let myForm = document.getElementById('question_generator');
  let formData = new FormData(myForm);
  values = [];
  for (var value of formData.values()) {
    values.push(value);
  }
  var route="/get_file"
  var data_file = server_addr+route;
  var http_request = new XMLHttpRequest();
  var language = values[0];
  var category = values[1];
  var program = values[2];
  if(folder == "solution")
  {
    var params = JSON.stringify([language, category, program, folder]);
  }
  else
  {
    console.log(values[3]);
    var params = JSON.stringify([language, category, program, values[3]]);
  }
  http_request.onreadystatechange = function() {//Call a function when the state changes.
      if(http_request.readyState == 4) {
          var response = http_request.responseText;
          p = document.getElementById("codesegment");
          p.innerHTML = response;
      }
  }
  http_request.open('POST', data_file, true);
  http_request.send(params);
}
function get_outputs(){
  let myForm = document.getElementById('question_generator');
  let formData = new FormData(myForm);
  values = [];
  for (var value of formData.values()) {
    values.push(value);
  }
  var route="/get_outputs"
  var data_file = server_addr+route;
  var http_request = new XMLHttpRequest();
  var language = values[0];
  var category = values[1];
  var program = values[2];
  var params =JSON.stringify([language, category, program]);
  http_request.onreadystatechange = function() {//Call a function when the state changes.
      if(http_request.readyState == 4) {
        var response = JSON.parse(http_request.responseText);
        var files = response['files']
        div = document.getElementById("outputs");
        if(div===null)
        {
          div = document.createElement("div");
          div.setAttribute("id", "outputs")
          h2 = document.createElement("h2");
          h2.innerHTML = "Error File: ";
          div.appendChild(h2);

        }
        else
        {
          div = document.getElementById("outputs");
          if(div !== null)
            myForm.removeChild(div);
          var child = div.lastElementChild;
          div.removeChild(child);
        }
        var select = document.createElement("select");
        select.setAttribute("class", "outputs");
        select.setAttribute("name", "outputs");
        select.setAttribute("onchange", "get_file('error_file')");
        for(i = 0; i < files.length; i++)
        {
          var opt = document.createElement("option");
          opt.setAttribute("value", files[i]);
          opt.innerHTML = files[i];
          select.appendChild(opt);
        }

        div.appendChild(select);
        myForm.appendChild(div);

      }
  }
  http_request.open('POST', data_file, true);
  http_request.send(params);
}

function get_programs(){
  let myForm = document.getElementById('question_generator');
  let formData = new FormData(myForm);
  values = [];
  for(var value of formData.values()){
    values.push(value)
  }
  var language = values[0];
  var category = values[1];
  var route = "/get_programs";
  var data_file = server_addr+route;
  var http_request = new XMLHttpRequest();
  var params =JSON.stringify([language, category]);
  http_request.onreadystatechange = function() {//Call a function when the state changes.
      if(http_request.readyState == 4) {
          var response = JSON.parse(http_request.responseText);
          var files = response['files']
          div = document.getElementById("program");
          if(div===null)
          {
            div = document.createElement("div");
            div.setAttribute("id", "program")
            h2 = document.createElement("h2");
            h2.innerHTML = "Program: ";
            div.appendChild(h2);

          }
          else
          {
            div2 = document.getElementById("outputs");
            if(div2!== null)
              myForm.removeChild(div2);
            if(div !== null)
              div = document.getElementById("program");
            myForm.removeChild(div);
            var child = div.lastElementChild;
            div.removeChild(child);
            child1 = div.lastElementChild;
            div.removeChild(child1);
          }
          var select = document.createElement("select");
          select.setAttribute("class", "program");
          select.setAttribute("name", "program");
          select.setAttribute("onchange", "get_outputs()");
          for(i = 0; i < files.length; i++)
          {
            var opt = document.createElement("option");
            opt.setAttribute("value", files[i]);
            opt.innerHTML = files[i];
            select.appendChild(opt);
          }
          var button = document.createElement("button");
          button.setAttribute("id", "solution");
          button.setAttribute("type", "button");
          button.setAttribute("onclick", "get_file('solution')");
          button.innerHTML = "VIEW SOLUTION";

          div.appendChild(select);
          //div.appendChild(button);
          var leftbar = document.getElementById("leftbar");
          var soln = document.getElementById("solution")
          if (soln === null)
          {
            leftbar.appendChild(button)
          }
          myForm.appendChild(div);

      }
  }
  http_request.open('POST', data_file, true);
  http_request.send(params);
}
function get_folders(){
  let myForm = document.getElementById('question_generator');
  let formData = new FormData(myForm);
  values = [];
  for(var value of formData.values()){
    values.push(value)
  }
  var language = values[0];
  var route = "/get_categories";
  var data_file = server_addr+route;
  var http_request = new XMLHttpRequest();
  var params =JSON.stringify([language]);
  http_request.onreadystatechange = function() {//Call a function when the state changes.
      if(http_request.readyState == 4) {
          var response = JSON.parse(http_request.responseText);
          var dirs = response['directories']
          div = document.getElementById("category");
          if(div===null)
          {
            div = document.createElement("div");
            div.setAttribute("id", "category")
            h2 = document.createElement("h2");
            h2.innerHTML = "Category: ";
            div.appendChild(h2);

          }
          else
          {
            div3 = document.getElementById("outputs");
            if(div3 !== null)
              myForm.removeChild(div3);
            div2 = document.getElementById("program");
            if(div2 !== null)
              myForm.removeChild(div2)
            div = document.getElementById("category");
            if(div !== null)
              myForm.removeChild(div);
            var child = div.lastElementChild;
            div.removeChild(child);
          }
          var select = document.createElement("select");
          select.setAttribute("class", "category");
          select.setAttribute("name", "category")
          select.setAttribute("onchange", "get_programs()");
          for(i = 0; i < dirs.length; i++)
          {
            var opt = document.createElement("option");
            opt.setAttribute("value", dirs[i]);
            opt.innerHTML = dirs[i];
            select.appendChild(opt);
          }
          div.appendChild(select);
          myForm.appendChild(div);

      }
  }

  http_request.open('POST', data_file, true);
  http_request.send(params);
}
