sol =0;
var current_solution;
var current_incorrect;

var editor;

window.onload=function(){
console.log("\n\n\n\n\n\n\n\JUST WORK OH MY GOD WHAT ON EARTH \n\n\n\n\n\n\n\n");
var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
if (slider!==null)
{
  console.log("meg" + slider.value);

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
}



/*  var code = document.getElementById("codesegment");
  var lines= document.getElementById("linenumbers");
  lines.scrollTop = code.scrollTop;
}, 100);*/



function change_view()
{
    sol=1;
    console.log("in change_view")
    document.getElementById("solutionhead").style.display = "inline-block";
    //document.getElementById("codesegment").cols = 30;
    block = document.getElementById("areas");
    div = document.createElement("textarea");
    div.cols = 30;
    div.rows = 25;
    div.style.display = "inline-block";
    div.style.backgroundColor='#e3f2f6';
    div.style.color='green';
    div.style.marginLeft="530px";
    div.style.marginTop="-500px";
    div.style.marginLeft="580px";
    // div.style.fontSize= "35px";
    // editor.setSize(500,500);
    document.getElementById("codediv").style.width = "45%";
    div.setAttribute("id", "solutionarea")
    if(document.getElementById("solutionarea")==null)
    {
      block.appendChild(div);
    }
    document.getElementById("solutionarea").innerHTML = current_solution;
    submit = document.getElementById("showerrors");
    // submit.innerHTML= "TRY AGAIN";
    // submit.onclick = revert_view1;
    submit.style.display = "none";

}

function revert_view()
{
  console.log("in revert_view");
  sol=0;
  d = document.getElementById("showcolorerrors");
  d.innerHTML ="";
  c = document.getElementById("colorerrorhead");
  c.innerHTML = "";
  block = document.getElementById("areas");
  div = document.getElementById("solutionarea");

  document.getElementById("codediv").style.width = "100%";
  // current_solution = div.value;
  if (div!==  null)
    {
       block.removeChild(div);
    }
  document.getElementById("code").cols = 64;
  document.getElementById("solutionhead").style.display = "none";
  submit = document.getElementById("showerrors");
  submit.innerHTML= "VIEW SOLUTION";
  submit.style.display = "inline-block";

  submit.setAttribute("onclick","calc_score(); store_data();")     //calc_score_1()) for Jaro similarity, calc_score_2() for no.of errors
  document.getElementById("error_msg").innerHTML = "";
  // document.getElementById("code").value = "";

  editor.setValue("");
  document.getElementById("score").innerHTML = "Score : 0";

}

function clear_box()
{
  document.getElementById("code").innerHTML ='';
  console.log("in clear_box")

}

var server_addr="http://0.0.0.0:80";

function perc_errors(){
  var route="/perc_errors"
  var output = document.getElementById("demo");
  var params=JSON.stringify(output.innerHTML);
  console.log((params))
  var data_file = server_addr+route;
  var http_request = new XMLHttpRequest();
  http_request.onreadystatechange = function(){
    if(http_request.readyState==4){
      var response = http_request.responseText;
      console.log(response);
    }
  }
  http_request.open('POST', data_file, true);
  http_request.send(params);
  console.log("inside");


}
function submitting(){
  get_file('solution');  show_errors();
  console.log("show_errors done");

  change_view();
  // setTimeout(  store_data(), 6000);

}

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
  var submission = editor.getValue() ;
  var params = JSON.stringify([language, category, program, file, submission]);
  http_request.onreadystatechange = function() {//Call a function when the state changes.
      if(http_request.readyState == 4) {
          var response = http_request.responseText;

          p = document.getElementById("error_msg");
          p.innerHTML = response;
          console.log("\n\n\nCALCULATIN SCORE OKAY\n\n")
          console.log(p.innerHTML)
          calc_score();

      }
  }
  http_request.open('POST', data_file, true);
  http_request.send(params);


}
function get_file(folder, no_display = 0){
  console.log("in get_file, this current_correct should be set")
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
    var params = JSON.stringify([language, category, program, values[3], "solution"]);
  }
  else
  {
    console.log(values[3]);
    var params = JSON.stringify([language, category, program, values[3], "output"]);
  }
  http_request.onreadystatechange = function() {//Call a function when the state changes.
      if(http_request.readyState == 4) {
          var response = http_request.responseText;
          if(folder != "solution")
          {
            if(no_display == 0)
            {
              // p = document.getElementById("code");
              editor.setValue(response.trim());
            }
            current_incorrect = response;
          }
          else
          {
            console.log(response);
            response = response.split(" thisisauniquecombinationofcharactersnoonesgonnause ")
            if(response.length == 2)
            {
              disp_errors = response[0]
              response = response[1]
            }
            else
            {
              response = response[0]
              disp_errors = ""
            }
            if(no_display == 0)
            {

              p = document.getElementById("solutionarea");
              var c = document.getElementById("colorerrorhead");
              c.innerHTML = "Highlighted Errors: "
              var disp_errors_p = document.getElementById("showcolorerrors");
              disp_errors_p.innerHTML = disp_errors;
              disp_errors_p.style.display = "inline-block";
              disp_errors_p.style.fontSize = "20px";
              disp_errors_p.style.marginTop = "-20px";
              disp_errors_p.style.overflow = "scroll";
              disp_errors_p.style.width = '100%';
              disp_errors_p.style.height = '200px';

            }
            console.log("folder is solution but no_display is 1");
            current_solution = response;
            console.log("current_solution set in get_file");
            console.log(current_solution);
          }
          if(no_display==0)
          {

              p=document.getElementById("solutionarea");
              console.log("jsk");
              console.log(no_display);
              console.log(p);
              //console.log(response);
              if(p!==null)
              {
                p.value=response.trim();
              }
          }

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
          //this is for removing the select from the div
          var child = div.lastElementChild;
          console.log(child)
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
        var opt = document.createElement("option");
        opt.innerHTML = "Select option";
        opt.disabled = true;
        opt.selected = true;
        select.appendChild(opt);

        div.appendChild(select);
        myForm.appendChild(div);

      }
  }
  http_request.open('POST', data_file, true);
  http_request.send(params);
  get_file("solution", 1);
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

            myForm.removeChild(div);
            var child = div.lastElementChild;
            div.removeChild(child);
            // child1 = div.lastElementChild;
            // div.removeChild(child1);
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

          var opt = document.createElement("option");
          opt.innerHTML = "Select option";
          opt.disabled = true;
          opt.selected = true;
          select.appendChild(opt);

          div.appendChild(select);
          var leftbar = document.getElementById("leftbar");
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
          var opt = document.createElement("option");
          opt.innerHTML = "Select option";
          opt.disabled = true;
          opt.selected = true;
          select.appendChild(opt);

          div.appendChild(select);
          myForm.appendChild(div);

      }
  }

  http_request.open('POST', data_file, true);
  http_request.send(params);
}


