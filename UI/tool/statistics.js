var c_count =0;
var p_count =0;
var c_score = 0;
var p_score = 0;
var avg_score_chart;
var sc_chart;
function calc_stats()
{
  document.getElementById("stats").style.display ="inline";
  var total_score=parseFloat("0.0");
  var num = 0;

  //gets table
  var oTable = document.getElementById('history_table');
  //gets rows of table
  var rowLength = oTable.rows.length;
  //loops through rows
  for (i = 0; i < rowLength; i++)
  {
     //gets cells of current row
     var oCells = oTable.rows.item(i).cells;
     //gets amount of cells of current row
     var cellLength = oCells.length;
     //Language wise
     var sc = parseFloat(oCells.item(3).innerHTML.substring(0, oCells.item(3).innerHTML.length - 1)) ;
     if(oCells.item(0).innerHTML.localeCompare("c")==0)
     {
       c_count+=1;
       c_score+=sc;
     }
     else if(oCells.item(0).innerHTML.localeCompare("python")==0)
     {
       p_count+=1;
       p_score+=sc;
     }

     //loops through each cell in current row
     for(var j = 0; j < cellLength; j++)
     {
        var cellVal = oCells.item(j).innerHTML;

        //Average score
        if(j==3)
        {
          var s = parseFloat(cellVal.substring(0, cellVal.length - 1)) ;
          if(!isNaN(s))
          {
              num+=1;
              total_score +=  s;
          }
        }

     }
   }
   document.getElementById("avg").innerHTML = "Average Score :   "+ (total_score/num).toFixed(2)+ "%";
   p_score /= p_count;
   c_score /= c_count;
   var max,min;
   var max_score,min_score;
   if (p_count>c_count)
   {
     max="python";
     max_score = p_score;
     min="c";
     min_score = c_score;
   }
   else {

       max="c";
       max_score = c_score;
       min="python";
       min_score = p_score;
   }
   document.getElementById("s_lang").innerHTML = "Strongest Language  :  "+max + "   (Average score = " + (max_score).toFixed(2) + "%)";
   document.getElementById("w_lang").innerHTML = "Weakest Language  :  "+ min + "   (Average score = " + (min_score).toFixed(2)+ "%)";

   document.getElementById("tot_sub").innerHTML = "Total Submissions  :  "+ parseFloat(parseFloat(c_count)+parseFloat(p_count));
   document.getElementById("c_sub").innerHTML = "C Submissions  :  "+ c_count;
   document.getElementById("p_sub").innerHTML = "Python Submissions  :  "+ p_count;

   display_chart();
   // bar_chart(p_score,c_score,"Average Scores");
   // bar_chart(p_count,c_count,"Submission counts");
}
function display_chart()
{
  // var ele = document.getElementsByName('radio');
  //
  // for(i = 0; i < ele.length; i++) {
  //     if(ele[i].checked)
  //       var selected = ele[i].value;
  // }
  //
bar_chart(p_score,c_score,"Average Scores");
bar_chart(p_count,c_count,"Submission counts");
  // if (selected =="as")
  // {
  //    bar_chart(p_score,c_score,"Average Scores");
  //
  // }
  // else if (selected =="sc"){
  //   bar_chart(p_count,c_count,"Submission counts");
  // }

  // else if (selected =="t"){
  //
  // }


}
function bar_chart(v1,v2,title){
//delete chart;
var cc;
if( title ==  "Submission counts")
{
   cc = "chartContainer1";
}
else
{
  cc = "chartContainer2";
}
var chart = new CanvasJS.Chart(cc, {
 animationEnabled: true,
 exportEnabled: true,
 theme: "light2", // "light1", "light2", "dark1", "dark2"
 title:{
   text: title
 },
 data: [{
   type: "column", //change type to bar, line, area, pie, etc
   //indexLabel: "{y}", //Shows y value on all Data Points
   indexLabelFontColor: "#5A5757",
   indexLabelFontSize: 20,
   indexLabelPlacement: "outside",
   dataPoints: [
     { x: 10, y: parseInt(v1) , indexLabel: "\u2605 Python" },
     { x: 20, y: parseInt(v2), indexLabel: "\u2605 C"}

   ]
 }]
});
if( title ==  "Submission counts")
{
   avg_score_chart = chart;
}
else
{
  sc_chart = chart;
}
chart.render();

}


var server_addr="http://0.0.0.0:80";
function get_submissions()
{
  var route="/get_submissions"
  var data_file = server_addr+route;
  var http_request = new XMLHttpRequest();
  http_request.onreadystatechange = function() {//Call a function when the state changes.
      if(http_request.readyState == 4) {
          var response = JSON.parse(http_request.responseText);
          console.log(response)
          var table = document.getElementById("history_table");

          for(var key in response)
          {
            var u = document.getElementById("user");
            u.innerHTML = "User : "+response[key]["username"];
            console.log(key);
            var tr = document.createElement("tr");

            // var td2 = document.createElement("td");
            // td2.innerHTML = response[key]["cur_uname"];
            // tr.appendChild(td2);
            var td3 = document.createElement("td");
            td3.innerHTML = response[key]["language"];
            tr.appendChild(td3);
            var td4 = document.createElement("td");
            td4.innerHTML = response[key]["category"];
            tr.appendChild(td4);
            var td5 = document.createElement("td");
            td5.innerHTML = response[key]["program"];
            tr.appendChild(td5);
            var td6 = document.createElement("td");
            td6.setAttribute("class", "table_score")
            td6.innerHTML = response[key]["score"];
            tr.appendChild(td6);
            var td1 = document.createElement("td");
            td1.innerHTML = response[key]["datetime"];
            tr.appendChild(td1);
            table.appendChild(tr);

          }
      }
  }
  http_request.open('GET', data_file, true);
  http_request.send();
}