function sign_up()
{
  route = "/signup"
  var data_file = server_addr+route;
  var http_request = new XMLHttpRequest();
  var username= document.getElementById("username").value;
  var password= document.getElementById("password").value;
  var params =JSON.stringify({'username': username,'password':password});
  http_request.onreadystatechange = function() {//Call a function when the state changes.
      if(http_request.readyState == 4) {
          var jsonObj = JSON.parse(http_request.responseText);
          if(jsonObj.status == "Successful")
          {
            document.getElementById("status").innerHTML = "Welcome, " + username;
          }
          else
          {
            document.getElementById("status").innerHTML=jsonObj.status;
          }
          //alert(jsonObj.status);
          document.getElementById("username").value = '';
          document.getElementById("password").value= '';
      }
  }
  http_request.open('POST', data_file, true);
  http_request.send(params);

}

function store_data()
{
  console.log("Here")
  route = "/store_data";
  var data_file = server_addr + route;
  var http_request = new XMLHttpRequest();
  let myForm = document.getElementById('question_generator');
  let formData = new FormData(myForm);
  values = [];
  for (var value of formData.values()) {
    values.push(value);
  }
  var language = values[0];
  var category = values[1];
  var program = values[2];
  var err_pgm = values[3];
  //calc_score_jaro();
  var score = document.getElementById("score").innerHTML;
  console.log(score);
  console.log(document.getElementById("error_msg").innerHTML);
  var params =JSON.stringify({"language":language, "category":category, "program":program, "score":score});
  http_request.onreadystatechange = function() {//Call a function when the state changes.
      if(http_request.readyState == 4) {
          var jsonObj = JSON.parse(http_request.responseText);
          console.log(jsonObj);
          // if(jsonObj.status == 'Login Successful')
          // {
          //   console.log("here")
          //   document.getElementById("status").innerHTML = "Welcome, " + username;
          //   window.open("index.html")
          // }
          // else
          // {
          //   document.getElementById("status").innerHTML=jsonObj.status;
          // }
          // //alert(jsonObj.status);
          // document.getElementById("username").value = '';
          // document.getElementById("password").value= '';
      }
  }
  http_request.open('POST', data_file, true);
  http_request.send(params);

}
function sign_in()
{
  route = "/signin"
  var data_file = server_addr+route;
  var http_request = new XMLHttpRequest();
  var username= document.getElementById("username").value;
  var password= document.getElementById("password").value;
  var params =JSON.stringify({'username': username,'password':password});
  http_request.onreadystatechange = function() {//Call a function when the state changes.
      if(http_request.readyState == 4) {
        console.log(http_request.readyState)
          if(http_request.status == 200)
          {
            console.log("here")
            document.getElementById("status").innerHTML = "Welcome, " + username;
            window.open("render_index", "_self");
          }
          else
          {
            document.getElementById("status").innerHTML='There has been an error';
          }
          //alert(jsonObj.status);
          document.getElementById("username").value = '';
          document.getElementById("password").value= '';
      }
  }
  http_request.open('POST', data_file, true);
  http_request.send(params);

}
function  calc_score_jaro()
{

          get_file('solution');
          change_view();
          ans = editor.getValue();
          correct = current_solution;

          correct = document.getElementById("solutionarea").innerHTML;
          console.log(correct);
          base = jaro_distance(current_incorrect,current_solution);
          score = ((jaro_distance(ans,correct)-base)/(1-base)) *100;
          if (score<0)
          {
            if (Math.abs(score)<50 )
            {
              score = -score;
            }
            else {
              score=0;
            }
          }
          //score= (jaro_distance(ans,correct)*100 );
          score= score.toFixed(2);
          console.log("score");

          document.getElementById("score").innerHTML = "Score: "+ score+"%";
          console.log("DONE BRO");

          return score;



}
function calc_score()
{
    get_file('solution');
    change_view();
    ans = editor.getValue();
    correct = current_solution;

    correct = document.getElementById("solutionarea").innerHTML;
    console.log(correct);
    base = jaro_distance(current_incorrect,current_solution);
    score = ((jaro_distance(ans,correct)-base)/(1-base)) *100;
    if (score<0)
    {
      if (Math.abs(score)<30)
      {
        score = -score;
      }
      // else {
      //   score=0;
      // }
    }
    //score= (jaro_distance(ans,correct)*100 );
    if(calc_score_jaro() >99.9)
    {
      score = 100.00;
      document.getElementById("score").innerHTML = "Score: " + score +"%" ;
      document.getElementById("score_deets1").innerHTML = "" ;
      document.getElementById("score_deets2").innerHTML ="";

          elements = document.getElementsByClassName("not_corrected");
          for (var i = 0; i < elements.length; i++)
          {
              elements[i].style.color="green";
          }

    }
    else if(calc_score_jaro() == 0)
    {
      score = 0.00;
      document.getElementById("score").innerHTML = "Score: " + score +"%" ;
      document.getElementById("score_deets1").innerHTML = "" ;
      document.getElementById("score_deets2").innerHTML ="";
          elements = document.getElementsByClassName("corrected");
          for (var i = 0; i < elements.length; i++)
          {
              elements[i].style.color="red";
          }
    }
    else
    {

          //correct = document.getElementById("solutionarea").innerHTML;
          var error_msgs = document.getElementById("error_msg").innerHTML;
          var total_errors,corrected_errors,missed_errors;

          total_errors = count_errors(error_msgs, "<span class=");
          missed_errors = count_errors(error_msgs, "not_corrected");
          corrected_errors = total_errors-missed_errors;
          score = (corrected_errors/total_errors)*100;
          score= score.toFixed(2);
          document.getElementById("score").innerHTML = "Score: " + score +"%" ;
          document.getElementById("score_deets1").innerHTML = "Total errors: " + total_errors ;
          document.getElementById("score_deets2").innerHTML ="   Corrected Errors: " + corrected_errors;
    }


    console.log("DONE BRO");
  //   get_file('solution');
  //   change_view();
  //   ans = editor.getValue();
  //   correct = current_solution;
  //
  //   //correct = document.getElementById("solutionarea").innerHTML;
  //   error_msgs = document.getElementById("error_msg").innerHTML;
  //   var total_errors = (error_msgs.match(/class/g) || []).length;
  //   var corrected_errors = (error_msgs.match(/class='corrected'/g) || []).length;
  //   var missed_errors = (error_msgs.match(/class='not_corrected'/g) || []).length;
  //   console.log("_________ERRORORJEDFHEKFLDFKVBLDKSFJBVLKSDJFVKLDSBFKJV\n\n\ntotal_errors, corrected_errors, missed_errors");
  //
  //   document.getElementById("score").innerHTML = "Score: "+ score+"%";
  // }

   store_data();


}

function count_errors(error_msgs, subString)
{
  error_msgs += "";
  subString += "";

  var count = 0,
      pos = 0,
      step =  subString.length;

  while (true) {
      pos = error_msgs.indexOf(subString, pos);
      if (pos >= 0) {
          ++count;
          pos += step;
      } else break;
  }

  return count;
}


function jaro_distance(s1, s2)
{
        var m = 0;
        // Exit early if either are empty.
        if ( s1.length === 0 || s2.length === 0 ) {
            return 0;
        }
        // Exit early if they're an exact match.
        if ( s1 === s2 ) {
            return 1;
        }
        s1= s1.replace(/\s/g,'');
        s2= s2.replace(/\s/g,'');
        var range     = (Math.floor(Math.max(s1.length, s2.length) / 2)) - 1,
            s1Matches = new Array(s1.length),
            s2Matches = new Array(s2.length);

        for ( i = 0; i < s1.length; i++ ) {
            var low  = (i >= range) ? i - range : 0,
                high = (i + range <= s2.length) ? (i + range) : (s2.length - 1);
            for ( j = low; j <= high; j++ ) {
            if ( s1Matches[i] !== true && s2Matches[j] !== true && s1[i] === s2[j] ) {
                ++m;
                s1Matches[i] = s2Matches[j] = true;
                break;
            }
            }
        }        // Exit early if no matches were found.
        if ( m === 0 ) {
            return 0;
        }
        // Count the transpositions.
        var k = n_trans = 0;
        for ( i = 0; i < s1.length; i++ ) {
            if ( s1Matches[i] === true ) {
            for ( j = k; j < s2.length; j++ ) {
                if ( s2Matches[j] === true ) {
                k = j + 1;
                break;
                }
            }
            if ( s1[i] !== s2[j] ) {
                ++n_trans;
            }
            }
        }
        var weight = (m / s1.length + m / s2.length + (m - (n_trans / 2)) / m) / 3,
            l      = 0,
            p      = 0.1;
        if ( weight > 0.7 ) {
            while ( s1[l] === s2[l] && l < 4 ) {
            ++l;
            }
            weight = weight + l * p * (1 - weight);
        }
        return weight;
}
